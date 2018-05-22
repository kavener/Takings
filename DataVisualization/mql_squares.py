from matplotlib import pyplot as plt

squares = [1, 4, 9, 16, 25]
input_valuse = [1, 2, 3, 4, 5]
# 设置样式
plt.plot(input_valuse, squares, linewidth=5)

plt.title("Square Number", fontsize=24)
plt.xlabel("Values", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

plt.tick_params(axis="both", labelsize=14)

plt.show()
