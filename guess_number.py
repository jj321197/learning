import random 
x = random.randint(1,100)
print ('猜數字，範圍為1-100的整數\n')
while True:
	y = input('請輸入數字: ')
	y = int(y)
	if y == x :
		print('你猜對了數字')
		print('答案是 ',x)
		break
	elif y>x :
		print('數字太大')
	elif y<x :
		print('數字太小')		