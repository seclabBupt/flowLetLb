import sys
import random
import time
from p4utils.utils.helper import load_topo
from subprocess import Popen

import os
from datetime import datetime

topo = load_topo('topology.json')

# 以当前系统时间创建flowInfo文件路径
now = datetime.now()
timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
folder_name = "flowInfo/" + f"{timestamp}"
os.mkdir(folder_name)

# iperf_send = "mx {0} iperf3 -M 9000 -c {1} -t {2} --bind {3} --cport {4} -p {5} 2>&1 >/dev/null"
iperf_send = "mx {0} iperf3 -M 9000 -f Mbits -c {1} -t {2} --bind {3} --cport {4} -p {5} 2>&1 > {6}"
iperf_recv = "mx {0} iperf3 -s -f Mbits -p {1} --one-off 2>&1 > /dev/null"

duration = 10
if len(sys.argv) > 1:
    duration = int(sys.argv[1])
    
send_cmds = []
recv_cmds = []

Popen("sudo killall iperf iperf3 > /dev/null", shell=True)

num_hosts = 8
num_senders= 4

for src_host in sorted(topo.get_hosts().keys(), key = lambda x: int(x[1:]))[:num_senders]:
    dst_host = 'h' + str((int(src_host[1:]) + 3) % num_hosts + 1)
    output_dir = folder_name + "/h" + str(int(src_host[1:])) + ".log"

    src_port = random.randint(1025, 65000)
    dst_port = random.randint(1025, 65000)
    src_ip = topo.get_host_ip(src_host)
    dst_ip = topo.get_host_ip(dst_host)

    send_cmds.append(iperf_send.format(src_host, dst_ip, duration, src_ip, src_port, dst_port, output_dir))
    recv_cmds.append(iperf_recv.format(dst_host, dst_port))

#start receivers first
for recv_cmd in recv_cmds:
    Popen(recv_cmd, shell=True)
    # print(recv_cmd)

time.sleep(1)

for send_cmd in send_cmds:
    Popen(send_cmd, shell=True)
    # print(recv_cmd)

# Popen(send_cmds[0], shell=True)
# Popen(send_cmds[1], shell=True)