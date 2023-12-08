from sensor_simulation import SensorManager
from sensor_simulation.clients import MqttClient
from sensor_simulation.sensors import TemperatureSensor, HumiditySensor, LightIntensitySensor
import random

if __name__ == '__main__':
   mqtt_client = MqttClient('ffd.broker.org')
   
   temperature_sensor = TemperatureSensor(mqtt_client, 'sensor/temperature')
   humidity_sensor = HumiditySensor(mqtt_client, 'sensor/humidity')
   light_intensity_sensor = LightIntensitySensor(mqtt_client, 'sensor/light_intensity')
   
   sensor_manager = SensorManager()
   sensor_manager.add_sensor(temperature_sensor)
   sensor_manager.add_sensor(humidity_sensor)
   sensor_manager.add_sensor(light_intensity_sensor)
   
   try:
       sensor_manager.run()
   except KeyboardInterrupt:
       sensor_manager.stop_all()
