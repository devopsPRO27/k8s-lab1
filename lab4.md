# Microservices Application in Flask
- Build a microservices-based application using Flask.
- Add core business logic to each service.
- Dockerize each service.
- Deploy the application in a Minikube environment.


1.  Define Microservices Structure
Identify services based on project requirements ( User Service, Product Service, Order Service).
Design the business logic (BL) for each service ( User Service handles authentication, Product Service manages product data, etc.).
2.  Set Up Flask Application for Each Microservice
Initialize Flask projects for each service in separate folders.
Define routes for each service ( User Service could have /login, /register; Product Service could have /add, /delete).
Implement business logic (BL) within each route:
User Service: Handle login, registration, profile management.
Product Service: Manage adding, removing, and viewing products.
Order Service: Process orders, payment, and track orders.
Test each service locally to ensure they work as standalone applications.
3.  Dockerize Each Microservice
Create Dockerfiles for each microservice:
Specify the base image  .
Install dependencies .
Copy service code into the container.
Set environment variables if needed ( API keys, database URLs).
Build Docker images for each service.
Test the Docker containers locally to ensure each service runs as expected.
4. : Set Up a Local Database in Docker --optional
Use Docker to create a container for a database (e.g., MySQL, PostgreSQL, MongoDB).
Configure each microservice to connect to this local database.
5. : Create a Docker-Compose File for Local --ptional
Write a docker-compose.yml file to define all microservices and the database.
Link each microservice to the database if necessary.
Test the entire application using Docker Compose to ensure services communicate as expected.
6. : Prepare for Kubernetes (Minikube) Deployment
## Create Kubernetes manifests for each microservice:
- Deployment files to define pods and replicas.
- Service files to expose each microservice within the Kubernetes cluster.
- Configure environment variables in Kubernetes manifests for each service ( database connection strings).
7. : Deploy to Minikube
Start Minikube and enable necessary addons (ngress).
Apply Kubernetes manifests to deploy each microservice on Minikube.
Expose services using Ingress if you want a single entry point for your microservices.
8. : Verify and Test in Minikube
Verify each pod is running and services are accessible.
Test each service endpoint to ensure correct functionality and inter-service communication.
9. : Clean Up --optional
Remove resources in Minikube when the testing is complete.
Ensure each student documents their steps, especially around business logic.
