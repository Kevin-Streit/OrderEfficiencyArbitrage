#Pearl starts 2/16
from pearlglobalnums import*
from PearlRealTheoData_Functions import *
import csv


testnum = 1
newstart = "EntryBegin " + str(testnum) + ' - '
newend = "EntryEnd " + str(testnum) + ' - '
copy = False
testChunk=[]
finalData=[]
titles = ["Symbol", "Days2Ex" , "Nbbo Bid Price", "Bid Exchanges", "Bid Size", "Nbbo Ask Price", "Ask Exchanges", "Ask Size", "VWAP", "Order Price", "Order Side", "Order Size", "Amount Filled", "Perc Fille"]




openCSV = open('MarketOrderDataMarMay.csv', 'wb')
CSVuse = csv.writer(openCSV)
for m in range(2,6,1):
	if m ==2: #2 = Feb
		for i in range(16,29,1):#starting at 16 because that's when MPL starts

			testnum = 1
			newstart = "EntryBegin " + str(testnum) + ' - '
			newend = "EntryEnd " + str(testnum) + ' - '
			
			if ( i == 18 or i == 19 or i == 20 or i == 25 or i == 26):
				print i#these or the weeked dates in feb so do nothing
			else:
				if i < 10:
					fileName = "MarketOrderRecorder_ 2_ %d_2017.txt" %i	
				else:
					fileName = "MarketOrderRecorder_ 2_%d_2017.txt" %i
				openFile = open(fileName)
				printReader = openFile.readlines()
				print fileName
				for line in printReader:
					line = line.strip()
					if line.startswith(newstart):
						copy = True
						testChunk.append(line)
					elif line.startswith(newend):
						copy = False
						optOpra = symbol_title(testChunk)
						finalData.append(optOpra)
						
						dayToExp = stock_exp(testChunk, fileName)
						finalData.append(dayToExp)
						
						nbboList = nbboCalc(testChunk)
						for item in nbboList:
							finalData.append(item)
							
						OrderSentList = OrderSentInfo(testChunk)
						for item in OrderSentList:
							finalData.append(item)
						
						#print finalData
						#if testnum ==1:
							#CSVuse.writerow(titles)
						CSVuse.writerow(finalData)
						
						testnum +=1
						newstart = "EntryBegin " + str(testnum) + ' - '
						newend = "EntryEnd " + str(testnum) + ' - '
						testChunk=[]
						finalData=[]
						
						
					elif copy == True:
						testChunk.append(line)
			
			openFile.close()
	if m ==3: #3=March
		for i in range(1,32,1):

			testnum = 1
			newstart = "EntryBegin " + str(testnum) + ' - '
			newend = "EntryEnd " + str(testnum) + ' - '
			
			if ( i == 4 or i == 5 or i == 11 or i == 12 or i == 18 or i == 19 
				or i == 25 or i == 26):
				print i#these or the weeked dates in march so do nothing
			else:
				if i < 10:
					fileName = "MarketOrderRecorder_ 3_ %d_2017.txt" %i	
				else:
					fileName = "MarketOrderRecorder_ 3_%d_2017.txt" %i
				openFile = open(fileName)
				printReader = openFile.readlines()
				print fileName
				for line in printReader:
					line = line.strip()
					if line.startswith(newstart):
						copy = True
						testChunk.append(line)
					elif line.startswith(newend):
						copy = False
						optOpra = symbol_title(testChunk)
						finalData.append(optOpra)
						
						dayToExp = stock_exp(testChunk, fileName)
						finalData.append(dayToExp)
						
						nbboList = nbboCalc(testChunk)
						for item in nbboList:
							finalData.append(item)
							
						OrderSentList = OrderSentInfo(testChunk)
						for item in OrderSentList:
							finalData.append(item)
						
						#print finalData
						#if testnum ==1:
							#CSVuse.writerow(titles)
						CSVuse.writerow(finalData)
						
						testnum +=1
						newstart = "EntryBegin " + str(testnum) + ' - '
						newend = "EntryEnd " + str(testnum) + ' - '
						testChunk=[]
						finalData=[]
						
						
					elif copy == True:
						testChunk.append(line)
			
			openFile.close()
	if m ==4: #4=April
		for i in range(1,31,1):

			testnum = 1
			newstart = "EntryBegin " + str(testnum) + ' - '
			newend = "EntryEnd " + str(testnum) + ' - '
			
			if ( i == 1 or i == 2 or i == 8 or i == 9 or i == 14 or i == 15 
				or i == 16 or i == 22 or i == 23 or i == 29 or i == 30):
				print i#these or the weeked dates in april so do nothing
			else:
				if i < 10:
					fileName = "MarketOrderRecorder_ 4_ %d_2017.txt" %i	
				else:
					fileName = "MarketOrderRecorder_ 4_%d_2017.txt" %i
				openFile = open(fileName)
				printReader = openFile.readlines()
				print fileName
				for line in printReader:
					line = line.strip()
					if line.startswith(newstart):
						copy = True
						testChunk.append(line)
					elif line.startswith(newend):
						copy = False
						optOpra = symbol_title(testChunk)
						finalData.append(optOpra)
						
						dayToExp = stock_exp(testChunk, fileName)
						finalData.append(dayToExp)
						
						nbboList = nbboCalc(testChunk)
						for item in nbboList:
							finalData.append(item)
							
						OrderSentList = OrderSentInfo(testChunk)
						for item in OrderSentList:
							finalData.append(item)
						
						#print finalData
						#if testnum ==1:
							#CSVuse.writerow(titles)
						CSVuse.writerow(finalData)
						
						testnum +=1
						newstart = "EntryBegin " + str(testnum) + ' - '
						newend = "EntryEnd " + str(testnum) + ' - '
						testChunk=[]
						finalData=[]
						
						
					elif copy == True:
						testChunk.append(line)
			
			openFile.close()
	if m ==5: #5=may
		for i in range(1,32,1):

			testnum = 1
			newstart = "EntryBegin " + str(testnum) + ' - '
			newend = "EntryEnd " + str(testnum) + ' - '
			
			if ( i == 6 or i == 7 or i == 13 or i == 14 or i == 20 or i == 21 
				or i == 22 or i == 27 or i == 28 or i == 29):
				print i#these or the weeked dates in may so do nothing
			else:
				if i < 10:
					fileName = "MarketOrderRecorder_ 5_ %d_2017.txt" %i	
				else:
					fileName = "MarketOrderRecorder_ 5_%d_2017.txt" %i
				openFile = open(fileName)
				printReader = openFile.readlines()
				print fileName
				for line in printReader:
					line = line.strip()
					if line.startswith(newstart):
						copy = True
						testChunk.append(line)
					elif line.startswith(newend):
						copy = False
						optOpra = symbol_title(testChunk)
						finalData.append(optOpra)
						
						dayToExp = stock_exp(testChunk, fileName)
						finalData.append(dayToExp)
						
						nbboList = nbboCalc(testChunk)
						for item in nbboList:
							finalData.append(item)
							
						OrderSentList = OrderSentInfo(testChunk)
						for item in OrderSentList:
							finalData.append(item)
						
						#print finalData
						#if testnum ==1:
							#CSVuse.writerow(titles)
						CSVuse.writerow(finalData)
						
						testnum +=1
						newstart = "EntryBegin " + str(testnum) + ' - '
						newend = "EntryEnd " + str(testnum) + ' - '
						testChunk=[]
						finalData=[]
						
						
					elif copy == True:
						testChunk.append(line)
			
			openFile.close()

openCSV.close()
		






