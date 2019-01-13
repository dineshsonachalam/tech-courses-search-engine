import requests
import json

def check_if_index_is_present(url):
    response = requests.request("GET", url, data="")
    json_data = json.loads(response.text)
    return json_data


if __name__ == "__main__":
    url = "http://localhost:9200/_template/search_engine_template/"
    response = requests.request("GET", url, data="")
    if(len(response.text)>2):
        print("1. Deleted template: search_engine_template")
        response_delete = requests.request("DELETE", url)
    payload = {
          "template": "hacker",
          "settings": {
            "number_of_shards": 1
          },
          "mappings": {
            "tutorials":{
                "_source": {
                    "enabled": True
                },
                "properties":{
                    "upvotes":{
                        "type":"integer"
                    },
                    "topic":{
                        "type":"text"
                    },
                    "title":{
                        "type":"text"
                    },
                    "url":{
                        "type":"text"
                    },
                    "labels":{
                        "type":"text"
                    }
                }
            }

          }
    }
    payload = json.dumps(payload)
    headers = {
            'Content-Type': "application/json",
            'cache-control': "no-cache"
        }
    response = requests.request("PUT", url, data=payload, headers=headers)
    if (response.status_code == 200):
        print("2. Created a new template: search_engine_template")

    url = "http://localhost:9200/hacker"
    json_data = check_if_index_is_present(url)

    if(not 'error' in json_data):
        print("3. Deleted an index: hacker")
        response = requests.request("DELETE", url)

    response = requests.request("PUT", url)
    if (response.status_code == 200):
        print("4. Created an index: hacker")

    url = "http://localhost:9200/autocomplete"
    json_data = check_if_index_is_present(url)

    if(not 'error' in json_data):
        print("5. Deleting index: autocomplete")
        response = requests.request("DELETE", url)

    payload = {
      "mappings": {
        "titles" : {
          "properties" : {
            "title" : { "type" : "string" },
            "title_suggest" : {
              "type" :     "completion",
              "analyzer" :  "standard",
              "search_analyzer" : "standard",
              "preserve_position_increments": False,
              "preserve_separators": False
            }
          }
        }
      }
    }
    payload = json.dumps(payload)
    response = requests.request("PUT", url, data=payload, headers=headers)

    if(response.status_code==200):
        print("6. Created a new index: autocomplete")





