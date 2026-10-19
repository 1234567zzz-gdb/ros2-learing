import launch
import launch_ros

def generate_launch_description():
    """产生launch描述"""
    action_node_turtlesim_node = launch_ros.actions.Node(
        package='turtlesim',
        executable='turtlesim_node',
        output='screen'
    )
    action_node_partol_client = launch_ros.actions.Node(
        package='demo_cpp_service',
        executable='partol_client',
        output='log'
    )
    action_node_turtle_control = launch_ros.actions.Node(
        package='demo_cpp_service',
        executable='turtle_control',
        output='both'
    )
    return launch.LaunchDescription({
        # action动作
        action_node_turtlesim_node,
        action_node_partol_client,
        action_node_turtle_control
    })