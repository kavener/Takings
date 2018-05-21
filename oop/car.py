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

