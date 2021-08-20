<a href="https://search.dineshsonachalam.com">
    <p align="center">
    <img src="https://i.imgur.com/j0ZQqwV.png" alt="SearchEngine">
    </p>
</a>
<p align="center">
    <em>Powered by ElasticSearch, Python, React, Redux, Kubernetes, Cypress E2E, Pytest and Github CI/CD</em>
</p>
<p align="center">
    <a href="https://sonarcloud.io/dashboard?id=tech-courses-search-engine">
        <img src="https://sonarcloud.io/api/project_badges/quality_gate?project=tech-courses-search-engine"/>
    </a>
</p>
<p  align="center">
  <a href="https://www.codacy.com/gh/dineshsonachalam/tech-courses-search-engine/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=dineshsonachalam/tech-courses-search-engine&amp;utm_campaign=Badge_Grade">
        <img src="https://app.codacy.com/project/badge/Grade/978c48d5a7ae4b28a1b17df88b6f1d0e"/>
  </a>
  <a href="https://github.com/dineshsonachalam/tech-courses-search-engine/actions" alt="CI/CD status">
      <img src="https://github.com/dineshsonachalam/tech-courses-search-engine/actions/workflows/k8-deploy.yml/badge.svg" />
  </a>
  <a href="https://www.python.org/downloads/release/python-390/" alt="Python 3.9">
      <img src="https://img.shields.io/badge/python-3.9-blue.svg" />
  </a>
  <a href="https://hub.docker.com/repository/docker/dineshsonachalam/tech-courses-search-engine-backend" alt="Docker pulls">
      <img src="https://img.shields.io/docker/pulls/dineshsonachalam/tech-courses-search-engine-backend.svg" />
  </a>
</p>
<p  align="center">
    
## Demo
1. <a href="https://search.dineshsonachalam.com/">Live demo</a>  
2. <a href="https://vimeo.com/589852893">Video demo</a> 

## What's this project all about?

This project showcases how to build real-time search engines like Google, Coursera, Medium, etc. We focus on the following aspects as part of this project.

1. Understanding all significant components in ElasticSearch and its Auto completion feature.
2. Building an API service that interacts with ElasticSearch to be used by the UI.
3. Testing our API using Pytest.
4. Building UI using React and Redux.
5. Testing our UI using Cypress.
6. Add SonarQube Quality gate to your application.
7. Deploy our application in the Kubernetes cluster using the Helm chart. 

#### 1. Understanding all significant components in ElasticSearch and it's Auto completion feature.

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

1. Start ElasticSearch docker container
```
mkdir -p ES_DATA && docker run -v $(pwd)/ES_DATA:/usr/share/elasticsearch/data -e "discovery.type=single-node" -e "ES_JAVA_OPTS=-Xms750m -Xmx750m" -p 9200:9200 elasticsearch:7.12.0 
```

2. Verify health status of a cluster.
```
dineshsonachalam@macbook ~ % curl --location --request GET 'http://elasticsearch:9200/_cat/health'
1629473241 15:27:21 docker-cluster green 1 1 0 0 0 0 0 0 - 100.0%
```

3.  Create an index template that contains the following properties topic, title, URL, labels and upvotes.
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


WIP: Work in Progress