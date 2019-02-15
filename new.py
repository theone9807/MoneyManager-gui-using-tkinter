from tkinter import *
import tkinter as tk
from tkinter import messagebox
from matplotlib.figure import Figure
from collections import defaultdict
from pprint import pprint
import matplotlib.pyplot as plt
from moneymanager import MoneyManager
from pylab import plot, show, xlabel, ylabel
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


root = Tk()
root.geometry("500x660") # size of the window width:- 500, height:- 375
root.resizable(0, 0) # this prevents from resizing the window
root.title("FedUni Money Manager")
Label (root, text = "FedUni Money Manager", fg = "skyblue", font= "none 28 bold") .grid(row = 0, sticky="w", padx= (40,10), pady=(15,15))
#The user number and associated variable

Label (root, text = "User Number/PIN", fg = "black", font= "none 14") .grid(row = 1, column = 0, sticky='W')
u_number_var = StringVar()
u_number_var.set('167736')
user_entry = Entry(root, textvariable=u_number_var, width = 27,  background = 'white') .grid(row = 1, column = 0, padx = 1, pady = 1)

#The pin number entry and associated variables
pin_var = StringVar()
#This is set as a default for ease of testing
pin_var.set('4558')

#Modify the following to display a series of * rather than the pin ie **** not 1234
user_pin_entry = Entry(root, textvariable=pin_var, show="*",width = 27,  background = 'white') .grid(row = 1, column = 0, padx = 1, pady = 1, sticky='e')

tkVar=StringVar(root)
amount_entry = tk.Entry(root)
entry_type=tk.Entry(root)
 
# The transaction text widget holds text of the transactions
transaction_text_widget = tk.Text(root, height=10, width=48)

# The money manager object we will work with
#set the user file by default to an empty string
user_file = ''

# The balance label and associated variable
balance_var = tk.StringVar()
balance_var.set('Balance: $0.00')
balance_label = tk.Label(root, textvariable=balance_var)

# The Entry widget to accept a numerical value to deposit or withdraw
#amount_var = tk.StringVar()
iVar=StringVar(root)
amount_entry = tk.Entry(root)
entry_type=tk.Entry(root)

# The transaction text widget holds text of the transactions
transaction_text_widget = tk.Text(root, height=10, width=48)

# The money manager object we will work with
enduser = MoneyManager()

# ---------- Buttons for Login Screen ----------


def handle_buttons(event):
    '''Function to add the number of the button clicked to the PIN number entry.'''    
    # Limit to 4 chars in length
    count = 0
    count += 1
    if count in range(0,4): 
        global user_file
        user_file = user_file + str(event)
        pin_var.set(user_file)
    # Set the new pin number on the pin_number_var

def Log_In():
    '''Function to log in to the banking system using a known user number and PIN.'''
    remove_all_widgets()
    global enduser
    global pin_var
    global user_file
    global user_num_entry
    create_screen()
    enduser.get_details()
    # Create the filename from the entered account number with '.txt' on the end
    
def clear_pin_entry(event):
    '''Function to clear the PIN number entry when the Clear / Cancel button is clicked.'''    
    # Clear the pin number entry here
    global user_file
    user_file = ""
    pin_var.set("")
    u_number_var.set('')    
# ---------- Button Handlers for User Screen ----------

def save_and_log_out():
    '''Function  to overwrite the user file with the current state of
       the user object (i.e. including any new transactions), remove
       all widgets and display the login screen.'''
    global enduser

    enduser.save_to_file()
    clear_pin_entry(event)
    create_screen()
    

def perform_deposit():
    '''Function to add a deposit for the amount in the amount entry to the
       user's transaction list.'''
    global enduser    
    global amount_entry
    global balance_label
    global balance_var

    # Try to increase the account balance and append the deposit to the account file
    
        # Get the cash amount to deposit. Note: We check legality inside account's deposit method

        # Deposit funds
        
        # Update the transaction widget with the new transaction by calling account.get_transaction_string()
        # Note: Configure the text widget to be state='normal' first, then delete contents, then instert new
        #       contents, and finally configure back to state='disabled' so it cannot be user edited.

        # Change the balance label to reflect the new balance

        # Clear the amount entry

        # Update the interest graph with our new balance

    # Catch and display exception as a 'showerror' messagebox with a title of 'Transaction Error' and the text of the exception

def perform_transaction():
    '''Function to add the entry the amount in the amount entry from the user balance and add an entry to the transaction list.'''
    global enduser    
    global amount_entry
    global balance_label
    global balance_var
    global entry_type

    
def remove_all_widgets():
    '''Function to remove all the widgets from the window.'''
    global root
    for widget in root.winfo_children():
        widget.grid_remove()

def read_line_from_user_file():
    '''Function to read a line from the users file but not the last newline character.
       Note: The user_file must be open to read from for this function to succeed.'''
    global user_file
    return user_file.readline()[0:-1]


def create_LogIn_screen():
    '''Function to create the login screen.'''    
    
    # ----- Row 0 -----

    # 'FedUni Money Manager' label here. Font size is 28.
    Label (root, text = "FedUni Money Manager", fg = "black", font= "none 28 bold") .grid(row = 0, sticky="w", padx= (40,10), pady=(15,15))


    expression = ""
    expression1 = ""
    # 'StringVar()' is used to get the instance of input field
    
    # creating another 'Frame' for the button below the 'input_frame'
    btnframe = Frame(root, width = 500, height = 660, bg = "grey")
    btnframe.grid()

    # second row
    seven = Button(btnframe, text = "7", fg = "black", width = 24, height = 7, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: handle_buttons(7)).grid(row = 1, column = 0, padx = 1, pady = 1)
    eight = Button(btnframe, text = "8", fg = "black", width = 23, height = 7, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: handle_buttons(8)).grid(row = 1, column = 1, padx = 1, pady = 1)
    nine = Button(btnframe, text = "9", fg = "black", width = 24, height = 7, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: handle_buttons(9)).grid(row = 1, column = 2, padx = 1, pady = 1)


    # third row
    four = Button(btnframe, text = "4", fg = "black", width = 24, height = 7, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: handle_buttons(4)).grid(row = 2, column = 0, padx = 1, pady = 1)
    five = Button(btnframe, text = "5", fg = "black", width = 23, height = 7, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: handle_buttons(5)).grid(row = 2, column = 1, padx = 1, pady = 1)
    six = Button(btnframe, text = "6", fg = "black", width = 24, height = 7, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: handle_buttons(6)).grid(row = 2, column = 2, padx = 1, pady = 1)


    # fourth row
    one = Button(btnframe, text = "1", fg = "black", width = 24, height = 7, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: handle_buttons(1)).grid(row = 3, column = 0, padx = 1, pady = 1)
    two = Button(btnframe, text = "2", fg = "black", width = 23, height = 7, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: handle_buttons(2)).grid(row = 3, column = 1, padx = 1, pady = 1)
    three = Button(btnframe, text = "3", fg = "black", width = 24, height = 7, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: handle_buttons(3)).grid(row = 3, column = 2, padx = 1, pady = 1)


    # fourth row
    cc = Button(btnframe, text = "Cancel/Clear", fg = "black", width = 24, height = 8, bd = 0, bg = "red", cursor = "hand2", command = lambda: clear_pin_entry(user_pin_entry)).grid(row = 4, column = 0,  padx = 1, pady = 1)
    zero = Button(btnframe, text = "0", fg = "black", width = 23, height = 8, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click(".")).grid(row = 4, column = 1, padx = 1, pady = 1)
    login = Button(btnframe, text = "Log In", fg = "black", width = 24, height = 8, bd = 0, bg = "green", cursor = "hand2", command = lambda:Log_In()).grid(row = 4, column = 2, padx = 1, pady = 1)

def create_screen():
    '''Function to create the user screen.'''
    global amount_text
    global amount_label
    global transaction_text_widget
    global balance_var
    
    # ----- Row 0 -----
    # 'FedUni Money Manager' label here. Font size is 28.
    Label (root, text = "FedUni Money Manager", fg = "black", font= "none 28 bold") .grid(row = 0, sticky="w", padx= (40,10), pady=(15,15))

    # ----- Row 1 -----
    # Account number label here
    Label (root, text = "Account number", fg = "black", font= "none 14 bold") .grid(row = 1, sticky="w", pady=(15,15))
    # Balance label here
    Label (root, text = "Balance", fg = "black", font= "none 14 bold") .grid(row = 1, sticky="n", padx= (40,10), pady=(15,15))
    # Log out button hereb
    #btns_frame = Frame(root, width = 500, height = 660, bg = "grey")
    #btns_frame.grid(row = '1', sticky='e')
    logout = Button(root, text = "Log Out", fg = "black", width = 24, height = 7, bd = 0, bg = "green", cursor = "hand2", command = lambda:create_LogIn_screen()).grid(row = 4, column = 0, padx = 1, pady = 1)

    # ----- Row 2 -----

    # Amount label here
    #Label (root, text = "FedUni Money Manager", fg = "black", font= "none 28 bold") .grid(row = 2, sticky="w", pady=(15,15))

    #Amount entry here
   
    #amount_entry = Entry(root, textvariable=iVar, width = 27,  background = 'white') .grid(row = 1, column = 0, padx = 1, pady = 1)
    
    # # Deposit button here
    deposit = Button(root, text = "deposit", fg = "black", width = 24, height = 7, bd = 0, bg = "green", cursor = "hand2", command = lambda:perform_deposit()).grid(row = 2, column = 0, padx = 1, pady = 1)

# ---------- Display Login Screen & Start Main loop ----------

create_LogIn_screen()
root.mainloop()
