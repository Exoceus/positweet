from flask import Flask, render_template, url_for, request, redirect
from sentiment_analysis import sentiment_analysis

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('Index.html')


@app.route('/analysis', methods=['POST', 'GET'])
def boi():
    if request.method == 'POST':
        username = request.form['user']
        return redirect(url_for('sentiment', username=username))


@app.route('/user/<username>')
def sentiment(username):
    percent_negative, percent_positive, percent_neutral, pos_array, neg_array = sentiment_analysis(
        username=username, count=200)

    negative_percentage = str(percent_negative)
    negative_tweets = neg_array

    positive_percentage = str(percent_positive)
    positive_tweets = pos_array

    neutral_percentage = str(percent_neutral)

    return render_template('sentiment.html', negative_percentage=negative_percentage, negative_tweets=negative_tweets, positive_percentage=positive_percentage, positive_tweets=positive_tweets, neutral_percentage=neutral_percentage)


if __name__ == '__main__':
    app.run(debug=True)
