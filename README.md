# Microservers-python
# Microservices based in python. Implement celery

# This example start up application with fastAPI and when you send a request GET with route http:localhost/file
# Create a task in celery. This task write a file in the .tmp directory 

# Make sure you have a redis image in your docker
docker pull redis
# Execute the follow command
docker compose up
# This command will build the docker container with all dependencies and start de app and services
# Feel free to modify this example whereever you want and enjoy
# If you know how to improve pls tell me.