from flask import Flask, render_template, request
import os
from color_calculator import ColorCalculator

UPLOAD_FOLDER = 'static/uploads/'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/uploader', methods=['GET', 'POST'])
def upload_img():
    if request.method == 'POST':
        f = request.files['file']
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], f.filename))
        file_name = f.filename.split('.')[0]
        file_location = f'{UPLOAD_FOLDER}{f.filename}'
        col_calc = ColorCalculator(file_location)
        col_calc.hex_converter()
        palette = col_calc.make_palette(10)
        color_count = '{:,}'.format(col_calc.color_count())
        file_size = round(os.stat(file_location).st_size / 1000000, 2)
    return render_template('index.html', palette=palette, file_name=file_name, color_count=color_count,
                           file_size=file_size, file_location=file_location)


@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
