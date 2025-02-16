# Human and Wild Animal Classifier Web Application
## Installation Methods

### 1. Building with Docker

You can build the Docker image.

#### Prerequisites

- Docker installed on your machine.

#### Steps

1. Clone the repository:
    ```bash
    git clone https://github.com/yegekucuk/classifier1.git
    cd classifier1/web
    ```
2. Build the Docker image:
    ```bash
    docker build -t classifierimage .
    ```

3. Run the Docker container:
    ```bash
    docker run --name classifier -d -p 80:8000 classifierimage
    ```
4. Access the application by navigating to `http://127.0.0.1` in your web browser.

5. You can stop and remove the application with the following command:
    ```bash
    docker rm -f classifier
    ```

### 2. Running Locally with Python

You can also run the application directly on your local machine.

#### Prerequisites

- Python 3.10+ and Pip installed on your environment.

#### Steps

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/classifier1.git
    cd classifier1/web
    ```
2. Create a virtual environment and activate it:
    ```bash
    python3 -m venv env
    source env/bin/activate  # On Windows use `env\\Scripts\\activate`
    ```
3. Install the packages:
    ```bash
    pip install -r requirements.txt
    ```
4. Apply migrations and start the Django development server:
    ```bash
    python manage.py migrate
    python manage.py runserver
    ```
5. Access the application by navigating to `http://localhost:8000` in your web browser.

## Project Files

- **classifier/**: Django application handling image uploads and predictions.
- **project/**: Django project settings and configurations.
- **kube/**: Kubernetes deployment files.
- **Dockerfile**: Instructions to build the Docker image.
- **Jenkinsfile**: CI pipeline configuration.
- **requirements.txt**: Python dependencies required by the project.
- **model.h5**: Pre-trained Keras model used for image classification.
