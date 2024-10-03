import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

from tmdb_api import get_movie_details

import random
import sys
import requests
import random

def movies():
    BASE_URL = "https://api.themoviedb.org/3"

    genre = {"comedy": "Comedy", "drama": "Drama", "action": "Action", "adventure": "Adventure", "thriller": "Thriller"}
    
    mood = input("What's your mood today (comedy, drama, action, adventure, thriller)? ").lower()

    if mood not in genre:
        print("Sorry, we don't have movie suggestions for", mood, "yet. Try a different mood!")
        main()
        return

    genre_name = genre[mood]
    
    API_KEY = os.getenv('TMDB_API_KEY')
    genre_url = f"{BASE_URL}/genre/movie/list"
    params = {"api_key": API_KEY, "language": "en-US"}
    response = requests.get(genre_url, params=params)
    genres = response.json()["genres"]
    genre_id = next((g["id"] for g in genres if g["name"].lower() == genre_name.lower()), None)
    
    if not genre_id:
        print(f"No genre found for mood '{mood}'.")
        main()
        return

    def get_movie_suggestion():
        discover_url = f"{BASE_URL}/discover/movie"
        params = {
            "api_key": API_KEY,
            "language": "en-US",
            "sort_by": "popularity.desc",
            "include_adult": "false",
            "include_video": "false",
            "with_genres": genre_id,
            "page": random.randint(1, 5)
        }

        response = requests.get(discover_url, params=params)
        movies = response.json()["results"]
        
        if not movies:
            print("No movies found for this mood.")
            main()
            return None

        movie = random.choice(movies)
        return movie["title"]

    random_movie = get_movie_suggestion()
    if random_movie:
        print("\nHere's a", mood, "movie suggestion for you:", random_movie)

    def shuffle():  
        while True:
            res = int(input("\nDo you want a different suggestion? \nPress 1 for a different suggestion\nPress 2 if this suggestion is good \n"))
            if res == 1:
                random_movie = get_movie_suggestion()
                if random_movie:
                    print("Here is another suggestion:", random_movie)
            elif res == 2:
                print("Enjoy!!")
                main()
                break
            else:
                print("\n!!!!Press 1 for a different suggestion OR Press 2 if you don't want another suggestion!!!!\n")

    shuffle()
def food():
        food = {
            "spicy": ["Chili", "Jalapeno", "Wasabi", "Pepper"],

            "sweet": ["Chocolate", "Ice cream", "Cake", "Candy"],

            "healthy": ["Salad", "Fruits", "Vegetables", "Whole grains", "Nuts"],

            "Savory": ["Pizza", "Pasta", "Burger", "Fries", "Chicken", "Steak"],

            "Bitter": ["Coffee", "Dark chocolate", "Olive oil", "Broccoli", "Spinach"]
              }
        # Get user's mood
        food_mood = input("What do u feel like eating(spicy, sweet, healthy, Savory, Bitter)? ").lower()

        # Check if user's mood is a valid key in the dictionary
        if food_mood in food:
            # Choose
            random_food = random.choice(food[food_mood])
            print("\nHere's a", food_mood, "food item for you: ",random_food)

            def shuffle_food():  
                while True: # 'while' creates an infinite loop, until the break condition is met..
                    res = int(input("\nDo you want a different suggestion? \nPress 1 for a different suggestion\nPress 2 if this suggestion is good \n"))
                    if res == 1:
                        random_food = random.choice(food[food_mood])
                        print("Here is another suggestion:",random_food) 
                    elif res == 2:
                     print ("Enjoy!!")
                     main()
                    else:
                     print("\n!!!!Press 1 for a different suggestion OR Press 2 if you don't want another suggestion!!!!\n")

            shuffle_food()

        else:
            print("Sorry, we don't have suggestions for ", food_mood, " yet. Try a different taste!")
            main()


###########

def activities():
        activities = {
            "outdoor": ["Go for a walk","Have a picnic","Play badminton", "Ride a bike","Go for a run","Play frisbee","Visit a park","Sit in a cafe outdoors", "Fly a kite","Go for a swim","Play with a street dog","Gardening","Yoga in the park"],

            "indoor": ["Read a book", "Watch a movie or TV series", "Play video games", "Listen to music", "Cook or bake", "Learn a new skill", "Do a puzzle", "Play board games", "Meditate", "Write in a journal", "Organize your space", "Listen to podcasts", "Play with pets", "Try a new recipe"],

            "learning": ["Online course", "Coding tutorial", "Learn a new language", "Read a book", "Write a blog", "Start a podcast", "Take an online quiz", "Follow a YouTube tutorial", "Practice public speaking"],

            "wellness": ["Meditate", "Yoga", "Deep breathing", "Stretching", "Take a bath", "Listen to calming music", "Spend time in nature", "Journaling", "Spend time with loved ones", "Get enough sleep", "Practice mindfulness", "Take a break from screens"],
              }
        # Get user's mood
        activity_mood = input("What kind of activity do u feel like doing(Outdoor, Indoor, Learning, Wellness)? ").lower()
        # Check if user's mood is a valid key in the dictionary
        if activity_mood in activities:
            # Choose
            random_act = random.choice(activities[activity_mood])
            print("\nHere's a", activity_mood, "activity item for you: ", random_act)

            def shuffle_act():  
                while True: # 'while' creates an infinite loop, until the break condition is met..
                    res = int(input("\nDo you want a different suggestion? \nPress 1 for a different suggestion\nPress 2 if this suggestion is good \n"))
                    if res == 1:
                        random_act = random.choice(activities[activity_mood])
                        print("Here is another suggestion:",random_act) 
                    elif res == 2:
                     print ("Enjoy!!")
                     main()
                    else:
                     print("\n!!!!Press 1 for a different suggestion OR Press 2 if you don't want another suggestion!!!!\n")

            shuffle_act()

        else:
            print("Sorry, we don't have suggestions for ", activity_mood, " yet. Try a different activity!")
            main()


def TV_shows():
    BASE_URL =  "https://api.themoviedb.org/3"

    genre = {"comedy": "Comedy", "drama": "Drama", "action": "Action & Adventure", "mystery": "Mystery", "scifi": "Sci-Fi & Fantasy"}
    
    mood = input("What's your mood for TV shows today (comedy, drama, action, mystery, scifi)? ").lower()

    if mood not in genre:
        print("Sorry, we don't have TV show suggestions for", mood, "yet. Try a different mood!")
        main()
        return

    genre_name = genre[mood]
    
    API_KEY = os.getenv('TMDB_API_KEY')
    genre_url = f"{BASE_URL}/genre/tv/list"
    params = {"api_key": API_KEY, "language": "en-US"}
    response = requests.get(genre_url, params=params)
    genres = response.json()["genres"]
    genre_id = next((g["id"] for g in genres if g["name"].lower() == genre_name.lower()), None)
    
    if not genre_id:
        print(f"No genre found for mood '{mood}'.")
        main()
        return

    def get_tv_show_suggestion():
        discover_url = f"{BASE_URL}/discover/tv"
        params = {
            "api_key": API_KEY,
            "language": "en-US",
            "sort_by": "popularity.desc",
            "include_adult": "false",
            "with_genres": genre_id,
            "page": random.randint(1, 5)
        }

        response = requests.get(discover_url, params=params)
        tv_shows = response.json()["results"]
        
        if not tv_shows:
            print("No TV shows found for this mood.")
            main()
            return None

        tv_show = random.choice(tv_shows)
        return tv_show["name"]

    random_tv_show = get_tv_show_suggestion()
    if random_tv_show:
        print("\nHere's a", mood, "TV show suggestion for you:", random_tv_show)

    def shuffle():  
        while True:
            res = int(input("\nDo you want a different suggestion? \nPress 1 for a different suggestion\nPress 2 if this suggestion is good \n"))
            if res == 1:
                random_tv_show = get_tv_show_suggestion()
                if random_tv_show:
                    print("Here is another suggestion:", random_tv_show)
            elif res == 2:
                print("Enjoy!!")
                main()
                break
            else:
                print("\n!!!!Press 1 for a different suggestion OR Press 2 if you don't want another suggestion!!!!\n")

    shuffle()

def main():
    what = int(input("\nWhat do you need a suggestion for? \n\nPress 1 for movies\nPress 2 for food items\nPress 3 for entertaining activities\nPress 4 for TV shows\nPress 0 to exit\n"))

    if what == 1:
            movies()
    elif what == 2:
            food()
    elif what == 3:
            activities()
    elif what == 4:
            TV_shows()
    elif what == 0:
            print("Thankyou!")
            sys.exit()
            
    else:
         print("\n!!Choose a number between 1-4!!\n")
         main()

main()