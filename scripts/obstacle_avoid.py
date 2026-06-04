#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
from pid_controller import PID


class ObstacleAvoidance:

    def __init__(self):

        rospy.init_node("obstacle_avoidance")

        self.pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)
        rospy.Subscriber("/scan", LaserScan, self.callback)

        self.cmd = Twist()

        self.pid = PID(1.5, 0.0, 0.3)
        self.target = 0.6

    def callback(self, msg):

        front = min(min(msg.ranges[0:20]), min(msg.ranges[340:360]))

        control = self.pid.compute(self.target, front)

        self.cmd.linear.x = 0.2
        self.cmd.angular.z = control

        if front < 0.3:
            self.cmd.linear.x = -0.1
            self.cmd.angular.z = 0.8

        self.pub.publish(self.cmd)


if __name__ == "__main__":
    try:
        ObstacleAvoidance()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
