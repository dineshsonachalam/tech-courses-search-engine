from pathlib import Path
import requests
import json
import csv

class Elasticsearch:
    def __init__(self):
        self.cluster_health_url = "http://elasticsearch:9200/_cluster/health"
        self.index_template_url = "http://elasticsearch:9200/_index_template/template_1"
        self.index_url = "http://elasticsearch:9200/cs.stanford/"
        self.index_doc_count_url = "http://elasticsearch:9200/cs.stanford/_count"
        self.index_doc_url = "http://elasticsearch:9200/cs.stanford/_doc/"
        self.headers = {
                    'Content-Type': 'application/json'
        }

    def es_healthcheck(self):
        try:
            response = requests.request("GET", self.cluster_health_url, headers={}, data={})
            if(response.status_code==200):
                response = response.json()
                status = response["status"]
                if(status != "red"):
                    print("💪 ES is {} and healthy".format(status))
                    return True
                else:
                    print("🤒 ES is {} and not healthy".format(status))
                    return False
            else:
                return False
        except Exception as e:
            print("❌ Exception: ",e)
            return False

    def create_es_index(self):
        # Create ES template and index if not exist
        response = requests.request("GET", self.index_template_url, headers={}, data={})
        if(response.status_code != 200):
            payload = json.dumps({
            "index_patterns": "cs.stanford",
            "template": {
                "settings": {
                "number_of_shards": 1
                },
                "mappings": {
                "_source": {
                    "enabled": True
                },
                "properties": {
                    "topic": {
                    "type": "text"
                    },
                    "title": {
                    "type": "completion"
                    },
                    "url": {
                    "type": "text"
                    },
                    "labels": {
                    "type": "text"
                    },
                    "upvotes": {
                    "type": "integer"
                    }
                }
                }
            }
            })
            requests.request("PUT", self.index_template_url, headers=self.headers, data=payload)
            print("Index template creation is successful")
        else:
            print("Index template already exists")

        response = requests.request("GET", self.index_url, headers={}, data={})
        if(response.status_code != 200):
            requests.request("PUT", self.index_url, headers={}, data={})
            print("Index creation is successful")
        else:
            print("Index already exists")

    def es_record_count(self):
        response = requests.request("GET", self.index_doc_count_url, headers={}, data={})
        response  = json.loads(response.text)
        total_doc = response["count"]
        return total_doc

    def add_documents(self):
        total_doc = self.es_record_count()
        if total_doc<=0:
            tutorials_csv_file_path = "{}/tutorials.csv".format(Path(__file__).parents[1])
            # Add documents if there are no records in the index.
            with open(tutorials_csv_file_path) as csv_file:
                # creating a csv reader object
                csv_reader = csv.reader(csv_file)
                # extracting field names through first row
                fields = next(csv_reader)
                print(fields)
                # extracting each data row one by one
                for row in csv_reader:
                    payload={
                        "topic": row[1],
                        "title": {
                            "input": row[2],
                        },
                        "url": row[3],
                        "labels": row[4],
                        "upvotes": int(row[5])
                    }
                    payload = json.dumps(payload)
                    response = requests.request("POST", self.index_doc_url, headers=self.headers, data=payload)
                    if response.status_code == 200 or response.status_code == 201:
                        response  = json.loads(response.text)
                        print("Indexed document: {}".format(response["_seq_no"]+1))

    def pre_condition_check(self):
        health_check_result = self.es_healthcheck()
        if(health_check_result == True):
            self.create_es_index()
            self.add_documents()
            total_doc = self.es_record_count()
            if(total_doc>0):
                return True
            else:
                return False
        else:
            return False