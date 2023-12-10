# app.py

from flask import Flask, request, render_template
from dotenv import load_dotenv
import os
import openai

app = Flask(__name__)
load_dotenv()

# Load OpenAI API key from the environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    user_input = request.form['user_input']

    # Use OpenAI API for movie recommendation
    recommendations = get_movie_recommendations(user_input, num_recommendations=10)

    return render_template('recommendation.html', recommendations=recommendations)

def get_movie_recommendations(user_input, num_recommendations=1):
    # Use OpenAI API to generate movie recommendations based on user input
    separator = "><"
    prompt = f"Recommend me 10 unique movies that are similar to this theme/genre: {user_input}. Give me a structured output by providing details for each movie in the following format:\n1. Title:\n2. Genre:\n3. Release Year:\n4. Director:\n5. Description:{separator}"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=1500
    )

    recommendations_text = response['choices'][0]['text']

    # Split the recommendations using the separator
    recommendations_list = recommendations_text.split(separator)

    recommendations = []

    for i in range(num_recommendations):
        if i < len(recommendations_list):
            recommendation_text = recommendations_list[i].strip()
            title_start = recommendation_text.find(f"{i + 1}. Title:")
            genre_start = recommendation_text.find(f"{i + 1}. Genre:")
            release_year_start = recommendation_text.find(f"{i + 1}. Release Year:")
            director_start = recommendation_text.find(f"{i + 1}. Director:")
            description_start = recommendation_text.find(f"{i + 1}. Description:")

            title = recommendation_text[title_start + len(f"{i + 1}. Title:"):genre_start].strip()
            genre = recommendation_text[genre_start + len(f"{i + 1}. Genre:"):release_year_start].strip()
            release_year = recommendation_text[release_year_start + len(f"{i + 1}. Release Year:"):director_start].strip()
            director = recommendation_text[director_start + len(f"{i + 1}. Director:"):description_start].strip()
            description = recommendation_text[description_start + len(f"{i + 1}. Description:"):].strip()

            recommendations.append({
                'title': title,
                'genre': genre,
                'release_year': release_year,
                'director': director,
                'description': description
            })
        else:
            # Handle the case when there are not enough recommendations
            recommendations.append({
                'title': 'Not Available',
                'genre': 'Not Available',
                'release_year': 'Not Available',
                'director': 'Not Available',
                'description': 'Not Available'
            })

    return recommendations

if __name__ == '__main__':
    app.run(debug=True)
