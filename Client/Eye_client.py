from opcua import Client, ua
from opcua.ua import ua_binary as uabin


class Eye_client:
    def __init__(self):
        #start by connecting to given endpoint, ask ip for Ilmatar from school.
        self.client = Client("opc.tcp://0.0.0.0:0000/ilmatar/eye/")
        self.client.connect()

        # Get the correct variables from the server and save references to them.

        uri = "https://www.aalto.fi/en/industrial-internet-campus/ilmatar-open-innovation-environment"
        idx = self.client.get_namespace_index(uri)

        self.root = self.client.get_root_node()
        self.bridge_pos = self.root.get_child(["0:Objects", "{}:RealSenseT265".format(idx), "{}:bridge_pos_m".format(idx) ])
        self.trolley_pos = self.root.get_child(["0:Objects", "{}:RealSenseT265".format(idx), "{}:trolley_pos_m".format(idx) ])



    #method used to get data from the server. Returns bridge and trolley position respectively
    def get_pos(self):
        bridge = self.bridge_pos.get_value()
        trolley = self.trolley_pos.get_value()

        return bridge, trolley


    #Method for disconnecting from the server when stopping the main script.
    def stop(self):
        self.client.disconnect()
    




