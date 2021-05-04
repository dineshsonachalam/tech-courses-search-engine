# Dev environment:

1. Add the following domains to /etc/hosts that points to localhost.
```
dineshsonachalam@macbook Desktop % sudo -i
127.0.0.1	localhost
127.0.0.1 elasticsearch
127.0.0.1 api-search.dineshsonachalam.com
```
2. Generate self signed ssl certificate for localhost and paste in certs-dev folder.
```
openssl req -x509 -sha256 -nodes -newkey rsa:2048 -days 365 -keyout private.key -out certificate.crt
```

3. Start nginx server:
```
# To start the nginx reverse proxy
nginx -c /Users/dineshsonachalam/Desktop/tech-courses-search-engine/nginx.conf

dineshsonachalam@macbook ~ % ps -ef | grep nginx
  501  3710     1   0  9:07PM ??         0:00.01 nginx: master process nginx -c /Users/dineshsonachalam/Desktop/ADP-Hackathon/nginx.conf
  501  3711  3710   0  9:07PM ??         0:00.00 nginx: worker process
  501  3712  3710   0  9:07PM ??         0:00.02 nginx: worker process
  501  3713  3710   0  9:07PM ??         0:00.02 nginx: worker process
  501  3714  3710   0  9:07PM ??         0:00.03 nginx: worker process
  501  4142  4110   0  9:26PM ttys002    0:00.01 grep nginx

# To stop the nginx:
nginx -s stop
```


4. Start the docker-compose
```
docker-compose up
```

5. Open the https://api-search.dineshsonachalam.com URL in firefox and allow use of self signed certificate.

# K8 deployment:

1. Display list of contexts/clusters.
```
dineshsonachalam@macbook Desktop % kubectl config get-contexts
CURRENT   NAME               CLUSTER            AUTHINFO         NAMESPACE
*         do-nyc1-home-lab   do-nyc1-home-lab   sonachalam       kube-system
          docker-desktop     docker-desktop     docker-desktop
          minikube           minikube           minikube         default
```

2. To delete a namespace.
```
dineshsonachalam@macbook tech-courses-search-engine % kubectl delete ns dinesh   
namespace "dinesh" deleted
```

3. Create a new namespace.
```
dineshsonachalam@macbook tech-courses-search-engine % kubectl create namespace dinesh
namespace/dinesh created
```

4. To get all resource of a namespace.
```
dineshsonachalam@macbook Desktop % kubectl get all -n=dinesh
No resources found in dinesh namespace.
dineshsonachalam@macbook Desktop %
```

5. Now let's create a Statefulset and Service for Elasticsearch.
```
dineshsonachalam@macbook tech-courses-search-engine % kubectl create -f k8/es.yaml -n=dinesh
statefulset.apps/es created
service/elasticsearch created
```

(ii) Now a pod is created which is smallest deployable object in K8.
```
dineshsonachalam@macbook tech-courses-search-engine % kubectl get pods -n=dinesh
NAME   READY   STATUS    RESTARTS   AGE
es-0   1/1     Running   0          100s
```
(iii) Now the Statefulset is created. It's used to manage stateful applications(containers) with volumes. 
```
dineshsonachalam@macbook tech-courses-search-engine % kubectl get statefulsets -n=dinesh
NAME   READY   AGE
es     1/1     14m
```
(iv) Persistent volume claims is created successfully for our statefulset.
```
dineshsonachalam@macbook tech-courses-search-engine % kubectl get pvc -n=dinesh
NAME           STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS       AGE
es-data-es-0   Bound    pvc-e83abdfb-f819-441e-87a9-f4b53cdfec6d   5Gi        RWO            do-block-storage   8m43s
```
(v) Now the elasticsearch service is created successfully.
```
dineshsonachalam@macbook tech-courses-search-engine % kubectl get services -n=dinesh
NAME            TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)    AGE
elasticsearch   ClusterIP   10.245.43.67   <none>        9200/TCP   5m23s
```
6. Debugging the elasticsearch pod to ensure whether it is running successfully.
(i) We can fetch all the details about using describe command.
```
dineshsonachalam@macbook tech-courses-search-engine % kubectl describe pod es-0 -n=dinesh
Name:         es-0
Namespace:    dinesh
Priority:     0
Node:         default-pool-8yj5d/10.136.0.3
Start Time:   Wed, 05 May 2021 00:27:59 +0530
Labels:       app=es
              controller-revision-hash=es-79f4768cb
              statefulset.kubernetes.io/pod-name=es-0
Annotations:  <none>
Status:       Running
IP:           10.244.0.132
IPs:
  IP:           10.244.0.132
Controlled By:  StatefulSet/es
Init Containers:
  init-sysctl:
    Container ID:  containerd://4df576b8503c0651fd63a011395e10b5ee4bd02618750e6541eefe014a6d28e1
    Image:         busybox
    Image ID:      docker.io/library/busybox@sha256:ae39a6f5c07297d7ab64dbd4f82c77c874cc6a94cea29fdec309d0992574b4f7
    Port:          <none>
    Host Port:     <none>
    Command:
      /bin/sh
      -c
    Args:
      sysctl -w vm.max_map_count=262144; chown -R 1000:1000 /usr/share/elasticsearch/data
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Wed, 05 May 2021 00:28:04 +0530
      Finished:     Wed, 05 May 2021 00:28:04 +0530
    Ready:          True
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /usr/share/elasticsearch/data from es-data (rw)
      /var/run/secrets/kubernetes.io/serviceaccount from default-token-2dtw4 (ro)
Containers:
  es:
    Container ID:   containerd://8986c1bb6f567b6b27b30ac9d8e36071387775c32c0316e590905ae3b804aa3c
    Image:          docker.elastic.co/elasticsearch/elasticsearch:7.12.0
    Image ID:       docker.elastic.co/elasticsearch/elasticsearch@sha256:4999c5f75c1d0d69754902d3975dd36875cc2eb4a06d7fdceaa8ec0e71a81dfa
    Port:           9200/TCP
    Host Port:      0/TCP
    State:          Running
      Started:      Wed, 05 May 2021 00:28:05 +0530
    Ready:          True
    Restart Count:  0
    Environment:
      discovery.type:  single-node
    Mounts:
      /usr/share/elasticsearch/data from es-data (rw)
      /var/run/secrets/kubernetes.io/serviceaccount from default-token-2dtw4 (ro)
Conditions:
  Type              Status
  Initialized       True
  Ready             True
  ContainersReady   True
  PodScheduled      True
Volumes:
  es-data:
    Type:       PersistentVolumeClaim (a reference to a PersistentVolumeClaim in the same namespace)
    ClaimName:  es-data-es-0
    ReadOnly:   false
  default-token-2dtw4:
    Type:        Secret (a volume populated by a Secret)
    SecretName:  default-token-2dtw4
    Optional:    false
QoS Class:       BestEffort
Node-Selectors:  <none>
Tolerations:     node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                 node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
Events:
  Type     Reason                  Age                From                     Message
  ----     ------                  ----               ----                     -------
  Warning  FailedScheduling        20m (x3 over 20m)  default-scheduler        0/1 nodes are available: 1 pod has unbound immediate PersistentVolumeClaims.
  Normal   Scheduled               20m                default-scheduler        Successfully assigned dinesh/es-0 to default-pool-8yj5d
  Normal   SuccessfulAttachVolume  20m                attachdetach-controller  AttachVolume.Attach succeeded for volume "pvc-e83abdfb-f819-441e-87a9-f4b53cdfec6d"
  Normal   Pulled                  20m                kubelet                  Container image "busybox" already present on machine
  Normal   Created                 20m                kubelet                  Created container init-sysctl
  Normal   Started                 20m                kubelet                  Started container init-sysctl
  Normal   Pulled                  20m                kubelet                  Container image "docker.elastic.co/elasticsearch/elasticsearch:7.12.0" already present on machine
  Normal   Created                 20m                kubelet                  Created container es
  Normal   Started                 20m                kubelet                  Started container es
dineshsonachalam@macbook tech-courses-search-engine % clear
dineshsonachalam@macbook tech-courses-search-engine % kubectl describe pod es-0 -n=dinesh
Name:         es-0
Namespace:    dinesh
Priority:     0
Node:         default-pool-8yj5d/10.136.0.3
Start Time:   Wed, 05 May 2021 00:27:59 +0530
Labels:       app=es
              controller-revision-hash=es-79f4768cb
              statefulset.kubernetes.io/pod-name=es-0
Annotations:  <none>
Status:       Running
IP:           10.244.0.132
IPs:
  IP:           10.244.0.132
Controlled By:  StatefulSet/es
Init Containers:
  init-sysctl:
    Container ID:  containerd://4df576b8503c0651fd63a011395e10b5ee4bd02618750e6541eefe014a6d28e1
    Image:         busybox
    Image ID:      docker.io/library/busybox@sha256:ae39a6f5c07297d7ab64dbd4f82c77c874cc6a94cea29fdec309d0992574b4f7
    Port:          <none>
    Host Port:     <none>
    Command:
      /bin/sh
      -c
    Args:
      sysctl -w vm.max_map_count=262144; chown -R 1000:1000 /usr/share/elasticsearch/data
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Wed, 05 May 2021 00:28:04 +0530
      Finished:     Wed, 05 May 2021 00:28:04 +0530
    Ready:          True
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /usr/share/elasticsearch/data from es-data (rw)
      /var/run/secrets/kubernetes.io/serviceaccount from default-token-2dtw4 (ro)
Containers:
  es:
    Container ID:   containerd://8986c1bb6f567b6b27b30ac9d8e36071387775c32c0316e590905ae3b804aa3c
    Image:          docker.elastic.co/elasticsearch/elasticsearch:7.12.0
    Image ID:       docker.elastic.co/elasticsearch/elasticsearch@sha256:4999c5f75c1d0d69754902d3975dd36875cc2eb4a06d7fdceaa8ec0e71a81dfa
    Port:           9200/TCP
    Host Port:      0/TCP
    State:          Running
      Started:      Wed, 05 May 2021 00:28:05 +0530
    Ready:          True
    Restart Count:  0
    Environment:
      discovery.type:  single-node
    Mounts:
      /usr/share/elasticsearch/data from es-data (rw)
      /var/run/secrets/kubernetes.io/serviceaccount from default-token-2dtw4 (ro)
Conditions:
  Type              Status
  Initialized       True
  Ready             True
  ContainersReady   True
  PodScheduled      True
Volumes:
  es-data:
    Type:       PersistentVolumeClaim (a reference to a PersistentVolumeClaim in the same namespace)
    ClaimName:  es-data-es-0
    ReadOnly:   false
  default-token-2dtw4:
    Type:        Secret (a volume populated by a Secret)
    SecretName:  default-token-2dtw4
    Optional:    false
QoS Class:       BestEffort
Node-Selectors:  <none>
Tolerations:     node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                 node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
Events:
  Type     Reason                  Age                From                     Message
  ----     ------                  ----               ----                     -------
  Warning  FailedScheduling        21m (x3 over 21m)  default-scheduler        0/1 nodes are available: 1 pod has unbound immediate PersistentVolumeClaims.
  Normal   Scheduled               21m                default-scheduler        Successfully assigned dinesh/es-0 to default-pool-8yj5d
  Normal   SuccessfulAttachVolume  21m                attachdetach-controller  AttachVolume.Attach succeeded for volume "pvc-e83abdfb-f819-441e-87a9-f4b53cdfec6d"
  Normal   Pulled                  21m                kubelet                  Container image "busybox" already present on machine
  Normal   Created                 21m                kubelet                  Created container init-sysctl
  Normal   Started                 21m                kubelet                  Started container init-sysctl
  Normal   Pulled                  21m                kubelet                  Container image "docker.elastic.co/elasticsearch/elasticsearch:7.12.0" already present on machine
  Normal   Created                 21m                kubelet                  Created container es
  Normal   Started                 21m                kubelet                  Started container es
```
(ii) To view pod logs for Elasticsearch container.
```
dineshsonachalam@macbook tech-courses-search-engine % kubectl logs es-0 -n=dinesh
{"type": "server", "timestamp": "2021-05-04T18:58:14,039Z", "level": "INFO", "component": "o.e.p.PluginsService", "cluster.name": "docker-cluster", "node.name": "es-0", "message": "loaded module [analysis-common]" }
{"type": "server", "timestamp": "2021-05-04T18:58:14,039Z", "level": "INFO", "component": "o.e.p.PluginsService", "cluster.name": "docker-cluster", "node.name": "es-0", "message": "loaded module [constant-keyword]" }
{"type": "server", "timestamp": "2021-05-04T18:58:14,040Z", "level": "INFO", "component": "o.e.p.PluginsService", "cluster.name": "docker-cluster", "node.name": "es-0", "message": "loaded module [flattened]" }
{"type": "server", "timestamp": "2021-05-04T18:58:14,040Z", "level": "INFO", "component": "o.e.p.PluginsService", "cluster.name": "docker-cluster", "node.name": "es-0", "message": "loaded module [frozen-indices]" }
```
7. Use port-forwarding to access application in a cluster. It's similar to create a tunnel from the cluster and exposing it to our local computer.
```
dineshsonachalam@macbook tech-courses-search-engine % kubectl port-forward service/elasticsearch 9200:9200 -n=dinesh
Forwarding from 127.0.0.1:9200 -> 9200
Forwarding from [::1]:9200 -> 9200
Handling connection for 9200
Handling connection for 9200
```

(ii) Now let's check healthstatus of elasticsearch service. Then let's create, get and delete an index.
```
dineshsonachalam@macbook ~ % curl --location --request GET '127.0.0.1:9200/_cat/health'
1620157487 19:44:47 docker-cluster green 1 1 0 0 0 0 0 0 - 100.0%

dineshsonachalam@macbook ~ % curl --location --request PUT 'http://127.0.0.1:9200/test_index/'
{"acknowledged":true,"shards_acknowledged":true,"index":"test_index"}%

dineshsonachalam@macbook ~ % curl --location --request GET 'http://127.0.0.1:9200/test_index/' | jq .
{
  "test_index": {
    "aliases": {},
    "mappings": {},
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
        "provided_name": "test_index",
        "creation_date": "1620157595345",
        "number_of_replicas": "1",
        "uuid": "IW8dIYvVQ_67r9G7mzp1hQ",
        "version": {
          "created": "7120099"
        }
      }
    }
  }
}
dineshsonachalam@macbook ~ % curl --location --request DELETE 'http://127.0.0.1:9200/test_index/'
{"acknowledged":true}%
```


##### In-progress - Deployment for frontend and backend module.