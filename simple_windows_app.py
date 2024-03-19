import tkinter as tk

def display_greeting():
    name = entry.get()
    greeting_label.config(text="Hi there " + name)

# Create the main window
window = tk.Tk()
window.title("Greeting App")

# Create a label and a textbox for user input
label = tk.Label(window, text="Enter your name:")
label.pack()

entry = tk.Entry(window)
entry.pack()

# Create a button to display the greeting
button = tk.Button(window, text="Say Hi", command=display_greeting)
button.pack()

# Create a label to display the greeting message
greeting_label = tk.Label(window, text="")
greeting_label.pack()

# Start the main loop
window.mainloop()
