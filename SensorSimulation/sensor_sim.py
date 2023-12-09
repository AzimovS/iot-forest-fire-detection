import paho.mqtt.client as mqtt
import random
import time
import configparser
import threading

# Load MQTT configuration from file
config = configparser.ConfigParser()
config.read('config.ini')

client_address = config['mqtt']['client_address']
port = int(config['mqtt']['port'])
topics = {
    'temperature': config['mqtt']['topic_temperature'],
    'humidity': config['mqtt']['topic_humidity'],
    'light_intensity': config['mqtt']['topic_light'],
    'air_quality': config['mqtt']['topic_air_quality']
}

# Function to publish sensor data to MQTT broker
def publish_sensor_data(sensor, topic):
    mqtt_client = mqtt.Client()
    mqtt_client.connect(client_address, port=port)
    while True:
        # Generate random sensor data
        if sensor == 'temperature':
            data = round(random.uniform(20, 30), 2)  # Simulating temperature between 20 to 30 degrees Celsius
        elif sensor == 'humidity':
            data = round(random.uniform(30, 70), 2)  # Simulating humidity between 30% to 70%
        elif sensor == 'light_intensity':
            data = random.randint(0, 1000)  # Simulating light intensity between 0 to 1000
        elif sensor == 'air_quality':
            data = random.randint(0, 500)  # Simulating air quality index between 0 to 500

        mqtt_client.publish(topic, payload=str(data))
        time.sleep(time_sleep)  # Breaks between publishing data (defined in config)

        # Uncomment the line below if you want to see the published data in the console
        #print(f"Published {sensor} data: {data}")

# Publish data for each sensor
threads=[]
for sensor, topic in topics.items():
    thread = threading.Thread(target=publish_sensor_data, args=(sensor, topic))
    threads.append(thread)
    thread.start()

# Wait for all threads to complete (which they won't, as they're infinite loops)
for thread in threads:
    thread.join()
