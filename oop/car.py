import re


class Car():
    def __init__(self, make, model, year):
        """
            初始化描述汽车的属性
            :param make:
            :param model:
            :param year:
        """
        self.make = make
        self.model = model
        self.year = year
        # 添加一个初始是为0的类
        self.odometer_reading = 0

    def get_describe_name(self):
        # 返回整洁的描述性信息.
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        # 传参
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("FIB Forbidden!!!")
    def incremnt_odometer(self,miles):
        # 将里程表读数增加指定的量
        self.odometer_reading += miles



my_new_car = Car('audi', 'a4', '2018')
print(my_new_car.get_describe_name())
my_new_car.read_odometer()

# 修改属性的方式
# 使用句点表示法直接访问属性然后直接修改
my_new_car.odometer_reading = 22
my_new_car.read_odometer()

# 另一种方法：通过方法修改属性的值
my_new_car.update_odometer(40)
my_new_car.read_odometer()

my_new_car.update_odometer(50)
my_new_car.read_odometer()

# 比如还可以对属性的值进行递增
my_new_car.read_odometer()
my_new_car.incremnt_odometer(10)
my_new_car.read_odometer()

# Try To Try

