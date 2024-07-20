import os
import schedule
import time

directory_in_str = r"C:\Users\jeroe\OneDrive\Coding Projects\Python\Discord-To-Drive\temp"
directory = os.fsencode(directory_in_str)

filecount = 0

def clean_temp_folder():
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        full_path_to_file = os.path.join(directory_in_str, filename)
        os.remove(full_path_to_file)
        filecount + 1
    print(f"Successfully ran clean-up script at 00:00, removed {filecount} files")

schedule.every().day.at("12:00").do(clean_temp_folder)


while True:
    schedule.run_pending()
    time.sleep(1)
