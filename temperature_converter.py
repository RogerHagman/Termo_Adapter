import polars as po
import logging
from sensors import FahrenheitTemperatureSensor, TemperatureSensorAdapter

class TemperatureConverter:
    """
    A class to convert temperatures from Fahrenheit to Celsius utilizing
    the adapter pattern. Resulting in a Polars DataFrame.

    Attributes
    ----------
    dataframe : po.DataFrame
        The input dataframe containing temperature data.
    fahrenheit_sensor : FahrenheitTemperatureSensor
        An instance of FahrenheitTemperatureSensor used to fetch 
        Fahrenheit temperature readings.
    adapter : TemperatureSensorAdapter
        An instance of TemperatureSensorAdapter used to convert 
        Fahrenheit temperatures into Degree Celsius.

    Methods
    -------
    convert_to_celsius(temp_col: str) -> po.DataFrame
        Converts temperatures in a column from Fahrenheit to Celsius 
        and adds the converted temperatures as a new column to the
        DataFrame.
    """
    def __init__(self, dataframe: po.DataFrame):
        """
        Initializes the TemperatureConverter.

        Parameters
        ----------
        dataframe : po.DataFrame
            The input dataframe containing temperature data.
        """
        self.dataframe = dataframe
        self.fahrenheit_sensor = FahrenheitTemperatureSensor()
        self.adapter = TemperatureSensorAdapter(self.fahrenheit_sensor)

    def convert_to_celsius(self, temp_col: str) -> po.DataFrame:
        """
        Converts temperatures from Fahrenheit to Celsius via the 
        adapter. It then adds the converted temperatures as a new 
        column in the DataFrame.

        Parameters
        ----------
        temp_col : str
            The name of the column in `dataframe` containing 
            Fahrenheit temperatures.

        Returns
        -------
        po.DataFrame
            The original DataFrame with an additional column 
            holding temperatures processed into Celsius.
        """
        
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