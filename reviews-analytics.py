#留言分析程式
data = []         #建立名為data的空清單
count = 0         #計數用變數
with open('reviews.txt', 'r') as f:        #載入文字txt檔案  ，取名為f
	for line in f:                    #for迴圈，逐個將f檔案內各串取出，逐個皆命名為line
		data.append(line)          #用append函式將line值輸入data清單內
		count += 1                 #每次迴圈時變數countr加1 。 等同: count = count + 1
		if count % 1000 == 0:       #如果 變數count 除1000之餘數 等於0成立
			print(len(data))        #則印出data清單之長度(清單內數量)

print('資料讀取完畢，總共有 ',len(data),'筆資料。')		#迴圈完成後印出data清單總長度(數量)
sum = 0                                 #建立變數sum ，作為字串長度總和用
for d in data:               #for迴圈。 自data清單內逐項取出，命名為d。
	sum += len(d)          #迴圈內加總每次之d字串長度。  sum = sum +len(d)
	a_sum = sum /len(data)  #總和除以data清單內之總數
print('平均長度是', a_sum)   #印出reviews平均之字數長度
