#增加範圍決定功能
print ('猜數字(整數)，範圍由你決定')               
import random 
maximum = input('請輸入最大值: ')
minimum = input('請輸入最小值: ')
maximum = int(maximum)
minimum = int(minimum)
x = random.randint(minimum, maximum)
z= 0
while True:
	z = z + 1
	y = input('請輸入數字:')
	y = int(y)
	if y == x :
		print('你猜對了數字')
		print('答案是 ',x)
		print('你共猜了', z,'次。')
		break
	elif y>x :
		print('數字太大')
	elif y<x :
		print('數字太小')		
	print('你現在猜了', z,'次')
