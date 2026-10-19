import rclpy
from rclpy.node import Node
from chapt4_interfaces.srv import FaceDetector
import face_recognition
import cv2
from ament_index_python.packages import get_package_share_directory #获取功能包share目录绝对路径
import os
from cv_bridge import CvBridge
import time
from rcl_interfaces.srv import SetParameters
from rcl_interfaces.msg import Parameter,ParameterValue,ParameterType

class FaceDetectClientNode(Node):
    def __init__(self):
        super().__init__('face_detect_client_node')
        self.bridge = CvBridge()
        self.default_image_path = os.path.join(get_package_share_directory('demo_python_service'), 'resource/test1.jpeg')
        self.get_logger().info(f'人脸检测服务已经启动！')
        self.client = self.create_client(FaceDetector,'face_detect')
        self.image = cv2.imread(self.default_image_path)

    def call_set_parameters(self, parameters):
        """
        调用服务修改参数值
        """
        # 1.创建一个客户端，等待服务上线
        update_param = self.create_client(SetParameters, '/face_detect_node/set_parameters')
        while update_param.wait_for_service(timeout_sec=1.0) is False:
            self.get_logger().info(f'等待出参数更新服务端上线！')
        #2.创建request
        request = SetParameters.Request()
        request.parameters = parameters
        #3.调用服务端更新参数
        future = update_param.call_async(request)
        rclpy.spin_until_future_complete(self,future) # 等待服务端返回响应
        response = future.result()
        return response

    def update_detect_model(self,model='hog'):
        """根据传入的model,构造Parameter，然后call_set_parameter更新服务端的参数"""
        #1.创建参数对象
        param = Parameter()
        param.name = 'model'
        #2.创建 param_val
        param_val = ParameterValue()
        param_val.string_value = model
        param_val.type = ParameterType.PARAMETER_STRING
        param.value = param_val
        #3.请求更新参数
        response = self.call_set_parameters([param])
        for result in response.results:
            self.get_logger().info(f'设置参数结果：{result.successful} {result.reason}')
        

    def send_request(self):
        # 1.判断服务端是否在线
        while self.client.wait_for_service(timeout_sec=1.0) is False:
            self.get_logger().info(f'等待服务端上线！')
        # 2.构造request
        request = FaceDetector.Request()
        request.image = self.bridge.cv2_to_imgmsg(self.image)
        # 3.发生请求并等待处理完成
        future = self.client.call_async(request) #现在的fature并没有包含相应结果，需要等待服务端处理完成才会把结果放到future中
        #while not future.done():
        #    time.sleep(1.0) #休眠等待服务完成,等待服务处理完成，造成当前线程无法再接受来自服务期的返回，导致永远无法完成，future无法返回true
        def result_callback(result_future):
            response = future.result() #获取相应
            self.get_logger().info(f'接受到相应，共检测到{response.number}张人脸，耗时{response.use_time}秒')
            self.show_response(response)

        future.add_done_callback(result_callback)



    def show_response(self,response):
        for i in range(response.number):
            top = response.top[i]
            left = response.left[i]
            right = response.right[i]
            bottom = response.bottom[i]
            cv2.rectangle(self.image,(left,top),(right,bottom),(255,0,0),4)
        cv2.imshow('Face Detecte Result',self.image)
        cv2.waitKey(0) #也是堵塞的，会导致spin无法正常运行

def main():
    rclpy.init()
    node = FaceDetectClientNode()
    node.update_detect_model('hog')
    node.send_request()
    node.update_detect_model('cnn')
    node.send_request()
    rclpy.spin(node)
    rclpy.shutdown()