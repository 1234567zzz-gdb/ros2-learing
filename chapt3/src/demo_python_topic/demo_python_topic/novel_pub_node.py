import rclpy
from rclpy.node import Node
import requests
from example_interfaces.msg import String
from queue import Queue

class NovelPubNode(Node):
    def __init__(self, node_name):
        super().__init__(node_name)
        self.get_logger().info(f'{node_name},启动')
        self.novel_queue = Queue()
        self.novel_publisher = self.create_publisher(String, 'novel', 10)
        self.create_timer(5, self.timer_callback)

    def timer_callback(self):
        if self.novel_queue.qsize() > 0:
            line = self.novel_queue.get()
            msg = String()
            msg.data = line
            self.novel_publisher.publish(msg)
            self.get_logger().info(f'发布小说：{msg}')
    
    def download(self, url):
        response = requests.get(url)
        response.encoding = 'utf-8'
        text = response.text
        self.get_logger().info(f'下载小说：{url}，长度：{len(text)}')
        for line in text.splitlines():
            self.novel_queue.put(line)

def main():
    rclpy.init()
    node = NovelPubNode('novel_pub')
    node.download("http://localhost:8000/novel1.txt")
    rclpy.spin(node)
    rclpy.shutdown()