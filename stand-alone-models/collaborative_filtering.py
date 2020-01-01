"""
Cosine similarity.
Calulating the angle of the two vectors
(Between -1 and 1)
cosim = cos(a) = (X . y)/||x||*||y||
Should normalize/de-mean so the angles of "opposite" vectors are captured
as 180' rather than 0' apart. Called: Centred cosine similarity.
This makes it the same as "pearson correlation".
"""
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv('data\\ratings.csv')
df.columns = df.columns.str.lower()

# scaling ratings to -1 to 1
df['rating'] = (df['rating']-3)/2

# Expand df into a matrix
matrix = df.set_index(['userid','movieid'])['rating'].unstack(1)
matrix
# fillnas' with 0 (middle value)
matrix.fillna(0.0, inplace=True)


def user_input_to_array(user_input):
    for k, v in user_input.items():
        ratings_dict[k] = (v-3)/2

    new_user_vec = list(ratings_dict.values())
    new_user_vec = pd.DataFrame(new_user_vec, index=movie_titles).T
    new_user_vec_filled = new_user_vec.fillna(0.0)

    return new_user_vec_filled

def new_user_cosine_sim(user_input):
    """
    Compares the users vector to the sparse matrix
    and returns most similar user(s).
    """


    return cosine_similarities(matrix, user)


if __name__ == '__main__':

    sim_matrix = cosine_similarities(matrix)
