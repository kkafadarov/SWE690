import markovify
import sys
import csv

# Configure the CSV reader to allow for very large files
csv.field_size_limit(sys.maxsize)

# TODO(Kiril): Expand this to more than 100 articles

articles = []
article_titles = []
with open('articles_data/articles1.csv') as articles1_csv:
  csv_reader = csv.reader(articles1_csv, delimiter=',')
  line_count = 0
  for row in csv_reader:
    if line_count == 0:
      print ('Column names are %s' % ", ".join(row))
    else:
      article_titles.append(row[2])
      # TODO(Kiril): Build the model with articles included as well.
      # articles.append(row[-1])

    line_count +=1

print 'Training the markov model'
titles_model = markovify.Text(article_titles)

print 'Generating samples: '
print '--------------------'
for i in range(10):
    print(titles_model.make_short_sentence(140))
    print '------------------------'