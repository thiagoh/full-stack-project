
class controlled_exec:

   def __init__(self):
      print 'innited object'

   def __enter__(self):
      print 'entered in execution'

   def __exit__(self, *arg):
      print 'exited the execution'

thing = controlled_exec()

with thing as thing:
   print 'oh my god!'

print 'program finished'
