from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import messagebox

root = Tk()
root.geometry("1000x720")
root.title("Students Record Management")
root.iconbitmap("Exercise 3/icon.ico")

def students_record():
    Students = []
    with open("Exercise 3/studentMarks.txt", "r") as file: # Open the text file and read its contents
        lines = file.readlines()[1:]    # Skip the first line of the text file
        for Students_record in lines:
            Students_record = Students_record.strip()
            if Students_record == "":
                continue 
            info = Students_record.split(",")
            Number = info[0]
            Name = info[1]
            # Convert course work mark to integer
            course_mark1, course_mark2, course_mark3 = map(int, info[2:5])
            Exam_mark = int(info[5])  # Convert exam mark to integer
            total_mark = course_mark1 + course_mark2 + course_mark3   # Calculate total mark
            Percentage = (total_mark + Exam_mark) / 160 * 100  # Calculate percentage
            Grade = grade(Percentage)
            # Store data in tuples
            Students.append((Number, Name, course_mark1, course_mark2, course_mark3, Exam_mark, Percentage, Grade))
    return Students

# Calculating Grades
def grade(percentage):
    if percentage >= 70:
       return "A"
    elif percentage >= 60:
       return "B"
    elif percentage >= 50:
       return "C"
    elif percentage >= 40:
       return "D"
    else:
        return "F"

# Function to display Treeview table  
def display_info(window, students):
    heading_columns = ("Number", "Name", "Total Coursework marks", "Exam marks", "Percentage", "Grade")
    record_table = ttk.Treeview(window, columns=heading_columns, show="headings", height=15)
    record_table.grid(row=0, column=0, pady=20, columnspan=2)

    # Add headings in table
    for column in heading_columns:
        record_table.heading(column, text=column, anchor="center")
        record_table.column(column, width=150, anchor="center")
    
    # Insert student information into the table
    for record in students:
        total_coursework = record[2] + record[3] + record[4]
        record_table.insert("", END, values=(record[0], record[1], total_coursework, record[5], f"{record[6]:.1f}%", record[7]))

# Function to display all student records
def all_student_records():
    window = Toplevel(root)  # Create a new window to display all student records
    window.title("All students record")
    window.geometry("900x450")
    window.iconbitmap("Exercise 3/icon.ico")
    window.configure(bg='sky blue')
    students = students_record()
    display_info(window, students)
    total_students = len(students) # Get the total number of students
    average_percentage = sum(s[6] for s in students) / total_students
    Label(window, text=f"Total students: {total_students} | Average %: {average_percentage:.2f}%", bg="sky blue", font=("Arial", 12, "bold")).place(x=300, y=370)

# Function to display idividual student record
def individual_student_records():
    window = Toplevel(root)
    window.title("Individual student record")
    window.geometry("300x300")
    window.iconbitmap("Exercise 3/icon.ico")
    window.configure(bg='sky blue')

    students = students_record()
    Students_Name = [s[1] for s in students]

    Label(window, text="Enter a student name", bg="sky blue", font=("Arial", 12)).place(x=85, y=30)
    dropdown = ttk.Combobox(window, values=Students_Name) # Create a dropdown menu 
    dropdown.place(x=80, y=80)

    def display_record():
        chosen_name = dropdown.get()
        if chosen_name == "":
            return
        selected_student = [s for s in students if s[1] == chosen_name] # Select the student by name
        if selected_student:
            record =  Toplevel(window)  # Create another window for idividual record
            record.title("Individual student record")
            record.geometry("900x250")
            record.configure(bg='sky blue')
            display_info(record, selected_student) # Call function to display student information
    Button(window, text="Show record", bg="#1b294a", fg="white", font=("Arial", 12, "bold"), width=10, command=display_record).place(x=90, y=140)

# Function to display highest score student 
def highest_score():
    students = students_record()
    Highest_score = max((s[2] + s[3] + s[4] + s[5]) for s in students)  # Find the highest total score among all students
    top_students = [s for s in students if (s[2] + s[3] + s[4] + s[5]) == Highest_score]  # Find all students with the highest marks
    record =  Toplevel(root)
    record.title("Highest score")
    record.geometry("900x250")
    record.iconbitmap("Exercise 3/icon.ico")
    record.configure(bg='sky blue')
    display_info(record, top_students)

# Function to display lowest score student
def lowest_score():
    students = students_record()
    Lowest_score = min((s[2] + s[3] + s[4] + s[5]) for s in students)   # Find the lowest total score among all students
    Lowest_students = [s for s in students if (s[2] + s[3] + s[4] + s[5]) == Lowest_score]  # Find all students with the lowest marks
    record =  Toplevel(root)
    record.title("Lowest score")
    record.geometry("900x250")
    record.iconbitmap("Exercise 3/icon.ico")
    record.configure(bg='sky blue')
    display_info(record, Lowest_students)

# Function to add new record 
def add_student_record():
    global record, number, name, Course_mark1, Course_mark2, Course_mark3, exam
    record =  Toplevel(root)
    record.title("Add student record")
    record.geometry("500x500")
    record.iconbitmap("Exercise 3/icon.ico")
    record.configure(bg='sky blue')

    Label(record, text="Add student details", bg="sky blue", font=("Arial", 12, "bold")).place(x=170, y=30)

    Student_number = Label(record, text="Student Number", bg="sky blue", font=("Arial", 12, "bold"))
    Student_number.place(x=30, y=80)
    number = Entry(record, width=20, font=("Arial", 16))
    number.place(x=240, y=80)

    Student_Name = Label(record, text="Student Name", bg="sky blue", font=("Arial", 12, "bold"))
    Student_Name.place(x=30, y=130)
    name = Entry(record, width=20, font=("Arial", 16))
    name.place(x=240, y=130)

    Coursework_mark1 = Label(record, text="Course mark 1 (out of 20)", bg="sky blue", font=("Arial", 12, "bold"))
    Coursework_mark1.place(x=30, y=180)
    Course_mark1 = Entry(record, width=20, font=("Arial", 16))
    Course_mark1.place(x=240, y=180)

    Coursework_mark2 = Label(record, text="Course mark 2 (out of 20)", bg="sky blue", font=("Arial", 12, "bold"))
    Coursework_mark2.place(x=30, y=230)
    Course_mark2 = Entry(record, width=20, font=("Arial", 16))
    Course_mark2.place(x=240, y=230)
    
    Coursework_mark3 = Label(record, text="Course mark 3 (out of 20)", bg="sky blue", font=("Arial", 12, "bold"))
    Coursework_mark3.place(x=30, y=280)
    Course_mark3 = Entry(record, width=20, font=("Arial", 16))
    Course_mark3.place(x=240, y=280)

    Exam_mark = Label(record, text="Exam mark (out of 100)", bg="sky blue", font=("Arial", 12, "bold"))
    Exam_mark.place(x=30, y=330)
    exam = Entry(record, width=20, font=("Arial", 16))
    exam.place(x=240, y=330)

    Button(record, text="Add record", bg="#1b294a", fg="white", font=("Arial", 12, "bold"), width=10, height=2, command=save_student_record).place(x=170, y=400)

def save_student_record():
    student_number = number.get()
    student_name = name.get()
    coursework_mark1 = Course_mark1.get()
    coursework_mark2 = Course_mark2.get()
    coursework_mark3 = Course_mark3.get()
    exam_mark = exam.get()

    if student_number == "" or student_name == "" or coursework_mark1 == "" or coursework_mark2 == "" or coursework_mark3 == "" or exam_mark == "":
        messagebox.showerror("Error", "Please fill all fields")
        record.lift()
        record.focus_force()
        return
    
    # Add new student record to the text file
    with open("Exercise 3/studentMarks.txt", "a") as file:
        file.write(f"\n{student_number},{student_name},{coursework_mark1},{coursework_mark2},{coursework_mark3},{exam_mark}")
    messagebox.showinfo("Success", "Student record has been added.")

# Function to delete student record
def delete_student_record():
    window =  Toplevel(root)
    window.title("Delete student record")
    window.geometry("900x400")
    window.iconbitmap("Exercise 3/icon.ico")
    window.configure(bg='sky blue')

    students = students_record()
    
    heading_columns = ("Number", "Name", "Total Coursework marks", "Exam marks", "Percentage", "Grade")
    record_table = ttk.Treeview(window, columns=heading_columns, show="headings", height=15)
    record_table.grid(row=0, column=0, pady=20, columnspan=2)

    for column in heading_columns:
        record_table.heading(column, text=column, anchor="center")
        record_table.column(column, width=150, anchor="center")

    for record in students:
        total_coursework = record[2] + record[3] + record[4]
        record_table.insert("", END, values=(record[0], record[1], total_coursework, record[5], f"{record[6]:.1f}%", record[7]))

    
    def record_selection():
        selected = record_table.selection()
        if not selected:
            messagebox.showerror("Error", "Please select a student to delete")
            return
        
        record = selected[0]
        values = record_table.item(record, "values")
        student_number = values[0]

        with open("Exercise 3/studentMarks.txt", "r") as file:
            lines = file.readlines()
        with open("Exercise 3/studentMarks.txt", "w") as file:
            for student_record in lines:
                if not student_record.startswith(student_number + ","):
                    file.write(student_record)

        record_table.delete(record)
        messagebox.showinfo("Success", "Record deleted!")
    Button(window, text="Delete record", bg="#1b294a", fg="white", font=("Arial", 12, "bold"), width=15, command=record_selection).place(x=350, y=360)

# Add background image behind the menu screen
bg_image = Image.open("Exercise 3/image.png")
bg_image = bg_image.resize((1000, 720))
bg_label = Label(root)
bg_label.image = ImageTk.PhotoImage(bg_image)
bg_label.config(image = bg_label.image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Function to update existing student record
def update_student_record():
    window =  Toplevel(root)
    window.title("Update student record")
    window.geometry("950x400")
    window.iconbitmap("Exercise 3/icon.ico")
    window.configure(bg='sky blue')
    
    students = students_record()

    heading_columns = ("Number", "Name", "Total Coursework marks", "Exam marks", "Percentage", "Grade")
    record_table = ttk.Treeview(window, columns=heading_columns, show="headings", height=15)
    record_table.grid(row=0, column=0, pady=20, columnspan=2)

    for column in heading_columns:
        record_table.heading(column, text=column, anchor="center")
        record_table.column(column, width=150, anchor="center")

    for record in students:
        total_coursework = record[2] + record[3] + record[4]
        record_table.insert("", END, values=(record[0], record[1], total_coursework, record[5], f"{record[6]:.1f}%", record[7]))
    def update_record():
        selected = record_table.selection()
        if not selected:
            messagebox.showerror("Error", "Please select a student")
            return
        
        record = selected[0]
        values = record_table.item(record, "values")

        current_number = values[0]
        current_name = values[1]
        selected_student = [s for s in students if s[0] == current_number][0]
        current_coursework1 = selected_student[2]
        current_coursework2 = selected_student[3]
        current_coursework3 = selected_student[4]
        current_exam = selected_student[5]

        record =  Toplevel(root)
        record.title("Update a student record")
        record.geometry("500x500")
        record.configure(bg='sky blue')

        
        Label(record, text="Add student details", bg="sky blue", font=("Arial", 12, "bold")).place(x=140, y=30)
        Student_number = Label(record, text="Student Number", bg="sky blue", font=("Arial", 12, "bold"))
        Student_number.place(x=30, y=80)
        number = Entry(record, width=20, font=("Arial", 16))
        number.place(x=240, y=80)
        number.insert(0, current_number)

        Student_name = Label(record, text="Student Name", bg="sky blue", font=("Arial", 12, "bold"))
        Student_name.place(x=30, y=130)
        name = Entry(record, width=20, font=("Arial", 16))
        name.place(x=240, y=130)
        name.insert(0, current_name)

        Coursework_mark1 = Label(record, text="Course mark 1 (out of 20)", bg="sky blue", font=("Arial", 12, "bold"))
        Coursework_mark1.place(x=30, y=180)
        Course_mark1 = Entry(record, width=20, font=("Arial", 16))
        Course_mark1.place(x=240, y=180)
        Course_mark1.insert(0, current_coursework1)

        Coursework_mark2 = Label(record, text="Course mark 2 (out of 20)", bg="sky blue", font=("Arial", 12, "bold"))
        Coursework_mark2.place(x=30, y=230)
        Course_mark2 = Entry(record, width=20, font=("Arial", 16))
        Course_mark2.place(x=240, y=230)
        Course_mark2.insert(0, current_coursework2)
    
        Coursework_mark3 = Label(record, text="Course mark 3 (out of 20)", bg="sky blue", font=("Arial", 12, "bold"))
        Coursework_mark3.place(x=30, y=280)
        Course_mark3 = Entry(record, width=20, font=("Arial", 16))
        Course_mark3.place(x=240, y=280)
        Course_mark3.insert(0, current_coursework3)

        Exam_mark = Label(record, text="Exam mark (out of 100)", bg="sky blue", font=("Arial", 12, "bold"))
        Exam_mark.place(x=30, y=330)
        exam = Entry(record, width=20, font=("Arial", 16))
        exam.place(x=240, y=330)
        exam.insert(0, current_exam)


        def save_record():
            student_number = number.get()
            student_name = name.get()
            coursework_mark1 = Course_mark1.get()
            coursework_mark2 = Course_mark2.get()
            coursework_mark3 = Course_mark3.get()
            exam_mark = exam.get()

            if student_number == "" or student_name == "" or coursework_mark1 == "" or coursework_mark2 == "" or coursework_mark3 == "" or exam_mark == "":
              messagebox.showerror("Error", "Please fill all fields")
              record.lift()
              record.focus_force()
              return
    
            with open("Exercise 3/studentMarks.txt", "r") as file:
                lines = file.readlines()

            with open("Exercise 3/studentMarks.txt", "w") as file:
                for student_record in lines:
                    if student_record.startswith(current_number + ","):
                       file.write(f"{student_number},{student_name},{coursework_mark1},{coursework_mark2},{coursework_mark3},{exam_mark}")
                    else:
                       file.write(student_record)
    
            messagebox.showinfo("Success", "Record updated!")
            record.destroy()
            window.destroy()
        
        Button(record, text="Save Changes", bg="#1b294a", fg="white", font=("Arial", 12, "bold"), width=15, command=save_record).place(x=170, y=400)
    Button(window, text="Update Record", bg="#1b294a", fg="white", font=("Arial", 12, "bold"), width=20, command=update_record).place(x=350, y=360)

# Function to sort student records
def sort_student_records():
    window =  Toplevel(root)
    window.title("Sort student record")
    window.geometry("300x250")
    window.iconbitmap("Exercise 3/icon.ico")
    window.configure(bg='sky blue')
    
    students = students_record()

    Label(window, text="Sort by:", bg="sky blue", font=("Arial", 12)).place(x=50, y=50)
    sort_field = ttk.Combobox(window, values=["Number", "Name", "Course mark 1", "Course mark 2", "Course mark 3", "Exam", "Percentage", "Grade"])
    sort_field.place(x=130, y=53)

    Label(window, text="Order:", bg="sky blue", font=("Arial", 12)).place(x=50, y=100)
    sort_order = ttk.Combobox(window, values=["Ascending order", "Descending order"])
    sort_order.place(x=130, y=105)

    def perform_sort():
        field = sort_field.get()
        order = sort_order.get()

        if field == "" or order == "":
           messagebox.showerror("Error", "Please select both sort field and order")
           return
        
        reverse = True if order == "Descending order" else False

        field_map = {
           "Number": 0,
           "Name": 1,
           "Course mark 1": 2,
           "Course mark 2": 3,
           "Course mark 3": 4,
           "Exam": 5,
           "Percentage": 6,
            "Grade": 7
        }

        index = field_map[field]

        sorted_students = sorted(students, key=lambda s: s[index], reverse=reverse)

        record_window =  Toplevel(window)
        record_window.title("Update student record")
        record_window.geometry("950x400")
        record_window.iconbitmap("Exercise 3/icon.ico")
        record_window.configure(bg='sky blue')
        display_info(record_window, sorted_students)

    Button(window, text="Sort", bg="#1b294a", fg="white", font=("Arial", 12, "bold"), width=15, command=perform_sort).place(x=70, y=170)


# Create buttons for the menu
Button(root, text="View all student records", bg="#1b294a", fg="white", font=("Arial", 12, "bold"), width=30, height=2, command=all_student_records).place(x=80, y=160)
Button(root, text="View individual student record", bg="#1b294a", fg="white", font=("Arial", 12, "bold"), width=30, height=2, command=individual_student_records).place(x=80, y=220)
Button(root, text="Show student with highest total score", bg="#1b294a", fg="white", font=("Arial", 12, "bold"), width=30, height=2, command=highest_score).place(x=80, y=280)
Button(root, text="Show student with lowest total score", bg="#1b294a", fg="white", font=("Arial", 12, "bold"), width=30, height=2, command=lowest_score).place(x=80, y=340)
Button(root, text="Sort students records", bg="#1b294a", fg="white", font=("Arial", 12, "bold"), width=30, height=2, command=sort_student_records).place(x=80, y=400)
Button(root, text="Add a student record", bg="#1b294a", fg="white", font=("Arial", 12, "bold"), width=30, height=2, command=add_student_record).place(x=80, y=460)
Button(root, text="Delete a student record", bg="#1b294a", fg="white", font=("Arial", 12, "bold"), width=30, height=2, command=delete_student_record).place(x=80, y=520)
Button(root, text="Update a student record", bg="#1b294a", fg="white", font=("Arial", 12, "bold"), width=30, height=2, command=update_student_record).place(x=80, y=580)

root.mainloop()