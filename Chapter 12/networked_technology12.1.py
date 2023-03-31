#Transport control Protocol(tcp)
#built on top of Ip(internet Protocol)
#Assumes IP might lose some data - stores and
#retransmits data if it seems to be lost
#Handles "flow control" using a transmit window

#Sockets in Python

#Python has built-in support for TCP Sockets

import socket        
                            #the actual connection happens when we say mysock.connec#end point inside your computer thats ready to connectout
                              #a connection point thats not yet connectt.
             
  #we're going to hook a thing across
  # the internet and we're going to use a stream.           
             #A stream means its a series of
             #characters that just keep coming back.
             #
             #  ^                                      #^
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
              
              
              
                    #^
              #HOst  , the actual conncection happens when we
              # say "mysock.connect" this returns us a object
              #we call the connect method in that object and we pass two things.
              #the host we want to connect to, which is the domain name, and 
              #a port we want to connect to 
