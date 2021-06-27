import tkinter as tk
import PyPDF2
from tkinter.filedialog import askopenfile
from PIL import Image,ImageTk



root = tk.Tk()
#root.mainloop()
convas = tk.Canvas(root,width=600,height=300)
convas.grid(columnspan = 3,rowspan=3)
convas.configure(bg='white')

#logo
logo = Image.open("logo.jpg")
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1,row=0)
print("is this working")


#instructions
instructions = tk.Label(root,text="Welcome to Rgukt Examinaiton System",font="Raleway",bg="white")
instructions.grid(columnspan=3,column=0,row=1)


#open_file
def open_file():
    browse_text.set("Loading...")
    file = askopenfile(parent=root,mode="rb",title="Choose a file",filetype = [("Pdf file","*.pdf")])
    if(file):
        read_pdf = PyPDF2.PdfFileReader(file)
        print("Dgfd")
        page = read_pdf.getPage(0)
        page_content = page.extractText()
        print(page_content)

#browse button
browse_text = tk.StringVar()
brwose_btn = tk.Button(root,textvariable = browse_text,command=lambda:open_file(),font="Raleway",bg="#20bebe",fg="white",height=2,width=15)
brwose_btn.grid_rowconfigure(row=3,bg='white')
browse_text.set("Open Camera")
brwose_btn.grid(column=1,row=3)


#conavas
convas = tk.Canvas(root,width=600,height=250)
convas.grid(columnspan = 3)
convas.configure(bg='white')


root.mainloop()