import os
import shutil
import json
import pyfiglet
from tqdm import tqdm
import time


class FileOrganizer:

    def __init__(self):

        self.moved_files = 0
        self.ignored_items = 0

    def display_banner(self):
        banner = pyfiglet.figlet_format("File Organizer", font="slant")
        print(banner)
        print("Author: Yassine REZGUI")
        print("-" * 65)
        print("\n")


    def load_configuration(self):
        try:
            with open("organizer/config.json", "r") as config_file:
                self.categories = json.load(config_file)
                print("[+] Configuration loaded successfully!")
        except FileNotFoundError:
            print("Configuration file 'config.json' not found. Please ensure it exists and try again.")
            os._exit(1)




    def scan_directory(self, directory):
        
        try:    

            print("[+] Scanning directory ...")

            files = []

            for item in os.scandir(directory):
                if item.is_file():
                    files.append(item)
                else:
                    self.ignored_items += 1

            return files
        
        except FileNotFoundError:
            print(f"Directory '{directory}' not found. Please check the path and try again.")
            os._exit(1)
        except PermissionError:
            print(f"[x] Permission denied for directory '{directory}'. Please check your permissions and try again.")
        except Exception as e:
            print(f"An error occurred while scanning the directory: {e}")


    def process_files(self, directory):

        files = self.scan_directory(directory)
        if not files:
            print("[-] No files found in the directory.")
            return
        print(f"[+] {len(files)} files found in the directory.\n")

        for item in tqdm(files, desc="File organizing: ",ncols=90):

            full_path = item.path

            extension = item.name.split(".")[-1].lower()
            category = self.get_category(extension)

            category_path = os.path.join(directory, category)
            self.move_file(category_path, full_path)    
        
        print(f"[+] {self.moved_files} files moved successfully!")
        print(f"[+] {self.ignored_items} items ignored (not files).")


            

    def get_category(self, extension):

        for category, extensions in self.categories.items():

            if extension in extensions:
                return category
        return "Others"


    def move_file(self, category_path, full_path):

        try:

            os.makedirs(category_path, exist_ok=True)
                
            file_name = os.path.basename(full_path)
            destination_path = os.path.join(category_path, file_name)
            destination_path = self.get_unique_name(destination_path)

            shutil.move(full_path, destination_path)
            self.moved_files += 1

        except PermissionError as e:
            print(f"Permission denied while moving file '{full_path}': {e}")
        except FileNotFoundError as e:
            print(f"File '{full_path}' not found: {e}")


    def get_unique_name(self, destination_path):
        base, ext = os.path.splitext(destination_path)
        counter = 1

        while os.path.exists(destination_path):
            destination_path = f"{base}({counter}){ext}"
            counter += 1

        return destination_path

        

    

    def run(self):

        while True:

            self.display_banner()

            print("[+] File Organizer started successfully!")
            time.sleep(1)
            self.load_configuration()
            print("\n")

            directory = input("(Enter directory path (type 'exit' to quit)) > ")

            if directory.lower() == "exit":
                print("Exiting File Organizer. Goodbye!")
                break

            time.sleep(1)
            self.process_files(directory)

            input("\nDo you want to organize another directory? (Press Enter to continue or type 'exit' to quit) > ")
            if input().lower() == "exit":
                break
                print("Exiting File Organizer. Goodbye!")

