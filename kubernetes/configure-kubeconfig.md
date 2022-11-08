
Configure k8s cluster in bastion instance or your local system where kubectl is installed 

```
aws eks --region us-east-1 update-kubeconfig --name e2esa-demo-eks-cluster

wget https://s3.us-west-2.amazonaws.com/amazon-eks/docs/eks-console-full-access.yaml

#Please make sure you have AWS CLI configured in the system

kubectl apply -f eks-console-full-access.yaml
```
