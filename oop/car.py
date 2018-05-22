"""
    每个模块都应有的必要的概述信息，
    一个可以用于表示汽车的类，
    包括四个属性和四个方法
"""


class Car():

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descirptive_name(self):
        """返回整洁性的描述信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name

    def read_odometer(self):
        """打印一条汽车里程的信息"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """更新指定里程"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("Forbidden!!!")
    def incerment_odometer(self, miles):
        """增加里程"""
        self.odometer_reading += miles
