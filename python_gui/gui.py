import tkinter as tk

def main():
    # Create the main window
    root = tk.Tk()
    root.title("Hello, World!")

    # Create a label with the message
    label = tk.Label(root, text="Hello, World!")

    # Pack the label into the window
    label.pack(padx=10, pady=10)

    # Start the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()
