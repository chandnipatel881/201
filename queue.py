# Filename: queue.py
# Contains the code to implement a Queue

# queue()  
# creates a new queue 
# Inputs: None 
# Output: an empty queue
def queue(): 
    return [] 
 
# isEmpty(items)  
# checks to see if queue is empty 
# Inputs: items, a queue
# Output: True if queue is empty, False if not 
def isEmpty(items): 
    return len(items) == 0 

# enequeue(items, item) 
# pushes the item passed in onto the queue passed in, items.
# Inputs: items, a queue
#         item,  an item to put into queue 
# Output: None
def enqueue(items, item):
    items.append(item)

    
# dequeue(items) 
# removes an item from the queue passed in and returns it.
# Input: items, a queue
# Output: removed, the item removed from queue or 
#         "Empty queue" if the queue was empty
def dequeue(items):
    size = len(items)

    if size > 0:
        removed = items[0]
        del(items[0])
        return removed
    else:
        return "Empty queue"
         
def main():
    cars = queue()
    enqueue(cars, 'Audi')
    print 'putting Audi'
    enqueue(cars, 'Buick')
    print 'putting Buick'
    enqueue(cars, 'Chevy')
    print 'putting Chevy'
    print
 
    while not isEmpty(cars):
        print 'removing', dequeue(cars)
 
