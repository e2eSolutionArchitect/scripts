
aws eks --region us-east-1 update-kubeconfig --name e2esa-tutorials-eks-cluster

wget https://s3.us-west-2.amazonaws.com/amazon-eks/docs/eks-console-full-access.yaml

kubectl apply -f eks-console-full-access.yaml
