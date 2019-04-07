from flask import Flask, render_template, Response
import os
from os import walk

photo_to_show = os.path.join('static','images')
print(photo_to_show)
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = photo_to_show

@app.route('/')
def hello():
    filename=[]
    for (dirpath, dirnames, filenames) in walk(app.config['UPLOAD_FOLDER']):
            for i in range(6):
                filename.append(os.path.join(app.config['UPLOAD_FOLDER'], filenames[i]))
                render_template('index.html', user_image = filename)
    return render_template('index.html', user_image = filename)


if __name__ == '__main__':
    app.run()