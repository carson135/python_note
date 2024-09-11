import matplotlib.pyplot as plt

x_values = range(1, 101)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')
#squares =  [1,4,9,16,25]
fig, ax = plt.subplots()
# ax.plot(x_values, y_values, linewidth = 3)
ax.scatter(x_values, y_values, s=10)

plt.show()