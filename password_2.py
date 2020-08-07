password = 'a123456'
a = 3
print('你總共有三次機會')
while a>0:
	a= a-1
	pwd = input('請輸入密碼: ')
	if pwd == password :
		print('密碼正確! ')
		break
	else :
		print ('密碼錯誤,你還有',a,'次機會。')
