#  thao tác với file 
#  đọc file 
file = open('CONTACT.in', 'r')
s = {}
for x in file :
	#  nếu kí tự cuối là kí tự xuong dòng
	if x[-1] == '\n' :
	     #  thực hiện cắt chuỗi từ đầu đến vị trí x.length()-2
            # ví dụ có chuỗi hello, thì x[0]=h,x[1]=e,x[2]=l,x[3]=l,x[4]=l, x[:-1]= hell
            # .strip() là loại bỏ khoảng trắng hai đầu 
		x = x[:-1]
		#  đảm bảo cá chuỗi k bị trùng lặp trong từ điển s 
	s[x.lower()] = 1
	# sawps xeeps 
s = sorted(s.keys())
for x in s :
	print(x)