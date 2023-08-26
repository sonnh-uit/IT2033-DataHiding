FROM python:3.6

# Install pip3 and other packages
RUN apt-get update && apt-get install -y \
python3-pip \
&& pip3 install --upgrade pip \
&& pip3 install scikit-image matplotlib numpy opencv-python pyqt5 seaborn steganogan
