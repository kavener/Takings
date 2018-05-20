# 学习语法
## 二级标题  
**markdown编辑器**  
Pycharm自带插件：
>引用形式，怎么在github中的readme.md引用自己的图片呢，首先可以上传到github，然后点击下载，复制图片链接地址即可
![我的图片](https://raw.githubusercontent.com/kavener/Takings/master/images/%E7%A4%BA%E4%BE%8BGithub.png)

尝试使用引入代码段：
```python
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
```