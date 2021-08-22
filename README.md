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

- [x] [1. Understanding all significant components in ElasticSearch and its Auto completion feature.](#1-understanding-all-significant-components-in-elasticsearch-and-its-auto-completion-feature)
- [x] [2. Building an API service that interacts with ElasticSearch to be used by the UI.](#2-building-an-api-service-that-interacts-with-elasticsearch-to-be-used-by-the-ui)
- [x] [3. Testing API using Pytest.](#3-testing-api-using-pytest)
- [x] [4. Building UI using React and Redux.](#4-building-ui-using-react-and-redux)
- [x] [5. Testing UI using Cypress.](#5-testing-ui-using-cypress)

## Application Architecture

<img src="https://user-images.githubusercontent.com/12673979/117518002-c0017c00-afbb-11eb-97f3-14c253cad321.png"/>
<img src="https://user-images.githubusercontent.com/12673979/117521109-ae26d580-afc9-11eb-8dbd-663eeabaf0ff.png"/>

## 1. Understanding all significant components in ElasticSearch and it's Auto completion feature.

**What is ElasticSearch?**

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

## 2. Building an API service that interacts with ElasticSearch to be used by the UI.

1. Start the ElasticSearch, Backend and Frontend services
```
sh dev-startup.sh
```

2. API Documentation

#### ElasticSearch Autocomplete

```http
  GET /autocomplete
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `query` | `string`   | **Required**. Query string |

**Sample response**
```
dineshsonachalam@macbook ~ % curl --location --request GET 'elasticsearch:8000/autocomplete?query=python'
[
    {
        "id": 1,
        "value": "Python Data Science Handbook"
    },
    {
        "id": 2,
        "value": "Python GUI with Tkinter Playlist"
    },
    {
        "id": 3,
        "value": "Python Game Programming Tutorial: SpaceWar"
    },
    {
        "id": 4,
        "value": "Python PostgreSQL Tutorial Using Psycopg2"
    },
    {
        "id": 5,
        "value": "Python Programming for the Raspberry Pi"
    }
]
```


#### Query Search

```http
  POST /string-query-search
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `query` | `string`   | **Required**. Query string |

**Sample response**
```
dineshsonachalam@macbook ~ % curl --location --request POST 'elasticsearch:8000/string-query-search?query=python'
[
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
```

## 3. Testing API using Pytest

Pytest is a testing framework based on python. It is mainly used to write API based test cases. Here we are going to test our two API's (autocomplete and string-query-search).

**Start Pytest:**
```
dineshsonachalam@macbook tech-courses-search-engine % pytest backend
=========================================== test session starts ===========================================
platform darwin -- Python 3.9.5, pytest-6.2.4, py-1.10.0, pluggy-0.13.1
rootdir: /Users/dineshsonachalam/Desktop/tech-courses-search-engine
plugins: cov-2.12.1, metadata-1.11.0
collected 2 items                                                                                         

backend/tests/test_api.py ..                                                                        [100%]

============================================ 2 passed in 0.35s ============================================
dineshsonachalam@macbook tech-courses-search-engine % 
```

## 4. Building UI using React and Redux.

**What is React?**

A declarative, efficient, and flexible JavaScript library for building user interfaces.

**What is Redux?**

Redux is a JS library for managing client data in applications. Redux allow your state to be available in one place. It is used to manage data in your application.

Things to care about when using redux:
1. Identify the state.
2. Write good reducers.
3. Let's redux state handle the rest.

**Building Parts of redux:**

1. Action -> Action have a type field that tells what kind of action to perform and all other fields contain information or data.
2. Reducer -> They are functions that take the (current state and action) and return the new state and tell the store how to do.
3. Store -> The store is the object which holds state of the application.

<img src="https://i.imgur.com/G45gjRr.png"/>

**React components used in our application:**

**What are React components?**

Components are independent and reusable bits of code. They serve the same purpose as JavaScript functions, but work in isolation and return HTML via a render() function.

Components are classified into two types, Class components and Function components.

**What's the difference between class vs functional components:**

In class component, we can access the value of the state by using this.state inside JSX and we would use setState to update the value of the state. You can set the function inside the event or outside of the render() method -- for readability.

In functional component, we would use useState to assign initial state and we would use setCount (in our example) to update the state. If we want to access the value of the state, we can omit this.state and call the name of the state instead, in our case, it would just be count.


**React components used in our application:**

Here all our React components are available in the **src/components** folder.

```
dineshsonachalam@macbook frontend % tree src/components 
src/components
├── Nav.js
├── ResponsiveAntMenu.js
├── SearchBar.js
└── SearchResults.js

0 directories, 4 files
```
<img src="https://i.imgur.com/eYefwnE.png"/>

**How Redux is integrated into this React application:**

Here all our Redux components are available in the **src/redux** folder. Here we intialized Actions, Search Reducer and Redux store.

```
dineshsonachalam@macbook frontend % tree src/redux 
src/redux
├── actionTypes.js
├── actions.js
├── reducers
│   ├── index.js
│   └── searchReducer.js
└── store.js

1 directory, 5 files
```

**To start the UI in development mode:**
```
npm i && npm run start --prefix frontend
```

## 5. Testing UI using Cypress.

**What is Cypress?**

Fast, easy and reliable testing for anything that runs in a browser. Cypress is the most popular choice for Integration testing for web applications.

**Cypress Features**

- Test runner: So hands down one of the best features about Cypress is its test runner. It provides a whole new experience to end-to-end testing.
- Setting up tests: Another great feature that we talked about already is setting up tests are extremely easy, you just install Cypress and then everything gets set up for you
- Automatic waits – you will barely have to use waits when using Cypress
- Stubbing – you can easily stub application function behavior and server response.

**Running Cypress Integration test**

The cypress integration tests for our application is available at frontend/cypress/integration/search-courses.spec.js filepath.

```
dineshsonachalam@macbook tech-courses-search-engine % tree frontend/cypress
frontend/cypress
├── fixtures
│   └── example.json
├── integration
│   └── search-courses.spec.js
├── plugins
│   └── index.js
└── support
    ├── commands.js
    └── index.js

4 directories, 5 files
dineshsonachalam@macbook tech-courses-search-engine % 
```

**Running your Cypress Test in the Cypress Test Runner:**

To open the Cypress Test Runner, you can execute the following command below:
```
npx cypress open
```

Once the Cypress Test Runner opens up, you can execute your test which will show results similar to this below:

You can see all the Cypress commands listed below such as visit, URL & title
All your successful assertions will show in Green and failed assertions in Red.

<img src="https://i.imgur.com/F97ooaD.png"/>
<img src="https://i.imgur.com/jfmBLuk.png"/>

## License

[MIT](https://choosealicense.com/licenses/mit/) © [dineshsonachalam](https://www.github.com/dineshsonachalam)