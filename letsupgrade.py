import random
statment1='Today will be a licky day'
statment2='You will meet someone new and interesting'
statment3='Watch out for obstacles in your path'
statment=random.randrange(3)+1
if(statment==1):
	print(statment1)
elif(statment==2):
	print(statment2)
elif(statment==3):
	print(statment3)