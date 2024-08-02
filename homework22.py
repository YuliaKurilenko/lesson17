from time import sleep
from threading import Thread
from datetime import datetime
def wite_words(word_count, file_name):
    with open(file_name, 'a', encoding='UTF-8') as file:
        for i in range(word_count):
            file.write(f'Какое-то слово № {i} \n')
            sleep(0.1)
        print(f'Завершилась запись в файл {file.name}')
time_start = datetime.now()
wite_words(10, 'example1.txt')
wite_words(30, 'example2.txt')
wite_words(200, 'example3.txt')
wite_words(100, 'example4.txt')
time_end = datetime.now()
time_res = time_end - time_start
print(f'Работа {time_res} сек.')

start_ = datetime.now()
thr_first = Thread(target=wite_words, args = (10, 'example5.txt'))
thr_second = Thread(target=wite_words, args = (30, 'example6.txt'))
thr_third = Thread(target=wite_words, args = (200, 'example7.txt'))
thr_fourth = Thread(target=wite_words, args = (100, 'example8.txt'))
thr_first.start()
thr_second.start()
thr_third.start()
thr_fourth.start()

thr_first.join()
thr_second.join()
thr_third.join()
thr_fourth.join()
end = datetime.now()
time_res_ = end - start_
print(f'Работа {time_res_} сек.')