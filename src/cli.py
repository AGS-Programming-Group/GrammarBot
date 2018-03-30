import argparse

def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--info", action="store_true", help="Sets the logging module to INFO")
    parser.add_argument("-t", "--token", help="Sets the token for the bot")
    return parser.parse_args()
