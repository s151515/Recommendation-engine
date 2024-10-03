import os
from dotenv import load_dotenv
import requests

# Load environment variables from .env file
load_dotenv()

# Get the API key from environment variables
api_key = os.getenv('TMDB_API_KEY')

# Your TMDB API request
def get_movie_details(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    params = {
        'api_key': api_key,
        'language': 'en-US'
    }
    response = requests.get(url, params=params)
    return response.json()

# Example usage
if __name__ == "__main__":
    movie_id = 550  # Fight Club
    movie_details = get_movie_details(movie_id)
    print(movie_details)