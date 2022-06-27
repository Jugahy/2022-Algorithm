import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
# import warnings warnings.filterwarnings("ignore", category=DeprecationWarning)


malaysian = np.array([3.4270, 0.034300, 0, 82.707, 26.933, 2.2276, 1837.7], dtype=float).reshape((-1, 1))
korea = np.array([1000, 10, 0, 24134, 7859, 650, 536241], dtype=float).reshape((-1, 1))

for i,c in enumerate(malaysian):
	print("%s malaysian = %s korea" % (c, korea[i]))

from sklearn.linear_model import LinearRegression
# create a linear regression model
model = LinearRegression()

# train data
model.fit(korea, malaysian)

# predict data - 30.0 pounds to kilograms
result_malaysian = model.predict([[12345]])

print('12345 korea >> %s malaysian' %(result_malaysian[0][0]))