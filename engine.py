import sqlite3
from pathlib import Path
from tkinter import messagebox
import views

# Set the Path up
path = Path(Path.cwd(),"UPWORK","p2app","airport.db")

def get_data():
    # Connect to database
    database = sqlite3.connect(path)
    db = database.cursor()
    db.execute("SELECT country.name, country.country_code, region.name, \
                region.keywords FROM country INNER JOIN region \
                ON country.country_id = region.country_id")
    rows = db.fetchall()
    db.close()

    return rows

def del_data():
    pass

def update_data():
    pass




if __name__ == "__main__":
    get_data()
