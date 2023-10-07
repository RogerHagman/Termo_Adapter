# Termo_Adapter

Termo Adapter Facilitates a uniform reading of Thermometer Sensors so that the user may peruse both Fahrenheit and Celsius calibrated sensors in their data. Uniformly converting when needed into Celsius Units.

# USE

The Adaptor interface can be used stand alone to get a reading from sensors to Celsius units for various implementations.

The temperature_converter can be used to wrangle a dataset containing Fahrenheit readings, convert them to Celsius and return the altered dataset containing the processed temperatures in a new row.

convert_temp_readings.ipynb shows an example use on Body Temperature data.