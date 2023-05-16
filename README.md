# Crane Eye

**System consists of:** <br>
Intel T265 stereo camera <br>
Lenovo ThinkCentre mini-pc <br>
Mounts on the crane trolley <br>

**System description:** <br>
PC is connected to Ilmatar5GHz LAN, remote control with Anydesk-software is possible (pw: Crane_eye, IP: ask from school). PC works as a server for client computers via LAN. Server boots when crane main power is switched on, Anydesk and python code are run at start-up. Server can be accessed for maintenance via Anydesk. Client can receive camera position and crane laser position in (x, y). Client can be modified to do whatever necessary. Our example client code (Client_plot.py) will plot camera position using matplotlib.pyplot to an updating xy-graph for visual inspection. 

**Libraries:** <br>
Server’s Python code utilizes opcua and crane –libraries, which are necessary. Libraries can be found below. <br>
OPC UA: https://github.com/AaltoIIC/OPC-UA-GraphQL-Wrapper <br>
Crane: https://github.com/AaltoIIC/ilmatar-python-lib <br>

**How to boot server:** <br>
-Turn on crane and the server will be powered. <br>
-Server can be accessed using Anydesk. IP: ask from school and password: Crane_eye <br>
-Server should launch Server_client.py automatically, but it can be also launched manually. <br>
-Python file should be launched using terminal if not selected as default. <br>

**How to boot client:** <br>
-You can use any computer that can access the LAN and has Python 3.10 or older. <br>
-Connect to Ilmatar LAN. <br>
-Custom client scripts require Eye_client.py to be in the same folder to receive bridge and trolley data from server. <br>
-Run Client_plot.py or your own custom script in terminal or using IDE. <br>

**Important parts in script:** <br>
eye.get_pos() -- x and y position from the camera <br>
eye.stop() -- Stopping and disconnecting Eye_client.py script <br>

