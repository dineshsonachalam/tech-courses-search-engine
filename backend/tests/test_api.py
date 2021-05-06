import requests
import json

def test_autocomplete():
    url = 'http://localhost:8000/autocomplete?query=kubernetes'
    response = requests.request("GET", url, headers={}, data={})    
    assert response.status_code == 200
    response = response.json()
    expected_response = [
        {
            "id": 1,
            "value": "Kubernetes By Example"
        },
        {
            "id": 2,
            "value": "Kubernetes On The Cloud & The CNCF CKA Certificati"
        },
        {
            "id": 3,
            "value": "Kubernetes Tutorial"
        },
        {
            "id": 4,
            "value": "Kubernetes in Action"
        }
    ]
    assert response == expected_response

def test_string_query_search():
    url = 'http://localhost:8000/string-query-search?query=Python' 
    response = requests.request("POST", url, headers={}, data={}) 
    assert response.status_code == 200
    response = response.json()
    expected_response = [
                                {
                                    "id": 1,
                                    "title": "Google's Python Class",
                                    "topic": "Python",
                                    "url": "https://developers.google.com/edu/python/",
                                    "labels": [
                                        "Free",
                                        "Python 2"
                                    ],
                                    "upvotes": 213
                                },
                                {
                                    "id": 2,
                                    "title": "Complete Python Bootcamp",
                                    "topic": "Python",
                                    "url": "https://click.linksynergy.com/deeplink?id=jU79Zysihs4&mid=39197&murl=https://www.udemy.com/complete-python-bootcamp",
                                    "labels": [
                                        "Paid",
                                        "Video",
                                        "Beginner",
                                        "Python 3"
                                    ],
                                    "upvotes": 196
                                },
                                {
                                    "id": 3,
                                    "title": "Automate the Boring Stuff with Python",
                                    "topic": "Python",
                                    "url": "http://automatetheboringstuff.com/",
                                    "labels": [
                                        "Free",
                                        "Book"
                                    ],
                                    "upvotes": 93
                                },
                                {
                                    "id": 4,
                                    "title": "Official Python Tutorial",
                                    "topic": "Python",
                                    "url": "https://docs.python.org/3/tutorial/index.html",
                                    "labels": [
                                        "Free"
                                    ],
                                    "upvotes": 74
                                },
                                {
                                    "id": 5,
                                    "title": "Working with Strings in Python",
                                    "topic": "Python",
                                    "url": "https://academy.vertabelo.com/course/python-strings",
                                    "labels": [
                                        "Free",
                                        "Beginner",
                                        "Python 3"
                                    ],
                                    "upvotes": 4
                                },
                                {
                                    "id": 6,
                                    "title": "Learn Python the Hard Way",
                                    "topic": "Python",
                                    "url": "https://learnpythonthehardway.org/book/",
                                    "labels": [
                                        "Paid",
                                        "Book",
                                        "Python 3"
                                    ],
                                    "upvotes": 293
                                },
                                {
                                    "id": 7,
                                    "title": "Python for Beginners - Learn Python Programming Language in 2 Hours",
                                    "topic": "Python",
                                    "url": "https://www.youtube.com/watch?v=yE9v9rt6ziw",
                                    "labels": [
                                        "Free",
                                        "Video",
                                        "Beginner",
                                        "Python 3"
                                    ],
                                    "upvotes": 62
                                },
                                {
                                    "id": 8,
                                    "title": "Automate the Boring Stuff with Python",
                                    "topic": "Python",
                                    "url": "https://click.linksynergy.com/deeplink?id=jU79Zysihs4&mid=39197&murl=https://www.udemy.com/automate/",
                                    "labels": [
                                        "Paid",
                                        "Video",
                                        "Beginner"
                                    ],
                                    "upvotes": 45
                                },
                                {
                                    "id": 9,
                                    "title": "Introduction to Programming with Python",
                                    "topic": "Python",
                                    "url": "https://mva.microsoft.com/en-US/training-courses/introduction-to-programming-with-python-8360",
                                    "labels": [
                                        "Free",
                                        "Video"
                                    ],
                                    "upvotes": 41
                                },
                                {
                                    "id": 10,
                                    "title": "A Byte of Python",
                                    "topic": "Python",
                                    "url": "http://www.swaroopch.com/notes/python/",
                                    "labels": [
                                        "Free"
                                    ],
                                    "upvotes": 22
                                }
     ]
    assert response == expected_response
