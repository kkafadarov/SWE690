import markovify

from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


articles_model = None
with open('articles1_model.json', 'r+') as f:
  print 'Reading the articles markov model.'
  data = f.read()
  print 'Restoring model.'
  articles_model = markovify.Text.from_json(data)
  print 'Done.'

tweets_model = None
with open('tweets_model.json', 'r+') as f:
  print 'Reading the tweets markov model.'
  data = f.read()
  print 'Restoring model.'
  tweets_model = markovify.Text.from_json(data)
  print 'Done.'

@app.route("/")
def index_page():
  return render_template('index.html')

@app.route('/generate')
def generate_text():
  text_type  = request.args.get('textType', '')
  length  = int(request.args.get('length', 300))
  
  model = None
  if text_type == 'article':
    model = articles_model
  elif text_type == 'tweet':
    model = tweets_model
  else:
    return 'Unrecognized text type'
  
  # Generate a sentence within 10% of the target character count.
  if length < 300:
    return model.make_short_sentence(length, length - 50, tries=200, test_output=False)

  return generate_composite_text(model, length)

def generate_composite_text(model, length):
  output = '\t'
  current_paragraph_length = 0

  while len(output) + 50 < length:
    sentence = model.make_sentence(tries=200, test_output=False)
    current_paragraph_length += len(sentence)
    output += sentence

    if current_paragraph_length > 550:
      current_paragraph_length = 0
      output += '\n\n\t'
    else:
      output += ' '

  return output