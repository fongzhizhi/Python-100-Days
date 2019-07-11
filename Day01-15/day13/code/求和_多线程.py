from time import time
from threading import Thread, Lock

total = 0

class AddThread(Thread):
	def __init__(self, start, end, lock):
		super().__init__()
		self._start = start
		self._end = end
		self._lock = lock

	def run(self):
		global total
		num = 0
		for x in range(self._start, self._end+1):
			num += x

		self._lock.acquire()
		try:
			total += num
		finally:
			self._lock.release()
		

def main():
	global total
	lock = Lock()
	start_time = time()

	maxnum = 100000000
	index = maxnum // 7
	start_num = 1
	end_num = index
	tlist = []
	while end_num <= maxnum:
		t = AddThread(start_num, end_num, lock)
		t.start()
		start_num = end_num+1
		end_num += index
		if end_num > maxnum and end_num < maxnum + index:
			end_num = maxnum
		tlist.append(t)

	for t in tlist:
		t.join()
	print(total)
	end_time = time()
	print('Execution time: %.3fs' % (end_time - start_time))

if __name__ == '__main__':
	main()