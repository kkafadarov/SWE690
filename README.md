# SWE690
ITU Capstone Project

# Set Up
- Ensure you have `pip` and python2.7 installed (https://packaging.python.org/tutorials/installing-packages/).
- run `pip install markovify`
- Download the articles training training data from https://www.kaggle.com/account/login?returnUrl=%2Fsnapcrack%2Fall-the-news%2Fversion%2F4
- Also download the tweets training data from https://www.kaggle.com/kazanova/sentiment140
- Unzip the articles data under `articles_data` and the tweets under `tweets_data` 
- Run `python trainer.py`. The process will take a few minutes to generate the ML models.

# Running the web app
- `pip install flask`
- Run `FLASK_APP=web/server.py flask run` from the root folder of the project.
- The app should now be running at `localhost:5000`
