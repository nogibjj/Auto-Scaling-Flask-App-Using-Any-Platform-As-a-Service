from app import get_movie_recommendations

def test_app():
    # Sample preference input
    user_input = "Horror"

    # Call the recommendation function with the sample input
    recommendations = get_movie_recommendations(user_input, num_recommendations=1)

    # Print the recommendations for inspection (you can remove this in the final version)
    # print(recommendations)

    # Add your assertions based on the expected structure of the recommendation
    # For example, you can check if the recommendation contains the movie title, genre, etc.
    assert recommendations  # Check if recommendations are not empty

    for recommendation in recommendations:
        assert 'title' in recommendation
        assert 'genre' in recommendation
        assert 'release_year' in recommendation
        assert 'director' in recommendation
        assert 'description' in recommendation

if __name__ == '__main__':
    test_app()
