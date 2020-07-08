# encoding = utf-8
"""
自己写一个面向对象的例子
描述：
创建一个类（Animal）【动物类】，类里有属性（名称，颜色，年龄，性别），类方法（会叫，会跑）

创建子类【猫】，继承【动物类】，
- 复写父类的__init__方法，继承父类的属性，
- 添加一个新的属性，毛发=短毛，
- 添加一个新的方法， 会捉老鼠，
- 复写父类的‘【会叫】的方法，改成【喵喵叫】

创建子类【狗】，继承【动物类】，
- 复写父类的__init__方法，继承父类的属性，
- 添加一个新的属性，毛发=长毛，
- 添加一个新的方法， 会看家，
- 复写父类的【会叫】的方法，改成【汪汪叫】

创建一个猫猫实例
- 调用捉老鼠的方法
- 打印【猫猫的姓名，颜色，年龄，性别，毛发，捉到了老鼠】。

创建一个狗狗实例
- 调用【会看家】的方法
- 打印【狗狗的姓名，颜色，年龄，性别，毛发】。
4、使用 yaml 来管理实例的属性
5、提交代码到自己的github仓库， 贴到作业贴上
"""
import pytest
import yaml

class Animal:
    name: str = "default"
    colour: str = "default"
    age: int = 5
    gender: str = "男"

    def __init__(self, name, colour, age, gender):
        self.name = name
        self.colour = colour
        self.age = age
        self.gender = gender

    def bark(self):
        print(f"{self.name} can bark")

    def run(self):
        print(f"{self.name} can run")

class Cat(Animal):

    def __init__(self, name, colour, age, gender, hair: str = '短毛'):
        self.name = name
        self.colour = colour
        self.age = age
        self.gender = gender
        self.hair = hair

    def catch_mice(self):
        #- 打印【猫猫的姓名，颜色，年龄，性别，毛发，捉到了老鼠】。
        print(f"{self.name}，{self.colour}, {self.age}, {self.gender}, {self.hair}, 捉到了老鼠")

    def bark(self):
        print(f"{self.name} 喵喵叫")

class Dog(Animal):
    def __init__(self, name, colour, age, gender, hair: str = '长毛'):
        self.name = name
        self.colour = colour
        self.age = age
        self.gender = gender
        self.hair = hair

    def lookafter_home(self):
        #打印【狗狗的姓名，颜色，年龄，性别，毛发】。
        print(f"{self.name}，{self.colour}, {self.age}, {self.gender}, {self.hair}")

    def bark(self):
        print(f"{self.name} 汪汪叫")


if __name__ == '__main__':
    with open("attribute.yml", 'rb') as f:
        data = yaml.safe_load(f)

    #print(data)
    data_cat = data["cat"]
    #print(data_cat['name'])
    cat = Cat(data_cat['name'], data_cat['colour'], data_cat['age'], data_cat['gender'])
    cat.catch_mice()

    data_dog = data["dog"]
    dog = Dog(data_dog['name'], data_dog['colour'], data_dog['age'], data_dog['gender'])
    dog.lookafter_home()
