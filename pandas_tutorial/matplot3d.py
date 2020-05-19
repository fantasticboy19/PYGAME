import numpy as np
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D

# fg = plt.figure(1)
# ax = Axes3D(fg)
#
# x = np.linspace(-4, 4, 32)
# y = np.linspace(-4, 4, 32)
# xv, yv = np.meshgrid(x, y)
# # r = np.sqrt(xv*2+yv)
# # z = np.sin(r)
# z = xv*2+yv
#
# # ax.plot_surface(xv, yv, z, rstride=1,cstride=1, cmap=plt.get_cmap('rainbow'))
# # ax.contourf(xv,yv,z,zdir='z',offset=-1)
# ax.scatter(xv, yv, z)
# # plt.zlim(-2, 2)
# plt.show()

fig = plt.figure('my picture', figsize=(10,20))
ax01 = fig.add_subplot(211)
x = np.linspace(-4, 4, 32)
y = np.linspace(-4, 4, 32)
ax01.plot(x, y)

ax02 = fig.add_subplot(212, projection='3d')
xv, yv = np.meshgrid(x, y)
z = xv*2+yv
ax02.plot_surface(xv, yv, z, rstride=1, cstride=1, cmap=plt.get_cmap('rainbow'))

plt.show()

