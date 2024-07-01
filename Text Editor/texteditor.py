import pytesseract
from PIL import Image
import tkinter as tk
from tkinter import filedialog, Text, Scrollbar

# Initialize tkinter
root = tk.Tk()
root.title("OCR Text Editor")
root.geometry("800x600")  # Set the window size

# Function to open image and perform OCR
def open_image():
    # Open file dialog to select an image file
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.tiff")])
    if file_path:
        perform_ocr(file_path)

def perform_ocr(image_path):
    # Open the selected image file
    with Image.open(image_path) as img:
        # Perform OCR using pytesseract
        text = pytesseract.image_to_string(img)
        # Insert the extracted text into the text editor
        text_editor.delete(1.0, tk.END)
        text_editor.insert(tk.END, text)

# Create a menu
menu = tk.Menu(root)
root.config(menu=menu)

# Add a "File" menu
file_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open Image", command=open_image)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Create a text editor with a scrollbar
frame = tk.Frame(root)
frame.pack(expand=True, fill=tk.BOTH)

scrollbar = Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

text_editor = Text(frame, wrap=tk.WORD, undo=True, yscrollcommand=scrollbar.set)
text_editor.pack(expand=True, fill=tk.BOTH)

scrollbar.config(command=text_editor.yview)

# Start the tkinter main loop
root.mainloop()
