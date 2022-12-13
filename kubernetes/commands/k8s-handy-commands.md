
```
# without specifying namespace will consider 'default' name space
kubectl get all --namespace=e2esa-webapp01-ns
kubectl get nodes --namespace=e2esa-webapp01-ns
kubectl get pods -o wide --namespace=e2esa-webapp01-ns
kubectl describe pod <podname>
```

Check service
```
kubectl get svc --namespace=e2esa-webapp01-ns
```

Change namespace

```
change-ns <namespace>
change-ns webapp
```

## Create a pod

```
#If kubernetes version is latest then only run below  (without generator tag)
kubectl run e2esa-pod01 --image nginx:latest
```

# Debug pod issue
```
kubectl describe pod <podname>
# check the event section after running destribe on any k8s object for any failure or success
```

# List EKS Clusters
```
eksctl get clusters --region [region]
eksctl get clusters --region us-east-1
```

# Capture Node Group name
```
eksctl get nodegroup --cluster=e2esa-demo-eks-cluster --region us-east-1
```

# Delete Node Group
```
eksctl delete nodegroup --cluster=<clusterName> --name=<nodegroupName>  --region [region]
eksctl delete nodegroup --cluster=eksdemo1 --name=eksdemo1-ng-public1 --region us-east-1
```
  
# Delete Cluster
```
eksctl delete cluster <clusterName> --region [region]
eksctl delete cluster eksdemo1 --region us-east-1
```

# Pod port details

```
### nodePort:31961 - node port
### port:81 - service port
### targetPort: 80 -  this is container port or application port
```

## Pod logs

```
kubectl logs <pod-name> 
kubectl logs <pod-name> -c <container-name>
kubectl logs -l name=<my-label> <pod-name> -c <container-name>
kubectl logs -f <pod-name> # streams pod log stdout 
kubectl logs -f <pod-name> -c <container-name>
```
# Connect to container in a pod

```
kubectl exec -it <pod-name> -- /bin/bash

ls
cd /usr/share/nginx/html
cat index.html
exit

# to get all env variables
kubectl exec -it <pod-name> env
kubectl exec -it <pod-name> ls
kubectl exec -it <pod-name> cat /usr/share/nginx/html/index.html
```

## Get YAML definition as output

```
kubectl get pod <pod-name> -o yaml
kubectl get pod <service-name> -o yaml
```

# Expose ReplicaSet as a service
```
kubectl expose rs <ReplicaSer name> --type=NodePort --port=80 --target-port=8080 -name=<service-name-to-be-created>
```
# Expose Deployment as a service
```
kubectl expose deployment <deployment name> --type=NodePort --port=80 --target-port=8080 -name=<service-name-to-be-created>
```
```
# Create Deployment
kubectl create deployment <Deplyment-Name> --image=<Container-Image>
kubectl create deployment my-first-deployment --image=stacksimplify/kubenginx:1.0.0 

# Verify Deployment
kubectl get deployments  --namespace=e2esa-webapp01-ns
kubectl get deploy  --namespace=e2esa-webapp01-ns

# Describe Deployment
kubectl describe deployment <deployment-name>
kubectl describe deployment my-first-deployment

# Verify ReplicaSet
kubectl get rs

# Verify Pod
kubectl get po
```

## Scale deployment
```
# Scale Up the Deployment
kubectl scale --replicas=20 deployment/<Deployment-Name>
kubectl scale --replicas=20 deployment/my-first-deployment 

# Verify Deployment
kubectl get deploy

# Verify ReplicaSet
kubectl get rs

# Verify Pods
kubectl get po

# Scale Down the Deployment
kubectl scale --replicas=10 deployment/my-first-deployment 
kubectl get deploy
```

# Expose Deployment as a service
```
# Expose Deployment as a Service
kubectl expose deployment <Deployment-Name>  --type=NodePort --port=80 --target-port=80 --name=<Service-Name-To-Be-Created>
kubectl expose deployment my-first-deployment --type=NodePort --port=80 --target-port=80 --name=my-first-deployment-service

# Get Service Info
kubectl get svc
Observation: Make a note of port which starts with 3 (Example: 80:3xxxx/TCP). Capture the port 3xxxx and use it in application URL below. 

# Get Public IP of Worker Nodes
kubectl get nodes -o wide
Observation: Make a note of "EXTERNAL-IP" if your Kubernetes cluster is setup on AWS EKS.
```

```
http://<worker-node-public-ip>:<Node-Port>
```
 
## Create Namespace
```
kubectl create -f https://raw.githubusercontent.com/e2eSolutionArchitect/scripts/main/kubernetes/create-namespace.yaml
```
