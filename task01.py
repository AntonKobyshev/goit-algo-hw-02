from queue import Queue
import time

class RequestProcessor:
    def __init__(self):
        self.request_queue = Queue()

    def generate_request(self, request):
        self.request_queue.put(request)

    def process_request(self):
        if not self.request_queue.empty():
            item = self.request_queue.get()
            print(f"Обробка завдання {item}")
            time.sleep(1)
            print(f"Завдання виконано {item}")
            time.sleep(1)
            self.request_queue.task_done()
        else:
            print("Черга порожня")

    def run(self, tasks_num):
        counter = 0
        while counter < tasks_num:
            counter += 1
            self.generate_request(counter)
            self.process_request()

if __name__ == "__main__":
    try:
        tasks_num = int(input("Введіть кількість завдань у черзі: "))
        processor = RequestProcessor()
        
        processor.run(tasks_num)

        print("Черга порожня. Програма завершена.")

    except KeyboardInterrupt as err:
        print(err)
    except ValueError as err:
        print(err)
