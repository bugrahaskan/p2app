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
        self.var5 = tk.StringVar()

    # @staticmethod
    # def connection_decorator(func):
    #     def connection(self):
    #         self.database = sqlite3.connect(self.path)
    #         func()
    #         self.database.close()
    #     return connection

    # @connection_decorator
    def get_data(self):
        self.database = sqlite3.connect(self.path)
        _db = self.database.cursor()
        _db.execute("SELECT country.name, country.country_code, continent.name, airport.name, region.name \
                    FROM airport \
                    INNER JOIN country ON airport.country_id = country.country_id \
                    INNER JOIN region ON airport.region_id = region.region_id \
                    INNER JOIN continent ON airport.continent_id = continent.continent_id \
                    ORDER BY country.name")
        rows = _db.fetchall()
        self.database.close()

        return rows

    def del_data(self):
        self.database = sqlite3.connect(self.path)
        message='Following Record Deleted Succesfully: \
                {}, {}, {}'.format(self.var1.get(),
                                    self.var2.get(),
                                    self.var3.get())
        try:
            # SQL Query
            messagebox.showinfo("title", message)
        except Exception as e:
            print(e)
        finally:
            self.var1.set("")
            self.var2.set("")
            self.var3.set("")
            self.var4.set("")
            self.var5.set("")
            self.database.close()
        
    def update_data(self):
        self.database = sqlite3.connect(self.path)
        message='Following Record Updated Succesfully: \
                {}, {}, {}'.format(self.var1.get(),
                                    self.var2.get(),
                                    self.var3.get())
        try:
            # SQL Query
            messagebox.showinfo("title", message)
        except Exception as e:
            print(e)
        finally:
            self.var1.set("")
            self.var2.set("")
            self.var3.set("")
            self.var4.set("")
            self.var5.set("")
            self.database.close()

    def insert_data(self):
        self.database = sqlite3.connect(self.path)
        message='Following Record Added Succesfully: \
                {}, {}, {}'.format(self.var1.get(),
                                    self.var2.get(),
                                    self.var3.get())
        try:
            # SQL Query
            messagebox.showinfo("title", message)
        except Exception as e:
            print(e)
        finally:
            self.var1.set("")
            self.var2.set("")
            self.var3.set("")
            self.var4.set("")
            self.var5.set("")
            self.database.close()

    def search_data(self):
        self.database = sqlite3.connect(self.path)
        try:
            # SQL Query
            messagebox.showinfo("title", "Search Query")
        except Exception as e:
            print(e)
        finally:
            self.database.close()