password = 'a123456'
x=3
while True:
	ps = input('請輸入密碼: ')
	if ps == password:
		print('輸入正確')
		break
	else:
		x=x-1
		print('還剩', x, '次機會' )
		if x==0:
			break
			
		
	
		
		
		








	
