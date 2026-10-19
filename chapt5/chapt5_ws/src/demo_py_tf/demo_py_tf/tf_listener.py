import rclpy
from rclpy.node import Node
from tf2_ros import TransformListener,Buffer #坐标监听器
from geometry_msgs.msg import TransformStamped #消息接口
from tf_transformations import euler_from_quaternion #四元数转换欧拉角函数
import math #角度转弧度

class TFLister(Node):
    def __init__(self):
        super().__init__('tf_lister')
        self.buffer_ = Buffer()
        self.lister_ = TransformListener(self.buffer_ ,self)
        self.timer_ = self.create_timer(0.01, self.get_transform)
    def get_transform(self):
        """
        定时查询坐标关系
        """

        try:
            result = self.buffer_.lookup_transform('base_link','bottle_link',rclpy.time.Time(seconds=0.0), rclpy.time.Duration(seconds=1.0))
            transform = result.transform
            self.get_logger().info(f'平移：{transform.translation}')
            self.get_logger().info(f'旋转：{transform.rotation}')
            rotation_euler = euler_from_quaternion([
            transform.rotation.x,
            transform.rotation.y,
            transform.rotation.z,
            transform.rotation.w])
            self.get_logger().info(f'旋转RPY：{rotation_euler}')
        except Exception as e:
            self.get_logger().warn(f'获取坐标失败：原因{str(e)}')


def main():
    rclpy.init()
    node = TFLister()
    rclpy.spin(node)
    rclpy.shutdown()