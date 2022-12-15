
Configure k8s cluster in bastion instance or your local system where kubectl is installed 

```
aws eks --region us-east-1 update-kubeconfig --name e2esa-demo-eks-cluster

wget https://s3.us-west-2.amazonaws.com/amazon-eks/docs/eks-console-full-access.yaml
```
```
#Please make sure you have AWS CLI configured in the system

kubectl apply -f eks-console-full-access.yaml
```


output

```
ubuntu@ip-172-31-47-155:~$ ls
eks-console-full-access.yaml
ubuntu@ip-172-31-47-155:~$ aws eks --region us-east-1 update-kubeconfig --name e2esa-demo-eks-cluster
Added new context arn:aws:eks:us-east-1:<accountno>:cluster/e2esa-demo-eks-cluster to /home/ubuntu/.kube/config
ubuntu@ip-172-31-47-155:~$ kubectl apply -f eks-console-full-access.yaml
error: You must be logged in to the server (the server has asked for the client to provide credentials)
ubuntu@ip-172-31-47-155:~$ aws configure
AWS Access Key ID [None]: #########
AWS Secret Access Key [None]: ########
Default region name [None]: 
Default output format [None]: 
ubuntu@ip-172-31-47-155:~$ kubectl apply -f eks-console-full-access.yaml
clusterrole.rbac.authorization.k8s.io/eks-console-dashboard-full-access-clusterrole created
clusterrolebinding.rbac.authorization.k8s.io/eks-console-dashboard-full-access-binding created
ubuntu@ip-172-31-47-155:~$ kubectl edit configmap aws-auth -n kube-system
configmap/aws-auth edited
ubuntu@ip-172-31-47-155:~$ eksctl get clusters --region us-east-1
NAME                    REGION          EKSCTL CREATED
e2esa-demo-eks-cluster  us-east-1       False
ubuntu@ip-172-31-47-155:~$ kubectl get nodes -o wide
NAME                           STATUS   ROLES    AGE   VERSION               INTERNAL-IP    EXTERNAL-IP     OS-IMAGE         KERNEL-VERSION                 CONTAINER-RUNTIME
ip-172-31-8-166.ec2.internal   Ready    <none>   24m   v1.23.9-eks-ba74326   172.31.8.166   100.26.149.66   Amazon Linux 2   5.4.209-116.367.amzn2.x86_64   docker://20.10.17
ip-172-31-84-68.ec2.internal   Ready    <none>   24m   v1.23.9-eks-ba74326   172.31.84.68   54.163.177.23   Amazon Linux 2   5.4.209-116.367.amzn2.x86_64   docker://20.10.17
ubuntu@ip-172-31-47-155:~$
```

Update configmap
```
kubectl edit configmap aws-auth -n kube-system
```

configmap to allow an ec2 bastion host to connect to cluster by role "e2esa-ec2-profile-bastion-role".
Goal is to allow any user who connects through bastion host should be able to connect eks clsuter without using user's aws creds

```
apiVersion: v1
data:
  mapRoles: |
    - groups:
      - system:bootstrappers
      - system:nodes
      rolearn: arn:aws:iam::<aws-acc-no>:role/e2esa-eks-nodegroup-role
      username: system:node:{{EC2PrivateDNSName}}
    - rolearn: arn:aws:iam::<aws-acc-no>:role/e2esa-eks-cluster-access-role
      username: eksadmin
      groups:
      - system:masters
    - rolearn: arn:aws:iam::<aws-acc-no>:role/e2esa-ec2-profile-bastion-role
      username: ec2bastionusr
      groups:
      - system:masters
  mapUsers: |
    - userarn: arn:aws:iam::<aws-acc-no>:user/<iam-user-name>
      username: <iam-user-name>
      groups:
      - system:bootstrappers
      - system:nodes
	  - system:masters
      - eks-console-dashboard-full-access-group
kind: ConfigMap
metadata:
  creationTimestamp: "2022-11-02T19:37:33Z"
  name: aws-auth
  namespace: kube-system
  resourceVersion: "730"
  uid: 1cghhtf0-bgh3-4ed1-b7df-e9dd7310oj7fd
```

multiple user can be added like below
```
    mapUsers: |
    - userarn: arn:aws:iam::<aws-acc-no>:user/<iam-user-name>
      username: <iam-user-name>
      groups:
      - e2esa-development-role-01 # Role from K8S Role contructs
      - system:bootstrappers
      - system:nodes
      - eks-console-dashboard-full-access-group

```
