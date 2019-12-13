#!/usr/bin/env python
#encoding: utf8
import rospy, cv2
import numpy as np
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

class FaceToFace():
    def __init__(self):
        sub = rospy.Subscriber("/cv_camera/image_raw", Image, self.get_image)
        self.pub = rospy.Publisher("red", Image, queue_size=1)
        self.bridge = CvBridge()
        self.image_org = None

    def monitor(self,org):                                 #このメソッドを追加
        bgrLower = np.array([17, 15, 150])    # 抽出する色の下限
        bgrUpper = np.array([128, 191, 255])    # 抽出する色の上限
        img_mask = cv2.inRange(org, bgrLower, bgrUpper)
        org = cv2.bitwise_and(org, org, mask=img_mask)
        self.pub.publish(self.bridge.cv2_to_imgmsg(org, "bgr8"))
   
    def get_image(self,img):
        try:
            self.image_org = self.bridge.imgmsg_to_cv2(img, "bgr8")
        except CvBridgeError as e:
            rospy.logerr(e)

    def detect_face(self):
        if self.image_org is None:
            return None
    
        org = self.image_org
    
        self.monitor(org)   
        
if __name__ == '__main__':
    rospy.init_node('face_to_face')
    fd = FaceToFace()

    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        rospy.loginfo(fd.detect_face())
        rate.sleep()
