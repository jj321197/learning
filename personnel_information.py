import os           #引入os模組

data = []

#檢查並讀取檔案
if os.path.isfile('people.csv'):
	print('讀取到people.csv檔案')
	with open('people.csv', 'r',encoding='utf-8') as f:
		for p in f:
			if '姓名,年齡' in p:
				continue
			name, year = p.strip().split(',')
			data.append([name, year])
		print('檔案內資料:', data)
else:
	print('未讀取到people.csv檔案')


#輸入資料
while True:
	name = input('請輸入姓名: ')
	if name == 'q':
		break
	year = input('請輸入年齡(數字): ')
	data.append([name,year])
print(data)

#顯示資料
for i in data :
	print('姓名: ',i[0],',年齡: ',i[1],'歲')

#資料寫入檔案
with open ('people.csv', 'w',encoding='utf-8') as f:
	f.write('姓名,年齡\n')  
	for i in data:
		f.write(i[0] + ',' +  i[1] + '\n')
