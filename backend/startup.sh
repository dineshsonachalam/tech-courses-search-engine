#!/bin/bash

python3 es-health-check.py


# 1. Create elasticsearch template
curl -X PUT "elasticsearch:9200/_index_template/template_1?pretty" -H 'Content-Type: application/json' -d'
{
  "index_patterns": "cs.stanford",
  "template": {
    "settings": {
      "number_of_shards": 1
    },
    "mappings": {
      "_source": {
        "enabled": true
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
}
'

# 2. Delete elasticsearch indice if exists
curl --location --request DELETE 'http://elasticsearch:9200/cs.stanford'

# 3. Create elasticsearch indice
curl --location --request PUT 'http://elasticsearch:9200/cs.stanford/'

# 4. Add record to elasticsearch
python3 add_documents.py

# 5. Kill Backend and Frontend server
lsof -i tcp:8000 | awk 'NR!=1 {print $2}' | xargs kill # Backend server
lsof -i tcp:3000 | awk 'NR!=1 {print $2}' | xargs kill # Frontend server

# # 6. Start Backend server
python3 main.py 