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


#### Helm install:
```
dineshsonachalam@macbook tech-courses-search-engine % helm list
NAME              	NAMESPACE  	REVISION	UPDATED                             	STATUS  	CHART                           	APP VERSION
tech-search-engine	kube-system	1       	2021-05-08 09:04:54.806979 +0530 IST	deployed	tech-courses-search-engine-0.1.0	1.0
dineshsonachalam@macbook tech-courses-search-engine % kubectl get deployments -n=dinesh
NAME              READY   UP-TO-DATE   AVAILABLE   AGE
search-backend    1/1     1            1           25s
search-frontend   1/1     1            1           25s
dineshsonachalam@macbook tech-courses-search-engine % kubectl get pods -n=dinesh
NAME                               READY   STATUS    RESTARTS   AGE
elasticsearch-0                    1/1     Running   0          35s
search-backend-8647cdb658-cszl4    1/1     Running   0          35s
search-frontend-6f6876fc7f-fmnkk   1/1     Running   0          35s
dineshsonachalam@macbook tech-courses-search-engine % kubectl get sts -n=dinesh
NAME            READY   AGE
elasticsearch   1/1     42s
dineshsonachalam@macbook tech-courses-search-engine % kubectl get svc -n=dinesh
NAME              TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)    AGE
elasticsearch     ClusterIP   10.245.213.240   <none>        9200/TCP   49s
search-backend    ClusterIP   10.245.33.10     <none>        8000/TCP   49s
search-frontend   ClusterIP   10.245.254.139   <none>        3000/TCP   49s
dineshsonachalam@macbook tech-courses-search-engine %
```

#### Useful helm commands:
```
# uninstall a release

dineshsonachalam@macbook ~ % helm uninstall elasticsearch
release "elasticsearch" uninstalled
```
