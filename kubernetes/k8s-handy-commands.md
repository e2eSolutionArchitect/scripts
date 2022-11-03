
```
kubectl get nodes
kubectl get nodes -o wide
kubectl describe pod <podname>
```

## Create a pod

```
kubectl run <desired-pod-name> --image <Container-Image> --generator=run-pod/v1
kubectl run e2esa-pod01 --image nginx:latest --generator=run-pod/v1

# generator is added to deploy pod as a pod instead of deployment

#If kubernetes version is latest then only run below 
kubectl run e2esa-pod01 --image nginx:latest
```

# Debug pod issue
```
kubectl describe pod <podname>
# check the event section after running destribe on any k8s object for any failure or success
```

