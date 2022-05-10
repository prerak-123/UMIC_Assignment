#! /usr/bin/env python

import actionlib
import rospy
import umic_assignment.msg

class SumServer(object):
    _result = umic_assignment.msg.SumResult()

    def __init__(self, name):
        self._action_name = name
        self._as = actionlib.SimpleActionServer(self._action_name, umic_assignment.msg.SumAction, execute_cb=self.execute_cb, auto_start = False)
        self._as.start()
      
    def execute_cb(self, goal):        
        
        rospy.loginfo(goal.num1)
        rospy.loginfo(goal.num2)
                  
        self._result.sum = goal.num1 + goal.num2
        self._as.set_succeeded(self._result)

if __name__ == '__main__':
    rospy.init_node('sum')
    server = SumServer(rospy.get_name())
    rospy.spin()