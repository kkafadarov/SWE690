import markovify
import sys
import csv

# Configure the CSV reader to allow for very large files
csv.field_size_limit(sys.maxsize)


print 'Generating the articles markov model.'
articles = []
article_titles = []
with open('articles_data/articles1.csv') as articles1_csv:
  csv_reader = csv.reader(articles1_csv, delimiter=',')
  line_count = 0
  for row in csv_reader:
    if line_count == 0:
      print ('Column names are %s' % ", ".join(row))
    else:
      articles.append(row[-1])

    line_count +=1

print 'Training the markov model'
articles_model = markovify.Text(articles)

print 'Exporting'
model_json = articles_model.to_json()

print 'Writing to disk'
with open('articles1_model.json', 'w+') as f:
  f.write(model_json)

print 'Done!'


print 'Generating the tweets markov model.'
tweets = []
with open('tweets_data/training.1600000.processed.noemoticon.csv') as tweets_csv:
  csv_reader = csv.reader(tweets_csv, delimiter=',')
  row_num = 0
  for row in csv_reader:
    row_num += 1
    try:
      tweets.append(unicode(row[-1], 'latin-1'))
    except:
      print 'Error parsing row ' + str(row_num)

print 'Training the markov model'
tweets_model = markovify.Text(tweets)

print 'Exporting'
tweets_json = tweets_model.to_json()

print 'Writing to disk'
with open('tweets_model.json', 'w+') as f:
  f.write(tweets_json)

print 'Done!'
