#!/usr/bin/env python

from math import pi
import rospy
from geometry_msgs.msg import Twist

def arc(angle, radius): #anticlockwise
    
    speed = 0.5
    angular_speed = speed/radius
    
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()
    
    vel_msg.linear.x = speed
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = angular_speed
    
    while not rospy.is_shutdown():
        t0 = rospy.Time.now().to_sec()
        current_angle = 0
        
        while(current_angle < angle):
            velocity_publisher.publish(vel_msg)
            t1 = rospy.Time.now().to_sec()
            current_angle = angular_speed*(t1-t0)

        vel_msg.linear.x = 0
        vel_msg.angular.z = 0
        velocity_publisher.publish(vel_msg)
        return

def straight_line(distance):
    
    speed = 1
    
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()
    
    vel_msg.linear.x = speed
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0
    
    while not rospy.is_shutdown():
        t0 = rospy.Time.now().to_sec()
        current_distance = 0
        
        while(current_distance <= distance):
            velocity_publisher.publish(vel_msg)
            t1 = rospy.Time.now().to_sec()
            current_distance = speed*(t1 - t0)
        
        vel_msg.linear.x = 0
        velocity_publisher.publish(vel_msg)
    
        return    
        
def rotate(angle): #Anticlockwise rotation
    
    angular_speed = 1
    angular_velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()
    vel_msg.linear.x=0
    vel_msg.linear.y=0
    vel_msg.linear.z=0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = angular_speed

    while not rospy.is_shutdown():
        t0 = rospy.Time.now().to_sec()
        current_angle = 0
        while(current_angle < angle):
            angular_velocity_publisher.publish(vel_msg)
            t1 = rospy.Time.now().to_sec()
            current_angle = angular_speed*(t1-t0)
            
        vel_msg.angular.z = 0
        angular_velocity_publisher.publish(vel_msg)
    
        return        
if __name__ == '__main__':
    try:
        rospy.init_node('my_initials', anonymous=True)
        
        arc(pi, 1.5)
        rotate(pi/2)
        straight_line(6)        
 
    except rospy.ROSInterruptException: pass