class Queue:
    def __init__(self):
        self.queue = []
    

    def enqueue(self, element):
        self.queue.append(element)
    

    def dequeue(self):
        if len(self.queue) == 0:
            return "queue is currently empty"
        else:
            return self.queue.pop(0)
        

    def read(self):
        if len(self.queue) == 0:
            return "queue is currently empty"
        else:
            return self.queue[0]