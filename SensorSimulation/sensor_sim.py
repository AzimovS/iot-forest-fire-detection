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

forests = int(config['data_generation']['forests'])
areas = int(config['data_generation']['areas'])
time_sleep = int(config['data_generation']['time_sleep'])
sensors = config['data_generation']['sensors'].split('|')

mqtt_client = mqtt.Client()
mqtt_client.connect(client_address, port=port)
# Function to publish area data to MQTT broker
def publish_area_data(mqtt_client, sensors, forest, area):
    while True:
        # Generate random sensor data
        for sensor in sensors:
            if sensor == 'temperature':
                data = round(random.uniform(0, 40), 2)  # Simulating temperature between 0 to 40 degrees Celsius
            elif sensor == 'humidity':
                data = round(random.uniform(30, 70), 2)  # Simulating humidity between 30% to 70%
            elif sensor == 'light_intensity':
                data = random.randint(0, 1000)  # Simulating light intensity between 0 to 1000
            elif sensor == 'air_quality':
                data = random.randint(0, 500)  # Simulating air quality index between 0 to 500
            #mqtt_client.publish(topic, payload=str(data))
            topic = f"{sensor}/forest_{forest}/area_{area}"
            mqtt_client.publish(topic, f'{{"{sensor}":{data}}}')
            print(f"Published {topic}: {data}")

        time.sleep(time_sleep)  # Breaks between publishing data (defined in config)
        # Uncomment the line below if you want to see the published data in the console
        # print(f"Published {sensor} data: {data}")

# Publish data for each sensor
threads=[]
for forest in range(forests):
    for area in range(areas):
        thread = threading.Thread(target=publish_area_data, args=(mqtt_client, sensors, forest, area))
        threads.append(thread)
        thread.start()

# Wait for all threads to complete (which they won't, as they're infinite loops)
for thread in threads:
    thread.join()
