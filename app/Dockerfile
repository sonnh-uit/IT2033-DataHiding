# Use python 3.10 as base image
FROM python:3.10

# Install pip3 and other packages
RUN apt-get update && apt-get install -y python3-pip wget \
&& pip3 install --upgrade pip 

COPY ninja /usr/bin/ninja
RUN chmod +x /usr/bin/ninja

COPY setup.sh /setup.sh
RUN chmod +x /setup.sh
RUN bash /setup.sh

COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip3 install -r requirements.txt



# Set the working directory
# WORKDIR /app

# Copy your application files to the container (if needed)
# COPY app/* /app

# Define the default command to run when the container starts
# CMD ["python3", "test.py"]
