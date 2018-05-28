#Pearl starts 2/16
from pearlglobalnums import*
from operator	import itemgetter
import re
from datetime import date

def symbol_title (quoteChunkList):
	opraList = quoteChunkList[opra].split(" ")
	symbol_name = opraList[3]
	
	return symbol_name


def stock_exp (quoteChunkList, fname):
	opraList = quoteChunkList[opra].split(" ")
	optTit = re.split('(\d+)',opraList[3])
	stock = optTit[0]
	expMonth = optTit[1]
	expDay =optTit[3]
	expYear = optTit[5]
	strike = int(optTit[7])/10000
	CorP = optTit[8]
	
	dateSplit = re.split('(\d+)',fname)
	
	curMonth = dateSplit[1]
	curDay = dateSplit[3]
	curYear = dateSplit[5]
	
	expDate = date((2000+int(expYear)), int(expMonth), (int(expDay)))
	curDate	= date(int(curYear), int(curMonth), int(curDay))
	d2x = expDate-curDate
	
	return d2x.days+1

def vwapCalc (bP, bS, aP, aS):
	if bP == 0:
		bP = .001
	if bS == 0:
		bS = 1
	if aS == 0:
		aS = 1
		
	vwap = float(bP)+((float(aP)-float(bP))*(float(bS)/(float(aS)+float(bS))))
	return vwap
	
def nbboCalc (quoteList):
	
	aseInfo = quoteList[ase].replace('/', ' ').split(" ")
	aseBidInfo = [aseInfo[underlying],aseInfo[bidSize],aseInfo[bidPrice]]
	aseAskInfo = [aseInfo[underlying],aseInfo[askSize],aseInfo[askPrice]]
	
	batInfo = quoteList[bat].replace('/', ' ').split(" ")
	batBidInfo = [batInfo[underlying],batInfo[bidSize],batInfo[bidPrice]]
	batAskInfo = [batInfo[underlying],batInfo[askSize],batInfo[askPrice]]
	
	bseInfo = quoteList[bse].replace('/', ' ').split(" ")
	bseBidInfo = [bseInfo[underlying],bseInfo[bidSize],bseInfo[bidPrice]]
	bseAskInfo = [bseInfo[underlying],bseInfo[askSize],bseInfo[askPrice]]
	
	cc2Info = quoteList[cc2].replace('/', ' ').split(" ")
	cc2BidInfo = [cc2Info[underlying],cc2Info[bidSize],cc2Info[bidPrice]]
	cc2AskInfo = [cc2Info[underlying],cc2Info[askSize],cc2Info[askPrice]]
	
	cboInfo = quoteList[cbo].replace('/', ' ').split(" ")
	cboBidInfo = [cboInfo[underlying],cboInfo[bidSize],cboInfo[bidPrice]]
	cboAskInfo = [cboInfo[underlying],cboInfo[askSize],cboInfo[askPrice]]
	
	iseInfo = quoteList[ise].replace('/', ' ').split(" ")
	iseBidInfo = [iseInfo[underlying],iseInfo[bidSize],iseInfo[bidPrice]]
	iseAskInfo = [iseInfo[underlying],iseInfo[askSize],iseInfo[askPrice]]
	
	ndqInfo = quoteList[ndq].replace('/', ' ').split(" ")
	ndqBidInfo = [ndqInfo[underlying],ndqInfo[bidSize],ndqInfo[bidPrice]]
	ndqAskInfo = [ndqInfo[underlying],ndqInfo[askSize],ndqInfo[askPrice]]
	
	nysInfo = quoteList[nys].replace('/', ' ').split(" ")
	nysBidInfo = [nysInfo[underlying],nysInfo[bidSize],nysInfo[bidPrice]]
	nysAskInfo = [nysInfo[underlying],nysInfo[askSize],nysInfo[askPrice]]
	
	phsInfo = quoteList[phs].replace('/', ' ').split(" ")
	phsBidInfo = [phsInfo[underlying],phsInfo[bidSize],phsInfo[bidPrice]]
	phsAskInfo = [phsInfo[underlying],phsInfo[askSize],phsInfo[askPrice]]
	
	miaInfo = quoteList[mia].replace('/', ' ').split(" ")
	miaBidInfo = [miaInfo[underlying],miaInfo[bidSize],miaInfo[bidPrice]]
	miaAskInfo = [miaInfo[underlying],miaInfo[askSize],miaInfo[askPrice]]
	
	tboInfo = quoteList[tbo].replace('/', ' ').split(" ")
	tboBidInfo = [tboInfo[underlying],tboInfo[bidSize],tboInfo[bidPrice]]
	tboAskInfo = [tboInfo[underlying],tboInfo[askSize],tboInfo[askPrice]]
	
	gemInfo = quoteList[gem].replace('/', ' ').split(" ")
	gemBidInfo = [gemInfo[underlying],gemInfo[bidSize],gemInfo[bidPrice]]
	gemAskInfo = [gemInfo[underlying],gemInfo[askSize],gemInfo[askPrice]]
	
	edxInfo = quoteList[edx].replace('/', ' ').split(" ")
	edxBidInfo = [edxInfo[underlying],edxInfo[bidSize],edxInfo[bidPrice]]
	edxAskInfo = [edxInfo[underlying],edxInfo[askSize],edxInfo[askPrice]]
	
	merInfo = quoteList[mer].replace('/', ' ').split(" ")
	merBidInfo = [merInfo[underlying],merInfo[bidSize],merInfo[bidPrice]]
	merAskInfo = [merInfo[underlying],merInfo[askSize],merInfo[askPrice]]
	
	mplInfo = quoteList[mpl].replace('/', ' ').split(" ")
	mplBidInfo = [mplInfo[underlying],mplInfo[bidSize],mplInfo[bidPrice]]
	mplAskInfo = [mplInfo[underlying],mplInfo[askSize],mplInfo[askPrice]]
	
	bidQuoteList = [aseBidInfo,batBidInfo,bseBidInfo,cc2BidInfo,cboBidInfo,iseBidInfo,ndqBidInfo,nysBidInfo,phsBidInfo,miaBidInfo,tboBidInfo,gemBidInfo,edxBidInfo,merBidInfo,mplBidInfo]
	askQuoteList = [aseAskInfo,batAskInfo,bseAskInfo,cc2AskInfo,cboAskInfo,iseAskInfo,ndqAskInfo,nysAskInfo,phsAskInfo,miaAskInfo,tboAskInfo,gemAskInfo,edxAskInfo,merAskInfo,mplAskInfo]
	bidSortedList = sorted(bidQuoteList, key=itemgetter(2))
	bidSortedList.reverse()
	askSortedList = sorted(askQuoteList, key=itemgetter(1))
	
	nbboAskExchs = 0
	nbboAskSize = 0
	nbboBidExchs = 0
	nbboBidSize = 0
			
	for bitem in bidSortedList:
		if bitem[2] == bidSortedList[0][2]:
			nbboBidExchs +=1
			nbboBidSize += int(bitem[1])
			
	for item in askSortedList:
		if item[1] == askSortedList[0][1]:
			nbboAskExchs +=1
			nbboAskSize += int(item[2])
	
	fin_vwap = vwapCalc(float(bidSortedList[0][2]),nbboBidSize,float(askSortedList[0][1]),nbboAskSize)
	
	nbbo_calc_final_list = []
	nbbo_calc_final_list.append(bidSortedList[0][2])
	nbbo_calc_final_list.append(nbboBidExchs)
	nbbo_calc_final_list.append(nbboBidSize)
	nbbo_calc_final_list.append(askSortedList[0][1])
	nbbo_calc_final_list.append(nbboAskExchs)
	nbbo_calc_final_list.append(nbboAskSize)
	nbbo_calc_final_list.append(fin_vwap)
	
	return nbbo_calc_final_list
	
def OrderSentInfo(quoteChunkList):
	ordSentInfo = quoteChunkList[order].split(" ")
	price_sent = ordSentInfo[7]
	side_sent = ordSentInfo[9]
	size_sent = ordSentInfo[3]
	size_filled = ordSentInfo[5]
	
	perc_filled = float(size_filled)/float(size_sent)
	#if int(size_filled) > 0:
	#	perc_filled = float(size_sent)/float(size_filled)
	#else:
	#	perc_filled = 0
	
	order_sent_final_list = []
	order_sent_final_list.append(price_sent)
	order_sent_final_list.append(side_sent)
	order_sent_final_list.append(size_sent)
	order_sent_final_list.append(size_filled)
	order_sent_final_list.append(perc_filled)
	
	return order_sent_final_list
	
