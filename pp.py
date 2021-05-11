from tkinter import *
from tkinter.messagebox import *
import matplotlib.pyplot as plt

root = Tk()
root.geometry("500x500+400+400")
root.title("Report Generator")

def f1():
	try:
		name = ent_name.get()
		aoa = int(ent_aoa.get())
		os = int(ent_os.get())
		python = int(ent_python.get())
		am4 = int(ent_am4.get())
		mp = int(ent_mp.get())
		subject = ['AOA', 'OS', 'PYTHON', 'AM4', 'MP']
		marks = [aoa,os,python,am4,mp]

		plt.plot(subject,marks,linewidth=3)
		plt.xlabel("Subjects")
		plt.ylabel("Marks")
		plt.title(name+"s Performance")
		plt.show()
		
		plt.bar(subject,marks,linewidth=3)
		plt.xlabel("Subjects")
		plt.ylabel("Marks")
		plt.title(name+"s Performance")
		plt.show()
       
		plt.pie(marks, labels=subject, autopct='%.2f%%', shadow=True)
		plt.show()
	
	except ValueError:
		showerror("Mistake",'invalid marks')
		ent_aoa.delet(0, END)
		ent_os.delet(0, END)
		ent_python.delet(0, END)
		ent_am4.delet(0, END)
		ent_mp.delet(0, END)
		ent_aoa.focus()
	

	

f = ('Calibri', 20, 'bold')
lbl_name = Label(root, text="Name Of Student", font=f,)
ent_name = Entry(root, bd=5, font=f)
lbl_aoa = Label(root, text="AOA Marks", font=f,)
ent_aoa = Entry(root, bd=5, font=f)
lbl_os = Label(root, text="OS Marks", font=f,)
ent_os = Entry(root, bd=5, font=f)
lbl_python = Label(root, text="PYTHON Marks", font=f,)
ent_python = Entry(root, bd=5, font=f)
lbl_am4 = Label(root, text="AM4 Marks", font=f,)
ent_am4 = Entry(root, bd=5, font=f)
lbl_mp = Label(root, text="MP Marks", font=f,)
ent_mp = Entry(root, bd=5, font=f)

lbl_name.pack(pady=3)
ent_name.pack(pady=3)
lbl_aoa.pack(pady=3)
ent_aoa.pack(pady=3)
lbl_os.pack(pady=3)
ent_os.pack(pady=3)
lbl_python.pack(pady=3)
ent_python.pack(pady=3)
lbl_am4.pack(pady=3)
ent_am4.pack(pady=3)
lbl_mp.pack(pady=3)
ent_mp.pack(pady=3)


btn_line = Button(root, text="Result Analysis", font=f, width=15, command=f1).pack(pady=10)


root.mainloop()