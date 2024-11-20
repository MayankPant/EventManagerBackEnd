

## Overview
This project is a EVENT MANAGER. It uses Docker to simplify the setup process and ensures the application runs seamlessly across different environments.

---

## Prerequisites

Before starting, ensure you have the following installed on your system:
- [Git](https://git-scm.com/downloads)
- [Docker](https://www.docker.com/products/docker-desktop)
- [Docker Compose](https://docs.docker.com/compose/install/)

---

## Getting Started

Follow these steps to set up and run the project locally.

### 1. Clone the Repository

Open your terminal and run the following command to clone the repository:

```bash
git clone https://github.com/MayankPant/EventManagerBackEnd.git
```

Navigate into the project directory:

```bash
cd EventManagerBackEnd
```

---

### 2. Build and Run the Docker Container

Use Docker Compose to build and run the application:

```bash
docker-compose up --build
```

This command will:
1. Build the Docker image(s) specified in the `docker-compose.yml` file.
2. Start the containers for the application.

---

## Accessing the Application

Once the container is running:
- Visit [http://localhost:3000/](http://localhost:your-port) to access the application.
- Monitor the logs in your terminal for additional information.

---

## Stopping the Application

To stop the application and its containers, press `Ctrl+C` in your terminal or run:

```bash
docker-compose down
```

---

## Feedback and Contribution

Feel free to fork the repository, open issues, or submit pull requests. Contributions are always welcome!

---

## License

This project is licensed under the [MIT License](LICENSE).  
