from tkinter import *
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup

class ScraperApplicaiton:
    def __init__(self):
        self.root = Tk()
        self.setup_interface()
        self.parsed_html = None

    def setup_interface(self):
        Label(self.root, text='URL To Load').pack()
        self.url_entry = Entry(self.root)
        self.url_entry.pack()
        Button(self.root, text='Load HTML', command=self.load_html).pack()

    def load_html(self):
        url = self.url_entry.get()
        try:
            response = requests.get(url)
            self.parsed_html = BeautifulSoup(response.content, 'html.parser')
            a_tags = self.parsed_html.select('a[href]')
            for tag in a_tags:
                print(tag.get_text())
        except Exception as e:
            messagebox.showerror('Error', f'An error occured: {e}')

    def run(self):
        self.root.mainloop()

if __name__ == '__main__':
    app = ScraperApplicaiton()
    app.run()