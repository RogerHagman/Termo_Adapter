import logging

class CelsiusTemperatureSensor:
    def __init__(self):
        self._temperature = 25

    def set_temperature(self, temperature):
        self._temperature = temperature

    def get_temperature_celsius(self):
        return self._temperature

class FahrenheitTemperatureSensor:
    def __init__(self):
        self._temperature = 77

    def set_temperature(self, temperature):
        self._temperature = temperature

    def get_temperature_fahrenheit(self):
        return self._temperature

class TemperatureSensorAdapter:
    def __init__(self, sensor: FahrenheitTemperatureSensor):
        self.sensor = sensor

    def set_temperature(self, temperature):
        celsius = (temperature - 32) * 5/9
        logging.info(f"Setting Fahrenheit sensor to {temperature:.2f}F ({celsius:.2f}C)")
        self.sensor.set_temperature(temperature)

    def get_temperature_celsius(self):
        fahrenheit = self.sensor.get_temperature_fahrenheit()
        celsius = (fahrenheit - 32) * 5/9
        logging.info(f"Getting Celsius {celsius:.2f} °C for Fahrenheit sensor value {fahrenheit:.2f}F")
        return celsius