import tkinter as tk
from tkinter import ttk
import engine
from engine import Data
from tkinter import messagebox

def views():
    window = tk.Tk()
    window.geometry("832x624")
    window.title("Project")

    data = Data()

    frame1 = tk.Frame(window, height=200, width=500)

    label1 = tk.Label(frame1, text="Country Name:")
    entry1 = tk.Entry(frame1, textvariable=data.var1)
    label2 = tk.Label(frame1, text="Country Code:")
    entry2 = tk.Entry(frame1, textvariable=data.var2)
    label3 = tk.Label(frame1, text="Region Name:")
    entry3 = tk.Entry(frame1, textvariable=data.var3)
    label4 = tk.Label(frame1, text="Region Keyword:")
    entry4 = tk.Entry(frame1, textvariable=data.var4)

    button1 = tk.Button(frame1, text="Add", width=5, command=window.destroy)
    button2 = tk.Button(frame1, text="Update", width=5, command=window.destroy)
    button3 = tk.Button(frame1, text="Delete", width=5, command=window.destroy)

    cols = ('Country Name', 'Country Code', 'Region Name', 'Region Keyword')
    table = ttk.Treeview(window, columns=cols, show='headings')
    for col in cols:
        table.heading(col, text=col)

    def selectItem(a):
        curItem = table.focus()
        data.var1.set(table.item(curItem)["values"][0])
        data.var2.set(table.item(curItem)["values"][1])
        data.var3.set(table.item(curItem)["values"][2])
        data.var4.set(table.item(curItem)["values"][3])
    table.bind('<Double-Button-1>', selectItem)

    rows = data.get_data()
    for i, (country, code, region, keyword) in enumerate(rows, start=1):
        table.insert("", "end", values=(country, code, region, keyword))
    
    

    label1.place(x=40, y=20), entry1.place(x=150, y=20)
    label2.place(x=40, y=60), entry2.place(x=150, y=60)
    label3.place(x=40, y=100), entry3.place(x=150, y=100)
    label4.place(x=40, y=140), entry4.place(x=150, y=140)
    button1.place(x=400, y=40), button2.place(x=400, y=80), button3.place(x=400, y=120)
    frame1.pack()
    table.pack()
    window.mainloop()

if __name__ == "__main__":
    views()