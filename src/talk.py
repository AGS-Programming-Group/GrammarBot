# Import external dependencies
from yaml import load
from random import randint

# Constants
READINGS_CONFIG = "./data/readings.yaml"

with open(READINGS_CONFIG, "r") as file:
    readings = load(file.read())
    readings_n = len(readings)

def reading():
    read = readings[randint(0, readings_n-1)]
    output = f"This morning's reading comes from the book of {read['Author']}:\n    {read['Text']}"
    return output
