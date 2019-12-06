from flask import Flask, render_template, request
import brains
from rate_me import movie_list_gen


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profiling')
def profiling():
    return render_template('profiling.html')


@app.route('/multiprofiling')
def multi_profiling():

    movies_to_rate = movie_list_gen()

    return render_template('multiprofiling.html', movies=movies_to_rate)

    # user_input = request.args
    # user_input = dict(user_input).values
    # user_top_movies = list(user_input)[0:-2]
    # user_worst_movies = list(user_input)[-1:]

    # recommended_list = deep_recommender(1, user_top_movies, user_worst_movies)


    return render_template('multiprofiling.html')


@app.route('/recommend', methods="PUSH")
def recommend():
    user_input = request.args
    print(user_input)

    movie_recommendation = brains.main(user_input)
    # user_input = dict(user_input).values
    # user_top_movies = list(user_input)[0:-2]
    # user_worst_movies = list(user_input)[-1:]
    #
    # recommended_list = deep_recommender(1, user_top_movies, user_worst_movies)
    return render_template('recommended.html', movie="The Matrix") #movie_recommendation
