#! /usr/bin/env python

from __future__ import print_function
import rospy
import sys

import actionlib

import umic_assignment.msg

def sum_client(a, b):
    client = actionlib.SimpleActionClient('sum', umic_assignment.msg.SumAction)

    client.wait_for_server()

    goal = umic_assignment.msg.SumGoal(num1 = a, num2 = b)

    client.send_goal(goal)

    client.wait_for_result()

    return client.get_result()  

if __name__ == '__main__':
    try:
        rospy.init_node('sum_client')
        num1 = 10
        num2 = 20
        result = sum_client(num1, num2)
        print("Sum = " + str(result.sum))
    except rospy.ROSInterruptException:
        print("program interrupted before completion", file=sys.stderr)