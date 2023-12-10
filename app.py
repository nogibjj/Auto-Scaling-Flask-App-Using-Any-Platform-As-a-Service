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
    recommendation = get_movie_recommendation(user_input)

    return render_template('recommendation.html', recommendation=recommendation)

def get_movie_recommendation(user_input):
    # Use OpenAI API to generate movie recommendations based on user input
    prompt = f"Recommend me a movie similar to: {user_input}"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=100
    )
    recommendation = response['choices'][0]['text'].strip()
    return recommendation

if __name__ == '__main__':
    app.run(debug=True)
