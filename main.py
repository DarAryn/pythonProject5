import random
import threading
from multiprocessing.pool import ThreadPool


def file (i):
  
  with open("%d.txt" % i, "w+") as file:
    x = random.randint(20,100)
    for _ in range(x):
      for _ in range(random.randint(5, 40)):
        file.write("%s" % random.randint(0, 9))
      file.write("\n")
def count (i):
  with open ("%d.txt" % i, "r+") as f:
    data = f.readlines()
  sum = 0
  for line in data:
    sum += int(line.strip())
  return sum

if __name__ == "__main__":
    threads = list()
    for index in range(1000):
        x = threading.Thread(target=file, args=(index,))
        threads.append(x)
        x.start()

    for thread in threads:
        thread.join()

    
    pool = ThreadPool(processes=1000)
    for index in range(1000):
        async_result = pool.apply_async(count, (index,))
        return_val = async_result.get()
        print(return_val)
