# POLYMORPHISM

class Department:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print(f"Department Name: {self.name}")

class Teacher(Department):
    def __init__(self, name, schedule_class):
        super().__init__(name)
        self.schedule_class = schedule_class

    def schedule_class(self):
        print(f"Schedule Class: {self.schedule_class}")

    def grade_student(self):
        print("Grading Students...")

    def display_name(self):
        super().display_name()
        print("Role: Teacher")

class Author(Department):
    def __init__(self, name):
        super().__init__(name)

    def write_article(self):
        print("Writing an Article...")

    def publish_blog(self):
        print("Publishing a Blog...")

class TeacherAuthor(Teacher, Author):
    def __init__(self, name, schedule_class):
        # Call the constructors of both Teacher and Author
        Teacher.__init__(self, name, schedule_class)
        Author.__init__(self, name)

    def display_name(self):
        super().display_name()  # Calls Teacher's display_name
        print("Role: Teacher and Author")

# Creating an instance of TeacherAuthor
teacher_author = TeacherAuthor("Dr. Smith", "Computer Science")

# Accessing methods
teacher_author.schedule_class()  # Schedule Class: Computer Science
teacher_author.grade_student()  # Grading Students...
teacher_author.write_article()  # Writing an Article...
teacher_author.publish_blog()  # Publishing a Blog...
teacher_author.display_name()  # Department Name: Computer Science, Role: Teacher and Author
