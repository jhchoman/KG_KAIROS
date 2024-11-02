#!/usr/bin/env python3
from geometry_msgs.msg import Twist
from sensor_msgs.msg import JointState
from rclpy.node import Node
import rclpy
import time

class jdamr_driver(Node): 
    def __init__(self):
        super().__init__('jdamr_driver')

        # Create a publisher that will publish to the /joint_states topic
        self.publisher_ = self.create_publisher(JointState, '/joint_states', 10)
        self.cmd_vel_sub = self.create_subscription(Twist, 'cmd_vel', self.cmd_vel_callback, 10)
        
        # Set a timer to publish at a specified rate (20 Hz in this case)
        self.timer = self.create_timer(0.05, self.publish_joint_states)
        
        # Initialize the JointState message
        self.joint_state = JointState()
        self.joint_state.name = ['wheel1_joint', 'wheel2_joint', 'wheel3_joint', 'wheel4_joint']
        self.joint_state.position = [0.0, 0.0, 0.0, 0.0]
        
        self.position = 0.0
        self.isRun = False

    def publish_joint_states(self):
        if self.isRun:
            self.position += 0.1
            if self.position > 3.14:
                self.position = -3.14

        # Update the timestamp
        self.joint_state.header.stamp = self.get_clock().now().to_msg()
        
        # Update the joint positions with simulated values
        for i in range(4):
            self.joint_state.position[i] = self.position

        # Log the joint positions for debugging
        self.get_logger().info(f'Publishing joint positions: {self.joint_state.position}')

        # Publish the JointState message
        self.publisher_.publish(self.joint_state)

    def cmd_vel_callback(self, msg):
        if isinstance(msg, Twist):
            self.isRun = msg.linear.x != 0 or msg.angular.z != 0
            self.get_logger().info(f"Received cmd_vel: linear={msg.linear.x}, angular={msg.angular.z}")

def main(args=None):
    rclpy.init(args=args)
    driver = jdamr_driver()
    rclpy.spin(driver)
    driver.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
