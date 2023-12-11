FROM python:3.11
WORKDIR ./
COPY . .
RUN pip3 install paho-mqtt
CMD ["python3", "sensor_sim.py"]