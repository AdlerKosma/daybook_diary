from tkinter import *

#class that defines entries in diary
class DiaryEntry:
    def __init__(self, date, city, text):
        """Constructor. Creates new diary entry.
        Inparametrar: self, date, text, city
        Returnerar: inget"""
        self.date = date #string
        self.city = city #string
        self.text = text #string

    def __repr__(self):
        """ Returns string with date and city
        Inparametrar: self
        Returnerar: sträng"""
        return "\nDate: " + str(self.date) + "\nCity: " + str(self.city) + "\nText: " + str(self.text)
    
    def __lt__(self, other):
        """Sorts diary in order of date
        Inparametrar: self, other
        Returnerar: True if self.date < other.date, otherwise False"""
        if (self.date < other.date):
         return True
        else:
          return False
        
    
class DiaryWrite: #main controller class
    def __init__(self, catalogue):
        """Creates catalogue of entries.
        Input: entries (list)
        Returns: nothing"""
        self.entries = catalogue
        self.GUI = GuiMaker(self)
        self.GUI.mainloop()
        
    def new_entry(self, date, city, text):
        """Creates DiaryEntry object, an object of a diary entry"""
        entry = DiaryEntry(date, city, text)
        self.entries.append(entry)
    
    def find_date(self, date):
        """Finds entry with help from date"""
        from datetime import datetime
        date_list = []
        for entry in self.entries:
            if entry.date == date:
                date_list.append(entry)
        self.print_show_all(date_list, date)

    def find_city(self, city):
        """Finds entry with help from city"""
        city_list = []
        if len(city) > 1:
            for entry in self.entries:
                if entry.city == city.lower():
                    city_list.append(entry)
        self.print_show_all(city_list, city) 

    def find_word(self, word):
        """Finds entry containg chosen word"""
        import re
        word_list = []
        if len(word) > 1:
            for entry in self.entries:
                if str(' '+word.lower()+' ') in entry.text.lower():
                    word_list.append(entry)
        self.print_show_all(word_list, word)

    def show_all_dates(self):
        """makes a list of all dates to print"""
        string = 'All Dates'
        date_list = []
        for entry in self.entries:
            if entry.date not in date_list:
                date_list.append(entry.date)
        date_list.sort()        
        #date_list = date_list.sort()
        self.print_show_all(date_list, string)

    def show_all_cities(self):
        """Makes a list of all cities to print"""
        string = 'All Cities'
        city_list = []
        for entry in self.entries:
            if entry.city.capitalize() not in city_list:
                city_list.append(entry.city.capitalize())
        self.print_show_all(city_list, string)

    def random_word(self):
        """Picks a random word from all text entries"""
        import random
        string = 'Random Word'
        entry_list=[]
        for entry in self.entries:
            entry_list.append(entry.text)
        try:
            entry_string = str(entry_list)
            entry_string = entry_string.split()
            word = random.choice(entry_string)
        except IndexError:
            word = ' '
        self.print_entry(word, string)

    def random_sentence(self):
        """"""
        import random
        import re
        string = 'Random sentance'
        entry_string = ''
        for entry in self.entries:
            entry_string += str(entry.text)
        sentence=re.split('\.|\,', entry_string)
        sentence = random.choice(sentence)
        self.print_entry(sentence, string)

    def random_entry(self):
        """"""
        import random
        entry_list = []
        string = 'Random Entry'
        for entry in self.entries:
            entry_list.append(entry)
        entry = random.choice(entry_list)
        self.print_entry(entry, string)
        
        
    def print_show_all(self, list_of_all, search):
        """Creates a structure of what to print for the GUI to configure"""
        import re
        to_print = "Search results for: " + search + " (" + str(len(list_of_all)) + " etries)" + "\n"
        to_print += "__________________________\n"
        list_of_all.sort()
        if len(list_of_all) >= 1:
            for entry in list_of_all:
                to_print += str(entry) + "\n"
        else:
            to_print += "nah nothing could be found"
        to_print = to_print.replace(search, '>'+ search.upper() + '<')
        self.GUI.print_entry(to_print)

    
    def print_entry(self, entry, search):
        """"""
        to_print = "Search results for: " + search + "\n"
        to_print += "__________________________\n"
        try:
            to_print += "\n" + entry.date + " | " +  entry.city + " | " + entry.text + "\n"
        except AttributeError:
            to_print += '\n' + entry
        self.GUI.print_entry(to_print)

class GuiMaker(Tk):
    def __init__(self, diaryWrite):
        """"""
        super().__init__()
        self.diary_app = diaryWrite

        self.declareGUI()
        self.activateGUI()

    def declareGUI(self):
        """
        Metoden skapar variabler för gränssnittet
        
        Indata: self (objekt)
        Returvärde: inget
        """
        import datetime
        self.title("Daybook Diary")
        
        self.add_entry = Label(text= 'Add entry here:', fg = 'red')
        self.now_label = Label(text = 'Now:', fg = 'blue') #command=self.diary_app.add_date)
        self.add_date = Label(text = 'Date:', fg ='blue')
        self.write_date = Entry()
        self.diary_textbox = Text(bg='grey',exportselection=0)
        self.city_textbox = Entry()
        self.city_label = Label(text='City:', fg= 'blue')
        self.text_label = Label(text='Text:', fg= 'blue')
        self.date_printed = Label(text=f"{datetime.datetime.now():%Y-%m-%d}")
        self.save_button = Button(text='Save', command=lambda:[self.diary_app.new_entry(self.decide_date(), self.city_textbox.get(), self.diary_textbox.get("1.0",END)),self.clear_field(self.write_date), self.clear_field(self.city_textbox)])

        self.ask_date = Entry()
        self.ask_city = Entry()
        self.ask_word = Entry()
        self.menuQ = Label(text= 'So what you wanna do?', fg = 'red')
        self.menu_button1 = Button(text='Find date', command=lambda: [self.diary_app.find_date(self.ask_date.get()), self.clear_field(self.ask_date)])
        self.menu_button2 = Button(text='Find city', command=lambda: [self.diary_app.find_city(self.ask_city.get()), self.clear_field(self.ask_city)])
        self.menu_button3 = Button(text='Find word', command=lambda: [self.diary_app.find_word(self.ask_word.get()), self.clear_field(self.ask_word)])
        self.menu_button4 = Button(text='Avsluta', command=lambda:avsluta(self))
        self.menu_button5 = Button(text='Show all dates', command=lambda: self.diary_app.show_all_dates())
        self.menu_button6 = Button(text='Show all cities', command=lambda: self.diary_app.show_all_cities())
        self.menu_button7 = Button(text='Random Word', command=lambda: self.diary_app.random_word())
        self.menu_button8 = Button(text='Random Sentence', command=lambda: self.diary_app.random_sentence())
        self.menu_button9 = Button(text='Random Entry', command=lambda: self.diary_app.random_entry())

        self.entry_printed = Label(text='', wraplength=600, anchor=SW)


    def activateGUI(self):
        """
        Metoden lägger till objektets GUI-objekt i användar-GUI:en
        
        Indata: self (objekt)
        Returvärde: inget
        """
        
        
        self.add_entry.place(x=10, y=0)
        self.now_label.place(x=10, y=30)
        self.add_date.place(x=10, y=60)
        self.write_date.place(x=55, y =60)
        self.diary_textbox.place(x = 55, y = 120, width=300, height=100)
        self.city_textbox.place(x = 55, y = 90)
        self.city_label.place(x=10, y=90)
        self.text_label.place(x=10, y=120)
        self.date_printed.place(x = 100, y = 30)
        self.menu_button4.place(x=200, y=300)
        self.save_button.place(x=100, y= 300)
        

        self.ask_date.place(x=500, y=30)
        self.ask_city.place(x=500, y=60)
        self.ask_word.place(x=500, y=90)
        self.menuQ.place(x=400, y = 0)
        self.menu_button1.place(x=400, y= 30)
        self.menu_button2.place(x=400, y= 60)
        self.menu_button3.place(x=400, y= 90)
        self.menu_button5.place(x=800, y=30)
        self.menu_button6.place(x=800, y=60)
        self.menu_button7.place(x=800, y=90)
        self.menu_button8.place(x=800, y=120)
        self.menu_button9.place(x=800, y=150)
        
        
        self.entry_printed.place(x=400, y=200 )

        self.geometry("1200x600")
        #self.configure(bg='grey')

    def decide_date(self): #FUNKAR INTE!! RETURNERAR ALLTID self.write_date
        """"""
        if self.write_date.get() == None:
            date=f"{datetime.datetime.now():%Y-%m-%d}"
        else:
            date = self.write_date.get()
        return date
            
    def print_entry(self, txt):
        """prints the entries that was serched for"""
        self.entry_printed.config(text=txt, fg = 'green')

    def clear_field(self, button):
        """clears the fields for new inputs after search has been done"""
        button.delete(first=0,last=1000)
        


#################### FUNCTIONS ####################


def read_file(filename):
    """
    returns: catalog of entries Diary-object"""
    try:
        file = open(filename, "r")
        rows = file.readlines()
        return rows
    except FileNotFoundError:
        return False
    
def convert_to_sting_from_file(rows):
    """"""
    from datetime import datetime
    entries = []
    for line in rows:
        values = line.strip().split("/")
        if len(values) >= 3:
            try:
                entry = DiaryEntry(values[0], values[1], values[2])
                values[0] = datetime.strptime(values[0], "%Y-%m-%d")
                entries.append(entry)
            except ValueError:
                print("Error in reading file!")
    return entries
    

def save_file(filename, string):
    """"""
    file = open(filename, "w")
    file.write(string)
    file.close()

def convert_to_string(list_of_entries):
    """"""
    string = ""
    for value in list_of_entries:
        string += str(value.date) + "/" + value.city.lower() + "/" + value.text.lower() + "\n\n"
    return string

def avsluta(gui):
    """"""
    gui.destroy()

def main():
    """"""
    FILE = "diary_file.txt"
    diary_data = read_file(FILE)
    entries = convert_to_sting_from_file(diary_data)
    program = DiaryWrite(entries)
    save_string = convert_to_string(program.entries)
    save_file(FILE, save_string)
   
main()



