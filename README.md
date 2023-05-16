# Crane Eye

System consists of: 
Intel T265 stereo camera 
Lenovo ThinkCentre mini-pc 
Mounts on the crane trolley 

PC is connected to Ilmatar5GHz LAN, remote control with Anydesk-software is possible (pw: Crane_eye, IP: ask from school). PC works as a server for client computers via WLAN. Server boots when crane main power is switched on, Anydesk and python code are run at start-up. Server can be accessed for maintenance via Anydesk. Client can receive camera position and crane laser position in (x, y). Client can be modified to do whatever necessary. Our example client code (Client_plot.py) will plot camera position using matplotlib.pyplot to an updating xy-graph for visual inspection. 

Server’s Python code utilizes opcua and crane –libraries, which are necessary. Libraries can be found below.
Crane:
Opcua:

How to boot server: 

-Turn on crane and the server will be powered. 
-Server can be accessed using Anydesk. IP: ask from school and password: Crane_eye 
-Server should launch Server_client.py automatically, but it can be also launched manually. 
-Python file should be launched using terminal if not selected as default. 

How to boot client: 
-You can use any computer that can access the LAN and has Python 3.10 or older. 
-Connect to Ilmatar LAN.  
-Custom client scripts require Eye_client.py to be in the same folder to receive bridge and trolley data from server. 
-Run Client_plot.py or your own custom script in terminal or using IDE. 

Important parts in script: 

eye.get_pos() -- x and y position from the camera 
eye.stop() -- Stopping and disconnecting Eye_client.py script 

