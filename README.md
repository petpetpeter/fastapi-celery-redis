# Sample FastAPI Application to demonstrate Async architecture with Celery and Reddis

## Overview
![Diagram](docs/diagram.png)

## Original Implementation From

https://github.com/sumanentc/fastapi-celery-rabbitmq-application

## List of Changes:
- Dockerized the application
- Added Redis as a broker

## How to run
- build the docker image
    ```
    docker compose -f deployment/docker-compose.yaml build
    ```
- run the docker image
    ```
    docker compose -f deployment/docker-compose.yaml up -d
    ```

## Test with swagger
- visit http://localhost:9000/docs

![Swagger UI Screenshot](docs/swagger.png)

## Visualize running tasks with flower
- visit http://localhost:5555

![Flower UI Screenshot](docs/flower.png)
