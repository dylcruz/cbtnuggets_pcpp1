from tkinter import *
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup
import csv

class ScraperApplicaiton:
    def __init__(self):
        self.root = Tk()
        self.parsed_html = None
        self.selectors = []

        self.setup_interface()

    def setup_interface(self):
        Label(self.root, text='URL To Load').pack()
        self.url_entry = Entry(self.root)
        self.url_entry.pack()
        Button(self.root, text='Load HTML', command=self.load_html).pack()

        for i in range(3):
            frame = Frame(self.root)
            frame.pack(fill='x', expand=True)

            name_entry = Entry(frame, width=50)
            name_entry.pack(side='left', padx=5)

            selector_entry = Entry(frame, width=50)
            selector_entry.pack(side='left', padx=5)

            self.selectors.append((name_entry, selector_entry))

        Button(self.root, text='Print Sample', command=self.print_sample).pack()

        self.file_name_entry = Entry(self.root)
        self.file_name_entry.pack()
        Button(self.root, text='Write to CSV', command=self.write_to_csv).pack()

    def print_sample(self):
        headers, data = self.scrape_data()
        lines = []

        for i, header in enumerate(headers):
            lines.append(f'{header}: {data[i][0]}')

        Label(self.root, text='\n'.join(lines)).pack()

    def write_to_csv(self):
        headers, data = self.scrape_data()
        filename = self.file_name_entry.get()

        try:
            with open(filename, 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(headers)
                data_rows = list(zip(*data))
                writer.writerows(data_rows)
        except Exception as e:
            print(f'Error: {e}')

    def scrape_data(self):
        headers = []
        data = []
        
        for name_entry, selector_entry in self.selectors:
            data_name = name_entry.get()
            selector = selector_entry.get()

            headers.append(data_name)
            extracted_data = [el.get_text(strip=True) for el in self.parsed_html.select(selector)]
            data.append(extracted_data)

        return (headers, data)

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
