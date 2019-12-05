import os
import numpy as np
import pandas as pd
from sklearn.decomposition import NMF
from sklearn.metrics.pairwise import cosine_similarity

class Recommender:

    def __init__(self, user_dict):
        self.user_dict = user_dict


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

    def vectorise_new_user(self, R, nmf):
        """
        Turns user input into a vector for
        nmf and cosim functions to find movie recommendations
        """
        titles = list(R.columns)
        empty_list = [np.nan] * len(titles)
        ratings_dict = dict(zip(titles, empty_list))


        for k, v in self.user_dict.items():
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
    recommender = Recommender(user_input)
    R, nmf = recommender.train_nmf_model()
    user_vec = recommender.vectorise_new_user(R, nmf, user_input)
    results = recommender.predict_with_nmf(R, nmf, user_vec)

    return results



if __name__ == '__main__':

    test_input = {'terminator' : '5.0',
                    'gladiator' : '5.0',
                    'matrix' : '5.0'}
    recommender = Recommender(test_input)

    R, nmf = recommender.train_nmf_model()

    user_vec = recommender.vectorise_new_user(R, nmf, test_input)
    results = recommender.predict_with_nmf(R, nmf)

    print(results)
