"""
"""

import brains

def test_brains_recommender():

    brains.Recommender()
    titles_df = pd.read_csv("data/movies.csv", index_col='movieId')

    recommender = Recommender(user_input)
    R, nmf = recommender.train_nmf_model()
    user_input = recommender.movie_name_finder(titles_df['title'], user_input)
    user_vec = recommender.vectorise_new_user(R, user_input)
    results = recommender.predict_with_nmf(R, nmf, user_vec)


    test_input = {'Titanic' : '5.0',
                    'Toy Story' : '5.0',
                    'Matrix, The' : '5.0'}
    results = main(test_input)

    print(results)


# check whether the result is a list of strings

# check if size changes based on n
@pytest.mark.parametrize(['n'],[[1],[2],[3],[4],[5],7])
def test_size(n):
    r = recommender()
    assert len(r) == n

# check if movie title is actually in the database
def test_movie_exists():
    r = recommender()
    assert r[0] in database_of_titles

def test_size(n):
    r = recommender()
    assert len(r) == n
