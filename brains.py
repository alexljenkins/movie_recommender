import os
import numpy as np
import pandas as pd
from fuzzywuzzy.process import extract
from sklearn.decomposition import NMF
from sklearn.metrics.pairwise import cosine_similarity

class Recommender:

    def __init__(self, user_dict):
        self.user_dict = user_dict

    def key_vaL(self):
        """
        Currently not in use, but creates ID Title pairs
        in both directions from 2 lists.
        """
        id_title_dic = dict(zip(list_id_movies, list_title_movies))
        title_id_dic = dict(zip(list_title_movies,list_id_movies))

        return id_title_dic


    def train_nmf_model(self):
        # Grab data from SQL
        # conns = 'postgres://postgres:postgres@localhost/nubflex'
        # db = create_engine(conns)
        # df = pd.read_sql_table("ratings", db)

        # or grab from CSV
        ratings = pd.read_csv("data/ratings.csv") # only file we really need for NMF
        ratings.columns = map(str.lower, ratings.columns)


        #make a matrix pivot table fill na with 0
        R = ratings[['userid','movieid','rating']].set_index(['userid','movieid']).unstack(1)['rating'].fillna(0.0)

        if os.path.exists('nmf_model.bin'): # load trained model
            nmf = pickle.loads(open('nmf_model.bin', 'rb').read())

        else: # train a new model
            nmf = NMF(n_components=42)
            nmf.fit(R)

        return R, nmf

    def movie_name_finder(self, titles, user_input):
        """
        Uses fuzzywuzzy to find the closest title to a given title.
        Might not be needed in final production as we wont be excepting user
        input as a text field.
        """
        temp_dict = dict()
        for k, v in user_input.items():
            actual_title = extract(k, titles)[0][0]
            print(actual_title)
            temp_dict[actual_title] = v

        return temp_dict


    def vectorise_new_user(self, R, user_input):
        """
        Turns user input into a vector for
        nmf and cosim functions to find movie recommendations
        """
        titles = list(R.columns)
        empty_list = [np.nan] * len(titles)
        ratings_dict = dict(zip(titles, empty_list))

        for k, v in user_input.items():
            ratings_dict[k] = v

        new_user_vec = list(ratings_dict.values())
        new_user_vec = pd.DataFrame(new_user_vec, index=titles).T
        user_vec = new_user_vec.fillna(0.0)

        return user_vec


    def predict_with_nmf(self, R, nmf, user_vec):
        # fit model on user
        hidden_profile = nmf.transform(user_vec)
        # extract the movies
        ypred = np.dot(hidden_profile, nmf.components_)
        recom = pd.DataFrame(ypred, columns=movie_titles, index=['Score'])

        # remove movies user has 'seen' based on rating
        mask = np.isnan(user_vec.values[0])
        movies_not_seen = recom.columns[mask]
        movies_not_seen_df = recom[movies_not_seen]
        self.results = list(movies_not_seen_df.T.sort_values(by='Score', ascending=False).index[:5])

        return self.results


    def cosim(self, matrix, user_vector):
        """
        Compares the users vector to the sparse matrix
        and returns most similar user(s).
        """
        # scaling ratings to -1 to 1
        ratings['rating'] = (ratings['rating']-3)/2

        x = cosine_similarities(matrix, user_vector)

        return x


    def hybrid_recommender(self):
        ...


def main(user_input):
    titles_df = pd.read_csv("data/movies.csv", index_col='movieId')

    recommender = Recommender(user_input)
    R, nmf = recommender.train_nmf_model()
    user_input = recommender.movie_name_finder(titles_df['title'], user_input)
    user_vec = recommender.vectorise_new_user(R, user_input)
    results = recommender.predict_with_nmf(R, nmf, user_vec)

    return results



if __name__ == '__main__':

    test_input = {'Titanic' : '5.0',
                    'Toy Story' : '5.0',
                    'Matrix, The' : '5.0'}
    results = main(test_input)

    print(results)
