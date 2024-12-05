import requests
import argparse
import shutil
import os
from dotenv import load_dotenv

def load_arg_parser() -> dict:
    parser = argparse.ArgumentParser(description="Advent of Code command-line application.")

    parser.add_argument('-day', type=int, required=True, help="The day of the Advent of Code challenge.")
    parser.add_argument('-year', type=int, required=False, help="The year of the Advent of Code challenge.", default=2024)
        
    parser.add_argument('--input-only', action='store_true', help="Only download the input for the challenge.")
    parser.add_argument('--init-only', action='store_true', help="Only initialize the files and structure for the challenge.")

    args = parser.parse_args()
        
    if args.input_only:
        print("Option: Input only (downloading the input for the challenge).")

    if args.init_only:
        print("Option: Init only (setting up the files and structure).")
        
    if args.input_only and args.init_only:
        print("You cannot use both --input-only and --init-only at the same time.")
        exit()
    
    return args

def create_day_folder(day: int) -> str:
    folder_name = f"Day{day:02}"
    
    # Check if the folder already exists
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)  # Create the directory if it doesn't exist
        print(f"Created directory: {folder_name}")
    else:
        print(f"Directory {folder_name} already exists. Skipping creation.")
    
    return folder_name

def create_day_project(day: int):
    folder_name = create_day_folder(day)

    # Define the path for the template.py file
    template_file_path = "template.py"  # Adjust if template.py is in a different location
    
    # Check if the template file exists
    if not os.path.exists(template_file_path):
        print("template.py file not found!")
        return

    try:
        # Copy template.py to p1.py and p2.py in the new directory
        shutil.copy(template_file_path, os.path.join(folder_name, "p1.py"))
        shutil.copy(template_file_path, os.path.join(folder_name, "p2.py"))
        
        # Modify p1.py and p2.py by replacing the DAY variable
        for filename in ["p1.py", "p2.py"]:
            file_path = os.path.join(folder_name, filename)
            with open(file_path, "r") as file:
                file_contents = file.read()

            # Replace the DAY value in the template with the current day_number
            file_contents = file_contents.replace("load_input(1, InputType.MAIN)", f"load_input({day}, InputType.MAIN)")

            # Write the updated contents back to the file
            with open(file_path, "w") as file:
                file.write(file_contents)
                
    except Exception as e:
        print(f"Error copying or modifying files: {e}")
        
    file = open(f"{folder_name}/example.txt", "w")
    file.close()

def download_input(day: int, year: int = 2024):
    session = requests.session()
    session_cookie = os.getenv('AOC_SESSION')
    
    if session_cookie == None:
        print('AOC_SESSION not set. Please create a .env file and set AOC_SESSION.')
        return
    
    session.cookies.set('session', os.getenv('AOC_SESSION'))
    response = session.get(f'https://adventofcode.com/{year}/day/{day}/input')
    
    if response.status_code != 200:
        print(f"Failed to retrieve the page. Status code: {response.status_code}. Content: {response.content}")
        return
    
    folder = create_day_folder(day)
    file = open(f"{folder}/input.txt", "w")
    file.write(response.text)
    file.close()
    
    print(f'Input file for Advent of Code Year {year} Day {day} downloaded successfully!')

if __name__ == '__main__':
    load_dotenv()
    args = load_arg_parser()
    
    if not args.input_only:
        create_day_project(args.day)
    if not args.init_only:
        download_input(args.day, args.year)

