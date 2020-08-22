# set base image (host OS)
FROM python:3.8

# set the working directory in the container
WORKDIR /app

# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

# copy the content of the local src directory to the working directory
COPY . /app

ENV APP_SETTINGS 'config.DevelopmentConfig'
ENV DATABASE_URL "mysql+mysqlconnector://root:testing@172.17.0.4:3306/health"
EXPOSE 5000

# command to run on container start
#CMD [ "python", "./app.py" ]