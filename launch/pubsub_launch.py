import launch
from launch_ros.actions import ComposableNodeContainer
from launch_ros.descriptions import ComposableNode

def generate_launch_description():
    """Generate launch description with multiple components."""
    container = ComposableNodeContainer(
            name='my_container',
            namespace='',
            package='rclcpp_components',
            executable='component_container',
            composable_node_descriptions=[
                ComposableNode(
                    package='my_composition_package',
                    plugin='my_composition_package::MinimalPublisher',
                    name='talker'),
                ComposableNode(
                    package='my_composition_package',
                    plugin='my_composition_package::MinimalSubscriber',
                    name='listener')
            ],
            output='screen',
    )

    return launch.LaunchDescription([container])

