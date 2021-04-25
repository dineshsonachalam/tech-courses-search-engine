import requests
import json
class Search_filters:
    def __init__(self):
        self.url = "http://elasticsearch:9200/cs.stanford/_search"
        self.headers = {
                    'Content-Type': 'application/json'
        }

    def autocomplete(self, query):
        payload = {
            "suggest": {
                "tutorial-suggest": {
                    "prefix": query,
                    "completion": {
                        "field": "title"
                    }
                }
            }
        }
        payload = json.dumps(payload)
        response = requests.request("GET", self.url, headers=self.headers, data=payload)
        titles = []
        if response.status_code == 200:
            response  = json.loads(response.text)
            options = response["suggest"]["tutorial-suggest"][0]["options"]
            id = 1
            for option in options:
                titles.append(
                    {
                        "id": id,
                        "value": option["text"]
                    }
                )
                id+=1
        return titles

    def string_query_search(self, query):
        payload = {
                    "query": {
                        "query_string": {
                            "analyze_wildcard": True,
                            "query": query,
                            "fields": ["title", "topic"]
                        }
                    },
                    "size": 10
        }
        payload = json.dumps(payload)
        response = requests.request("GET", self.url, headers=self.headers, data=payload)
        tutorials = []
        if response.status_code == 200:
            response  = json.loads(response.text)
            hits = response["hits"]["hits"]
            id = 1
            for item in hits:
                labels = item["_source"]["labels"]
                labels = eval(labels)
                tutorials.append({
                    "id": id,
                    "title": item["_source"]["title"]["input"],
                    "topic": item["_source"]["topic"],
                    "url": item["_source"]["url"],
                    "labels": labels,
                    "upvotes": item["_source"]["upvotes"]
                })
                id = id + 1
        return tutorials


    



