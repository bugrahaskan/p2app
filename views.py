import tkinter as tk
from tkinter import SINGLE, ttk
import engine
from engine import Data
from tkinter import messagebox

def views():
    window = tk.Tk()
    window.geometry("832x624")
    window.title("Project")

    data = Data()

    frame1 = tk.Frame(window, height=240, width=550)

    label1 = tk.Label(frame1, text="Country Name:")
    entry1 = tk.Entry(frame1, textvariable=data.var[0])
    label2 = tk.Label(frame1, text="Country Code:")
    entry2 = tk.Entry(frame1, textvariable=data.var[1])
    label3 = tk.Label(frame1, text="Continent:")
    entry3 = tk.Entry(frame1, textvariable=data.var[2])
    label4 = tk.Label(frame1, text="Airport:")
    entry4 = tk.Entry(frame1, textvariable=data.var[3])
    label5 = tk.Label(frame1, text="Region Name:")
    entry5 = tk.Entry(frame1, textvariable=data.var[4])
    
    def search():
        for child in table.get_children():
            if table.item(child)["values"][1] == data.var[0].get():
                messagebox.showinfo("title", "Found the record")
                table.focus(child)
                table.see(child)
                table.selection_set(child)
                print(table.index(child)+1)
                print(data.var[0].get() in table.item(child)["values"])
                break
    
    def advanced_search():
        top = tk.Toplevel(window)
        top.geometry("840x512")

        top_data = Data()

        top_list_label = tk.Label(top, text="Choose criteria:")

        top_list = tk.Listbox(top, selectmode=SINGLE)
        top_list.insert(1, "Country Name")
        top_list.insert(2, "Country Code")
        top_list.insert(3, "Continent")
        top_list.insert(4, "Airport")
        top_list.insert(5, "Region")

        top_label = tk.Label(top, text="Selected:")
        top_entry = tk.Entry(top, textvariable=top_data.var[0])

        def top_search():
            children = top_table.get_children()
            if children:
                for child in children:
                    top_table.delete(child)

            if top_list.curselection()[0] == 0:
                sub_query = "country.name"
            elif top_list.curselection()[0] == 1:
                sub_query = "country.country_code"
            elif top_list.curselection()[0] == 2:
                sub_query = "continent.name"
            elif top_list.curselection()[0] == 3:
                sub_query = "airport.name"
            elif top_list.curselection()[0] == 4:
                sub_query = "region_name"

            query = 'SELECT country.name, country.country_code, continent.name, airport.name, region.name \
                    FROM airport \
                    INNER JOIN country ON airport.country_id = country.country_id \
                    INNER JOIN region ON airport.region_id = region.region_id \
                    INNER JOIN continent ON airport.continent_id = continent.continent_id \
                    WHERE {} = "{}" \
                    ORDER BY country.name'.format(sub_query, top_data.var[0].get())
                    
            top_rows = top_data.search_data(query) # query
            for i, (country, code, continent, airport, region) in enumerate(top_rows, start=1):
                top_table.insert("", "end", values=(i, country, code, continent, airport, region))

        top_button = tk.Button(top, text="Search", command=top_search)

        cols = ('ID', 'Country Name', 'Code', 'Continent', 'Airport Name', 'Region Name')
        top_table = ttk.Treeview(top, columns=cols, show='headings')
        top_table.column("ID", width=50)
        top_table.column("Code", width=50)
        top_table.column("Continent", width=100)
        for col in cols:
            top_table.heading(col, text=col)

        top_list_label.place(x=30, y=10), top_list.place(x=30, y=30)
        top_label.place(x=250, y=30), top_entry.place(x=250, y=70)
        top_button.place(x=250, y=110)
        top_table.place(x=10, y=250)
        top.mainloop()
    
    button1 = tk.Button(frame1, text="Add", width=5, command=data.insert_data)
    button2 = tk.Button(frame1, text="Update", width=5, command=data.update_data)
    button3 = tk.Button(frame1, text="Delete", width=5, command=data.del_data)
    button4 = tk.Button(frame1, text="Search", width=5, command=search)
    button5 = tk.Button(frame1, text="Advanced Search", command=advanced_search)

    cols = ('ID', 'Country Name', 'Code', 'Continent', 'Airport Name', 'Region Name')
    table = ttk.Treeview(window, columns=cols, show='headings', height=19)
    table.column("ID", width=50)
    table.column("Code", width=50)
    table.column("Continent", width=100)
    for col in cols:
        table.heading(col, text=col)

    def selectItem(a):
        curItem = table.focus()
        data.var[0].set(table.item(curItem)["values"][1])
        data.var[1].set(table.item(curItem)["values"][2])
        data.var[2].set(table.item(curItem)["values"][3])
        data.var[3].set(table.item(curItem)["values"][4])
        data.var[4].set(table.item(curItem)["values"][5])
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
    button5.place(x=400, y=200)
    frame1.pack()
    table.pack()
    window.mainloop()

if __name__ == "__main__":
    views()