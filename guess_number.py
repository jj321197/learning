import random 
x = random.randint(1, 100)
print ('猜數字，範圍為1-100的整數\n')
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
