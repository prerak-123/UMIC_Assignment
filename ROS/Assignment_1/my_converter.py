#!/usr/bin/env python

import rospy
from umic_assignment.msg import EulerAngles
from umic_assignment.msg import Quaternion
from math import atan2, asin

def quaternion_to_euler_angle(x, y, z, w):
    roll = atan2(2*(x*y + z*w), 1-2*(y*y+z*z))
    pitch = asin(2*(x*z - w*y))
    yaw = atan2(2*(x*w + y*z), 1 - 2*(z*z + w*w))
    
    return [roll, pitch, yaw]

def talker(angles):
    pub = rospy.Publisher('topic2', EulerAngles, queue_size=10)
    if not rospy.is_shutdown():
        output = str(angles[0]) + " " + str(angles[1]) + " " + str(angles[2])
        rospy.loginfo(output)
        msg = EulerAngles()
        msg.roll = angles[0]
        msg.pitch = angles[1]
        msg.yaw = angles[2]
        pub.publish(msg)

    
def callback(data):
    angles = quaternion_to_euler_angle(data.x, data.y, data.z, data.w)
    talker(angles)
    
def listener():
    rospy.init_node('my_converter', anonymous=True)
    rospy.Subscriber("topic1", Quaternion, callback)
    rospy.spin()
    
if __name__ == '__main__':
    listener()