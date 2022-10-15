from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# oracle connection

import cx_Oracle

con=cx_Oracle.connect('C##SCOTT/tiger@localhost/orcl')
# function for inserting customer details
def Student():
    s_no = s_no_field.get()
    s_name = name_field.get()
    s_gender = gender_field.get()
    s_email = email_field.get()
    s_address = address_field.get()
    s_DOB = ph_field.get()
    s_major = add_field.get()
    Sem = add_sem.get()
    AdmissionDate =add_AdmissionDate.get()
    dep =Add_dep.get()
    mycur = con.cursor()

    new = [(s_no, s_name, s_gender, s_email, s_address, s_DOB, s_major,Sem,AdmissionDate,dep,)]
    mycur.executemany("insert into Student(StudentID,FullName,Gender,Email,Address,DOB,Major,Semester,AdmissionDate,DepartmentNo) values(:1,:2,:3,:4,:5,:10,:7,:8,:9,:6)",
        new)
    con.commit()
    messagebox.showinfo("successful!", "inserted")
    mycur.close()
def Teacher():
    t_no = t_no_field.get()
    t_name = name_field.get()
    Department = dept_field.get()
    Course = Course_field.get()
 
    mycur = con.cursor()

    new = [(t_no, t_name, Department, Course)]
    mycur.executemany("insert into Teacher(TeacherID,TeacherName,DepartmentNo,CourseID) values(:1,:2,:3,:4)",
        new)
    con.commit()
    messagebox.showinfo("successful!", "inserted")
    mycur.close()

def Course():
    c_no = c_no_field.get()
    c_name = name_field.get()
    c_hours = hours_field.get()
    mycur = con.cursor()
    new = [(c_no, c_name, c_hours)]
    mycur.executemany("insert into Course(CourseID,CourseName,CreditHours) values(:1,:2,:3)",
        new)
    con.commit()
    messagebox.showinfo("successful!", "inserted")
    mycur.close()

def ViewStudent():
    cursor = con.cursor()
    cursor.execute("""SELECT * FROM STUDENT""")
    root = tk.Tk()
    root.title('Treeview demo')
    root.geometry('2000x200')

# define columns
    columns = ("STUDENTID","FULLNAME","GENDER","EMAIL","ADDRESS","DOB","MAJOR","SEMESTER","ADMISSIONDATE")
    
    tree = ttk.Treeview(root, columns=columns, show='headings')

# define headings
    tree.heading('STUDENTID', text='STUDENTID')
    tree.heading('FULLNAME', text=' FULLNAME')
    tree.heading('GENDER', text='Gender')
    tree.heading('EMAIL', text=' Email')
    tree.heading('ADDRESS', text='ADDRESS')
    tree.heading('DOB', text=' DOB')
    tree.heading('MAJOR', text='MAJOR')
    tree.heading('SEMESTER', text=' SEMESTER')
    tree.heading('ADMISSIONDATE', text=' ADMISSIONDATE')
# generate sample data
    contacts = []
    for i in cursor:
        contacts.append(i)
        
# add data to the treeview
    for contact in contacts:
        tree.insert('', tk.END, values=contact)


    def item_selected(event):
        for selected_item in tree.selection():
            item = tree.item(selected_item)
            record = item['values']
        # show a message
            showinfo(title='Information', message=','.join(record))


    tree.bind('<<TreeviewSelect>>', item_selected)

    tree.grid(row=0, column=0, sticky='nsew')

# add a scrollbar
    scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=0, column=1, sticky='ns')

# run the app
    root.mainloop()
    
def ViewCourse():
    cursor = con.cursor()
    cursor.execute("""SELECT * FROM COURSE""")
    root = tk.Tk()
    root.title('Treeview demo')
    root.geometry('700x200')

# define columns
    columns = ("COURSEID","COURSENAME","CREDITHOURS")

    tree = ttk.Treeview(root, columns=columns, show='headings')

# define headings
    tree.heading('COURSEID', text='COURSEID')
    tree.heading('COURSENAME', text=' COURSENAME')
    tree.heading('CREDITHOURS', text='CREDITHOURS')

# generate sample data
    contacts = []
    for i in cursor:
        contacts.append(i)
# add data to the treeview
    for contact in contacts:
        tree.insert('', tk.END, values=contact)


    def item_selected(event):
        for selected_item in tree.selection():
            item = tree.item(selected_item)
            record = item['values']
        # show a message
            showinfo(title='Information', message=','.join(record))


    tree.bind('<<TreeviewSelect>>', item_selected)

    tree.grid(row=0, column=0, sticky='nsew')

# add a scrollbar
    scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=0, column=1, sticky='ns')

# run the app
    root.mainloop()
def ViewTeacher():
    cursor = con.cursor()
    cursor.execute("""SELECT * FROM TEACHER""")
    root = tk.Tk()
    root.title('Treeview demo')
    root.geometry('900x200')

# define columns
    columns = ("TEACHERID","TEACHERNAME","COURSEID","DEPARTMENTNO")

    tree = ttk.Treeview(root, columns=columns, show='headings')

# define headings
    tree.heading('TEACHERID', text='TEACHERID')
    tree.heading('TEACHERNAME', text=' COURSEID')
    tree.heading('DEPARTMENTNO', text='DEPARTMENTNO')
    tree.heading('COURSEID', text='CourseID')

# generate sample data
    contacts = []
    for i in cursor:
        contacts.append(i)
# add data to the treeview
    for contact in contacts:
        tree.insert('', tk.END, values=contact)


    def item_selected(event):
        for selected_item in tree.selection():
            item = tree.item(selected_item)
            record = item['values']
        # show a message
            showinfo(title='Information', message=','.join(record))


    tree.bind('<<TreeviewSelect>>', item_selected)

    tree.grid(row=0, column=0, sticky='nsew')

# add a scrollbar
    scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=0, column=1, sticky='ns')
    
# run the app
    root.mainloop()
# main function

main = Tk()
rad = StringVar()
main.configure(background='grey')
main.title("Student Information System")
main.geometry("1000x900")
##Student
top = Label(main, text="Student Details", bg="red", font="verdana 30 bold")
s_no = Label(main, text="Student ID:")
s_name = Label(main, text="NAME:")
s_gender = Label(main, text="Gender")
s_email = Label(main, text="E-MAIL:")
s_address = Label(main, text="ADDRESS:")
s_DOB = Label(main, text="DOB:")
s_major = Label(main, text="Major:")
Sem = Label(main, text="Semster:")
AdmissionDate = Label(main, text="Addmission:")

dep = Label(main, text="Department:")


top.grid(row=0, column=1)
s_no.grid(row=1, column=0)
s_name.grid(row=2, column=0)
s_gender.grid(row=3, column=0)
s_email.grid(row=4, column=0)
s_address.grid(row=5, column=0)
s_DOB.grid(row=6, column=0)
s_major.grid(row=7, column=0)
Sem.grid(row=8, column=0)
AdmissionDate.grid(row=9, column=0)

dep.grid(row=11, column=0)


s_no_field = Entry(main)
name_field = Entry(main)
gender_field = Entry(main)
email_field = Entry(main)
address_field = Entry(main)
ph_field = Entry(main)
add_field = Entry(main)
add_sem = Entry(main)
add_AdmissionDate = Entry(main)

Add_dep = Entry(main)



s_no_field.grid(row=1, column=1, ipadx="100")
name_field.grid(row=2, column=1, ipadx="100")
gender_field.grid(row=3, column=1, ipadx="100")
email_field.grid(row=4, column=1, ipadx="100")
address_field.grid(row=5, column=1, ipadx="100")
ph_field.grid(row=6, column=1, ipadx="100")
add_field.grid(row=7, column=1, ipadx="100")
add_sem.grid(row=8, column=1, ipadx="100")
add_AdmissionDate.grid(row=9, column=1, ipadx="100")
Add_dep.grid(row=11, column=1, ipadx="100")



b1 = Button(main, text="INSERT", font="30", fg="red", bg="blue", width="20", command=Student)
b1.grid(row=12, column=1)
b3 = Button(main, text="ViewStudent", font="30", fg="red", bg="blue", width="20", command=ViewStudent)
b3.grid(row=12, column=2)
##Teacher
top = Label(main, text="Teacher Details", bg="red", font="verdana 30 bold")
t_no = Label(main, text="Teacher ID:")
t_name = Label(main, text="Teacher NAME:")
Department = Label(main, text="Department")
Course = Label(main, text="Course:")




top.grid(row=13, column=1)
t_no.grid(row=14, column=0)
s_name.grid(row=15, column=0)
t_name.grid(row=16, column=0)
Department.grid(row=17, column=0)
Course.grid(row=18, column=0)





t_no_field = Entry(main)
name_field = Entry(main)
dept_field = Entry(main)
Course_field = Entry(main)


Add_dep = Entry(main)



t_no_field.grid(row=14, column=1, ipadx="100")
name_field.grid(row=15, column=1, ipadx="100")
dept_field.grid(row=16, column=1, ipadx="100")
Course_field.grid(row=17, column=1, ipadx="100")

b5 = Button(main, text="INSERT", font="30", fg="red", bg="blue", width="20", command=Teacher)
b5.grid(row=19, column=1)
b6 = Button(main, text="ViewTeacher", font="30", fg="red", bg="blue", width="20", command=ViewTeacher)
b6.grid(row=19, column=2)

##Course
top = Label(main, text="Course Details", bg="red", font="verdana 30 bold")
c_no = Label(main, text="Course ID")
c_name = Label(main, text="CourseName:")
c_hours = Label(main, text="CreduitHours")


top.grid(row=23, column=1)
c_no.grid(row=25, column=0)
c_name.grid(row=26, column=0)
c_hours.grid(row=27, column=0)




c_no_field = Entry(main)
name_field = Entry(main)
hours_field = Entry(main)




c_no_field.grid(row=25, column=1, ipadx="100")
name_field.grid(row=26, column=1, ipadx="100")
hours_field.grid(row=27, column=1, ipadx="100")




b2 = Button(main, text="INSERT", font="30", fg="red", bg="blue", width="20", command=Course)
b2.grid(row=28, column=1)
b4 = Button(main, text="ViewCourse", font="30", fg="red", bg="blue", width="20", command=ViewCourse)
b4.grid(row=28, column=2)


main.mainloop()
