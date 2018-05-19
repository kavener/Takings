class Dog():
    '''一次模拟小狗的简单尝试'''
    def __init__(self,name,age):
        '''初始化属性name和年龄'''
        self.name=name
        self.age=age

    def site(self):
        '''模拟小狗被命令时蹲下'''
        print(self.name.title()+"正在蹲着。")

    def roll_over(self):
        '''模拟小狗被命令时打滚'''
        print(self.name.title()+"在打滚！！！")
my_dog = Dog("小黑",2)
#使用句点表示法来获取实例化的类的属性和调用定义的任何方法
print("我家狗叫" + my_dog.name.title() +".")
print("它" + str(my_dog.age) + "岁了")

my_dog.site()
my_dog.roll_over()

#创建任意数量的实例
your_dog=Dog("瓜皮皮",3)
your_dog.site()

'''==========================动手试一试============================'''
class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type

    def describe_restaurant(self):
        print("餐馆名字是" + "“" + self.restaurant_name.title() + "”" + "。")
        print("菜肴类型是" + self.cuisine_type + "。")

    def open_restaurant(self):
        print(self.restaurant_name.title() + "正在营业中。")
my_restuarant=Restaurant("川中餐馆","川菜")
my_restuarant.describe_restaurant()
my_restuarant.open_restaurant()

your_restuarant=Restaurant("湘中菜馆","湘菜")
your_restuarant.describe_restaurant()
your_restuarant.open_restaurant()

his_restuarant=Restaurant("粤中菜馆","粤菜")
his_restuarant.describe_restaurant()
his_restuarant.open_restaurant()

class User():
    def __init__(self,first_name,last_name,sex,age):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.sex=sex

    def describe_user(self):
        full_name=self.first_name.title() + " " + self.last_name
        print(full_name + "is a " + self.sex + " who is " + str(self.age) + " yeas old.")

    def greet_user(self):
        full_name = self.first_name.title() + " " + self.last_name
        if self.sex == "man":
            print("Respected " + full_name + " gentleman,welcome!")
        elif self.sex == "women":
            print("Respected " + full_name + " lady,welcome!")
        else:
            print("user " + full_name +",please input your correct sex in your base information.")
my_user=User("liang","yun","man",20)
my_user.describe_user()
my_user.greet_user()

your_user=User("pu","qian qian","women",18)
your_user.describe_user()
your_user.greet_user()

