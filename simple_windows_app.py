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

# Create a label and a textbox for user input
label1 = tk.Label(window, text="Enter your name:")
label1.pack()

entry1 = tk.Entry(window)
entry1.pack()


# Create a button to display the greeting
button = tk.Button(window, text="Say Hi", command=display_greeting)
button.pack()

# Create a label to display the greeting message
greeting_label = tk.Label(window, text="")
greeting_label.pack()

# Get the screen width and height
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Calculate the new width and height for the window (25% of the screen)
new_width = int(screen_width * 0.25)
new_height = int(screen_height * 0.25)

# Set the window size and position it in the center of the screen
window.geometry(f"{new_width}x{new_height}+{int((screen_width - new_width)\
/ 2)}+{int((screen_height - new_height) / 2)}")


# Start the main loop
window.mainloop()
