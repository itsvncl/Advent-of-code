import requests
import argparse
import shutil
import os
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
from dotenv import load_dotenv

def load_arg_parser() -> dict:
    parser = argparse.ArgumentParser(description="Advent of Code command-line application.")

    parser.add_argument('-day', type=int, required=True, help="The day of the Advent of Code challenge.")
    parser.add_argument('-year', type=int, required=False, help="The year of the Advent of Code challenge.", default=2024)
        
    parser.add_argument('--input-only', action='store_true', help="Only download the input for the challenge.")
    parser.add_argument('--init-only', action='store_true', help="Only initialize the files and structure for the challenge.")
    parser.add_argument('--with-puzzle', action='store_true', help="Downloads the html of the puzzle.")
    parser.add_argument('--update-puzzle', action='store_true', help="Downloads the the html of the puzzle.")

    args = parser.parse_args()
        
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
    file_path = f"{folder_name}/p1.py"
    if os.path.exists(f"{folder_name}/p1.py"):
        print(f"The file {file_path} already exists. Skipping file creation.")
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

def aoc_request(url: str) -> requests.Response:
    session = requests.session()
    session_cookie = os.getenv('AOC_SESSION')
    
    if session_cookie == None:
        print('AOC_SESSION not set. Please create a .env file and set AOC_SESSION.')
        return None
    
    session.cookies.set('session', os.getenv('AOC_SESSION'))
    return session.get(url)

def download_input(day: int, year: int = 2024):
    response = aoc_request(f'https://adventofcode.com/{year}/day/{day}/input')
    
    if response.status_code != 200:
        print(f"Failed to retrieve the page. Status code: {response.status_code}. Content: {response.content}")
        return
    
    folder = create_day_folder(day)
    file = open(f"{folder}/input.txt", "w")
    file.write(response.text)
    file.close()
    
    print(f'Input file for Advent of Code Year {year} Day {day} downloaded successfully!')
    
# Function to download a file from a URL
def download_file(url, folder):
    local_filename = os.path.join(folder, os.path.basename(urlparse(url).path))
    try:
        with requests.get(url) as r:
            r.raise_for_status()  # Check if the request was successful
            with open(local_filename, "wb") as f:
                f.write(r.content)
            print(f"Downloaded: {url}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to download {url}: {e}")
    return local_filename

# Function to download all external resources (CSS, JS, images)
def download_resources(url, folder="downloaded_files"):
    if os.path.exists(folder):
        shutil.rmtree(folder)  # Remove the entire folder and its contents
    
    os.makedirs(folder, exist_ok=True)
    
    # Download the main HTML file
    response = aoc_request(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Find all resources: CSS, JavaScript, images, etc.
    resources = []
    # CSS links
    for link in soup.find_all("link", rel="stylesheet"):
        href = link.get("href")
        if href:
            resources.append(urljoin(url, href))
    
    # JS scripts
    for script in soup.find_all("script", src=True):
        src = script.get("src")
        if src:
            resources.append(urljoin(url, src))
    
    # Images
    for img in soup.find_all("img", src=True):
        src = img.get("src")
        if src:
            resources.append(urljoin(url, src))
    
    # Download all the resources
    downloaded_files = []
    for resource in resources:
        downloaded_files.append(download_file(resource, folder))
    
    # Update the HTML with local paths for the downloaded resources
    for tag in soup.find_all(["link", "script", "img"]):
        if tag.get("href"):
            tag["href"] = os.path.basename(urljoin(url, tag["href"]))
        elif tag.get("src"):
            tag["src"] = os.path.basename(urljoin(url, tag["src"]))
    
    # Save the modified HTML to a file
    with open(os.path.join(folder, "index.html"), "w", encoding="utf-8") as f:
        f.write(str(soup))
    
    print("All resources downloaded and HTML updated.")

if __name__ == '__main__':
    load_dotenv()
    args = load_arg_parser()
    
    if not args.input_only and not args.update_puzzle:
        create_day_project(args.day)
    if not args.init_only and not  args.update_puzzle:
        download_input(args.day, args.year)
    if args.with_puzzle or args.update_puzzle:
        download_resources(f'https://adventofcode.com/{args.year}/day/{args.day}', f"Day{args.day:02}/puzzle")
    
    print(f'Advent of Code Year {args.year} Day {args.day} ran successfully!')

