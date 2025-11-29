# # dispay multiple plots 


# import matplotlib.pyplot as plt 
# import numpy as np

# # plot 1:

# x = np.array([0, 1, 2, 3])
# y = np.array([3, 1, 8, 10])

# plt.subplot(1, 2, 1)
# plt.plot(x, y)

# # plot 2

# x = np.array([0, 1, 2, 3])
# y = np.array([10, 20, 30, 40])

# plt.subplot(1, 2, 3)
# plt.plot(x, y)

# plt.show()



# # the subplot function



# import matplotlib.pyplot as plt
# import numpy as np

# # plot1

# x = np.array([0, 1, 2, 3])
# y = np.array([10, 20, 30, 40])

# plt.subplot(1, 2, 3)
# plt.plot(x , y)

# #plot2

# x = np.array([0, 1, 2, 3])
# y = np.array([10, 20, 30, 40])

# plt.subplot(1, 2, 3)
# plt.plot(x, y)

# plt.show()



import matplotlib.pyplot as plt
import numpy as np

#plot1

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(1, 2, 1)
plt.plot(x, y)
plt.title('SALES')

#plot2

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(1, 2, 2)
plt.plot(x , y)
plt.title('INCOME')

plt.show()



# super title


import matplotlib.pyplot as plt
import numpy as np

#plot1

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(1, 2, 1)
plt.plot(x, y)
plt.title('SALES')

# plot2

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(1, 2, 2)
plt.plot(x, y)
plt.title('INCOME')

plt.suptitle('MY SHOP')
plt.show()