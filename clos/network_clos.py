from p4utils.mininetlib.network_API import NetworkAPI

net = NetworkAPI()

# Network general options
net.setLogLevel('info')
net.execScript('python routing-controller.py', reboot=True)

# Network definition
net.addP4Switch('s1')
net.addP4Switch('s2')
net.addP4Switch('s3')
net.addP4Switch('s4')
net.addP4Switch('s5')
net.addP4Switch('s6')
net.addP4Switch('s7')
net.addP4Switch('s8')
net.setP4SourceAll('p4src/loadbalancer.p4')

net.addHost('h1')
net.addHost('h2')
net.addHost('h3')
net.addHost('h4')
net.addHost('h5')
net.addHost('h6')
net.addHost('h7')
net.addHost('h8')
net.addHost('h9')
net.addHost('h10')
net.addHost('h11')
net.addHost('h12')


net.addLink("s1", "s3")
net.addLink("s1", "s4") 
net.addLink("s1", "s5")

net.addLink("s2", "s3")
net.addLink("s2", "s4")
net.addLink("s2", "s5")

net.addLink("s3", "s6")
net.addLink("s3", "s7")
net.addLink("s3", "s8")

net.addLink("s4", "s6")
net.addLink("s4", "s7")
net.addLink("s4", "s8")

net.addLink("s5", "s6")
net.addLink("s5", "s7")
net.addLink("s5", "s8")

net.addLink("s6", "h1")
net.addLink("s6", "h2")
net.addLink("s6", "h3")
net.addLink("s6", "h4")

net.addLink("s7", "h5")
net.addLink("s7", "h6")
net.addLink("s7", "h7")
net.addLink("s7", "h8")

net.addLink("s8", "h9")
net.addLink("s8", "h10")
net.addLink("s8", "h11")
net.addLink("s8", "h12")

net.setBwAll(10)

# Assignment strategy
net.l3()

# Nodes general options
net.enablePcapDumpAll()
net.enableLogAll()
net.enableCli()
net.startNetwork()