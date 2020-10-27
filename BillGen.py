#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 13:33:23 2020
@author: dell
Version: 0.1
"""
# ============================================================================ #
## import and declare ##
import datetime
itemname=[]
amount=[]
qty=[]
rate=[]
ch='y'

class bcolors:
    HEADER = '\033[95m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

# ============================================================================ #
## Name and date ##

d_date = datetime.datetime.now()
reg_format_date = d_date.strftime(bcolors.HEADER + bcolors.BOLD + "  %d-%m-%Y\t\t\t  Bill Generator\t\t\t  %I:%M:%S %p" + bcolors.ENDC)
print ('########################################################################################')
print (reg_format_date)
print ('########################################################################################')

# ============================================================================ #
## Some functions ##

def show():
	print(('\nItemname\t\t\t\t'+'\tRate\t'+'Qty\t'+'Amount'))
	for i in range(0,len(itemname)):
		print(('{0}\t\t\t\t\t{1}\t{2}\t{3}'.format(itemname[i],rate[i],qty[i],amount[i])))
	print(('\nTotal amount:\t\t\t\t\t\t\t{0}'.format(sum(amount))))

def errorhand(tempvalue):
	try:
		tempvalue=float(input('raw_input again: '))
	except:
		errorhand(tempvalue)
	return tempvalue


while ch=='y' or ch=='Y':
	tempitemname=input('\nEnter item name (max 15 character): ')
	tempitemname=tempitemname[0:15]
	if len(tempitemname)<8:
		tempitemname=tempitemname+'        '
	itemname.append(tempitemname)
	tempamount=0
	tempqty=0
	tempa=0
	tempq=0

	try:
		tempamount=float(input('Enter rate: '))
		tempa=tempamount
	except:
		tempa=errorhand(tempamount)

	try:
		tempqty=input('Enter quantity: ')
		tempq=float(tempqty)
	except:
		tempq=float(errorhand(tempqty))

	amount.append(tempq*tempa)
	qty.append(tempq)
	rate.append(tempa)
	show()
	ch=input('\nDo you want to add more(y for yes and n for no): ')


print ('\n\n#######################################################################################\n')
filename=input('Enter filename to save: ')
fob=open(filename+'.txt','w+')
fob.write('########################################################################################\n')
filedatetime=d_date.strftime("  %d-%m-%Y\t\t\t\t\t  Bill Generator\t\t\t\t\t  %I:%M:%S %p")
fob.write(filedatetime)
fob.write('\n########################################################################################\n\n')
fob.write('\t\t\tItemname\t\t\t\t'+'Rate\t'+'Qty\t'+'Amount\n')
for i in range(0,len(itemname)):
	fob.write('\n\t\t\t{0}\t\t\t\t{1}\t{2}\t{3}'.format(itemname[i],rate[i],qty[i],amount[i]))
fob.write('\n-----------------------------------------------------------------------------------------------------------------------')
fob.write('\n\t\t\tTotal amount:\t\t\t\t\t\t{0} Rs'.format(sum(amount)))
fob.write('\n-----------------------------------------------------------------------------------------------------------------------')
fob.close()

# ============================================================================ #
## Write in text and Excel ##

def excelsave():

	# import xlsxwriter module 
	import xlsxwriter 
	  
	workbook = xlsxwriter.Workbook(filename+'.xlsx') 
	worksheet = workbook.add_worksheet() 


	onlydate=d_date.strftime("%d-%m-%Y")
	onlytime=d_date.strftime("%I:%M:%S %p")

	worksheet.write(0,4, onlydate) 
	worksheet.write(0,10,onlytime) 
	worksheet.write(1,7, 'Bill     Generator')

	worksheet.write(4,4, 'Itemname')
	worksheet.write(4,6, 'Rate')
	worksheet.write(4,8, 'Qty')
	worksheet.write(4,10, 'Amount')

	for i in range(0,len(itemname)):
		temp=0
		worksheet.write(i+6,4,itemname[i])
		worksheet.write(i+6,6, rate[i])
		worksheet.write(i+6,8, qty[i])
		worksheet.write(i+6,10, amount[i])
		temp=i+6
	temp=temp+2
	worksheet.write(temp,4, 'Total Amount')
	#worksheet.write(temp,5, 'Amount')

	worksheet.write(temp,10, sum(amount))
	worksheet.write(temp,11, 'Rs')

	try:
		workbook.close()
	except(IOError):
		print('File Already Opened. Please Close and try again.')
excelsave()

print("Bill Created successfully in a text and Excel file "+filename+".txt and "+filename+".xlsx")
