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

    frame1 = tk.Frame(window, height=240, width=500)

    label1 = tk.Label(frame1, text="Country Name:")
    entry1 = tk.Entry(frame1, textvariable=data.var1)
    label2 = tk.Label(frame1, text="Country Code:")
    entry2 = tk.Entry(frame1, textvariable=data.var2)
    label3 = tk.Label(frame1, text="Continent:")
    entry3 = tk.Entry(frame1, textvariable=data.var3)
    label4 = tk.Label(frame1, text="Airport:")
    entry4 = tk.Entry(frame1, textvariable=data.var4)
    label5 = tk.Label(frame1, text="Region Name:")
    entry5 = tk.Entry(frame1, textvariable=data.var5)
    
    def search():
        for child in table.get_children():
            if table.item(child)["values"][1] == data.var1.get():
                table.focus(child)
                table.see(child)
                table.selection_set(child)
                print(table.index(child)+1)
                print(data.var1.get() in table.item(child)["values"])
                break
            
        

    button1 = tk.Button(frame1, text="Add", width=5, command=data.insert_data)
    button2 = tk.Button(frame1, text="Update", width=5, command=data.update_data)
    button3 = tk.Button(frame1, text="Delete", width=5, command=data.del_data)
    button4 = tk.Button(frame1, text="Search", width=5, command=search)

    cols = ('ID', 'Country Name', 'Code', 'Continent', 'Airport Name', 'Region Name')
    table = ttk.Treeview(window, columns=cols, show='headings')
    table.column("ID", width=50)
    table.column("Code", width=50)
    table.column("Continent", width=100)
    for col in cols:
        table.heading(col, text=col)

    def selectItem(a):
        curItem = table.focus()
        data.var1.set(table.item(curItem)["values"][1])
        data.var2.set(table.item(curItem)["values"][2])
        data.var3.set(table.item(curItem)["values"][3])
        data.var4.set(table.item(curItem)["values"][4])
        data.var5.set(table.item(curItem)["values"][5])
    table.bind('<Double-Button-1>', selectItem)

    rows = data.get_data()
    for i, (country, code, continent, airport, region) in enumerate(rows, start=1):
        table.insert("", "end", values=(i, country, code, continent, airport, region))


    label1.place(x=40, y=20), entry1.place(x=150, y=20)
    label2.place(x=40, y=60), entry2.place(x=150, y=60)
    label3.place(x=40, y=100), entry3.place(x=150, y=100)
    label4.place(x=40, y=140), entry4.place(x=150, y=140)
    label5.place(x=40, y=180), entry5.place(x=150, y=180)
    button1.place(x=400, y=40), button2.place(x=400, y=80)
    button3.place(x=400, y=120), button4.place(x=400, y=160)
    frame1.pack()
    table.pack()
    window.mainloop()

if __name__ == "__main__":
    views()