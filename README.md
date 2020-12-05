# Welcome to Flask-Nginx!

This is a simple Flask - uWsgi - Nginx - Loadbalancing application.
The Application would spin up 3 container of the flask application on port 8080, 8081, 8082.
uwsgi would spawn 4 processes, 2 thread of flask application on each of the above port. Nginx is configured to Round Robin the incomming traffic amoung the 3 ports.

# Design

![enter image description here](https://i.ibb.co/QnKjJDH/Pipeline.png)

# API's and Functionality

- **/flask_GUI** : I have created a simple user interface with you could use to test the functionality of the application. Allows you to add an user, search for a user and View all the users.
	- **/** : Renders SearchUser page.
	- **/AddUser** : Renders AddUser page.
	- **/GetAllUser** : Renders GetAllUser page.
- **/flask_db** : Container for hosting the DB and serves as a DB manager.
	- **/db/execute**  POST {"query" : < SQL QUERY> } :  Return the query output
- **/flast_rest** : 3 Rest API
	- **/rest/searchUser** GET name=< user id> : Returns the user_key of the user ID.
	- **/rest/addUser** POST {"userID":< user id>, "key":< user_key>} : adds the user to the DB.
	- **/rest/getAllUsers** GET : gets all the users in the DB.
- **/nginx** : Consists the mapping of routes to each of the other containers.

# Instructions To Execute

## Environment Setup
1. install Docker https://docs.docker.com/engine/install/

2. install Docker-compose https://docs.docker.com/compose/install/

3. install nginx https://www.nginx.com/resources/wiki/start/topics/tutorials/install/
## Execution:

Make sure you **cd** to the folder which containes the **docker-compose.yml** file 
(Eg: in this application it is the root folder of the project).

If **Docker-cli** was successfully installed then running the following command will start the application.

	docker-compose up --build
