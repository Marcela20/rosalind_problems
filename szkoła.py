import numpy as np
import matplotlib.pyplot as plt
a0 = np.mean([28.266, 25.575, 27.715])

a2 = np.mean([207.981, 194.779, 189.418])
a4 = np.mean([296.834, 309.200, 291.095])
a6 = np.mean([428.248, 434.136, 407.886])
a8 = np.mean([499.246, 473.697, 492.467])
y = [a0, a2, a4, a6, a8]
print(y)
plt.plot([0, 2, 4, 6, 8], y, "ro")
plt.xlabel("stężenia choloesterolu")
plt.ylabel("absorbancja")
plt.show()


