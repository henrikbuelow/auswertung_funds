from Anzeigen import showData
from tkinter import*
import pandas as pd
#from auswertung import *

def showData ():

    data = pd.read_csv("Funds_sheet_Data.csv")
    return data

def search_countries(country):
    results = []
    data = showData()
    for index in range(0, len(data['HQ'])):
        if country in data['HQ'][index]:
            titles = ["Name", "website", "Est. Date", "HQ", "Funds(total)", "Last Funding Type", "CB Rank",
                      "#employees"]
            row = ''
            for title in titles:
                if title == '#employees':
                    row = str(row) + str(data[title][index])
                else:
                    row = str(row) + str(data[title][index]) + "   -   "
            results.append(row)
    return results

def sort_by_funds():
    """
    Returns a list of all companies sorted descending by funds
    :return: list of all companies sorted descending by funds
    """
    data = showData()
    data = data.sort_values(by='Funds(total)', ascending=False)
    #data = data.reset_index(drop=True)
    results = []
    for index in range(0, len(data['Funds(total)'])):
        titles = ["Name", "website", "Est. Date", "HQ", "Funds(total)", "Last Funding Type", "CB Rank",
                  "#employees"]
        row = ''
        for title in titles:
            if title == '#employees':
                row = str(row) + str(data[title][index])
            else:
                row = str(row) + str(data[title][index]) + "   -   "
        results.append(row)
    return results


def sort_by_name():
    """
    Returns a list of all companies sorted by name
    :return: list of all companies sorted by name
    """
    data = showData()
    data_sorted = data.sort_values(by='Name')
    data_sorted = data_sorted.reset_index(drop=True)
    ergebnis = []
    for index in range(0, len(data_sorted['Name'])):
        titles = ["Name", "website", "Est. Date", "HQ", "Funds(total)", "Last Funding Type", "CB Rank",
                  "#employees"]
        row = ''
        for title in titles:
            if title == '#employees':
                row = str(row) + str(data_sorted[title][index])
            else:
                row = str(row) + str(data_sorted[title][index]) + "   -   "
        ergebnis.append(row)
    return ergebnis

#sorts out all HQ countries
class countryButton(Button):

    def action1(self):

        print("country Button")

        newList = search_countries(eingabe2.get())

        print(newList)

        liste.delete(0,"end")
        for iteam in newList:
            liste.insert(END, "")
            liste.insert(END, iteam)

#sorts out all HQ countries
class nameButton(Button):

    def action1(self):

        print("name Button")

        newList = sort_by_name()

        print(newList)

        liste.delete(0,"end")
        for iteam in newList:
            liste.insert(END, "")
            liste.insert(END, iteam)

#sorts out all HQ countries
class fundButton(Button):

    def action1(self):

        print("fund Button")

        newList = sort_by_funds()

        print(newList)

        liste.delete(0,"end")
        for iteam in newList:
            liste.insert(END, "")
            liste.insert(END, iteam)

fenster = Tk()

"""Sortiment soll hier angezeigt werden"""

fenster.geometry("1100x800")
fenster.title("Employee Survey Tool")
rahmen = Frame(fenster, relief="flat", borderwidth=5)
# rahmen.config(font=("g))
rahmen.pack(fill="both", expand=1)
label = Label(rahmen,text="Survey Tools")
label.config(font=("Arial", 14, "bold"))
label.place(x=500, y=5)

rahmen2 = Frame(rahmen,relief="ridge",borderwidth=1)
rahmen2.pack(pady=50, padx= 30)

f = showData()
print(f["Name"][0])
inhalt = f
#inhalt = f.readlines()

scrollbar = Scrollbar(rahmen2)
liste = Listbox(rahmen2,xscrollcommand=scrollbar.set,yscrollcommand=scrollbar.set,width=500, height=20)



i = 0

titles = ["Name", "website", "Est. Date", "HQ", "Funds(total)", "Last Funding Type", "CB Rank", "#employees"]
row = ""
#inserting the starting data
for index in range(len(f["Name"])):
    for title in titles:
        if title == "#employees":
            row = str(row) + str(f[title][index]) + "\n"
            liste.insert(END,"")
            liste.insert(END, row)
            row = ""
        else:
            row = str(row) + str(f[title][index]) + "   -   "
    print(row)


#f.close()

scrollbar.config(command=liste.yview)
liste.pack(side="left",fill="both")
scrollbar.pack(side="left",fill="y")

sortName = nameButton(rahmen, text="all Entries", width=30, height=2)
sortName["command"] = sortName.action1
sortName.place(x=350,y=450)

sortFunding = fundButton(rahmen, text="sort by $ funding", width=30, height=2)
sortFunding["command"] = sortFunding.action1
sortFunding.place(x=350,y=550)

label2 = Label(rahmen,text="Search Country: ")
eingabe2 = Entry(rahmen, bd=2,width=20)
label2.place(x=20,y=650)
eingabe2.place(x=150,y=650)

searchCountry = countryButton(rahmen, text="search", width=30, height=2)
searchCountry["command"] = searchCountry.action1
searchCountry.place(x=350,y=650)

beenden = Button(rahmen, text="Quit", width=10, height=5,command=fenster.destroy)
# autoh["command"] = autoh.aktion1
beenden.place(x=900,y=650)

fenster.mainloop()

#fenster = Tk()

"""Start des Programms. Es werden 4 Optionen: Sortiment Anzeigen, Auto Hinzufügen, Löschen und Preis ändern angeboten."""
"""
fenster.geometry("600x600")
fenster.title("Employee Survey Tools")
rahmen = Frame(fenster, relief="flat",borderwidth=5)"""
"""Button um Sortiment ausgeben zu lassen"""
"""
sortAnz = Anzeigen(rahmen, text="Sortiment Anzeigen", width=20, height=10)
sortAnz["command"] = sortAnz.aktion1
sortAnz.place(x=50,y=120) #warum öffnet sich beim Schließen ein 2. Fenster und warum ist mainloop nicht erforderlich ??

fenster.mainloop()
"""

