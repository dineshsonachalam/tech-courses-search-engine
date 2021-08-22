## 1. Understanding all significant components in ElasticSearch and it's Auto completion feature.

What is ElasticSearch?

Free and Open, Distributed, RESTful Search Engine. You can use Elasticsearch to store, search, and manage data for:

- Logs
- Metrics
- A search backend
- Application monitoring
- Endpoint security

How does Elasticsearch work?

Let's understand some basic components of how it organizes data in ElasticSearch.

**Logical components**

1. Documents:

Documents are the low level unit of information that can be indexed in Elasticsearch expressed in JSON, which is the global internet data interchange format. You can think of a document like a row in a relational database, representing a given entity — the thing you’re searching for. In Elasticsearch, a document can be more than just text, it can be any structured data encoded in JSON. That data can be things like numbers, strings, and dates. Each document has a unique ID and a given data type, which describes what kind of entity the document is. For example, a document can represent an encyclopedia article or log entries from a web server.

2. Indices:

An index is a collection of documents that have similar characteristics. An index is the highest level entity that you can query against in Elasticsearch. You can think of the index as being similar to a database in a relational database schema. Any documents in an index are typically logically related. In the context of an e-commerce website, for example, you can have an index for Customers, one for Products, one for Orders, and so on. An index is identified by a name that is used to refer to the index while performing indexing, search, update, and delete operations against the documents in it.

3. Index templates:

An index template is a way to tell Elasticsearch how to configure an index when it is created. The template is applied automatically whenever a new index is created with the matching pattern.

**Backend components**

1. Cluster:

An Elasticsearch cluster is a group of one or more node instances that are connected together. 

2. Node:

A node is a single server that is a part of a cluster. A node stores data and participates in the cluster’s indexing and search capabilities. An Elasticsearch node can be configured in different ways:

(i) Master Node — Controls the Elasticsearch cluster and is responsible for all cluster-wide operations like creating/deleting an index and adding/removing nodes.

(ii) Data Node — Stores data and executes data-related operations such as search and aggregation.

(iii) Client Node — Forwards cluster requests to the master node and data-related requests to data nodes.

3. Shards:

Elasticsearch provides the ability to subdivide the index into multiple pieces called shards. Each shard is in itself a fully-functional and independent “index” that can be hosted on any node within a cluster. By distributing the documents in an index across multiple shards, and distributing those shards across multiple nodes, Elasticsearch can ensure redundancy, which both protects against hardware failures and increases query capacity as nodes are added to a cluster.

4. Replicas: 

Elasticsearch allows you to make one or more copies of your index’s shards which are called replica shards or just replicas.

**How to implement Autocompletion ElasticSearch feature?**

1. Start ElasticSearch Docker container
```
mkdir -p ES_DATA && docker run -v $(pwd)/ES_DATA:/usr/share/elasticsearch/data -e "discovery.type=single-node" -e "ES_JAVA_OPTS=-Xms750m -Xmx750m" -p 9200:9200 elasticsearch:7.12.0 
```

2. Verify the health status of your cluster.
```
dineshsonachalam@macbook ~ % curl --location --request GET 'http://elasticsearch:9200/_cat/health'
1629473241 15:27:21 docker-cluster green 1 1 0 0 0 0 0 0 - 100.0%
```

3. Create an index template that contains the following properties topic, title, URL, labels, and upvotes.
```
curl -X PUT "elasticsearch:9200/_index_template/template_1?pretty" -H 'Content-Type: application/json' \
-d'{
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
}'
```

4. Validate if the index template is available.
```
dineshsonachalam@macbook ~ % curl --location --request GET 'http://elasticsearch:9200/_index_template/template_1'
{
    "index_templates": [
        {
            "name": "template_1",
            "index_template": {
                "index_patterns": [
                    "cs.stanford"
                ],
                "template": {
                    "settings": {
                        "index": {
                            "number_of_shards": "1"
                        }
                    },
                    "mappings": {
                        "_source": {
                            "enabled": true
                        },
                        "properties": {
                            "upvotes": {
                                "type": "integer"
                            },
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
                            }
                        }
                    }
                },
                "composed_of": []
            }
        }
    ]
}
```

5. Create a new index called cs.stanford
```
dineshsonachalam@macbook ~ % curl --location --request PUT 'http://elasticsearch:9200/cs.stanford/'
{
    "acknowledged": true,
    "shards_acknowledged": true,
    "index": "cs.stanford"
}
```

6. Validate if the cs.stanford index is available.
```
dineshsonachalam@macbook ~ % curl --location --request GET 'http://elasticsearch:9200/cs.stanford/'
{
    "cs.stanford": {
        "aliases": {},
        "mappings": {
            "properties": {
                "labels": {
                    "type": "text"
                },
                "title": {
                    "type": "completion",
                    "analyzer": "simple",
                    "preserve_separators": true,
                    "preserve_position_increments": true,
                    "max_input_length": 50
                },
                "topic": {
                    "type": "text"
                },
                "upvotes": {
                    "type": "integer"
                },
                "url": {
                    "type": "text"
                }
            }
        },
        "settings": {
            "index": {
                "routing": {
                    "allocation": {
                        "include": {
                            "_tier_preference": "data_content"
                        }
                    }
                },
                "number_of_shards": "1",
                "provided_name": "cs.stanford",
                "creation_date": "1629526849180",
                "number_of_replicas": "1",
                "uuid": "NrvQ6juOSNmf0GOPO2QADA",
                "version": {
                    "created": "7120099"
                }
            }
        }
    }
}
```

7. Add documents to cs.stanford index.
```
cd backend && python -c 'from utils.elasticsearch import Elasticsearch; es = Elasticsearch("cs.stanford"); es.add_documents()' && cd ..
```

8. Get the total count of the documents in cs.stanford index. We can able to see that the document count is 1350.
```
dineshsonachalam@macbook tech-courses-search-engine % curl --location --request GET 'http://elasticsearch:9200/cs.stanford/_count'
{
    "count": 1350,
    "_shards": {
        "total": 1,
        "successful": 1,
        "skipped": 0,
        "failed": 0
    }
}
```

9. Use ElasticSearch suggesters search for autocompletion. The suggest feature suggests similar looking terms based on a provided text by using a suggester.

```
dineshsonachalam@macbook tech-courses-search-engine % cd backend && python -c 'from utils.filters import SearchFilters; search = SearchFilters("cs.stanford"); print(search.autocomplete(query="python"))' && cd ..
[
    {
        "id": 1,
        "value": "Python Data Science Handbook"
    },
    {
        "id": 2,
        "value": "Python Game Programming Tutorial: SpaceWar"
    },
    {
        "id": 3,
        "value": "Python for Beginners - Learn Python Programming La"
    },
    {
        "id": 4,
        "value": "Python for Data Science and Machine Learning Bootc"
    },
    {
        "id": 5,
        "value": "Python for Security Professionals"
    }
]
```