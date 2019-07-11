from time import time
from multiprocessing import Process, Queue

def add(start_num, end_num, queue):
	total = 0
	for x in range(start_num, end_num+1):
		total += x
	queue.put(total)

def main():
	start_time = time()
	queue = Queue()

	maxnum = 100000000
	index = maxnum // 7
	start_num = 1
	end_num = index
	process_list = []

	while end_num <= maxnum:
		p = Process(target=add, args=(start_num, end_num, queue))
		p.start()
		start_num = end_num+1
		end_num += index
		if end_num > maxnum and end_num < maxnum + index:
			end_num = maxnum
		process_list.append(p)
	for p in process_list:
		p.join()

	total = 0
	while not queue.empty():
		total += queue.get()
	print(total)
	end_time = time()
	print('Execution time: %.3fs' % (end_time - start_time))

if __name__ == '__main__':
	main()