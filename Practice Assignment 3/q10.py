import numpy as np

scores = np.array([85, 92, 75, 85, 90, 92, 85, 75, 85, 92, 75, 85, 90, 92, 85, 75, 85, 92])

frequency_85 = np.sum(scores == 85)

print(f"The frequency of the score 85 is {frequency_85}")
