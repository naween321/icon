from flask import Flask, send_file
from PIL import Image, ImageFont, ImageDraw

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>ICON PROJECT</h1>'


@app.route('/static/')
def stat():
    return '<h1>ICON PROJECT</h1>'


@app.route('/icon/<placeholder>/')
def get_icon(placeholder):
    placeholder = placeholder.upper()[0:2]
    icon = Image.open("/home/ubuntu/icon/backend/static/theme_color.png")
    edit = ImageDraw.Draw(icon)
    font = ImageFont.truetype("/home/ubuntu/icon/backend/Lato-Regular.ttf", 20)
    w, h = edit.textsize(placeholder, font=font)
    edit.text(((50-w)/2, (50-h)/2-2), placeholder, (255, 255, 255), font=font)
    icon.save(f'/home/ubuntu/icon/backend/static/{placeholder}.png')
    return send_file(f'/home/ubuntu/icon/backend/static/{placeholder}.png', mimetype='image/gif')


if __name__ == '__main__':
    app.run()
