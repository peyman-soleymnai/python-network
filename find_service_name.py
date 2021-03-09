#!/bin/python   
import socket
def find_service_name():
    protocolname = 'tcp'
                                                                                           
    for port in [80, 25, 22, 23, 80, 443, 21]:
        print ("Port: %s => service name: %s" %(port, socket.getservbyport(port, protocolname)))
    print ("Port: %s => service name: %s" %(53, socket.getservbyport(53, 'udp')))
                                                                               
                                                                             
if __name__ == '__main__':                                      
    find_service_name()                        
                                                                          
