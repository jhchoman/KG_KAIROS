import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import serial  # 시리얼 통신을 위한 라이브러리

class TwistListener(Node):
    def __init__(self):
        super().__init__('twist_listener')
        self.subscription = self.create_subscription(
            Twist,
            '/cmd_vel',
            self.twist_callback,
            10
        )
        # 시리얼 포트 설정 (아두이노가 연결된 포트로 변경해야 합니다)
        self.ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)

    def twist_callback(self, msg):
        linear_x = msg.linear.x
        linear_y = msg.linear.y
        linear_z = msg.linear.z
        angular_x=msg.angular.x
        angular_y=msg.angular.y
        angular_z=msg.angular.z
        self.get_logger().info(f"Received linear: linear.x={linear_x},linear.y={linear_y},linear.z={linear_z}")
        self.get_logger().info(f"Received linear: angular.x={angular_x},angular.y={angular_y},angular.z={angular_z}")

        # linear.x 값에 따라 Arduino로 데이터 전송
        if linear_x >= 1.0:
            self.ser.write(b'1')  # LED 켜기
        else:
            self.ser.write(b'0')  # LED 끄기

def main(args=None):
    rclpy.init(args=args)
    node = TwistListener()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
