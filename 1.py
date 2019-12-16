import matplotlib.pyplot as plt
import matplotlib
import numpy as np 

# 设置行名
columns = ['一','二','三','四','五','六','七','八','九','十','十一','十二']

# 设置数据
data1 = [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3]
data2 = [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3]

zhfont1 = matplotlib.font_manager.FontProperties(fname="c:/windows/fonts/msyh.ttc") 

plt.xlabel('降水量',fontproperties=zhfont1)
plt.ylabel('月份',fontproperties=zhfont1)

plt.plot(columns, data1)
plt.plot(columns, data2)
plt.show()
# 主标题与副标题
# plt.title('一年的降水量与蒸发量')


# line=Line('折线图',"一年的降水量与蒸发量")
# line.add("降水量", columns, data1, is_label_show=True)
# line.add("蒸发量", columns, data2, is_label_show=True)
# line.render()
