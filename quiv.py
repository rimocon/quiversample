import numpy as np
import matplotlib.pyplot as plt
XL = 5
YL = 5
x = np.arange(-XL,XL,1)
y = np.arange(-YL,YL,1)
X,Y = np.meshgrid(x,y)
plt.figure()
a = np.array([[0,0],
              [-3,0]])

U = a[0][0] * X + a[0][1] * Y
V = a[1][0] * X + a[1][1] * Y

plt.quiver(X,Y,U,V,color='black',angles='xy',scale_units='xy', scale=4.5)
plt.xlim(-XL,XL)
plt.ylim(-YL,YL)
plt.savefig("images/i.png")
plt.show()