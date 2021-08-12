def ok(callback):
	x=8
	b=10
	c=x*b
	callback(c)

ok(lambda c:print(c));

def param(callback):
	user='Selasi'
	age=22
	school='Labone Senior High'
	callback({'name':user,'age':age,'school':school})


param(lambda dic:print(dic['name'],dic['age'],dic['school']))