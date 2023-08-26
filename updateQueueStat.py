import nnpy
import struct
import ipaddress
import sys
from p4utils.utils.helper import load_topo
from p4utils.utils.sswitch_thrift_API import SimpleSwitchThriftAPI
import subprocess

class Controller():
    topo = load_topo('topology.json')
    sw_names = topo.get_p4switches().keys()
    switch_CLIs = {}

    def __init__(self):
        self.connect_to_switches()

    def connect_to_switches(self):
        for p4switch in self.topo.get_p4switches():
            self.thrift_port = self.topo.get_thrift_port(p4switch)
            self.switch_CLIs[p4switch] = subprocess.Popen(['simple_switch_CLI', '--thrift-port', str(self.thrift_port)], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


class UpdateQueueRate(Controller):

    def __init__(self):
        super().__init__()
        self.topo = super().topo
        self.sw_names = super().sw_names
        self.switch_CLIs = super().switch_CLIs

    def update(self, sw_name, rate):
        self.port_sum = len(self.topo.get_interfaces_to_node(sw_name).items())
        input_str = "set_queue_rate %s" % rate
        input_bytes = input_str.encode()
        stdout, stderr = self.switch_CLIs[sw_name].communicate(input=input_bytes)
        print("set", sw_name, "rate: ", rate, "pps")

    def updateAll(self, rate):
        for sw_name in self.sw_names:
            self.update(sw_name, rate)

def main():
    print("init...")

    rate = 1000
    if len(sys.argv) > 1:
        rate = int(sys.argv[1])
    
    # bUpdateQueueRate().update("s1", rate)
    UpdateQueueRate().updateAll(rate)

if __name__ == "__main__":
    main()
