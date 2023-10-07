import polars as po
import logging
from sensors import FahrenheitTemperatureSensor, TemperatureSensorAdapter

class TemperatureConverter:
    def __init__(self, dataframe: po.DataFrame):
        self.dataframe = dataframe
        self.fahrenheit_sensor = FahrenheitTemperatureSensor()
        self.adapter = TemperatureSensorAdapter(self.fahrenheit_sensor)

    def convert_to_celsius(self, temp_col: str) -> po.DataFrame:
        """Convert a DataFrame of temperatures in Fahrenheit to Celsius
        using the adapter."""
        
        # Converting Fahrenheit to Celsius
        logging.info(f"Converting Temperatures")
        temperatures_celsius = [
            self.adapter.get_temperature_celsius() 
            for temp_f in self.dataframe[temp_col].to_list()
            # set_temperature() return None is the expected behavior
            if self.fahrenheit_sensor.set_temperature(temp_f) is None
        ]
        # Adding a new column to Polar dataframe with converted temperatures
        self.dataframe = self.dataframe.hstack(po.DataFrame({
            "Temperature_C": temperatures_celsius
        }))
        
        return self.dataframe