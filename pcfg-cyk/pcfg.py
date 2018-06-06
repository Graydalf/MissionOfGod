# coding=utf-8

class Stack(object):
    # 初始化栈为空列表
    def __init__(self):
        self.pools = []

    # 判断栈是否为空
    def is_empty(self):
        return size() == 0

    # 获取栈顶元素，不出栈
    def peek(self):
        return self.pools[len(self.pools) - 1]

    # 返回栈的大小
    def size(self):
        return len(self.pools)

    # 入栈
    def push(self, item):
        self.pools.append(item)

    # 出栈
    def pop(self):
        return self.pools.pop()

class Node(object):
    def __init__(self, arg):
        self.arg = arg
        self.nodes = []


def train():
	# ( (IP-HLN (NP-SBJ (NP-PN (NR 上海) 
	# 			         (NR 浦东)
	# 			   )  
	# 			  (NP (NN 开发) 
	# 	              (CC 与) 
	# 	              (NN 法制) 
	# 	              (NN 建设)
	# 			  )
	# 	   ) 
	#       (VP (VV 同步))) ) 
    with open('./ref/train.tree', 'r', encoding='utf-8') as f:
        print(f.readline())

def main():
    print("Hello World!")
    train()

if __name__ == '__main__':
    main()






