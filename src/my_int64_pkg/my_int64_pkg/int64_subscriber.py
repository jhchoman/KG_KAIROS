import rclpy
from rclpy.node import Node
from std_msgs.msg import Int64
import serial

class Int64SubscriberArduino(Node):

    def __init__(self):
        super().__init__('int64_subscriber_arduino')
        self.subscription = self.create_subscription(
            Int64,
            'int64_topic',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning
        
        # 시리얼 통신 설정 (아두이노 연결)
        self.arduino = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)
        self.get_logger().info('Int64 Subscriber Node with Arduino started')

    def listener_callback(self, msg):
        self.get_logger().info(f'Received: {msg.data}')
        # 아두이노로 데이터 전송
        self.arduino.write(f"{msg.data}\n".encode())

def main(args=None):
    rclpy.init(args=args)
    node = Int64SubscriberArduino()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
