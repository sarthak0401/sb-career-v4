<div align="center">
  <h1>SB-careers-website </h1>
  <p>"kubernetes implementation in k8s-setup branch"</p>
</div>
A careers website, in which I haved used the python framework flask to build this web application and made it functional, which will be running on a docker container. Upon clicking the apply button next to the jobs, an application form will appear.  And upon filling the details, it will get stored in the MySQL database running on the another container. This application also gives the function (route) to download the resume corresponding to a particular user, which will be useful for the recruiters

- Install dependencies: [Docker](https://docs.docker.com/engine/install/), [Docker Compose plugin](https://docs.docker.com/compose/install/linux/)
  
- Clone the repository and run below commands to run SB Career's application in your pc

- To build the docker images and running them on docker container : ```docker compose build --no-cache && docker compose up -d```

- To get the container id on which the flask application is running : ```docker ps ```

- To get the IP address of the container: ```docker inspect <flask-app-container-id> ```

- Enter ```<ip-of-flask-container>:5000``` in the browser, since flask app is running by default on port 5000

![image](https://github.com/user-attachments/assets/056071ac-66d1-49d0-ad1b-c642b1c46428)

![image](https://github.com/user-attachments/assets/6ccd4b5b-3545-4597-b669-a6e511bb0a77)

![image](https://github.com/user-attachments/assets/01d06925-7e6b-4253-9b6e-4e045471274e)

![image](https://github.com/user-attachments/assets/a01625c6-6264-4f58-8aa8-f4d30e854e6b)
- Upon clicking the apply button, application form page for respective job will come come

![image](https://github.com/user-attachments/assets/cc694dcb-9c9b-4dbb-bf0c-cd759dd7da5f)

![image](https://github.com/user-attachments/assets/473cab45-175c-41d4-a360-31164938c2c3)

![image](https://github.com/user-attachments/assets/652b3145-18cf-4030-b83d-09a3d089abe1)



- Getting into the mysql database container, for checking the entries of the db 

![image](https://github.com/user-attachments/assets/0c6119ba-bcc0-4082-8363-32418956bdd4)
- We can see the entry is showed up after the submit button is clicked

![image](https://github.com/user-attachments/assets/38878f7f-41eb-4eda-93ff-af63cfec8d09)
- I have also give a flask app route to download the resume ("/download/id_number"), This route will be used by the recruters to Download the resume of the applicant using the id number of the applicant and it is kept hidden, so only recruiters can download the resume

![image](https://github.com/user-attachments/assets/e21dbb87-0fea-4da8-913b-00b26e8a525b)

- Contact us button, opens the default Email-application along with the Email-id of us, so that user can contact us 

![image](https://github.com/user-attachments/assets/d2949269-2125-4822-9276-7f1779ccbe98)

## Do check the kubernetes implementation of this project : https://github.com/sarthak0401/sb-career-v4/tree/k8s-setup


<div align="center">
<p>Thank you for checking out my project :) </p>
</div>

<div align="center">
  <a href="https://www.linkedin.com/in/sarthak-bokade-1a0321224/">
    <img alt="LinkedIn" src="https://img.shields.io/badge/Connect_with_me-blue?logo=linkedin&logoColor=white">
  </a>
</div>
