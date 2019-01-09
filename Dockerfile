# Dockerfile to run a Django-based web application
# Based on an AMI
# https://medium.com/@rohitkhatana/deploying-django-app-on-aws-ecs-using-docker-gunicorn-nginx-c90834f76e21

# Set the abse image to use Ubuntu
FROM ubuntu:16.04

# Set the file maintainer
MAINTAINER William Dana

# Set env variables used in this Dockerfile with unique prefix DOCKYARD
# Local directory with project source

#ENV DOCKYARD_SRC=wrote_note_api/apps/notes
ENV DOCKYARD_SRC=wrote_note_api
# Directory in container for all project files
ENV DOCKYARD_SRVHOME=/srv
# Directory in container for project source files
ENV DOCKYARD_SRVPROJ=$DOCKYARD_SRVHOME/$DOCKYARD_SRC

# Update the default application repository sources list
RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y apt-utils
RUN apt-get install -y python3 python3-pip
RUN apt-get install -y python3-dev
RUN apt-get install -y postgresql postgresql-contrib
RUN apt-get install -y git
RUN apt-get install -y vim
RUN apt-get install -y nginx

# Copy application source code to SRCDIR
COPY $DOCKYARD_SRC $DOCKYARD_SRVPROJ

# Create application subdirectories
WORKDIR $DOCKYARD_SRVHOME
RUN mkdir media static logs
# Read
VOLUME ["$DOCKYARD_SRVHOME/media/", "$DOCKYARD_SRVHOME/logs/"]

# Debug
RUN echo $DOCKYARD_SRC
RUN echo $DOCKYARD_SRVPROJ

## Copy application source code to SRCDIR
#COPY $DOCKYARD_SRC $DOCKYARD_SRVPROJ

# Debug
RUN ls $DOCKYARD_SRVPROJ

# Upgrade pip
RUN pip3 install --upgrade pip

# Install Python dependencies
RUN pip3 install -r $DOCKYARD_SRVPROJ/requirements.txt

# Port to expose
EXPOSE 8000

# Copy entrypoint script into the image
WORKDIR $DOCKYARD_SRVPROJ
COPY ./docker-entrypoint.sh /
COPY ./django_nginx.conf /etc/nginx/sites-available/
RUN ln -s /etc/nginx/sites-available/django_nginx.conf /etc/nginx/sites-enabled
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
ENTRYPOINT ["/docker-entrypoint.sh"]
