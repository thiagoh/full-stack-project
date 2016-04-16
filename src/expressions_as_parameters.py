
class Age(object):

   def __init__(self):
      pass

   def __eq__(self, other):
      return ('one', other, 'third')

class Person(object):
   age = Age()

   def __init__(self):
      self.age=23

   def do_something(self, expr):
      return expr

p = Person()
print Person.age
print p.age
print p.do_something(Person.age == 'nha')
