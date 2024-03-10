from threading import Thread
from time import sleep


def show_el(*my_list):
    for el in my_list:
        print(el)
        sleep(1)


nums_list = [i for i in range(1, 11)]
alph_list = [chr(i) for i in range(97, 123)]

thread_nums = Thread(target=show_el, args=nums_list)
thread_alph = Thread(target=show_el, args=alph_list)

thread_nums.start()
thread_alph.start()

thread_nums.join()
thread_alph.join()
