

```
# Manage configmap output
kubectl get configmap aws-auth -n kube-system -o yaml
kubectl edit configmap aws-auth -n kube-system

```

```
aws eks --region <region> update-kubeconfig --name <cluster-name>
aws eks --region us-east-1 update-kubeconfig --name e2esa-demo-eks-cluster

# Read the config
cat /home/ubuntu/.kube/config 
```
