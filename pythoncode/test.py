
#2、创建模块，模块里面创建方法，定义有参数，和无参数，有返回值和无返回值的情况，并说明无返回值的默认返回值。


def fun1(name):
    return name

def fun2(name):
    name = "fun2"

def fun3():
    name = 'test3'
    return name

def fun4():
    name = 'test4'

print("有参数&有返回值", fun1('test1'))
print("有参数&无返回值", fun2('test2'))
print("无参数有回值", fun3())
print("无参数无回值", fun4())

#无返回值的默认返回None