import rclpy
from rclpy.node import Node

def main():
    rclpy.init()
    node = Node('python_node')
    node.get_logger().info('Hello from Python node!')
    rclpy.spin(node)
    rclpy.shutdown()