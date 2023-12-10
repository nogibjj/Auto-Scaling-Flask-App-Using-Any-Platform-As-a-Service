# test_app.py

import pytest
from app import get_movie_recommendations

@pytest.fixture
def example_response():
    return """Certainly! Here are five recommendations of movies,\
along with their details:\n\
1. Inception\n\
   Genre: Science Fiction\n\
   Release Year: 2010\n\
   Director: Christopher Nolan\n\
   Description: A mind-bending heist movie that explores the concept of dreams and reality.\n\
2. The Shawshank Redemption\n\
   Genre: Drama\n\
   Release Year: 1994\n\
   Director: Frank Darabont\n\
   Description: The story of a banker wrongly convicted of murder and his journey in Shawshank prison.\n\
3. The Dark Knight\n\
   Genre: Action\n\
   Release Year: 2008\n\
   Director: Christopher Nolan\n\
   Description: Batman faces the Joker in this intense superhero film.\n\
4. Pulp Fiction\n\
   Genre: Crime\n\
   Release Year: 1994\n\
   Director: Quentin Tarantino\n\
   Description: A nonlinear narrative exploring the interconnected lives of various characters.\n\
5. Forrest Gump\n\
   Genre: Drama\n\
   Release Year: 1994\n\
   Director: Robert Zemeckis\n\
   Description: The life story of Forrest Gump, a man with a low IQ but a remarkable life.\n\
"""

def test_get_movie_recommendations(example_response):
    recommendations = get_movie_recommendations(example_response, num_recommendations=5)

    # Asserting that the recommendations list is not empty
    assert recommendations

    # Asserting that the length of recommendations is as expected
    assert len(recommendations) == 5

    # Asserting that each recommendation has the expected keys
    for rec in recommendations:
        assert set(rec.keys()) == {'title', 'genre', 'release_year', 'director', 'description'}

    # Asserting that the release years are not 'Not Available'
    for rec in recommendations:
        assert rec['release_year'] != 'Not Available'
