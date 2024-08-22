from tkinter import *
from tkinter import filedialog
from PyPDF2 import PdfWriter, PdfReader

root = Tk()
root.geometry("200x200")
root.config(padx=20, pady=30)
root.title('Text Editor By Arslan')

pdfwriter = PdfWriter()

def get_file():
    file = filedialog.askopenfile(mode='rb')
    if file:
        pdf = PdfReader(file)
        get_button.config(text='Uploaded')
        write(pdf)

def write(pdf):
    for page_num in range(len(pdf.pages)):
        pdfwriter.add_page(pdf.pages[page_num])

def encrypt_file():
    passw = file_text.get()
    if passw:
        pdfwriter.encrypt(user_password=passw, owner_password=None)

        with open("encrypted_output.pdf", "wb") as output_pdf:
            pdfwriter.write(output_pdf)
        
        encrypt_button.config(text='Saved!!')
        file_text.delete(0, END)
        your_password.config(text=f'Your Password:\n{passw}')
    else:
        encrypt_button.config(text='Enter Password!')

get_button = Button(root, text='Upload', command=get_file, bg='yellow')
get_button.grid(row=0, column=0, padx=10)

encrypt_button = Button(root, text='Save File', command=encrypt_file, bg='green', fg='white')
encrypt_button.grid(row=0, column=1, padx=10)

password = Label(text='Enter Password :', fg='Red')
password.grid(row=1, column=0, columnspan=2, pady=10)

file_text = Entry(root)
file_text.grid(row=2, column=0, columnspan=2)

your_password = Label(text='', fg='Green')
your_password.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()
