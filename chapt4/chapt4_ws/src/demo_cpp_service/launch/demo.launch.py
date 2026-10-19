import launch
import launch_ros

def generate_launch_description():
    #1.生成一个launch参数
    action_declare_arg_background_g = launch.actions.DeclareLaunchArgument('launch_arg_bg',default_value='150')
    #2.把launch的参数手动传递给某个节点
    """产生launch描述"""
    action_node_turtlesim_node = launch_ros.actions.Node(
        package='turtlesim',
        executable='turtlesim_node',
        parameters=[{'background_g': launch.substitutions.LaunchConfiguration('launch_arg_bg',default='150')}],
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
        action_declare_arg_background_g,
        action_node_turtlesim_node,
        action_node_partol_client,
        action_node_turtle_control
    })