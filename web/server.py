from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def index_page():
    return render_template('index.html')

@app.route('/generate/<string:text_type>')
def generate_text(text_type):
    # show the post with the given id, the id is an integer
    return 'Hi - this is a sample but you asked for text type %s' % text_type