
```
kubectl get nodes
kubectl get nodes -o wide
```

Create a pod

```
kubectl run <desired-pod-name> --image <Container-Image> --generator=run-pod/v1
kubectl run e2esa-pod01 --image nginx:latest --generator=run-pod/v1

# generator is added to deploy pod as a pod instead of deployment
```

