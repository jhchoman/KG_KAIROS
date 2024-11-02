import rclpy
from rclpy.node import Node
from std_msgs.msg import Int64
import random

class Int64Publisher(Node):

    def __init__(self):
        super().__init__('int64_publisher')
        self.publisher_ = self.create_publisher(Int64, 'int64_topic', 10)
        self.timer = self.create_timer(1.0, self.publish_random_number)
        self.get_logger().info('Int64 Publisher Node started')

    def publish_random_number(self):
        msg = Int64()
        msg.data = random.randint(0, 1)  # 0부터 1까지의 랜덤 숫자
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    node = Int64Publisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
