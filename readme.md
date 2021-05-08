# Tech courses search engine using ES, Python, React, Redux, Kubernetes, Cypress E2E, Pytest and Github CI/CD:

<p>
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
 

https://user-images.githubusercontent.com/12673979/117389661-507f8400-af0a-11eb-95e5-f7ef1dee6ac6.mov

## Table of Contents
- [What is it?](#what-is-it)
- [Developer guidelines](#development-guidelines)
- [How to deploy containers to Kubernetes cluster?](#how-to-use-it)

## What is it?
![tech-search-engine-architecture](https://user-images.githubusercontent.com/12673979/117518002-c0017c00-afbb-11eb-97f3-14c253cad321.png)

![tech-search-engine-design](https://user-images.githubusercontent.com/12673979/117521109-ae26d580-afc9-11eb-8dbd-663eeabaf0ff.png)




## Developer guidelines

## How to deploy containers to Kubernetes cluster?


```
helm install elasticsearch ./k8/elasticsearch
helm install search-backend ./k8/search-backend
helm install search-frontend ./k8/search-frontend


dineshsonachalam@macbook tech-courses-search-engine % helm install elasticsearch ./k8/elasticsearch
NAME: elasticsearch
LAST DEPLOYED: Fri May  7 19:23:10 2021
NAMESPACE: kube-system
STATUS: deployed
REVISION: 1
TEST SUITE: None

dineshsonachalam@macbook tech-courses-search-engine % helm install search-backend ./k8/search-backend
NAME: search-backend
LAST DEPLOYED: Fri May  7 19:24:08 2021
NAMESPACE: kube-system
STATUS: deployed
REVISION: 1
TEST SUITE: None

dineshsonachalam@macbook tech-courses-search-engine % helm install search-frontend ./k8/search-frontend
NAME: search-frontend
LAST DEPLOYED: Fri May  7 19:24:18 2021
NAMESPACE: kube-system
STATUS: deployed
REVISION: 1
TEST SUITE: None











dineshsonachalam@macbook ~ % kubectl get deployments -n=dinesh
NAME              READY   UP-TO-DATE   AVAILABLE   AGE
search-backend    1/1     1            1           58s
search-frontend   1/1     1            1           41s

dineshsonachalam@macbook ~ % kubectl get statefulsets -n=dinesh
NAME            READY   AGE
elasticsearch   1/1     114s
dineshsonachalam@macbook ~ %
```

```
dineshsonachalam@macbook ~ % helm list
NAME           	NAMESPACE  	REVISION	UPDATED                             	STATUS  	CHART                	APP VERSION
elasticsearch  	kube-system	1       	2021-05-07 19:01:23.393557 +0530 IST	deployed	elasticsearch-0.1.0  	1.0
search-backend 	kube-system	1       	2021-05-07 19:01:48.866657 +0530 IST	deployed	search-backend-0.1.0 	1.0
search-frontend	kube-system	1       	2021-05-07 19:02:06.762722 +0530 IST	deployed	search-frontend-0.1.0	1.0
dineshsonachalam@macbook ~ %
```


Helm generated template:
```
helm template elasticsearch elasticsearch
```

# uninstall a release

dineshsonachalam@macbook ~ % helm uninstall elasticsearch

release "elasticsearch" uninstalled
dineshsonachalam@macbook ~ %
dineshsonachalam@macbook ~ % helm uninstall search-backend
