import rarfile
import zipfile
import os
from os import listdir
from Tkinter import *

root = Tk()

screenW = root.winfo_screenwidth()
screenH = root.winfo_screenheight()

root.title("Comic Unpacker")
root.geometry("400x200")
root.configure(background="light blue")

rarfile.UNRAR_TOOL = 'UnRAR.exe'

lblEnterDirectory = Label(root,bg="light blue",text="Enter a Directory (ex C:\USERS\ETC): ")
txtDir = Entry(root)

def btnClicked():
    direct = txtDir.get()

    for filename in os.listdir(direct):
        print filename[-4:]
        if filename[-4:] == ".rar" or filename[-4:] == ".cbr":
            #rar (or cbr, or any other type of rar file)
            try:
                rf = rarfile.RarFile(direct+"/"+filename)
                rf.extractall(direct+"/Extracted/"+filename[:-4]+"/")
            except:
                print "Error! "+filename+" cannot be extracted!(rar/cbr)"
        elif filename[-4:] == ".zip" or filename[-4:] == ".cbz":
            #zip (or cbz, or any other type of zip file)
            try:
                with zipfile.ZipFile(direct+"/"+filename, "r") as z:
                    z.extractall(direct+"/Extracted/"+filename[:-4]+"/")
            except:
                print "Error! "+filename+" cannot be extracted! (zip/cbz)"

    print "--------------------------------------------------"

btnExecute = Button(root, text="Extract!", command=btnClicked)

lblEnterDirectory.grid(row=1,column=1,pady=10)
txtDir.grid(row=1,column=2,pady=10)
btnExecute.grid(row=1,column=3,padx=20,pady=10)

root.mainloop()
