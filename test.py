import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import filedialog

# Create a tkinter GUI to ask the user for the website URL
root = tk.Tk()
root.withdraw()
url = filedialog.askstring(title="Enter Website URL", prompt="Enter the URL of the website to scrape:")

# Send a GET request to the URL and get the HTML content
response = requests.get(url)
html_content = response.content

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find the elements on the page that you want to scrape
# For example, let's say you want to scrape all of the links on the page
links = soup.find_all('a')

# Create a tkinter GUI to ask the user for the output file name and location
root = tk.Tk()
root.withdraw()
file_path = filedialog.asksaveasfilename(defaultextension=".txt", title="Save As", filetypes=(("Text Files", "*.txt"),))

# Write the scraped data to the output file
with open(file_path, 'w') as f:
    for link in links:
        f.write(link.get('href') + '\n')
