import nnpy
import struct
import ipaddress
from p4utils.utils.helper import load_topo
from p4utils.utils.sswitch_thrift_API import SimpleSwitchThriftAPI


class DigestController():

    def __init__(self, sw_name):
        self.topo = load_topo('topology.json')
        self.sw_name = "s1"
        self.thrift_port = 9090
        self.controller = SimpleSwitchThriftAPI(self.thrift_port)

    def recv_msg_digest(self, msg):
        topic, device_id, ctx_id, list_id, buffer_id, num = struct.unpack("<iQiiQi",
                                                                     msg[:32])
        print(num, len(msg))
        offset = 18
        msg = msg[32:]

        for sub_message in range(num):
            id = struct.unpack("!I", msg[0:4])
            enq_qdepth_row = struct.unpack("!I", b'\x00' + msg[4:7])
            deq_qdepth_row = struct.unpack("!I", b'\x00' + msg[7:10])
            enq_timestamp, deq_timedelta = struct.unpack("!II", msg[10:18])

            print(msg[:offset])
            print("id:", id,
                  "enq_qdepth_row:", enq_qdepth_row, 
                  "deq_qdepth_row:", deq_qdepth_row, 
                  "enq_timestamp:", enq_timestamp,
                  "deq_timedelta:", deq_timedelta)
            
            msg = msg[offset:]
        # self.controller.client.bm_learning_ack_buffer(ctx_id, list_id, buffer_id)

    def run_digest_loop(self):
        sub = nnpy.Socket(nnpy.AF_SP, nnpy.SUB)
        notifications_socket = self.controller.client.bm_mgmt_get_info().notifications_socket
        print("connecting to notification sub %s" % notifications_socket)
        sub.connect(notifications_socket)
        sub.setsockopt(nnpy.SUB, nnpy.SUB_SUBSCRIBE, '')
        
        while True:
            msg = sub.recv()
            print("captured a packet...")
            self.recv_msg_digest(msg)


def main():
    print("init...")
    DigestController("s1").run_digest_loop()


if __name__ == "__main__":
    main()
