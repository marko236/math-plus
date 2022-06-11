"""

mathplus is a free and open source python module.
It is licensed under the GNU GPLv3, 

"""

from math import *
def sqrt(num):
	return pow(num,2)

def divide(num,div): # checks if the number is divideable by X(div)
	if num %div == 0:
		print('Number ',num,' is divideable by ',div)
	else:
		print('Number ',num,' is not divideable by ',div)

def isdiv(n,d):
	if n%d==0:
		return True
	else:
		return False
def numbet(star,end): # counts all numbers between X(star) and Y(end)
	endd=end+1
	i=0
	for num in range(star,endd):
		i=i+1
	return i

def numbetEVEN(star,end):# counts even numbers between X(star) and Y(end)
	endd=end+1
	i=0
	for num in range(star,endd):
		if num %2 == 0:
			i=i+1
		else:
			pass
	return i

def numbetODD(star,end): # counts odd numbers between X(star) and Y(end)
	i=0
	endd=end+1
	for num in range(star,endd):
		if num %2 != 0:
			i=i+1
		else:
			pass
	return i

def sd(num): # gets the smallest divider
	for i in range(2,3000000): #looks for the divider from 2 to 3000000 - which is more than enough for nearly all numbers
		divv=isdiv(num,i)
		if divv==True:
			if num==i:
				print('Simple number. Undividable.')
				break
			else:
				print('Smallest divider:')
				print(str(int(num))+' | '+str(i))
				num=num/i
				print(int(num))
				break
		else:
			pass

def sc(num,nm): # gets the smallest condensor of two numbers
	NoT=50000000
	for i in range(1,NoT): # looks for it from 1 to number of tries(NoT) - default NoT is 50000000 - more than enough for your math homework
		dv=isdiv(i,nm)
		dvv=isdiv(i,num)
		if dv==True and dvv==True:
			return i
			break
		else:
			i+=1
	if i>=NoT:
		print('Smallest condensor of '+str(num)+' and '+str(nm)+' is not between 1 and '+str(NoT))
	else:
		pass

def sct(num,nm,nmm): # gets the smallest condensor of three numbers
	NoT=50000000
	for i in range(1,NoT): # looks for it from 1 to number of tries(NoT) - default NoT is 50000000 - more than enough for your math homework
		dv=isdiv(i,nm)
		dvv=isdiv(i,num)
		ddv=isdiv(i,nmm)
		if dv==True and dvv==True and ddv==True:
			return i
			break
		else:
			i+=1
	if i>=NoT:
		print('Smallest condensor of '+str(nmm)+', '+str(num)+' and '+str(nm)+' is not between 1 and '+str(NoT))
	else:
		pass

def sdt(num,nm): # gets the smallest divider of two numbers
	if num>nm: x=num
	else: x=nm
	for i in range(2,x+1):
		divv=isdiv(num,i)
		dvv=isdiv(nm,i)
		nmnm=False
		if divv==True and dvv==True:
			print('Smallest divider:')
			print(str(int(num)),str(int(nm))+' | '+str(i))
			print(int(num/i),int(nm/i))
			nmnm=True
			break
		else:
			if i>=num or i>=nm or i>=nnm:
				break
			else:
				pass
	if nmnm==False:
		print('No divider found')

def sdtr(num,nm,nnm): # gets the smallest divider of three numbers
	for i in range(2,3000000): #looks for the divider from 2 to 3000000
		divv=isdiv(num,i)
		dvv=isdiv(nm,i)
		ddv=isdiv(nnm,i)
		nmnm=False
		if divv==True and dvv==True and ddv==True:
				print('Smallest divider:')
				print(str(num),str(nm),str(nnm)+' | '+str(i))
				print(str(num/i),str(nm/i),str(nnm/i))
				nmnm=True
				break
		else:
			if i>=num or i>=nm or i>=nnm:
				break
			else:
				pass
	if nmnm==False:
		print('No divider found')

def cntP(num,procent): # gets part of number and procent
	prt=(procent/100)*num
	print(str(procent)+'% of '+str(num)+' is '+str(prt))
def cntPR(num,part): # gets procent of number and part
	proc=(part/num)*100
	print(str(part)+' of '+str(num)+' is '+str(proc)+'%')
def cntN(procent,part): # gets number out of part and procent
	num=part/procent*100
	print('If '+str(procent)+'% of number is '+str(part)+', then the number is '+str((part/(procent)*100)))

def getH(cat,cath): # gets the hypothenusis of a right-angled triangle by Pythagorus' theorem
	hyp=sqrt((cath*cath)+(cat*cat)) # double brackets aren't necessary, by the way
	print("Hypothenusis of the given triangle is: "+str(hyp))
def getC(hyp,cath): # same as one above, just reverse
	cat=sqrt((hyp*hyp)-(cath*cath))
	print("The second cathete of the given triangle is "+str(cat))

def root(num,pw): # gets Nth root of a number
	return pow(num,1/pw)
def numcomb(charpos,charnum): #essentially just x^y
	return charpos**charnum
if __name__ == '__main__':
	print("Function summary:")
	print("divide(divided,divider) - checks if the dividing result gives an intreger")
	print("numbet(start,end) - prints numbers between $start and $end")
	print("numbetODD(start,end);numbetEVEN(start,end) - self-explanatory")
	print('sd(number) - smallest divider of number')
	print("sdt(num1,num2) - smallest divider of 2 numbers")
	print("sdtr(num1,num2,num3) - smallest divider of 3 numbers")
	print('sc(number1,number2) - smallest condensor of two numbers')
	print('sct(number1,number2,number3) - smallest condensor of 3 numbers')
	print('cntPR(number,part) - procent from part and number')
	print("""cntN(procent,part) - number from procent and part
		cntP(number,procent) - part from number and procent
		getH(cathete1,cathete2) - hypothenusys from 2 cathetes
		getC(hypothenusys,cathete2) - cathete from hypothenusys and other cathete
        root(number,power) - gets Nth root of a number(ex. root(27,3) - 3; root(81,2) - 9)
	numcomb(charpos,charnum) - get number of possible combinations of X repeatable characters written Y times
        """)
