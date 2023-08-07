from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='demo_nodes_py',
            executable='listener'
        )
    ])


#   <exec_depend>demo_nodes_cpp</exec_depend>
#   <exec_depend>demo_nodes_py</exec_depend>