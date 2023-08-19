# Use python 3.10 as base image
FROM python:3.10

# Install pip3 and other packages
RUN apt-get update && apt-get install -y \
python3-pip \
&& pip3 install --upgrade pip \
&& pip3 install scikit-image matplotlib numpy opencv-python pyqt5 \
&& apt-get install ffmpeg libsm6 libxext6 -y

# Set the working directory
# WORKDIR /app

# Copy your application files to the container (if needed)
# COPY app/* /app

# Define the default command to run when the container starts
# CMD ["python3", "test.py"]
