import nnpy
import struct
import ipaddress
from p4utils.utils.helper import load_topo
from p4utils.utils.sswitch_thrift_API import SimpleSwitchThriftAPI
import subprocess

class RegistReader():

    def __init__(self):
        self.topo = load_topo('topology.json')
        self.sw_names = self.topo.get_p4switches().keys()
        
    def read_register_bulk(self, sw_name, register):
        self.thrift_port = self.topo.get_thrift_port(sw_name)
        self.port_sum = len(self.topo.get_interfaces_to_node(sw_name).items())
        
        p = subprocess.Popen(['simple_switch_CLI', '--thrift-port', str(self.thrift_port)], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        input_str = "register_read %s" % register
        input_bytes = input_str.encode()
        stdout, stderr = p.communicate(input=input_bytes)
        lines = stdout.decode().split('\n')
        
        reg_val_lines = [line for line in lines if register in line][0]
        reg_val_str = reg_val_lines.split('=')[1].strip().split(', ')
        reg_val_int = [int(num) for num in reg_val_str]
        
        print(reg_val_int)
    
    def run_bulk(self):
        for sw_name in self.sw_names:
            print(sw_name)
            self.read_register_bulk(sw_name, "enqlength_cache")
            self.read_register_bulk(sw_name, "deqlength_cache")

def main():
    print("init...")
    # RegistReader().read_register_bulk("s1", "enqlength_cache")
    # RegistReader().read_register_bulk("s1", "deqlength_cache")
    RegistReader().run_bulk()

if __name__ == "__main__":
    main()
