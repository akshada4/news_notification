import time
from news import stories
from disp_notification import display_notification



i=1
new=stories()
print('firs \n',new)
print('+++++++++++++++++++++++++++')


while i:
	newsitems=stories()
	print('news\n',newsitems)
	print('===========================================')
	new=new[0:101]	
	print('secondf',new)
	print('********************************************')
	diff=[i for i in newsitems if i not in new]
	print(diff)
	j=0
	for news in diff:
		display_notification(news)
		new.insert(j,news)
		j=j+1
		time.sleep(5)
	time.sleep(120)
