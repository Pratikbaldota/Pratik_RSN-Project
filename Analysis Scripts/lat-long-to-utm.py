#!/usr/bin/env python3
from tkinter import N
import rospy
import serial
import utm
import time
import roslib
import sys
from gps_driver.msg import gps_msg
from std_msgs.msg import String


argument = rospy.myargv(argv=sys.argv)
if len(argument) < 2:
     print("error")
     sys.exit(1)

gps_port_name = argument[1]

#serial_port = '/dev/ttyACM0'
serial_baud = 4800
port = serial.Serial(gps_port_name , serial_baud , timeout= 100.00)
line= port.readline()

msg = gps_msg()



try:
     
     pub = rospy.Publisher('gps',gps_msg)
     rospy.init_node('gps_sensor', anonymous=True)
     
     while (not rospy.is_shutdown()):
          line = port.readline().decode()
          
          if 'GPGGA' in line:
               print(line)
               data=line[1:].split(',')
               print(data)
               print('Latitude=' + data[2])
               print('Longitude=' + data[4])
               
               d1=data[3]
               d2=data[5]
               utc=float(data[1])
               
               la=float(data[2])
               lo=float(data[4])
               
               la1=(la)//100
               la2=la-la1*100
               la_d=la1 + la2/60
               
               if d1=='S':
                la_d=la_d*(-1)   
               
               lo1=(lo)//100
               lo2=lo-lo1*100
               lo_d=lo1 + lo2/60
               
               if d2=='W':
                lo_d=lo_d*(-1)
               
               print('Latitude in degrees=' + str(la_d))
               print('Longitude in degrees=' + str(lo_d))
               
               alt=float(data[9])
               
               utch=int(utc/10000)
               utcm=int((utc-utch*10000)/100)
               utcs= int((utc - utch*10000 - utcm*100)*100)
               utch_f=float(utch*3600 + utcm*60 + utcs)
               
               print(utch_f) 
          
           
           
           
               UTM_coordinate = utm.from_latlon(la_d,lo_d)
               print("easting",UTM_coordinate[0],"northing",UTM_coordinate[1],"zone",UTM_coordinate[2],"letter",UTM_coordinate[3])	
               print(UTM_coordinate)
               #f.write(s_UTM)
               msg.Latitude=float(la_d)
               msg.Longitude=float(lo_d)
               msg.Altitude=float(alt)
               msg.UTM_easting=float(UTM_coordinate[0])
               msg.UTM_northing=float(UTM_coordinate[1])
               msg.Zone=int(UTM_coordinate[2])
               msg.Letter=UTM_coordinate[3]
               msg.Header.frame_id ="GPS1_Frame"
               msg.Header.stamp = rospy.Time(utch_f)
          
               pub.publish(msg)
               rate = rospy.Rate(10)
              
               rate.sleep()     
                
           
           
           
           
           
           
           
           
           
           
           
           
         
except rospy.ROSInterruptException:
     port.close()       

except serial.serialutil.SerialException:
     port.close()
 # f.close()

if __name__ =='__main__':
     print(str(line))
     port.close()
     port.close()
     port.close()
     

