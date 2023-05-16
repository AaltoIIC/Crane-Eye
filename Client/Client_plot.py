from Eye_client import Eye_client
import matplotlib.pyplot as plt
import keyboard

# Setting up eye client
eye = Eye_client()

#Setting up realtime plot
fig = plt.figure(figsize=(7, 5))
ax = plt.axes()

# Fixed area for map, can be removed for automatic scaling
plt.xlim(-2.5,2.5)
plt.ylim(-2.5,2.5)

ax.set_xlabel("X-akseli (m)")
ax.set_ylabel("Y-akseli (m)")

# List for live plotting without slowing down
x = []
y = []

# Zeroing camera position to origo
x_eka, y_eka = eye.get_pos()


while(True):

    # Getting (x,y) position from server through eye client
    bridge, trolley = eye.get_pos()

    bridge = round((bridge - x_eka), 3)
    trolley = round((trolley - y_eka), 3)
    #print("eye_bridge: " + str(bridge) + " eye_Trolley: "+ str(trolley))

    # Append (x,y) values to list
    x.append(bridge)
    y.append(trolley)

    # If list longer than 3, remove last point in list
    # Helps with live plot performance issues
    if len(x) >= 3:
        x.pop(0)
        y.pop(0)

    # Plot position to graph and add legend
    plt.plot(x,y, c="red")
    ax.legend(["Camera"], loc="lower left")

    # Data refresh rate 10 Hz, advance timestep
    plt.pause(0.1)

    # Script is stopped by pressing Q or turning power off
    if keyboard.is_pressed("q"):
        print("quitting!")
        eye.stop()
        break






        








