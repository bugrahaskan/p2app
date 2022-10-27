import sqlite3
import os
from pathlib import Path
from tkinter import messagebox
import tkinter as tk

class Data(tk.Tk):
    def __init__(self):
        self.path = Path(Path(os.path.abspath(__file__)).parent,"airport.db")
        self.database = sqlite3.connect(self.path)
        self.var = [tk.StringVar() for i in range(5)]

    def get_data(self):
        self.database = sqlite3.connect(self.path)
        _db = self.database.cursor()
        try:
            _db.execute("SELECT country.name, country.country_code, continent.name, airport.name, region.name \
                    FROM airport \
                    INNER JOIN country ON airport.country_id = country.country_id \
                    INNER JOIN region ON airport.region_id = region.region_id \
                    INNER JOIN continent ON airport.continent_id = continent.continent_id \
                    ORDER BY country.name")
            rows = _db.fetchall()
        except Exception as e:
            print(e)
        finally:
            self.database.close()

        return rows

    def del_data(self):
        self.database = sqlite3.connect(self.path)
        message='Following Record Deleted Succesfully: \
                {}, {}, {}'.format(self.var[0].get(),
                                    self.var[1].get(),
                                    self.var[2].get())
        try:
            # SQL Query
            messagebox.showinfo("title", message)
        except Exception as e:
            print(e)
        finally:
            for i in range(5):
                self.var[i].set("")
            self.database.close()
        
    def update_data(self):
        self.database = sqlite3.connect(self.path)
        message='Following Record Updated Succesfully: \
                {}, {}, {}'.format(self.var[0].get(),
                                    self.var[1].get(),
                                    self.var[2].get())
        try:
            # SQL Query
            messagebox.showinfo("title", message)
        except Exception as e:
            print(e)
        finally:
            for i in range(5):
                self.var[i].set("")
            self.database.close()

    def insert_data(self):
        self.database = sqlite3.connect(self.path)
        message='Following Record Added Succesfully: \
                {}, {}, {}'.format(self.var[0].get(),
                                    self.var[1].get(),
                                    self.var[2].get())
        _db = self.database.cursor()
        try:
            # SQL Query
            messagebox.showinfo("title", message)
        except Exception as e:
            print(e)
        finally:
            for i in range(5):
                self.var[i].set("")
            self.database.close()

    def search_data(self, query):
        self.database = sqlite3.connect(self.path)
        _db = self.database.cursor()
        try:
            # SQL Query
            _db.execute(query)
            rows = _db.fetchall()
        except Exception as e:
            messagebox.showerror("title", "Search Query failed")
        finally:
            self.database.close()
        
        return rows