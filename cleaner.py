"""os module"""
import os
import time
import json
import schedule

with open("config.json", "r", encoding="utf-8") as config_file:
    config = json.load(config_file)

directory_in_str = config["directory_to_remove"]
time_to_remove = config["time_24h"]

directory = os.fsencode(directory_in_str)

def clean_temp_folder():
    failed_files = []
    succesfull = False
    filecount = 0
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        full_path_to_file = os.path.join(directory_in_str, filename)
        try:
            os.remove(full_path_to_file)
            succesfull = True
            print(filename)
            filecount = filecount + 1
        except OSError as error:
            print(error)
            failed_files.append(filename)
    if succesfull == True:
        print(f"Successfully ran clean-up script at {time_to_remove}, removed {filecount} files")
    if failed_files != []:
        print(f"Multiple files could not be deleted: \n {failed_files}")
        
schedule.every().day.at(time_to_remove).do(clean_temp_folder)

while True:
    schedule.run_pending()
    time.sleep(1)