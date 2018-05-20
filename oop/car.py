import re

class Car():
    def __init__(self, make, model, year):
        '''初始化描述汽车的属性'''
        self.make = make
        self.model = model
        self.year = year
        '''添加一个初始是为0的类'''
    def get_describe_name(self):
        '''返回整洁的描述性信息.'''
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model

        return long_name

print("---------")
my_new_car = Car('audi', 'a4', '2018')
print(my_new_car.get_describe_name())
print("改变没有呢")
print("测试集体改变")
print("测试集体改变")
print("测试，传送")
print("转换不同项目，然后切换到回来，是否托管")
