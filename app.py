from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from the .env file

app = Flask(__name__)

API_KEY = os.environ.get('API_KEY')
app.config['API_KEY'] = API_KEY
# print (API_KEY)

def get_results(search_input):
    url = f'http://www.omdbapi.com/?apikey={API_KEY}&s={search_input}'
    response = requests.get(url)
    search_results = response.json()
    return search_results

def get_movies(imdbID):
    url = f'http://www.omdbapi.com/?apikey={API_KEY}&i={imdbID}'
    response = requests.get(url)
    movie_info = response.json()
    return movie_info

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/movies')
def movies():
    # title = request.args.get('movie_title')
    imdbID = request.args.get('imdbID')
    movie_info = get_movies(imdbID)
    return render_template('movies.html', movie_info=movie_info)

@app.route('/search_results')
def seach_results():
    search_input = request.args.get('search_input')
    search_results = get_results(search_input)
    return render_template('search_results.html', search_results=search_results)