import numpy as np
from numpy import asarray
from PIL import Image
import pandas as pd


class ColorCalculator:

    def __init__(self, image_file):
        self.image_file = image_file
        self.image = Image.open(self.image_file)
        self.data = asarray(self.image)
        self.height = self.data.shape[0]
        self.length = self.data.shape[1]
        self.hex_df = []

    def hex_converter(self):
        hex_colors = np.empty([self.height, self.length], dtype="U10")
        for row in range(self.height):
            for col in range(self.length):

                R = str(hex(self.data[row, col, 0])).split('x')[1]
                G = str(hex(self.data[row, col, 1])).split('x')[1]
                B = str(hex(self.data[row, col, 2])).split('x')[1]

                if len(R) != 2:
                    R += '0'
                if len(G) != 2:
                    G += '0'
                if len(B) != 2:
                    B += '0'

                RGB = R + G + B

                hex_colors[row, col] = f'#{RGB}'

        values, counts = np.unique(hex_colors, return_counts=True)

        self.hex_df = pd.DataFrame({'color': values, 'frequency': counts})

        return self.hex_df

    def make_palette(self, color_qty):
        count = 0
        color_palette = []
        self.hex_df = self.hex_df.sort_values(by='frequency', ascending=False)

        for idx, row in self.hex_df.iterrows():
            color_palette.append({
                'color': row['color'],
                'color_pct': round(row['frequency'] / self.hex_df['frequency'].sum() * 100, 2)
            })
            count += 1
            if count == color_qty:
                break

        return color_palette

    def color_count(self):
        return len(self.hex_df)
