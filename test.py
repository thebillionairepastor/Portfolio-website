import requests
from bs4 import BeautifulSoup
import tkinter as tk

# Create the GUI
root = tk.Tk()
root.geometry("400x200")

# Create a function that retrieves data from a website
def scrape_website():
    # Get the URL from the user
    url = url_entry.get()

    # Use requests to get the HTML content of the page
    response = requests.get(url)
    content = response.content

    # Use BeautifulSoup to parse the HTML content
    soup = BeautifulSoup(content, "html.parser")

    # Get the desired data from the page
    data = soup.find("div", class_="my-data-class").text

    # Display the data in the GUI
    result_label.config(text=data)

# Add a label for the URL entry field
url_label = tk.Label(root, text="Enter the URL:")
url_label.pack()

# Add an entry field for the URL
url_entry = tk.Entry(root)
url_entry.pack()

# Add a button to start the scraping process
scrape_button = tk.Button(root, text="Scrape Website", command=scrape_website)
scrape_button.pack()

# Add a label to display the result
result_label = tk.Label(root)
result_label.pack()

# Start the GUI
root.mainloop()
