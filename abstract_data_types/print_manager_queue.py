from print_manager import PrintManager

my_print_manager = PrintManager()
my_print_manager.queue_print_job("Document 1")
my_print_manager.queue_print_job("Document 2")
my_print_manager.run_print_job()
my_print_manager.queue_print_job("Document 3")
my_print_manager.queue_print_job("Document 4")
my_print_manager.queue_print_job("Document 5")
my_print_manager.queue_print_job("Document 6")
my_print_manager.run_print_job()
