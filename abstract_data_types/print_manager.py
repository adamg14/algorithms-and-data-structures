from queue import Queue


class PrintManager:
    def __init__(self):
        self.print_queue = Queue()
    
    def queue_print_job(self, document):
        self.print_queue.enqueue(document)

    def run_print_job(self):
        while not self.print_queue.is_empty():
            print(self.print_queue.dequeue())
    
    