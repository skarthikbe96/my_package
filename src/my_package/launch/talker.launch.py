from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='demo_nodes_cpp',
            executable='talker'
        )
    ])


#install(DIRECTORY launch
# DESTINATION share/${PROJECT_NAME}
# )

# in CMakeList file
#  tell colcon how to run the launch file 