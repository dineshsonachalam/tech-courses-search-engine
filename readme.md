# [Building-a-search-engine-using-Elasticsearch]
[![Build Status](https://api.travis-ci.org/dineshsonachalam/Building-a-search-engine-using-Elasticsearch.svg?branch=master)](https://travis-ci.org/dineshsonachalam/Building-a-search-engine-using-Elasticsearch)
[![](https://img.shields.io/docker/pulls/dineshsonachalam/hacker.svg)](https://hub.docker.com/r/dineshsonachalam/hacker)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/5436c035ab974af3aeade51ebe9ec57a)](https://www.codacy.com/app/dineshsonachalam/Building-a-search-engine-using-Elasticsearch?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=dineshsonachalam/Building-a-search-engine-using-Elasticsearch&amp;utm_campaign=Badge_Grade)
[![](https://img.shields.io/badge/python-3.5%20%7C%203.6%20%7C%203.7-blue.svg)](https://www.python.org/downloads/release/python-370/)
[![](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/dineshsonachalam/Building-a-search-engine-using-Elasticsearch/blob/master/LICENSE)






### Running the application

```sh
sudo docker-compose up
```
Now hit **localhost:8005** and you can see the application running.

![](https://cdn-images-1.medium.com/max/800/1*ZvovF3fIKf1sh045UgXARQ.png)


**Medium Article:** https://medium.com/devopslinks/building-a-real-time-elastic-search-engine-using-python-32e05bcb9140



### Convert ES index data to output json
```
elasticdump \
  --input=http://localhost:9200/hacker/tutorials \
  --output=./tutorials.json \
  --type=data
 
elasticdump \
  --input=http://localhost:9200/autocomplete/titles \
  --output=./titles.json \
  --type=data
```