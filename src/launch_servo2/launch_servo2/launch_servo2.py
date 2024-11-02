import rclpy
from rclpy.node import Node
from std_msgs.msg import Int64
from geometry_msgs.msg import Twist
import serial

class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        # self.ser=serial.Serial('/dev/ttyUSB0',115200)
        self.subscription = self.create_subscription(
            Int64,
            'topic_servo_cjh',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning
        
        self.teleop_sub = self.create_subscription(
            Twist,
            'cmd_vel',
            self.teleop_callback,
            10)

    def teleop_callback(self, msg):
        self.get_logger().info(
            '\n linear.x:"%s", \n linear.y: "%s",\n linear.z: "%s", \n angular.x: "%s", \n angular.y: "%s", \n angular.z: "%s"' 
            % (msg.linear.x, msg.linear.y, msg.linear.z, msg.angular.x,msg.angular.y,msg.angular.z)
            )


    def listener_callback(self, msg):
        self.get_logger().info('Degree: "%s"' % msg.degree)
        angle=str(msg.degree)+'\n'
        self.ser.write(angle.encode())


def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()