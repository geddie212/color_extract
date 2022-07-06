import numpy as np
from PIL import Image
from numpy import asarray
import pandas as pd
import math

image = Image.open('profile2.jpg')

data = asarray(image)

hex_dict = {
    '0': '0', '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9', '10': 'A',
    '11': 'B', '12': 'C', '13': 'D', '14': 'E', '15': 'F'
}

R_full = 0
R_dec = 0
G_full = 0
G_dec = 0
B_full = 0
B_dec = 0

hex_colors = np.empty([566, 566], dtype="U10")

for x in range(len(data[:, 0, 0])):
    for y in range(len(data[0, :, 0])):
        R_full = math.floor(data[x, y, 0] / 16)
        G_full = math.floor(data[x, y, 1] / 16)
        B_full = math.floor(data[x, y, 2] / 16)
        R_dec = ((data[x, y, 0] / 16) - R_full) * 16
        G_dec = ((data[x, y, 1] / 16) - G_full) * 16
        B_dec = ((data[x, y, 2] / 16) - B_full) * 16

        hex_colors[x, y] = f'#{hex_dict[str(R_full)]}{hex_dict[str(int(R_dec))]}{hex_dict[str(G_full)]}' \
                           f'{hex_dict[str(int(G_dec))]}{hex_dict[str(B_full)]}{hex_dict[str(int(B_dec))]}'

values, counts = np.unique(hex_colors, return_counts=True)
print(values)
print(counts)

df = pd.DataFrame(list(zip(values, counts)), columns=['color', 'frequency'])

df = df.sort_values(by='frequency', ascending=False)

print(df.head())

# df = pd.DataFrame(hex_colors)
# df = df.astype('string')
# print(df[1].value_counts())
