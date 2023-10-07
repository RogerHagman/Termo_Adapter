import logging

class CelsiusTemperatureSensor:
    """
    A class used to represent a Celsius temperature sensor.
    """
    def __init__(self):
        """
        Initializes the CelsiusTemperatureSensor with a default 
        temperature of 25°C.
        """
        self._temperature = 25

    def set_temperature(self, temperature):
        """
        Sets the sensor's temperature to a new value.

        Args:
            temperature (float): \
                The new temperature value in Degree Celsius to be set.
        """
        self._temperature = temperature

    def get_temperature_celsius(self):
        """
        Gets the current temperature from the sensor.

        Returns:
            float: The current temperature in Degree Celsius.
        """
        return self._temperature


class FahrenheitTemperatureSensor:
    """
    A class used to represent a Fahrenheit temperature sensor.
    """
    def __init__(self):
        """
        Initializes the FahrenheitTemperatureSensor to a default
        temperature of 77°F.
        """
        self._temperature = 77

    def set_temperature(self, temperature):
        """
        Sets the sensor's temperature to a new value.

        Args:
            temperature (float): \
                The new temperature value in Fahrenheit to be set.
        """
        self._temperature = temperature

    def get_temperature_fahrenheit(self):
        """
        Gets the current temperature from the sensor.

        Returns:
            float: The current temperature in Fahrenheit.
        """
        return self._temperature


class TemperatureSensorAdapter:
    """
    A class used to adapt a FahrenheitTemperatureSensor to return
    temperatures in Celsius.
    """
    def __init__(self, sensor: FahrenheitTemperatureSensor):
        """
        Initializes the TemperatureSensorAdapter.

        Args:
            sensor (FahrenheitTemperatureSensor): \
                An instance of FahrenheitTemperatureSensor.
        """
        self.sensor = sensor

    def set_temperature(self, temperature):
        """
        Sets the temperature of the adapted Fahrenheit sensor and logs
        the action.

        Args:
            temperature (float): \
                The new temperature value in Fahrenheit to be set.

        Returns:
            None
        """
        celsius = (temperature - 32) * 5/9
        logging.info(f"Setting Fahrenheit sensor to \
                     {temperature:.2f}F ({celsius:.2f}C)")
        self.sensor.set_temperature(temperature)

    def get_temperature_celsius(self):
        """
        Retrieves the temperature from the adapted Fahrenheit sensor, 
        converts it to Celsius, and logs the action.

        Returns:
            float: The current temperature in Celsius.
        """
        fahrenheit = self.sensor.get_temperature_fahrenheit()
        celsius = (fahrenheit - 32) * 5/9
        logging.info(f"Getting Celsius {celsius:.2f} °C for Fahrenheit sensor value {fahrenheit:.2f}F")
        return celsius