from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def get_results(search_input):
    url = f'http://www.omdbapi.com/?apikey=cc10c3c3&s={search_input}'
    response = requests.get(url)
    search_results = response.json()
    return search_results

def get_movies(imdbID):
    url = f'http://www.omdbapi.com/?apikey=cc10c3c3&i={imdbID}'
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