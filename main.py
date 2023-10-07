import logging
from sensors import CelsiusTemperatureSensor, \
    FahrenheitTemperatureSensor, TemperatureSensorAdapter


def display_temperature(sensor):
    """
    Display the temperature of a given sensor in Degree Celsius.

    Args:
        sensor: A temperature sensor object that has a
        `get_temperature_celsius` method.

    Returns:
        None
    """
    print(f"Temperature: {sensor.get_temperature_celsius():.2f} °C")

def test_temperature_sensor_adapter(adapter, 
                                    celsius_sensor, 
                                    fahrenheit_sensor):
    """
    Test the functionality of the TemperatureSensorAdapter. 

    The function sets and tests temperature values, ensuring the
    adapter properly converts from Fahrenheit to Celsius and checks
    that the Celsius readings from the adapter and a Celsius sensor 
    match for corresponding temperature inputs.

    Args:
        adapter (TemperatureSensorAdapter):\
            Instance of TemperatureSensorAdapter.
        celsius_sensor (CelsiusTemperatureSensor):\
            Instance of CelsiusTemperatureSensor.
        fahrenheit_sensor (FahrenheitTemperatureSensor):\
            Instance of FahrenheitTemperatureSensor.

    Returns:
        None
    """
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
    """
    Main script.

    Configures logging, instantiates sensor and adapter objects, 
    displays the temperature readings, and wraps it up by running tests
    in order to validate the TemperatureSensorAdapter is working
    predicably.
    """
    # Logging configuration
    logging.basicConfig(level=logging.INFO,
                    format='%(levelname)s - %(message)s')

    # Instances
    celsius_sensor = CelsiusTemperatureSensor()
    fahrenheit_sensor = FahrenheitTemperatureSensor()
    adapter = TemperatureSensorAdapter(fahrenheit_sensor)

    display_temperature(celsius_sensor)
    if adapter:
        display_temperature(adapter)

    # Testing the Adapter
    test_temperature_sensor_adapter(adapter, celsius_sensor, fahrenheit_sensor)