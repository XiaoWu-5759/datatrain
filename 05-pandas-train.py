import pandas as pd
import numpy as np

b = pd.Series(np.arange(10))

d = pd.DataFrame(np.arange(10).reshape(2,5))

# 创建一个字典
cl = {"城市": ["北京", "上海", "广州", "深圳", "沈阳"],
      "环比": [101.5, 101.2, 101.3, 102.0, 100.1],
      "同比": [120.7, 127.3, 119.4, 140.9, 101.4],
      "定基": [121.4, 127.8, 120.0, 145.5, 101.6]
      }
c = pd.DataFrame(cl,index=['c1','c2', 'c3', 'c4', 'c5'])

# print(b)
# print(d)
print(c)
# print(c['同比'])
# print(c.loc['c1'])
# print(c['同比']['c2'])  # 顺序不能颠倒