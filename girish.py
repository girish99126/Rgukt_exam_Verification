
import tkinter as tk
import PyPDF2
from tkinter.filedialog import askopenfile
from PIL import Image,ImageTk
import final


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

#input student ID
tk.Label(root, text="ID Number:",font="Raleway").grid(columnspan=1,row=3)
id_str = tk.StringVar(root)
id_input=tk.Entry(root,textvariable=id_str)
id_input.place(width=15, height=1)
id_input.grid(column=1,row=3)

#id verification
def id_verify(id_str):
    final.run_all(id_str)

#browse button
browse_text = tk.StringVar()
brwose_btn = tk.Button(root,textvariable = browse_text,command=lambda:id_verify(id_str.get()),font="Raleway",bg="#20bebe",fg="white",height=1,width=15)
browse_text.set("Verification")
brwose_btn.grid(column=2,row=3)


#conavas
convas = tk.Canvas(root,width=600,height=250)
convas.grid(columnspan = 3)
convas.configure(bg='white')


root.mainloop()

