###################################
#          CLASS: CISP 71         #
#     AUTHOR: Jenna Armstrong     #
#   Project: Netflix Watchlist    #
###################################

#####################################################
# Import the required libraries and import database #
#####################################################
import sqlite3
from tkinter import *
from PIL import ImageTk, Image

# for message boxes
import tkinter.messagebox as mb
# for treeview
import tkinter.ttk as ttk
# for openning files
from tkinter import filedialog

#import the database created in Netflix_Watchlist_App_Create_DB python file
from Netflix_Watchlist_App_Create_DB import Database

#Create the path Variable
path="/Users/jennarhae/Documents/School_Documents/Mt SAC Classes/CISP 71/CRUD Project_Jenna Armstrong/"

#create an object of the database class
db = Database(path +"Watchlist.db")

# Create the window
root = Tk()
#change background
root.configure(bg='black')
# Add window title
root.title("Netflix Watchlist")
# set the size of the window
root.geometry("800x700")
#set window icon
root.iconbitmap(path + 'icons/Netflix.ico')


##########################
#  Define the Functions  #
##########################

#Validate the entry
def validate_entry():
    if entDate.get()=='':
        mb.showinfo('Information', 'Please enter the Date Watched.')
        entDate.focus_set()
        return False

    if entName.get()=='':
        mb.showinfo('Information', 'Please enter the Title.')
        entName.focus_set()
        return False

    if entGenre.get()=='':
        mb.showinfo('Information', 'Please enter the Genre.')
        entGenre.focus_set()
        return False
    
    if Cat_sel.get()=='':
        mb.showinfo('Information', 'Please select the Category.')
        return False
    
    if Rate_sel.get()=='':
        mb.showinfo('Information', 'Please select the Rating.')
        return False

    if rec_radio.get()=='':
        mb.showinfo('Information', 'Please select Recommendation.')
        return False

    #Date can only be numbers
    if not entDate.get().isdigit():
        mb.showinfo('information', 'Please enter a date in the format YYYYMMDD.')
        return False

#Validate the Title is not already entered
def validate_Title():
    for row in db.search_Title(entName.get()):
        if entName.get() == row[1]:
            mb.showinfo('Information', 'This Title is already entered. \nPlease press the Update Button.')
            return False

#Validate the Title when updating entry
def update_Title():
    if db.search_Title(entName.get()) == []:
        mb.showinfo('Information', 'The Title does not exist. \nPlease press the Add Button.')
        return False

#add to watchlist
def add_entry():
    if validate_entry() != False and validate_Title() != False:
        db.insert(entDate.get(), entName.get(), Cat_sel.get(), entGenre.get(), Rate_sel.get(), rec_radio.get())
    clear_form()
    load_data()

#Update an entry
def update_entry():
    if validate_entry() != False and update_Title() != False:
        db.update(entDate.get(), entName.get(), Cat_sel.get(), entGenre.get(), Rate_sel.get(), rec_radio.get())
    clear_form()
    load_data()

#Delete an entry
def delete_entry():
    if entName.get()=='':
        mb.showinfo('Information', 'Select an entry to delete.')
        return
    MsgBox = mb.askquestion('Delete', 'Are your sure you want to delete this selection?', icon='warning')
    if MsgBox== 'yes':
        db.remove(entName.get())
        clear_form()
        load_data()

#Clear the Form
def clear_form():
    entDate.delete(0, END)
    entName.delete(0, END)
    entGenre.delete(0, END)
    Cat_sel.set(' ')
    Rate_sel.set(' ')
    rec_radio.set(' ')
    return

#Show All entries in treeview
def load_data():
    for row in tvWatchlist.get_children():
        tvWatchlist.delete(row)
    for row in db.fetch():
        Date = row[0]
        Title = row[1]
        Category =row[2]
        Genre= row[3]
        Rating= row[4]
        Recommend=row[5]
        tvWatchlist.insert("",'end', text=Title, values=(Date, Title, Category, Genre, Rating, Recommend))

#Show specific entry
def show_selected_entry(event):
    clear_form()
    for selection in tvWatchlist.selection():
        item=tvWatchlist.item(selection)
        global Title
        Date,Title, Category,Genre,Rating,Recommend = item["values"][0:6]
        entDate.insert(0, Date)
        entName.insert(0, Title)
        entGenre.insert(0, Genre)
        Cat_sel.set(Category)
        Rate_sel.set(Rating)
        rec_radio.set(Recommend)
        return Title

#Exit the application
def exit():
    MsgBox = mb.askquestion('Close Window', 'Do you want to exit the application?', icon= 'warning')
    if MsgBox == 'yes':
        root.destroy()

###################################
#     Create The GUI Widgets      #
###################################

#create label widget for title
lblTitle = Label(root, text="NETFLIX WATCHLIST", font=('Tw Cen MT Condensed Bold', 45), bg='black', fg='red')

#labels for the fields
lblDate = Label(root, text='Date Watched:', font=('Tw Cen MT Condensed Bold', 14), bg='black', fg='white') 
lblName = Label(root, text='Title:', font=('Tw Cen MT Condensed Bold', 14), bg='black', fg='white')
lblGenre = Label(root, text='Genre:', font=('Tw Cen MT Condensed Bold', 14), bg='black', fg='white')
lblCategory = Label(root, text='Category:', font=('Tw Cen MT Condensed Bold', 14), bg='black', fg='white')
lblRating = Label(root, text='Rating:', font=('Tw Cen MT Condensed Bold', 14), bg='black', fg='white')
lblRec = Label(root, text='Would you recommend?', font=('Tw Cen MT Condensed Bold', 14), bg='black', fg='white')

#entry widgets
entDate = Entry(root)
entName = Entry(root)
entGenre = Entry(root)

#dropdown list
Cat_sel=StringVar()
Rate_sel=StringVar()
Cat_drop = OptionMenu(root, Cat_sel, "TV Show", "Movie", "Documentary")
rate_drop = OptionMenu(root, Rate_sel,'0','1','2','3','4','5',)

#create Buttons
btn_add = Button(root, text='Add', font= ('Tw Cen MT Condensed Bold',14), command= add_entry, bg='red', fg='white')
btn_update = Button(root, text='Update', font= ('Tw Cen MT Condensed Bold',14),command= update_entry, bg='red', fg='white')
btn_delete = Button(root, text ='Delete', font=('Tw Cen MT Condensed Bold', 14), command = delete_entry, bg='red', fg='white')
btn_clear = Button(root, text='Clear', font= ('Tw Cen MT Condensed Bold',14), command= clear_form, bg='red', fg='white')
btn_show_all = Button(root, text='Show All', font= ('Tw Cen MT Condensed Bold',14), command= load_data, bg='red', fg='white')
btn_exit = Button(root, text='Exit', font= ('Tw Cen MT Condensed Bold',14), command= exit, bg='white', fg='red')

#Create and pack the Radio Buttons
rec_radio= StringVar(root, ' ')
frm_Radio= Frame(root)
rbtn_1 = Radiobutton(frm_Radio, text= 'Yes', font=('Tw Cen MT Condensed Bold', 10),
                    bg= 'black',fg='white', variable= rec_radio, value= 'Yes', indicator= 0,
                    borderwidth= 2, selectcolor= 'red', width=5)
rbtn_2 = Radiobutton(frm_Radio, text= 'No', font=('Tw Cen MT Condensed Bold', 10),
                    bg='black', fg='white', variable= rec_radio, value= 'No', indicator= 0,
                    borderwidth= 2, selectcolor= 'red', width=5)
rbtn_1.pack(side=LEFT)
rbtn_2.pack(side=LEFT, ipady=5)

#Create clip art
image1=ImageTk.PhotoImage(Image.open(path+"icons/popcorn.png"))
photo_1 =Label(image=image1,bg='black')
image2=ImageTk.PhotoImage(Image.open(path+"icons/tickets.png"))
photo_2 =Label(image=image2,bg='black')

##########################
#   Place the Contents   #
##########################

#place the labels
lblTitle.place(x=150, y=10, height=80, width=500)
lblDate.place(x=145, y=100, height=25, width=100)
lblName.place(x=145, y=175, height=25, width=50)
lblCategory.place(x=425, y=100, height=25, width=78)
lblGenre.place(x=425, y=175, height=25, width=60)
lblRating.place(x=145, y=250, height=25, width=64)
lblRec.place(x=425, y=250, height=25, width=175)

#place entry widgets and lists
entDate.place(x=250,y=100, height=25, width= 150)
entName.place(x=250, y=175, height=25, width= 150)
entGenre.place(x=505, y=175, height=25, width= 150)
Cat_drop.place(x=505, y=100, height=25, width= 150)
rate_drop.place(x=250, y=250, height=25, width= 150)

#place the buttons
btn_add.place(x=165, y= 325, height=25, width=70)
btn_update.place(x=265, y= 325, height=25, width=70)
btn_delete.place(x=365, y= 325, height=25, width=70)
btn_clear.place(x=465, y= 325, height=25, width=70)
btn_show_all.place(x=565, y= 325, height=25, width=70)
btn_exit.place(x=375, y= 655, height=25, width=50)
frm_Radio.place(x=605, y=250, height=25, width=80)

#place the photos
photo_1.place(x= 5, y=225)
photo_2.place(x=650, y=10)

###################################
#  Create and Place the TreeView  #
###################################

#tuple columns
columns= ('1','2','3','4','5','6')

#TV for watchlist
tvWatchlist= ttk.Treeview(root, show='headings',height='5', columns=columns)

#headings for columns
tvWatchlist.heading('1', text='Date', anchor= 'center')
tvWatchlist.column('1', width= 60, anchor='center', stretch=FALSE)

tvWatchlist.heading('2', text='Title', anchor= 'center')
tvWatchlist.column('2', width= 10, anchor='center', stretch=TRUE)

tvWatchlist.heading('3', text='Category', anchor= 'center')
tvWatchlist.column('3', width= 10, anchor='center', stretch=TRUE)

tvWatchlist.heading('4', text='Genre', anchor= 'center')
tvWatchlist.column('4', width= 90, anchor='center', stretch=FALSE)

tvWatchlist.heading('5', text='Rating', anchor= 'center')
tvWatchlist.column('5', width= 50, anchor='center', stretch=FALSE)

tvWatchlist.heading('6', text='Recommend?', anchor= 'center')
tvWatchlist.column('6', width= 85, anchor='center', stretch=FALSE)

#add Scrollbars
vsb=ttk.Scrollbar(root, orient= VERTICAL, command=tvWatchlist.yview)
vsb.place(x=755, y= 375, height=250)

hsb=ttk.Scrollbar(root, orient=HORIZONTAL, command=tvWatchlist.xview)
hsb.place(x=50, y= 630, width=700)

#configure Scrollbars
tvWatchlist.configure(yscroll=vsb.set)
tvWatchlist.configure(xscroll=hsb.set)

#Place the TreeView
tvWatchlist.place(x=50, y=375, width=700, height=250)

#Bind TreeView to Functions
tvWatchlist.bind("<<TreeviewSelect>>", show_selected_entry)

#Load the data when you start the application
load_data()

root.mainloop()