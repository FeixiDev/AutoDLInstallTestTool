
class Date():
    def __init__(self):
        self.day=30
        self.month=9
        self.year=2022

class Student(Date): 
    def __init__(self):
        super().__init__()

    def danny(self):
        print("Hello Danny")
        
    def olivia(self):
        self.friend="Danny"
        print(self.friend)

    def print_date(self):
        # print(self.date.day)
        print(self.day)






if __name__=="__main__":
    student=Student()
    student.print_date()

    


