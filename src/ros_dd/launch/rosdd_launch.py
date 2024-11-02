from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    # 패키지 이름과 URDF 파일 이름 설정
    pkg_name = 'ros_dd'
    urdf_file_name = 'ros_dd.urdf'
    rviz_file_name = 'ros_dd.rviz'  # RViz 설정 파일이 있다면 사용

    # 패키지 공유 디렉토리 가져오기
    pkg_share = get_package_share_directory(pkg_name)

    urdf_file = os.path.join(pkg_share, 'urdf', urdf_file_name)
    rviz_config_file = os.path.join(pkg_share, 'rviz', rviz_file_name)

    # URDF 파일 읽기
    with open(urdf_file, 'r') as infp:
        robot_description = infp.read()

    # joint_state_publisher_gui 사용 (GUI가 필요한 경우)
    joint_state_publisher_node = Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui',
        name='joint_state_publisher_gui'
    )

    # wheel_publisher 노드 추가
    wheel_publisher_node = Node(
        package='ros_dd',
        executable='wheel_publisher',
        name='wheel_publisher'
    )


    # robot_state_publisher 노드
    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        parameters=[{'robot_description': robot_description}]
    )

    # RViz 노드
    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        arguments=['-d', rviz_config_file]
    )

    return LaunchDescription([
        wheel_publisher_node,
        joint_state_publisher_node,
        robot_state_publisher_node,
        rviz_node
    ])
if __name__ =='__main__':
    generate_launch_description()