import os

from flask import render_template
from . import main


slide_dir = 'static/slides/'


@main.route('/')
def index():

    slide_files = [f for f in os.listdir(slide_dir)]
    slide_files_number = len(slide_files)
    return render_template("index.html", slide_files_number=slide_files_number, slide_files=slide_files)

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/<filename>')
def video(filename):
    return render_template('presentation.html', title=filename, slide_file=filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)