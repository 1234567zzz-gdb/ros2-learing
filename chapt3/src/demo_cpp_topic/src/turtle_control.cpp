#include "rclcpp/rclcpp.hpp"
#include "geometry_msgs/msg/twist.hpp"
#include "turtlesim/msg/pose.hpp"
#include <chrono>

using namespace std::chrono_literals;

class TurtleControlNode : public rclcpp::Node
{
public:
    explicit TurtleControlNode(const std::string& node_name):Node(node_name)
    {
        publisher_ = this->create_publisher<geometry_msgs::msg::Twist>("/turtle1/cmd_vel", 10);
        //timer_ = this->create_wall_timer(1000ms, std::bind(&TurtleControlNode::time_callback, this));
        subscriber_ = this->create_subscription<turtlesim::msg::Pose>("/turtle1/pose",10,std::bind(&TurtleControlNode::on_pose_receiver_, this, std::placeholders::_1));
    }

    void on_pose_receiver_(const turtlesim::msg::Pose::SharedPtr pose) //参数：收到数据的共享指针
    {
        //获取当前位置
        auto current_x = pose->x;
        auto current_y = pose->y;
        RCLCPP_INFO(get_logger(), "当前:x=%f, y=%f", current_x, current_y);

        //计算当前海龟位置和目标位置之间的距离差和角度差
        auto distance = std::sqrt(
            (target_x_ - current_x)*(target_x_ - current_x) +
            (target_y_ - current_y)*(target_y_ - current_y));

        auto angle = std::atan2((target_y_ - current_y), (target_x_ - current_x)) - pose->theta;

        //控制策略
        auto msg = geometry_msgs::msg::Twist();
        if(distance>0.1) {
            if(fabs(angle)>0.2) {
                msg.angular.z = fabs(angle);
            } else {
                msg.linear.x = k_*distance;
            }
        }

        if(msg.linear.x > max_speed_){
            msg.linear.x = max_speed_;
        }

        publisher_->publish(msg);
    }
private:
    rclcpp::Publisher<geometry_msgs::msg::Twist>::SharedPtr publisher_;//发布者智能指针
    rclcpp::TimerBase::SharedPtr timer_;
    rclcpp::Subscription<turtlesim::msg::Pose>::SharedPtr subscriber_;//订阅者智能指针
    double target_x_{1.0};
    double target_y_{1.0};
    double k_{1.0}; //比例系数
    double max_speed_{3.0};
};


int main(int argc, char* argv[])
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<TurtleControlNode>("turtle_control");
    rclcpp::spin(node);

    rclcpp::shutdown();
    return 0;
}