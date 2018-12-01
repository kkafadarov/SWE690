from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route("/")
def index_page():
  return render_template('index.html')

@app.route('/generate')
def generate_text():
  text_type  = request.args.get('textType', '')
  length  = request.args.get('length', '')
  return 'Type: ' + text_type + ' length ' + length
