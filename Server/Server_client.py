import uuid
from threading import Thread
import copy
import logging
from datetime import datetime
import time
from math import sin,cos
import sys
from intel_live_posupdater import PosUpdater

from opcua.ua import NodeId, NodeIdType

sys.path.insert(0, "..")

try:
    from IPython import embed
except ImportError:
    import code

    def embed():
        myvars = globals()
        myvars.update(locals())
        shell = code.InteractiveConsole(myvars)
        shell.interact()

from opcua import ua, uamethod, Server




# class PosUpdater(Thread):
#     def __init__(self, x_var, y_var):
#         Thread.__init__(self)
#         self._stopev = False
#         self.x_var = x_var
#         self.y_var = y_var

#     def stop(self):
#         self._stopev = True

#     def run(self):
#         while not self._stopev:
#             x = sin(time.time() / 10)
#             y = cos(time.time() / 10)
#             self.x_var.set_value(x)
#             self.y_var.set_value(y)
#             time.sleep(0.5)
            
            


# now setup our server, ask ip from school
server = Server()

server.set_endpoint("opc.tcp://0.0.0.0:0000/ilmatar/eye/")

server.set_server_name("Crane_eye_server")

# set all possible endpoint policies for clients to connect through
server.set_security_policy([
    ua.SecurityPolicyType.NoSecurity,
    ua.SecurityPolicyType.Basic256Sha256_SignAndEncrypt,
    ua.SecurityPolicyType.Basic256Sha256_Sign])

# setup our own namespace/ idk if required tho currently uri is false
uri = "https://www.aalto.fi/en/industrial-internet-campus/ilmatar-open-innovation-environment"
idx = server.register_namespace(uri)

# create directly some objects and variables
myobj = server.nodes.objects.add_object(idx, "RealSenseT265")
x_pos = myobj.add_variable(idx, "bridge_pos_m", 0, ua.VariantType.Float)
y_pos = myobj.add_variable(idx, "trolley_pos_m", 0, ua.VariantType.Float)


# import some nodes from xml
server.import_xml("custom_nodes.xml")


# starting!
server.start()
print("Available loggers are: ", logging.Logger.manager.loggerDict.keys())
vup = PosUpdater(x_pos, y_pos)  #initializing and starting the variable updater device.
vup.start()
try:
    
    embed()
finally:
    vup.stop()
    server.stop()
