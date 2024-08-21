<div align="center">
  <h1>SB-Career's-v4 Kubernetes setup</h1>
</div>
This is the extended implementation of the sbcareer's flask web-app, In which i have leveraged the "kubernetes and kops" to create the cluster on AWS EC2 instances, running the containers (pods) in the cluster nodes (EC2 instances). 

- I have also used the AWS EBS to mount the volume to store the data from the MySQL server. 
- Created the deployment files for the flask-app and MySQL database, and also created two service definition files
  - type: ClusterIP for the db, to connect to the flask-app internally
  - type: LoadBalancer, to connect to the flask-app from outside world
- Used the secrets concept in kubernetes to store the sensitive data in a different yaml file and referenced it inside the deployment files.
- I have also created the AWS Route53 routing to my domain pointing to the application LoadBalancer's endpoint, with that domain name we were able to access the website.


<div align="center">
  <h2>Setup</h2>
</div>

NOTE: For the Virtual machine having the kubernetes running, Configure AWS CLI with IAM user which have the permisson - AdministratorAccess, to be able to make create and provision the cluster resources properly
- Create an AWS EC2 instance and install kubernetes and kops in it, configure AWS CLI in it to store the kops cluster configuration.

- To create a cluster definition: 
``` kops create cluster --name=<name-of-the-cluster> --state=s3://<create-s3-bucket-t0-store-config> --zones=us-east-1a,us-east-1b --node-count=2 --node-size=t3.small --master-size=t3.medium --dns-zone=<create-aws-hosted-zone-route53&getDnsName> --node-volume-size=8 --master-volume-size=8 ```

- Create cluster:  ```  kops update cluster --name <your-cluster-name> --yes --admin --state=s3://<your-s3bucket-to-store-cluster-data> ```

- Validate cluster: ```  kops validate cluster --name <your-cluster-name> --state=s3://<your-s3bucket-to-store-cluster-data> ```

- After validating the cluster, apply all the yaml definition files from the k8s-setup branch from the github repository

- Create a AWS EBS volume to store the mysql data: ```aws ec2 create-volume --availability-zone=us-east-1a --size=3 --volume-type=gp2```, and attach enter the vol-id in the Database deployment definition file

- IMP: Give the tag to the EBS volume created,  KubernetesCluster = <Your-kubernetes-cluster-name-defined-at-kops-clusterCreation-stage>, else ndoe won't be able to attach to the EBS volume

- Clone the github repository inside the virtual machine and checkout branch k8s-setup :``` git checkout k8s-setup ```. Then navigate into the Kubernetes directory

- Then create all the deployment and definitions:```kubectl create -f .```

- Now label both the nodes properly according to the zone they are hosted on, with this we will define the db service to run on a node in a particular zone where we have created our EBS block storage

- To get the node labels : ```kubectl get nodes --show-labels```

- Set the zone label to the node instances : ```kubectl label nodes <name-of-the-node-having-zone-us-east-1a> zone=us-east-1a```


<br>
<div align="center">
  <h2>Demo</h2>
</div>

- Access the application using the AWS Elastic LoadBalancer's endpoint

![image](https://github.com/user-attachments/assets/211c54e4-a25c-4d3a-8ba0-a6935aa86e38)

![image](https://github.com/user-attachments/assets/9b19dc6a-bd9a-454c-b01d-d576fbbb36c9)

![image](https://github.com/user-attachments/assets/458e4fb5-95ab-418c-93b4-8c07ec795333)
![image](https://github.com/user-attachments/assets/b8204f72-0248-49f7-a3e7-4b1246014558)

- Getting into the MySQL container pod to check if the user data entry is added in the database or not

![image](https://github.com/user-attachments/assets/99d3f511-bb4a-48ec-9b90-36f593fecded)

- We can see the entry of the user data from the application form is present
  
![image](https://github.com/user-attachments/assets/b6115376-877c-42b0-8da1-c38453d12a56)

- Created a new EC2 instance named MyInstance and attached the EBS block storage(3Gb) which we used to store the MySQL data to it, mounted the disk inside the EC2 instance on /mnt/ebs-vol directory

![image](https://github.com/user-attachments/assets/f42a7480-5f97-4bc8-930f-9b6a1e04af00)

- We can see the MySQL data is there inside this EBS volume, this verifies the MySQL data uploaded successfully on attached EBS vol 

![image](https://github.com/user-attachments/assets/cee20e35-bfc4-487d-a061-b6348521e301)

- Optional: Create a AWS route53 route to the loadBalancer's endpoint. I have created a simple DNS record in route53 hosted zone, which is connecting the application load balancer's endpoint to my domain "sbdevops.xyz". We can access application using this URL also (Notice the URL entered in browser)

![image](https://github.com/user-attachments/assets/7c94e165-0e5d-4f49-bf63-1f2a81b0bf5a)

- We will perform pods, cluster monitoring with the help of "Lens" application

- Get the kube-config file from the kubernetes running node, ```cat ~/.kube/config```

- Copy the config and paste it in the Lens application while creating a new cluster.

- And to get the proper analysis and monitoring, install prometheus on the kubernetes cluster from Lens: https://docs.k8slens.dev/cluster/cluster-metrics/

- These are the cluster dashboard from the Lens tool which gives a great way to monitor and analyse the cluster and its components

![image](https://github.com/user-attachments/assets/c0fe224c-bd41-497f-86f9-aebaab23574e)
![image](https://github.com/user-attachments/assets/c0da7245-10c8-4dcd-9607-61178c8b8ace)
![image](https://github.com/user-attachments/assets/85460fa1-2664-45df-8781-b97b611a4098)
![image](https://github.com/user-attachments/assets/66af1844-e5c1-4637-bb5d-b378e788ecb6)
![image](https://github.com/user-attachments/assets/3967af98-d42d-4f08-b32a-a7f95184ae00)

<div align="center">
<p>Thank you for checking out my project :) </p>
</div>

<div align="center">
  <a href="https://www.linkedin.com/in/sarthak-bokade-1a0321224/">
    <img alt="LinkedIn" src="https://img.shields.io/badge/Connect_with_me-blue?logo=linkedin&logoColor=white">
  </a>
</div>
