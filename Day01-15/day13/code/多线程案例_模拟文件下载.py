import tkinter
from time import sleep, time
from random import randint
from threading import Thread, Lock

class download_file(Thread):
	def __init__(self, t):
		super().__init__()
		self._time = t

	def run(self):
		sleep(self._time)
		

def main():
	names = ['jinpingmei.gif', 'lunyu.txt', 'daxue.pdf'] #要下载的文件
	lock = Lock()

	def download_all():
		start = time()
		label['text'] = ''
		threadlist = []
		for name in names:
			lock.acquire()
			try:
				t = randint(1, 3)
				thread = download_file(t)
				threadlist.append(thread)
				thread.start()
				msg = '\n%s下载完成，用时【%d】秒' % (name, t)
				label['text'] += msg
			finally:
				lock.release()

		for thread in threadlist:
			thread.join()
		end = time()
		msg = '\n全部下载完成，总共用时【%.2f】秒' % (end-start)
		label['text'] += msg
		btn['text'] = 'Download Again'
			

	#顶层窗口
	tk = tkinter.Tk()
	tk.geometry('240x160')
	tk.title('download')
	#GUI
	frame = tkinter.Frame(tk)
	frame.pack(side='bottom')
	#按钮
	btn = tkinter.Button(frame)
	btn['text'] = 'Download All'
	btn['command'] = download_all
	btn.pack(side='bottom')
	#显示标签
	label = tkinter.Label(tk, fg='red')
	label['text'] += '\n'.join(names)
	label.pack(expand=1)

	#开启主事件循环
	tkinter.mainloop()

if __name__ == '__main__':
	main()