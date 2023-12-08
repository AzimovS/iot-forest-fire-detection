from typing import Any
from sensor_simulation import SensorManager
from sensor_simulation.sensors import base_sensor
from sensor_simulation.clients import MqttClient
from sensor_simulation.sensors import TemperatureSensor, HumiditySensor, LightIntensitySensor
import configparser

#Read the config file
config = configparser.ConfigParser()
config.read('config.ini')

mqtt_client_address = config.get('DEFAULT', 'mqtt_client_address')
mqtt_port = config.getint('DEFAULT', 'mqtt_port')
topics = config.get('DEFAULT', 'topics').split(',')
number_of_areas = config.getint('DEFAULT', 'number_of_areas')
number_of_forests = config.getint('DEFAULT', 'number_of_forests')

# Create the MQTT client
mqtt_client = MqttClient(mqtt_client_address, mqtt_port)


# Create the sensors
temperature_sensor = TemperatureSensor(mqtt_client, topics[0])
humidity_sensor = HumiditySensor(mqtt_client, topics[1])
light_intensity_sensor = LightIntensitySensor(mqtt_client, topics[2])
#air_quality_sensor = AirQualitySensor(mqtt_client, topics[3])

# Add the sensors to the SensorManager
sensor_manager = SensorManager()
sensor_manager.add_sensor(temperature_sensor)
sensor_manager.add_sensor(humidity_sensor)
sensor_manager.add_sensor(light_intensity_sensor)
#sensor_manager.add_sensor(air_quality_sensor)

try:
   sensor_manager.run()
except KeyboardInterrupt:
   sensor_manager.stop_all()