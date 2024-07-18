from tkinter import *

def check_number():
  try:
    number = float(number_entry.get())
    is_integer = number.is_integer()
    result_text.delete(1.0, END)

    if is_integer:
     
      result_text.insert(INSERT, f"{number} is an int.\n")
     
      if number > 0:
        result_text.insert(INSERT, f"{number} is a whole number.\n")
     
      if number > 0:
        result_text.insert(INSERT, f"{number} is a natural number.\n")
      else:
        
        pass
    else:
      
      result_text.insert(INSERT, f"{number} is rational .\n")
     
      result_text.insert(INSERT, f"{number} probably a irrational number.\n")
      

    if number > 1:
      is_prime = True
      for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
          is_prime = False
          break
      if is_prime:
        result_text.insert(INSERT, f"{number} is prime .\n")
      else:
        result_text.insert(INSERT, f"{number} is composite .\n")
    else:
      
      pass

    if number % 2 == 0:
      result_text.insert(INSERT, f"{number} is  even.\n")
    else:
      result_text.insert(INSERT, f"{number} is odd.\n")
  except ValueError:
    result_text.delete(1.0, END)
    result_text.insert(INSERT, "don't you even know basic maths, enter a valid number.")

window = Tk()
window.title("juggling numbers") #window name

number_label = Label(window, text="give a number:") #number input
number_label.pack()

number_entry = Entry(window) #entry popup window
number_entry.pack()

check_button = Button(window, text="Check", command=check_number) #check button
check_button.pack()

result_text = Text(window) #response txt
result_text.pack()

window.mainloop()
