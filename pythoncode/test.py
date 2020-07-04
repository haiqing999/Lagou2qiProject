
#2、创建模块，模块里面创建方法，定义有参数，和无参数，有返回值和无返回值的情况，并说明无返回值的默认返回值。

def fun1(name):
    return name
def fun2():
    name = '李四'

print(fun1('张三'))
#无返回值的默认返回None
print("无返回值的默认返回:", fun2())
