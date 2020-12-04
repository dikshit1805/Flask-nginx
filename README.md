# Flask-nginx

About:
  This is a simple Flask - uWsgi - Nginx - Loadbalancing application.
  The Application would spin up 3 instance of the flask application on port 8080, 8081, 8082. 
  uwsgi would spawn 4 processes, 2 thread of flask application on each of the above port. Therefore in total 4 Process * 3 Ports = 12 instances of the flask application.
  Nginx is configured to Round Robin the incomming traffic amoung the 3 ports. 

Instruction to run:
  Environment Setup:
    1. install Docker https://docs.docker.com/engine/install/
    2. install Docker-compose https://docs.docker.com/compose/install/
    3. install nginx https://www.nginx.com/resources/wiki/start/topics/tutorials/install/
    
  Execution:
      Make sure you cd to the folder which containes the docker-compose.yml files (Eg in this application it is the root folder of the project).
      if Docker-cli was successfully installed then running the following command will start the application.
        docker-compose up --build 
