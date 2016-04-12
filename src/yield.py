
def ann2(path):
   print 'ann 2 was called: ' + path
   def inner_decorator(original_func):
      def new_func():
         original_func()
         print 'my func 2'
      return new_func
   return inner_decorator

#@ann1('path for ann 1')
@ann2('path for ann 2')
def nha():
   print 'nhaaaaaa'



def __more():
   for i in range(4,10):
      yield i

def f123_and_more():
    yield 1
    yield 2
    yield 3
    g = __more()
    for i in g:
      yield i


for item in f123_and_more():
    print item

