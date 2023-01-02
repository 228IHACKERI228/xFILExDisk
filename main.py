import yadisk
import threading
import time

y = yadisk.YaDisk(token="y0_AgAAAABcDgznAAj3ewAAAADYoZQyt6dkwG9kRoqyzC4c1QJQ2nh9iPU")

downloaded = False

def UploadFile(path):
	try:
		print('Загрузка файла...')
		x = y.upload(path, f"Загрузки/{path.split('/')[-1]}") #FROM PC to YDISK
		print('Файл загружен.')
		downloaded = True
	except Exception as e:
		print(e)
	return True




if __name__ == "__main__":
	print("\033[1m\033[91m{}".format(
		  "######################\n"+
		  "|~~~~~~~~~~~~~~~~~~~~|\n"+
		  "|       xFILEx       |\n"+
		  "|~~~~~~~~~~~~~~~~~~~~|\n"+
		  "######|by xBYTEx|#####\n"))
	while True:
		path = input("\033[93m{}".format('Путь к файлу: '))
		UploadFile(path)
