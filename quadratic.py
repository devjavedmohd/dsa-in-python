'''
array = ['Javed', 'Bashkar', 'Faham', 'Izzhaan']

for x in array:
    for y in array:
        print('1', x, '2', y)#
'''
'''
def count_to(n):
  for i in range(n):
    yield i  # Yields a value without exiting the function

for x in count_to(5):
  print(x)  # Prints 0 to 4
'''

def decorator(func):
  def wrapper():
    print("Before function")
    func()
    print("After function")
  return wrapper

@decorator
def my_function():
      print("Inside function")

my_function()

