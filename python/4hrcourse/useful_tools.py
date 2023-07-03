import random

def roll_die(num):
    return random.randint(1,num)

def get_file_ext(filename):
    return filename[filename.index(".") + 1:]

feet_in_mile = 5280