import logging
from temperature_converter import TemperatureConverter
from sensors import CelsiusTemperatureSensor, \
    FahrenheitTemperatureSensor, TemperatureSensorAdapter


def display_temperature(sensor):
    print(f"Temperature: {sensor.get_temperature_celsius():.2f} °C")

def test_temperature_sensor_adapter(adapter, celsius_sensor, fahrenheit_sensor):
    logging.info(f"Testing Thermometers")
    adapter.set_temperature(100)
    fahrenheit_sensor.set_temperature(100)
    assert abs(adapter.get_temperature_celsius() - 37.7778) < 0.0001, \
        "Adapter conversion is incorrect"
    celsius_sensor.set_temperature(0)
    adapter.set_temperature(32)
    assert abs(celsius_sensor.get_temperature_celsius() \
               - adapter.get_temperature_celsius()) < 0.0001, \
                "Adapter conversion is incorrect"

    print("All tests passed!")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                    format='%(levelname)s - %(message)s')

    celsius_sensor = CelsiusTemperatureSensor()
    fahrenheit_sensor = FahrenheitTemperatureSensor()
    adapter = TemperatureSensorAdapter(fahrenheit_sensor)

    display_temperature(celsius_sensor)
    if adapter:
        display_temperature(adapter)

    # Testing the Adapter
    test_temperature_sensor_adapter(adapter, celsius_sensor, fahrenheit_sensor)