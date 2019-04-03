#!/usr/bin/python

import rospy
import numpy as np
from sensor_msgs.msg import CompressedImage
from sensor_msgs.msg import Image

import cv2
from cv_bridge import CvBridge

class visualConversion():
    def __init__(self):
        self.image_sub = rospy.Subscriber('unity',CompressedImage,self.image_callback)
        self.image_pub = rospy.Publisher('unity/image_raw', Image, queue_size=1)
        self.rate = rospy.Rate(60)

    def image_callback(self, msg):
        self.bridge = CvBridge();
        image = self.bridge.compressed_imgmsg_to_cv2(msg);

        #------------------------------------
        #TESTING ONLY:
        #Get the byte array from the msg
        #arr = msg.data
        #print(arr)-shows encryption
        # 
        #cv2.imwrite("test.jpg",image);
        #cv2.imshow("",image);
        #cv2.waitKey(1);
        #------------------------------------

        #Do conversion from cv2 image to bgr8 image and publish
        msg = self.bridge.cv2_to_imgmsg(image, encoding="bgr8")
        self.image_pub.publish(msg)
	self.rate.sleep()
	
if(__name__ == '__main__'):
    rospy.init_node('visualConversion')
    node = visualConversion()
    rospy.spin()
