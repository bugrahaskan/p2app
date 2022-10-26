import sqlite3
from pathlib import Path
from tkinter import messagebox
import views
import tkinter as tk

class Data(tk.Tk):
    def __init__(self):
        self.path = Path(Path.cwd(),"UPWORK","p2app","p2app","airport.db")
        self.database = sqlite3.connect(self.path)
        self.var1 = tk.StringVar()
        self.var2 = tk.StringVar()
        self.var3 = tk.StringVar()
        self.var4 = tk.StringVar()

    def get_data(self):
        _db = self.database.cursor()
        _db.execute("SELECT country.name, country.country_code, region.name, \
                    region.keywords FROM country INNER JOIN region \
                    ON country.country_id = region.country_id \
                    ORDER BY country.name")
        rows = _db.fetchall()
        #_db.close()
        self.database.close()

        return rows

    def del_data(self):
        pass

    def update_data(self):
        pass


# if __name__ == "__main__":
#     data = Data()
#     data.get_data()
