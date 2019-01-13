
# Here we are creating an image for python alphine image.(https://hub.docker.com/r/library/python/)
FROM python:3

# Copying the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

# WORKDIR is nothing but current directory (cd app)
WORKDIR /app

# Install the requirements in the current directory.
RUN pip install -r requirements.txt

# Copying the entire application to the docker container in the app directory.
COPY . /app

# Setting environmental path to app directory. path environment variables tells shell,
# which directories to search for executable files.
ENV PATH /app:$PATH

# It executes the command python app.py in the app directory.
# start gunicorn
CMD ["gunicorn","--config","/app/gunicorn_config.py","app:app"]

EXPOSE 8005
