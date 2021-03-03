class FanQin(object):
    #公有
    def fangzi1(self):
        print("fanzi1")
    #私有
    def __fanzi2(self):
        print("fanzi2")


class XiaoMing(FanQin):
    def __init__(self):
        self.age = 18
        self.name = "小明"

    def ktv(self):
        print("今年我%s" % self.age)
        print("一起去ktv")
        return 2

    def chifan(self,name):
        if name == 1:
            print("一起吃饭")
            return 2

    def play_bbs(self):
        print("打游戏")
    #重写方法
    def fangzi1(self):
        print("fanzicongxie")
xiaoMing=XiaoMing()
print(xiaoMing.fangzi1())

# if __name__ == '__main__':
#     xiaoMing=XiaoMing()      #实例化
#     xiaoMing.age     #调用属性
#     xiaoMing.name     #调用属性
#
#     # xiaoMing.chifan() #调用方法
#     print(xiaoMing.chifan(1))
#     print()