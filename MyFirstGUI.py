#Gavril Marian
from tkinter import *

class MyFirstGUI:
    
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")
        
        self.label1 = Label(master, text="Enter your Firstname")
        self.label1.pack()
        self.entry1 = Entry()
        self.entry1.pack()

        self.label2 = Label(master, text="Enter your Surname")
        self.label2.pack()
        self.entry2 = Entry()
        self.entry2.pack()
        
        self.label3 = Label(master, text="Enter your Date of Birth")
        self.label3.pack()
        self.entry3 = Entry()
        self.entry3.pack()

        self.label4 = Label(master, text="Enter your Member Type")
        self.label4.pack()
        self.entry4 = Entry()
        self.entry4.pack()
        self.insertButton = Button(master, text="Insert Into DB", command=self.insert_into_db)
        self.insertButton.pack()

        self.printButton = Button(master, text="Print All Members", command=self.print_all)
        self.printButton.pack()

        self.closeButton = Button(master, text="Close", command=self.close)
        self.closeButton.pack()

    def insert_into_db(self):
        firstname = self.entry1.get()
        surname = self.entry2.get()
        dob = self.entry3.get()
        member_type = self.entry4.get()

   
        sql_command = f"INSERT INTO member(firstname, surname, dateofbirth, membertype) VALUES ('{firstname}', '{surname}', '{dob}', '{member_type}')"
       
     
        print(f"SQL Command: {sql_command}")
       
       
        try:
           
            connect = sqlite3.connect('tennisclub.db')
            cursor = conn.cursor()
           
         
            cursor.execute(sql_command)
           
           
            connect.commit()
           
         
            connect.close()
           
            print("Data inserted successfully")
       
        except Exception as e:
            print(f"An error occurred: {e}")
    def print_all(self):
        print()
    def close(self):
        root.destroy()
        
         
       



       
 
root = Tk()
my_gui = MyFirstGUI(root)
root.dooneevent()
