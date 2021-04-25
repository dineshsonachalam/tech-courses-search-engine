import csv
import requests
import json
import time

headers = {
  'Content-Type': 'application/json'
}

if __name__ == "__main__":
    url = "http://elasticsearch:9200/cs.stanford/_doc/"
    with open('tutorials.csv') as csv_file:
        
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
            response = requests.request("POST", url, headers=headers, data=payload)
            if response.status_code == 200 or response.status_code == 201:
                response  = json.loads(response.text)
                print("Indexed document: {}".format(response["_seq_no"]+1))

        time.sleep(10)

        url = "http://elasticsearch:9200/cs.stanford/_count"
        response = requests.request("GET", url, headers={}, data={})
        response  = json.loads(response.text)
        total_doc = response["count"]
        
        print("##########################################################")
        print("Total documents available in cs.stanford indice is {}".format(total_doc))
        print("##########################################################")