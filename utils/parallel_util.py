from threading import Thread
from time import sleep


def run_in_parallel(function, arg_list, thread_count=10, update_callback=None):
    result_list = [None] * len(arg_list)
    threads = []
    for parallel_index in range(thread_count):
        thread = Thread(target=_run, args=(function, arg_list, result_list, parallel_index, thread_count, update_callback))
        thread.start()
        threads.append(thread)

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    return result_list


def _run(function, arg_list, result_list, parallel_index, parallel_count, update_callback):
    for i in range(0, len(arg_list), parallel_count):
        idx = i + parallel_index
        result = function(*arg_list[idx])
        result_list[idx] = result
        if update_callback:
            update_callback()
        # print(f"Thread #{parallel_index} operation #{idx} complete!\n", end="")


if __name__ == "__main__":
    def plus_one(original):
        sleep(1)
        return original + 1


    results = run_in_parallel(plus_one, [[a] for a in range(20)])
    print(results)
