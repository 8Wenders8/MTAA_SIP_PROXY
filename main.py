import sipfullproxy
import SocketServer
import socket
import sys
import time
import logging


if __name__ == '__main__':
    HOST, PORT = sipfullproxy.HOST, sipfullproxy.PORT
    logging.basicConfig(format='(%(asctime)s): %(message)s', filename='proxy.log', level=logging.INFO,
                        datefmt='%H:%M:%S')
    logging.info(time.strftime("%a, %d %b %Y %H:%M:%S ", time.localtime()))
    hostname = socket.gethostname()
    ipaddress = sys.argv[1]
    print(ipaddress + ':' + str(PORT))
    logging.info("Zariadenie " + hostname + ' s IP ' + ipaddress)
    sipfullproxy.recordroute = "Record-Route: <sip:%s:%d;lr>" % (ipaddress, PORT)
    sipfullproxy.topvia = "Via: SIP/2.0/UDP %s:%d" % (ipaddress, PORT)
    server = SocketServer.UDPServer((HOST, PORT), sipfullproxy.UDPHandler)
    server.serve_forever()
