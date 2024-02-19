"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
    if(x <= 1):
      return x

    else:
      return foo(x-1) + foo(x-2)

  
    #pass

def longest_run(mylist, key):
    counter = 0
    max = counter
  
    for i in range(len(mylist)):
      if mylist[i] == key:
        counter += 1
        if counter > max:
          max = counter
          
      elif mylist[i] != key:
        counter = 0

    return max
      
    #pass


class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    

def to_value(v):
    """
    if it is a Result object, return longest_size.
    else return v
    """
    if type(v) == Result:
        return v.longest_size
    else:
        return int(v)
        
def longest_run_recursive(mylist, key):
    #if list is empty, return 0
    if len(mylist) == 0:
      return Result(0,0,0,False)

    #if list has one element, check if element is key
    if len(mylist) == 1:
      if (mylist[0] == key):
        return Result(1,1,1,True)
      else:
        return Result(0,0,0,False)

    else:

      #split list to get middle element
      mid = len(mylist) // 2 
      left = longest_run_recursive(mylist[:mid], key) 
      right = longest_run_recursive(mylist[mid:], key)
  
      # set range to true or false- will be false if either side is not the key or true if both sides are entirely the key
      is_entire_range = left.is_entire_range and right.is_entire_range
      left_size = left.left_size
      right_size = right.right_size
      longest_size = max(left.longest_size, right.longest_size, left.right_size + right.left_size)

      
      return Result(left_size, right_size, longest_size, is_entire_range)
  
    
      


print(to_value(longest_run_recursive([12,12,12,8,12,12,0,12,12,12,12], 12)))
  



  
  #  pass



