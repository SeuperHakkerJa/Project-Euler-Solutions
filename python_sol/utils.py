from multiprocessing import Process, Queue
import time

def timeout(seconds=60, report_time=False):
    def decorator(func):
        def wrapper(*args, **kwargs):
            def run_func(q):
                q.put(func(*args, **kwargs))
                
            queue = Queue()
            process = Process(target=run_func, args=(queue,))
            start_time = time.time()
            process.start()
            process.join(seconds)

            if process.is_alive():
                process.terminate()
                print(f"{func.__name__} terminated after {seconds} seconds.")
                return None

            result = queue.get() if not queue.empty() else None
            if report_time:
                print(f"{func.__name__} executed in {time.time() - start_time:.2f} seconds.")

            return result
        return wrapper
    return decorator


