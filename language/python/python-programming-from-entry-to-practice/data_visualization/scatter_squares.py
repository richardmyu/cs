import matplotlib.pyplot as plt

# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 4, 9, 16, 25]

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

# c 改变数据点的颜色
# cmap 颜色映射
# edgecolors 删除数据点的轮廓
# s 设置折线的宽度
plt.scatter(x_values, y_values, c=x_values, cmap=plt.cm.Blues, edgecolors='none', s=1)

plt.title('Square Numbers', fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Square of Value', fontsize=14)

plt.tick_params(axis='both', which='major', labelsize=14)

# 设置坐标轴取值范围
plt.axis([0, 1100, 0, 1100000])

# 自动保存
plt.savefig('square_plot.png', bbox_inches='tight')
plt.show()
