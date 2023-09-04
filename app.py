from flask import Flask,  render_template
from flask import request
from meme import get_meme

app = Flask (__name__)

@app.route('/')
def index():
    meme_pic, subreddit = get_meme()
    return render_template('index.html',meme_pic=meme_pic, subreddit=subreddit)

app.run(debug = True)


