from flask import Flask, render_template, Response
import os
from os import walk

photo_to_show = os.path.join('static' , 'images')
print(photo_to_show)
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = photo_to_show

@app.route('/')
def hello():
    for (dirpath, dirnames, filenames) in walk(app.config['UPLOAD_FOLDER']):
            for i in range(6):
                filename = os.path.join(app.config['UPLOAD_FOLDER'], "download (1).jpg")
                return render_template('index.html', user_image = filename)

if __name__ == '__main__':
    app.run()