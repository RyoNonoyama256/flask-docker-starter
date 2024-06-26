# Flask Internal App

This is a simple internal web application built with Flask and Docker. It includes basic routes, a file download feature, and Docker support for easy deployment.

## Setup

Follow these steps to set up and run the project locally.

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/my_internal_app.git
cd my_internal_app
```

### 2. Build and Run the Docker Container

Use Docker Compose to build and start the container.

```bash
docker-compose up --build
```

### 3. Access the Application

Once the container is up and running, you can access the application in your web browser at `http://localhost:5000`.

## Cleanup

To stop the application and clean up the Docker environment, use the following commands.

### 1. Stop the Application

Press `Ctrl+C` in the terminal where `docker-compose up` is running, or open a new terminal and run:

```bash
docker-compose down
```

### 2. Remove All Containers, Networks, and Volumes

If you want to remove all containers, networks, and volumes associated with the project, run:

```bash
docker-compose down --rmi all --volumes --remove-orphans
```
