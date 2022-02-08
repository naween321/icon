from flask import Flask, send_file
from PIL import Image, ImageFont, ImageDraw

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>ICON PROJECT</h1>'


@app.route('/static/')
def stat():
    return '<h1>ICON PROJECT</h1>'


@app.route('/static/<placeholder>/')
def get_icon(placeholder):
    placeholder = placeholder.upper()[0:2]
    try:
        return send_file(f'static/{placeholder}.png', mimetype='image/gif')
    except:
        icon = Image.open("static/theme_color.png")
        edit = ImageDraw.Draw(icon)
        font = ImageFont.truetype("salmapro.otf", 25)
        w, h = edit.textsize(placeholder, font=font)
        edit.text(((50-w)/2, (50-h)/2), placeholder, (255, 255, 255), font=font)
        icon.save(f'static/{placeholder}.png')
        return send_file(f'static/{placeholder}.png', mimetype='image/gif')


if __name__ == '__main__':
    app.run()
