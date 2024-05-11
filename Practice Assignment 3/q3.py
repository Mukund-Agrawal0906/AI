import pandas as pd
import numpy as np
from PIL import Image

img = Image.open('image.jpg')
img_array = np.array(img)
df = pd.DataFrame(img_array.reshape(-1, img_array.shape[-1]))
df.to_csv('image.csv', index=False)
df = pd.read_csv('image.csv', header=None)
df = df.iloc[:-1, :-1]
df.to_excel('image.xlsx',index=False, header=False)
