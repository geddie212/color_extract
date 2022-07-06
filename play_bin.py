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

# R_values, R_counts = np.unique(data[:,:,0], return_index=True)
#
# R_df = pd.DataFrame(list(zip(R_values, R_counts)), columns=['color', 'frequency'])
#
# R_df = R_df.sort_values(by='color')


R_values, R_counts = np.unique(data[:, :, 0], return_counts=True)
R_df = pd.DataFrame({'color': R_values, 'frequency': R_counts})
R_df = R_df.sort_values(by='frequency', ascending=False)
print(R_df.head())

G_values, G_counts = np.unique(data[:, :, 1], return_counts=True)
G_df = pd.DataFrame({'color': G_values, 'frequency': G_counts})
G_df = G_df.sort_values(by='frequency', ascending=False)
print(G_df.head())

B_values, B_counts = np.unique(data[:, :, 2], return_counts=True)
B_df = pd.DataFrame({'color': B_values, 'frequency': B_counts})
B_df = B_df.sort_values(by='frequency', ascending=False)
print(B_df.head())