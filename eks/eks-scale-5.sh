eksctl get cluster
eksctl get nodegroup --cluster igtik8s
eksctl scale nodegroup --cluster igtik8s -r us-east-2 --nodes-min=2 --nodes-max=6