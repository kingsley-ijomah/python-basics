class Human:
  def kind(self):
    print('Homo Sapien')

class Person:
  def name(self):
    print('Kingsley Ijomah')

class Student(Person, Human):
  pass


x = Student()
x.kind()
x.name()