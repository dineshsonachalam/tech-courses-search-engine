import requests

def test_autocomplete():
    url = "http://0.0.0.0:8000/autocomplete?query=kubernetes"
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
    assert len(response) == len(expected_response)
    assert all([a == b for a, b in zip(response, expected_response)])
    print(all([a == b for a, b in zip(response, expected_response)]))

def test_string_query_search():
    url = 'http://0.0.0.0:8000/string-query-search?query=react'
    response = requests.request("POST", url, headers={}, data={})
    assert response.status_code == 200
    response = response.json()
    expected_response = [
        {
            "id": 1,
            "title": "React Crash Course 2018 - React Tutorial with Examples",
            "topic": "React",
            "url": "https://www.youtube.com/watch?v=Ke90Tje7VS0",
            "labels": [
                "Free",
                "Video",
                "Beginner"
            ],
            "upvotes": 78
        },
        {
            "id": 2,
            "title": "Awesome React",
            "topic": "React",
            "url": "https://github.com/enaqx/awesome-react",
            "labels": [
                "Free"
            ],
            "upvotes": 42
        },
        {
            "id": 3,
            "title": "The Complete React Web Developer Course (with Redux)",
            "topic": "React",
            "url": "https://click.linksynergy.com/deeplink?id=jU79Zysihs4&mid=39197&murl=https://www.udemy.com/react-2nd-edition/",
            "labels": [
                "Paid",
                "Video",
                "Beginner"
            ],
            "upvotes": 30
        },
        {
            "id": 4,
            "title": "Modern React with Redux",
            "topic": "React",
            "url": "https://click.linksynergy.com/deeplink?id=jU79Zysihs4&mid=39197&murl=https://www.udemy.com/react-redux/",
            "labels": [
                "Paid",
                "Video",
                "Beginner"
            ],
            "upvotes": 22
        },
        {
            "id": 5,
            "title": "Survive JavaScript - Webpack and React",
            "topic": "React",
            "url": "https://survivejs.com/react/introduction/",
            "labels": [
                "Free",
                "Advanced"
            ],
            "upvotes": 19
        },
        {
            "id": 6,
            "title": "React for Beginners",
            "topic": "React",
            "url": "https://reactforbeginners.com",
            "labels": [
                "Paid",
                "Video"
            ],
            "upvotes": 11
        },
        {
            "id": 7,
            "title": "The Beginner's Guide to ReactJS",
            "topic": "React",
            "url": "https://egghead.io/courses/the-beginner-s-guide-to-reactjs",
            "labels": [
                "Free",
                "Video",
                "Beginner"
            ],
            "upvotes": 9
        },
        {
            "id": 8,
            "title": "Become a Professional React Developer",
            "topic": "React",
            "url": "https://udacity.com/course/react-nanodegree--nd019/",
            "labels": [
                "Paid",
                "Video",
                "Beginner"
            ],
            "upvotes": 7
        },
        {
            "id": 9,
            "title": "Fullstack Advanced React and GraphQL",
            "topic": "React",
            "url": "https://advancedreact.com/",
            "labels": [
                "Paid",
                "Advanced",
                "GraphQL"
            ],
            "upvotes": 5
        },
        {
            "id": 10,
            "title": "Learn ReactJS by Codecademy",
            "topic": "React",
            "url": "https://www.codecademy.com/learn/react-101",
            "labels": [
                "Paid",
                "Exercises/Practice-programs"
            ],
            "upvotes": 5
        }
    ]
    assert len(response) == len(expected_response)
    assert all([a == b for a, b in zip(response, expected_response)])
    print(all([a == b for a, b in zip(response, expected_response)]))