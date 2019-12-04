import pickle
import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from sklearn.decomposition import NMF
import random

def model_builder():

    # Grab data from SQL
    # conns = 'postgres://postgres:postgres@localhost/nubflex'
    # db = create_engine(conns)
    # df = pd.read_sql_table("ratings", db)

    # or grab from CSV
    ratings = pd.read_csv("data/ratings.csv") # only file we really need for NMF
    ratings.columns = map(str.lower, ratings.columns)

    #make a matrix pivot table
    R = ratings[['userid','movieid','rating']].set_index(['userid','movieid']).unstack(1)['rating'].fillna(3.0)
    # maybe use a sparse matrix because NMF model might be able to take it as an input

    m = NMF(n_components=42)
    m.fit(R)

    return m

def next_movie():

    movies = pd.read_csv('movies.csv')['title'].tolist()
    random.shuffle(movies)

    return movies[0]

def save_rating(rating):


    movies = pd.read_csv('movies.csv')['title'].tolist()
    random.shuffle(movies)

    return movies[0]

def deep_recommender(num, user_top_movies, user_worst_movies):

    movies = pd.read_csv('movies.csv')['title'].tolist()
    random.shuffle(movies)

    # create a new user vector for their movies and ratings

    # load the trained nmf model

    # feed in the user vector into the model (transform)

    # results np.dot(profile, nmf_model.components_)

    # results final = convert to names from nmf output

    return movies[:num]


def save_model(m):

    binary = pickle.dumps(m)
    open("nmf_model.bin","wb").write(binary)


def load_model():
    binary = open("nmf_model.bin","rb").read()
    m = pickle.loads(binary)
    return m


def recommender(model, user_top_movies, user_worst_movies):

    movie_titles = R.columns

    # convert user input to np array of (9700,1)

    movie_titles

    new_user = [3.0] * len(movie_titles)
    new_user = np.array(new_user)
    new_user = new_user.reshape(-1,1).T

    new_user[567] = 5.0
    new_user[555] = 5.0
    new_user[291] = 5.0
    new_user[1928] = 1.0

    # profile of the new user
    hidden_profile = m.transform(new_user)

    # recreate a (1,42) * (42, 9727) --> (1,9724)
    m.components_.shape

    result = np.dot(hidden_profile, m.components_)
    sorted(result.tolist()[0], reverse=True)[:10]




if __name__ == '__main__':
    model = model_builder()
    save_model(model)



#%% extracting a similar named movie
from fuzzywuzzy.process import extract

choices = ['Toy Story (1999)','The Matrix','Harry Potter: the Dark Story']
query = 'tory story'

extract(query, choices)
