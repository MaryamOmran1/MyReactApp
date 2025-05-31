Students = { }

class Person():
    def __init__(self, name, age, gender, address, city):
        self.name = name
        self.age = age
        self.gender = gender
        self.address = address
        self.city = city

    def print_info(self):
        return {
            'name': self.name,
            'age' : self.age,
            'gender': self.gender,
            'address': self.address,
            'city': self.city
        }
    
class Student(Person):
    def __init__(self, name, age, gender, address, city, grade):
        super.__init__(name, age, gender, address, city)
        self.grade = grade

    def evaluation(self):
        print(self.grade)
        mean = sum(self.grade.values())/len(self.grade.values())
        return mean

j=0
while True:
    j+=1
    student_name = input(f'\n Enter the name of student: ')
    student_age = input(f'\n Enter the age of student: ')
    student_gender = input(f'\n Enter the gender of student: ')
    student_address = input(f'\n Enter the address of student: ')
    student_city = input(f'\n Enter the city of student: ')
    math = input(f'\n Enter the math degree of the student: ')
    science = input(f'\n Enter the science degree of the student: ')
    english = input(f'\n Enter the english degree of the student: ')

    Students[j] = Student(student_name, student_age, student_gender, student_address, student_city,
                          {'Math: ': float(math), 'Science: ': float(science), 'English': float(english)})
    Students[j].print_info()
    mean = Students[j].evaluation()
    print(f'Mean = {mean}')

    end = input('if you finish your input enter end: ')
    if end == 'end':
        break

    print('*'*50)