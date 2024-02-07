from linked_list_queue import LLQueue
from bad_linked_list_queue import BadLLQueue
from time import process_time

if __name__ == '__main__':
    q = LLQueue()

    q_time1 = process_time()
    for i in range(50001):
        q.enqueue(i)
    q_time2 = process_time()

    q_time3 = process_time()
    for i in range(q.size):
        q.dequeue()
    q_time4 = process_time()

    bq = BadLLQueue()

    bq_time1= process_time()
    for i in range(50001):
        bq.enqueue(i)
    bq_time2 = process_time()

    bq_time3 = process_time()
    for i in range(bq.size):
        bq.dequeue()
    bq_time4 = process_time()

print('Elapsed time for enqueue good: ', q_time2 - q_time1  , 'sec')
print('Elapsed time for dequeue good: ', q_time4 - q_time3  , 'sec')
print('Elapsed time for enqueue bad:  ', bq_time2 - bq_time1, 'sec')
print('Elapsed time for dequeue bad:  ', bq_time4 - bq_time3, 'sec')

