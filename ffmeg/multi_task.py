import twee
from dataclasses import dataclass, field
import queue
import threading
import multiprocessing

#twee.twitter_data('Nike')

def ThreadHw4():
  while True:
    item = q.get()
    if item is None: break
    twee.twitter_data(item)
    print('-----------------Thread '+str(item)+' Done-------------------------')
    q.task_done()

q = queue.Queue()
threads = []
for i in range(2):
  t = threading.Thread(target = ThreadHw4)
  t.start()
  threads.append(t)

for item in ['Nike','Trump','CNN','HBO']:
  q.put(item)

q.join()

for i in range(2):
  q.put(None)
for t in threads:
  t.join()
