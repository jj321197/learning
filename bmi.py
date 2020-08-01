#建立一個BMI計算程式BMI = 體重(公斤) / 身高^2(公尺)
#計算出BMI數值，並顯示文字說明
height = input('你的身高是幾公分? ')
weight = input('你的體重是幾公斤? ')
height = int(height)
weight = int(weight)
bmi = weight / ( height /100 )**2 
print ('你的BMI數值為 =',bmi)
if bmi <18.5 :
	print ('你的體重過輕')
elif bmi >=18.5 and bmi < 24 :
    print ('你的身材正常')
elif bmi >=24 and bmi < 27  :
	print ('你的體重過重喔')
elif bmi >= 27 and bmi < 30 :
	print ('你的身材輕度肥胖')
elif bmi >= 30 and bmi <35 :
    print ('你的身材中度肥胖 ')
else :
    print ('你的身材重度肥胖')
