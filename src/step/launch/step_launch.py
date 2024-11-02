from launch import LaunchDescription
from launch_ros.actions import Node
import os
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    urdf_file = os.path.join(
        get_package_share_directory('step'),
        'urdf',
        'step.urdf')

    return LaunchDescription([
        # joint_state_publisher_gui 실행
        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui',
            name='joint_state_publisher_gui',
            output='screen'
        ),
        # robot_state_publisher 실행
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{'robot_description': open(urdf_file).read()}]
        ),
        # RViz 실행 (설정 파일 없이)
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen'
        ),
        # /cmd_vel 토픽을 구독하여 Twist 값을 출력하는 노드
        Node(
            package='step',
            executable='twist_listener_node',
            name='twist_listener',
            output='screen'
        ),
    ])
