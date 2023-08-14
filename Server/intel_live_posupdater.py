


import pyrealsense2 as rs
import matplotlib.pyplot as plt
import keyboard
import csv
import time
from threading import Thread

class Pos_updater(Thread):

    def __init__(self, x_var, y_var):
        Thread.__init__(self)
        self._stopev = False
        self.x_var = x_var
        self.y_var = y_var   
        
        # List for saving the position
        self.x = []
        self.y = []

        # Enabling communication with camera and enable map preservation

        self.pipe = rs.pipeline()
        self.cfg = rs.config()
        self.cfg.enable_stream(rs.stream.pose)
        self.pose_sensor = self.cfg.resolve(self.pipe).get_device().first_pose_sensor()

        self.pose_sensor.set_option(rs.option.enable_map_preservation, 1)
        self.pipe.start(self.cfg)



            
    def load_pos(self):
        # Read last position from file
        try:
            with open("lastpos.txt", "r") as f:
                x1 = float(f.readline())
                y1 = float(f.readline())
                print(x1, y1)

            return x1, y1
        # If no previous position, start from (0,0)
        except:
            x1 = float(0)
            y1 = float(0)
            return x1, y1


    def save_pos(self):

        # Reading last position from file
        with open("lastpos.txt", "w") as f:

            # Possibility to have date and time in file
            #now = datetime.now()
            #time = now.strftime("%H.%M.%S")
            #date = now.strftime("%d/%m/%Y")


            # Average of all list elements

            lenght = len(self.x)

            sum(self.x)
            X = sum(self.x)/lenght
            Y = sum(self.y)/lenght

            # Write to file as str
            f.write(str(X) + "\n")
            f.write(str(Y) + "\n")
            #f.write(str([date, time]))
            f.close()


    def run(self):

     
        # Getting last position before shutdown
        x_start, y_start = self.load_pos()

        # runs untill self.stop() is called
        while not self._stopev:

            # Reading camera data
            frames = self.pipe.wait_for_frames()
            pose = frames.get_pose_frame()

            if pose:

                # Append position data as x,y and live plot (meters)
                # Notice that in our case y-dir is camera's z-dir
                data = pose.get_pose_data()

                # Get camera position and write it to given variables. And append the list for savin average position.
                data_cam_x = round((data.translation.x + x_start), 4)
                data_cam_y = round((data.translation.z + y_start), 4)
            
                self.x_var.set_value(-data_cam_x)
                self.y_var.set_value(-data_cam_y)

                self.x.append(data_cam_x)
                self.y.append(data_cam_y)

                # Save positions to csv file and close so it saves if power off

                self.save_pos()

                # If list too long, remove last ones
                if len(self.x) >= 6:
                    self.x.pop(0)
                    self.y.pop(0)
                  
                # Data refresh rate 20 Hz, advance timestep
                time.sleep(0.05)


    def stop(self):
       self.save_pos()
       self._stopev = True   
       self.pipe.stop()        

            
      







