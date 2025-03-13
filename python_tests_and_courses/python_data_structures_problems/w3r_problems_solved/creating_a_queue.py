def create_queue_fifo(numbers):
    """
    Create a queue from the given list of numbers.
    The queue should be implemented using the method FIFO.
    """
    
    queue = []
    for num in numbers:
        queue.append(num)
    
    # queue.pop()
    
    return queue

numbers = [0, 1, 2, 3, 4]

queue = create_queue_fifo(numbers)

print("Members of the queue: ", queue)
size_of_queue = len(queue)

print("Size of the queue: ", size_of_queue)
    
def create_queue_lifo(numbers):
    """
    Create a queue from the given list of numbers.
    The queue should be implemented using the method LIFO.
    """
    
    queue = []
    for num in numbers:
        queue.insert(0, num)
    
    return queue

numbers = [0, 1, 2, 3, 4]

queue = create_queue_lifo(numbers)

print("Members of the queue: ", queue)
size_of_queue = len(queue)

print("Size of the queue: ", size_of_queue)
    
    