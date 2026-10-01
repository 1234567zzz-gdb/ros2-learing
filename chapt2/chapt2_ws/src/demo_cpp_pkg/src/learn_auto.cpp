#include <iostream>
#include <memory>
#include <algorithm>
#include <functional>

void save_with_free_func(const std::string &filename)
{
    std::cout << "Saving with free function: " << filename << std::endl;
}

class FileSave {
public:
    FileSave() = default;
    ~FileSave() = default;
    void save_with_member_func(const std::string &filename)
    {
        std::cout << "Saving with member function: " << filename << std::endl;
    }
private:
};



int main()
{
#if 0
    auto x = 5;
    auto y = 3.14f;
    auto z = 'a';
    std::cout << x << " " << y << " " << z << std::endl;
    auto p1 = std::make_shared<std::string>("Hello, World!");
    std::cout << p1.get() << " " << p1.use_count() <<std::endl;
    auto p2 = p1;
    std::cout << p1.get() << " " << p1.use_count() <<std::endl;
    std::cout << p2.get() << " " << p2.use_count() <<std::endl;
    p1.reset();
    std::cout << p1.get() << " " << p1.use_count() <<std::endl;
    std::cout << p2.get() << " " << p2.use_count() <<std::endl;

    std::cout << "p2: " << (p2 ? *p2 : "null") << std::endl;

    auto add = [](int a, int b) -> int {return a + b;};
    int result = add(3, 5);
    std::cout << "result: " << result << std::endl;
    auto print = [result]() {std::cout << "result: " << result << std::endl;};
    print();
#endif
    FileSave file_save;
    auto save_with_lambda_func = [](const std::string &filename) {
        std::cout << "Saving with lambda function: " << filename << std::endl;
    };

    //函数包装器
    std::function<void(const std::string &)> save1 = save_with_free_func;
    std::function<void(const std::string &)> save2 = save_with_lambda_func;
    std::function<void(const std::string &)> save3 = std::bind(&FileSave::save_with_member_func, &file_save, std::placeholders::_1);

    save1("file1.txt");
    save2("file2.txt");
    save3("file3.txt");
    return 0;
}