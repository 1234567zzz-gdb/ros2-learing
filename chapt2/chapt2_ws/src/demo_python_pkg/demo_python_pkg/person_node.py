class PersonNode:
    def __init__(self, name_value:str, age_value:int) -> None:
        self.name = name_value
        self.age = age_value
    def eat(self, food_name:str) -> None:
        print(f"{self.name} , {self.age} is eating {food_name}.")


def main():
    node = PersonNode('xllll', 25)
    node.eat('apple')