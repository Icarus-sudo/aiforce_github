import threading
import time

# 1. Define a function for the thread to execute
def worker_function(name, delay):
    print(f"Thread {name}: starting")
    time.sleep(delay)  # Simulate a time-consuming task
    print(f"Thread {name}: finishing")

if __name__ == "__main__":
    # 2. Create a Thread object
    # 'target' is the function, 'args' is a tuple of arguments
    my_thread = threading.Thread(target=worker_function, args=("Alpha", 2))

    # 3. Start the thread
    my_thread.start()

    print("Main: Thread is running, but I'm not blocked!")

    # 4. Wait for the thread to finish (optional but recommended)
    my_thread.join()
    
    print("Main: All done")