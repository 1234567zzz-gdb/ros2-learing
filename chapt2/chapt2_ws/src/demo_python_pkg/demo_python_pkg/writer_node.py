from demo_python_pkg.person_node import PersonNode

class WriterNode(PersonNode):
    def __init__(self, name_value:str, age_value:int, book_name:str) -> None:
        super().__init__(name_value, age_value)
        self.book = book_name
    def write(self) -> None:
        print(f"{self.name} , {self.age} is writing {self.book}.")

def main():
    node = WriterNode('xllll', 25, 'Python Programming')
    node.eat("鱼香肉丝")
