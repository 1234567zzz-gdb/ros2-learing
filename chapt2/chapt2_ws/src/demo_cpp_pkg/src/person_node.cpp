#include "rclcpp/rclcpp.hpp"

class PersonNode : public rclcpp::Node
{
private:
    std::string name_;
    int age_;

public:
    PersonNode(const std::string &node_name,const std::string &name,const int &age):Node(node_name), name_(name), age_(age)
    {
        
    }

    void eat(const std::string &food)
    {
        RCLCPP_INFO(this->get_logger(), "我是%s,我正在吃%s", name_.c_str(), food.c_str());
    }
};

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<PersonNode>("person_node", "张三", 20);
    node->eat("苹果");
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}