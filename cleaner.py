"""os module"""
import os
import json
import time
import schedule


with open("config.json", "r", encoding="utf-8") as config_file:
    config = json.load(config_file)

directory_in_str = config["directory_to_remove"]
time_to_remove = config["time_24h"]

directory = os.fsencode(directory_in_str)

def filenames():
    print(f"Files in {config["directory_to_remove"]}:")
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        print(filename)

def clean_temp_folder():
    """Function to clean specified folder"""
    
    succesfull = False
    filecount = 0
    for file in os.listdir(directory):
        filecount = filecount + 1
        filename = os.fsdecode(file)
        full_path_to_file = os.path.join(directory_in_str, filename)
        try:
            os.remove(full_path_to_file)
            succesfull = True
        except OSError as error:
            print(error)
    if succesfull == True:
        print(f"Successfully ran clean-up script at {time_to_remove}, removed {filecount} files")
    else:
        print(f"A file could not be deleted, please check {config["directory_to_remove"]}")

schedule.every().day.at(time_to_remove).do(filenames)
schedule.every().day.at(time_to_remove).do(clean_temp_folder)

while True:
    schedule.run_pending()
    time.sleep(1)
