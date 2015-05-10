#### How to Use : --- 
#### First you will find your IP in a label in the end of the Program 
#### ---------------------------------------------------------------
#### To SEND data :- 
#### You Start First with Reciever Side .. 
#### Start program There .. 
####  By Import Name of the file you will want to recive .. Like "Omar.mp3 " or " Drmicrosoft.jpg "
####
#### and click receive ..
####
#### Then Go to Sender Side
#### By Import name File or Its Path .. and Choose The reciever IP .. From the Combo Box
#### and Click Send .. 
####
#### The file will send 
####
#### In the reciever Side You will Find the file in the Program Folder .. 

#### Version 1.0.0
#### Open Source 
#### Free to Use
#### Drmicrosoft 

#### To work okay .. put in one folder the .glade file and the .py file ..

#### Thanks





from gi.repository import Gtk
import sys
import socket
import pygst
pygst.require("0.10")
import gst
import os
import fcntl
import struct


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def sendd (sssss) :
	#xc = f1.get_title()
	msg = e1.get_text()
	com = x1.get_active_text()
	
	#l1.set_text(msg)
	print msg
	print com
	sends(com,msg)

def recivv (sssss) :
	#xc = f1.get_title()
	msg = e1.get_text()
	com = get_ip_address("wlan0")
	
	#l1.set_text(msg)
	print msg
	print com
	recivs(com,msg)




def get_ip_address(ifname):
    print ("getiing ip adress")
    q = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        q.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])
    	


	
def initiaal_combo(z) :
		
	i=0
	while 1 :
		if i <=255 :
			x1.append_text("{}{}".format("192.168.1.", i))
			i=i+1
			print "{}{}".format("192.168.1.", i)
		else : 
			break
	





def ints (ssss) : 
	l1.set_text(get_ip_address("wlan0"))
	initiaal_combo(1)
	#pop_up("Drmicrosoft","Welcome to File Share")



x = Gtk.Builder()
x.add_from_file("1.glade")



def sends (ip , files) :

	s = socket.socket()         # Create a socket object
	host = socket.gethostname() # Get local machine name
	port = 12345                 # Reserve a port for your service.
	s.connect((ip, port))
	#s.send("Hello server!")
	f = open(files,'rb')
	print 'Sending...'
	l = f.read(1024)
	while (l):
		print 'Sending...'
		s.send(l)
		l = f.read(1024)
	s.shutdown(socket.SHUT_WR)
	f.close()
	print "Done Sending"
	print s.recv(1024)
	s.close                     # Close the socket when done




def recivs (ip , files) : 
		

	s = socket.socket()         # Create a socket object
	#host = socket.gethostname() # Get local machine name
	host = ip # Get local machine name
	port = 12345               # Reserve a port for your service.
	s.bind((host, port))        # Bind to the port
	f = open(files,'wb')
	s.listen(5)                 # Now wait for client connection.
	while True:
		c, addr = s.accept()     # Establish connection with client.
		print 'Got connection from', addr
		print "Receiving..."
		l = c.recv(1024)
		while (l):
			print "Receiving..."
			f.write(l)
			l = c.recv(1024)
		f.close()
		print "Done Receiving"
		c.send('Thank you for connecting')
		c.close()                # Close the connection




b1 = x.get_object("button1")
b3 = x.get_object("button5")
b2 = x.get_object("button4")
e1 = x.get_object("entry1")
l1 = x.get_object("label3")
x1 = x.get_object("comboboxtext1")









b1.connect("clicked", Gtk.main_quit)
b2.connect("clicked", sendd)
b3.connect("clicked", recivv)

	












ints(1)



window = x.get_object("window1")

window.show_all()

Gtk.main()
