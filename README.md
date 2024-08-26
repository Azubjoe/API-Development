
#### Project: API Development 

This document provides a step-by-step guide for buiding a simple containerized RESTful API that returns the current server time in West Africa Time (WAT) using Docker. It will walk you through creating the API using Python and Flask, and then show you how to containerize it.

### 1. Create the Flask Application

First, let's create the Flask application, which will be the same as in the previous example.

**File: `app.py`**

```python
from flask import Flask, jsonify
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/time', methods=['GET'])
def get_current_time():
    # Set the timezone to West Africa Time (WAT)
    wat_timezone = pytz.timezone('Africa/Lagos')  # Lagos, Nigeria is in WAT
    current_time = datetime.now(wat_timezone)
    
    # Format the time as a string
    formatted_time = current_time.strftime('%Y-%m-%d %H:%M:%S %Z')
    
    # Return the time in JSON format
    return jsonify({'current_time': formatted_time})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

### 2. Create a `Dockerfile`

Now, let's create a `Dockerfile` to containerize the application.

**File: `Dockerfile`**

```Dockerfile
# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir Flask pytz

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "app.py"]
```

### 3. Create a `requirements.txt`

To specify the dependencies for your Flask application, create a `requirements.txt` file.

**File: `requirements.txt`**

```
Flask
pytz
```

### 4. Build the Docker Image

Next, you need to build the Docker image. Open a terminal and navigate to the directory containing the `Dockerfile`, `app.py`, and `requirements.txt`. Then run the following command:

```bash
docker build -t wat-time-api .
```

### 5. Run the Docker Container

After the image is built, you can run it as a container:

```bash
docker run -d -p 5000:5000 wat-time-api
```

This command runs the container in detached mode (`-d`) and maps port 5000 on your host to port 5000 in the container (`-p 5000:5000`).

### 6. Access the API

Now you can access the API by navigating to `http://localhost:5000/time` in your web browser or using `curl`:

```bash
curl http://localhost:5000/time
```

### 7. Example Output using curl http://localhost:5000/time to access the API

The API should return the current server time in WAT in a JSON format like this:

```json
{
    "StatusCode        : 200
     StatusDescription : OK
     Content           : {"current_time":"2024-08-26 14:37:28 WAT"}"
}
```

### Summary

- **Flask** serves as the framework for the API.
- **Docker** containerizes the application, making it portable and easy to deploy.
- **Dockerfile** defines the environment and steps needed to run the application inside a container.


