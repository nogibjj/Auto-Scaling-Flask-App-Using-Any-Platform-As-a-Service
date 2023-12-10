# app.py

from flask import Flask, request, render_template
from dotenv import load_dotenv
import os
import openai
import re

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
    recommendations = get_movie_recommendations(user_input, num_recommendations=1)

    return render_template('recommendation.html', recommendation=recommendations[0])

def get_movie_recommendations(user_input, num_recommendations=1):
    # Use OpenAI API to generate movie recommendations based on user input
    separator = "><"
    prompt = f"Recommend me a movie that is similar to this theme/genre: {user_input}. Provide details in the following format:\nTitle:\nGenre:\nRelease Year:\nDirector:\nDescription:{separator}. I want to put this in a tabular format so follow this format always."
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=1500
    )

    recommendations_text = response['choices'][0]['text']

    # Use regex to extract movie details
    matches = re.findall(r"Title:(.+?)\s+Genre:(.+?)\s+Release Year:(.+?)\s+Director:(.+?)\s+Description:(.+?)(?=\nTitle:|$)", recommendations_text, re.DOTALL)

    recommendations = []

    for match in matches:
        title, genre, release_year, director, description = map(str.strip, match)
        recommendations.append({
            'title': title,
            'genre': genre,
            'release_year': release_year,
            'director': director,
            'description': description
        })

    return recommendations

if __name__ == '__main__':
    app.run(debug=True)
