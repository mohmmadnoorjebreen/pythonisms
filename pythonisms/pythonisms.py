from functools import wraps
from time import sleep


def f1(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        sleep(3)
        return func(*args, **kwargs)

    return wrapper

def f2(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        orig_val = func(*args, **kwargs)
        return f'{orig_val}=>this all data'

    return wrapper



class Node:
    def __init__(self,data=''):
        self.data = data
        self.next = None

class Linked_List:
    def __init__(self):
        self.head= None

    def insert(self,data):
        node = Node(data)
        if self.head:
            node.next = self.head

        self.head = node
    def __contains__(self,data):
        for value in self:
           if value == data:
                return True
        return False

    def __iter__(self):
        current_item = self.head
        while current_item:
            val = current_item.data
            yield val
            current_item = current_item.next
    @f2
    @f1        
    def __str__(self):
        string = ''
        currants = self.head

        for  currants in self:
            string += f'{str(currants)}->'

        string += 'NULL'
        return string


if __name__ == "__main__":
    print('s')
    print('work')
    x = Linked_List()
    x.insert(7)
    x.insert(9)
    x.insert(10)


    print(str(x))
  
    print(10 in x)    



    
    
    
    