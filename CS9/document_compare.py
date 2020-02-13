import sys
from vector import Vector
from sketch import Sketch

# 测试文档列表
filenames = ['华夏.txt', '中国.txt', '炎黄子孙.txt']
k = 5 #k-grams
d = 10000 #文档摘要维度
sketches = [0 for i in filenames]
for i in range(len(filenames)):
    with open(filenames[i], 'r', encoding='UTF-8') as f:
        text = f.read()
        sketches[i] = Sketch(text, k, d)

# 输出结果标题
print(' ' * 20, end = ' ')
for filename in filenames:
    print('{:>25}'.format(filename), end = ' ')
print()

# 输出结果比较明细
for i in range(len(filenames)):
    print('{:10}'.format(filenames[i]), end = ' ')
    for j in range(len(filenames)):
        print('{: <22}'.format(sketches[i].similarTo(sketches[j])), end = ' ')
    print()

