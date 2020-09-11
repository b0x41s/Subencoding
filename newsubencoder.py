#!/usr/bin/env python

shellcode = r"\x66\xe7\xca\xe7\x0f\xe7\x52\x75\x02\xff\xcd\xff\x3c\x05\x5a\xe7\xef\xb8\x77\x30\x30\x74\x8b\xfa\xaf\x75\xea\xaf\x75\xe7\xff\xe7"

if len(shellcode) /4 % 4 != 0:
	print "Shellcode not divisible by 4"
	print "Pad with nops" # todo 

def remove(shellcode):
	shellcode = shellcode.replace("\\x","")
	shellcode = shellcode.replace("'","")
	shellcode = shellcode.replace('"',"")
	print("Hex string   = " + shellcode)
	return shellcode

def reverse(hexstring):
	hexbyte1 = hexstring[0] + hexstring[1]
	hexbyte2 = hexstring[2] + hexstring[3]
	hexbyte3 = hexstring[4] + hexstring[5]
	hexbyte4 = hexstring[6] + hexstring[7]
	newhex = hexbyte4 + hexbyte3 + hexbyte2 + hexbyte1
	print("Hex reversed = " + newhex)
	return newhex

def split(hexstring):
	hexbyte1 = hexstring[0] + hexstring[1]
	hexbyte2 = hexstring[2] + hexstring[3]
	hexbyte3 = hexstring[4] + hexstring[5]
	hexbyte4 = hexstring[6] + hexstring[7]
	hexbyte5 = hexstring[8] + hexstring[9]
	return hexbyte2, hexbyte3, hexbyte4, hexbyte5

def calc(hexvalue1,hexvalue2):
	revhex = hexvalue1
	print "calculating " + hexvalue1 + " " + hexvalue2
	if hexvalue2 == "wrap":
		intofhex = int(revhex, 16) # Make int to be able to calculate
		zeroMin = 0-intofhex & 0xFFFFFFFF # Make the clock go round
		zeroMin = "0x" + hex(zeroMin)[2:].zfill(8) 
		return zeroMin
	else:
		intofhex1 = int(hexvalue1, 16) # Make int to be able to calculate
		intofhex2 = int(hexvalue2, 16)
		diff = intofhex1-intofhex2 & 0xFF # Make the clock go round
		diff = "0x" + hex(diff)[2:]
		return diff

def sub(values):
	zero = 0
	retvalue = [] 
	for i in values:
		print "the hexchar is: " + i
		hex7c = int('0x7c', 16)
		hexchar = int(i, 16)
		if hexchar == 0:
			print "Dealing with 00"
			hexchar += 100
			retvalue += '0x7c', '0x7c', '0x08'
		elif hexchar <= hex7c:
			nextsub = '0x01' 
			hexchar = hexchar - 0x02 # deze nog aanpassen ivm 0 
			#hexchar = hex(hexchar)
			hexchar = "0x" + hex(hexchar)[2:].zfill(2)
			print "<=7c so -2: " + hexchar
			retvalue += hexchar,nextsub,nextsub
			print retvalue
		elif hexchar >= hex7c*2:
			remainder = hexchar - (hex7c + hex7c)
			#remainder = int('0x06', 16)
			#print remainder
			remainder = "0x" + hex(remainder)[2:].zfill(2)
			print "groter dan 0xF8 aaa " + hex(hexchar) + " remainder is " + remainder
			hex7c = hex(hex7c)
			retvalue += hex7c, hex7c, remainder
			print retvalue
		else:
			remainder = hexchar - hex7c - 0x01
			remainder = "0x" + hex(remainder)[2:].zfill(2)
			print "tussen 7C en F8 " + hex(hexchar) + " remainder is " + remainder
			hex7c = hex(hex7c)
			retvalue += hex7c, remainder,'0x01'
			print retvalue
			#chunk1 = sub3(a)
	
	# In case of a 00 we must change some values
	if values[0] == "00":
		print "first value"
	if values[1] == "00":
		print "second value is 00"
		print retvalue
		#retvalue[0] = "0x15"
		retvalue[0] = calc(retvalue[0],'0x01') 

	if values[2] == "00":
		print "third value is 00"
		retvalue[3] = calc(retvalue[3],'0x01')

	if values[3] == "00":
		print "fourth value"
	return retvalue

def test(chunks):
	#print str(chunks[1])
	intofhex1 = int(chunks[0], 16)
	intofhex2 = int(chunks[1], 16)
	intofhex3 = int(chunks[2], 16)
	
	
	test = hex(0-intofhex1 - intofhex2 - intofhex3 & 0xFFFFFFFF)
	result = "0x" + test[2:].zfill(8)
	#print test
	return result
	 

def strip(ugly):
	n = 2
	nice = [ugly[index : index + n] for index in range(0, len(ugly), n)]
	nice = "".join(nice[1::2])
	nice = nice.upper() 
	return nice 

def subtable(retvalue):
	nice = []
	#chunk1 = retvalue[9:12][0] + retvalue[6:9][0] + retvalue[3:6][0] + retvalue[0:3][0]
	chunk1 = retvalue[0:3][0] + retvalue[3:6][0] + retvalue[6:9][0] + retvalue[9:12][0] 
	#chunk2 = retvalue[9:12][1] + retvalue[6:9][1] + retvalue[3:6][1] + retvalue[0:3][1]
	chunk2 = retvalue[0:3][1] + retvalue[3:6][1] + retvalue[6:9][1] + retvalue[9:12][1]
	#chunk3 = retvalue[9:12][2] + retvalue[6:9][2] + retvalue[3:6][2] + retvalue[0:3][2]
	chunk3 = retvalue[0:3][2] + retvalue[3:6][2]  + retvalue[6:9][2] + retvalue[9:12][2] 
	print chunk1, chunk2, chunk3   
	print "Creating  subtables ..."
	nice.append(strip(chunk1))
	nice.append(strip(chunk2))
	nice.append(strip(chunk3))
	print nice
	return nice

# ? weet ik ff niet meer
n = 4*4
# Cut shellcode in pieces of 4 bytes
shellcode = [shellcode[i:i+n] for i in range(0, len(shellcode), n)]
for i in shellcode:
	shellcode = str(i)
	loosevalues = []
	print "Sub-encoding: " + shellcode   	
	hexclean = remove(shellcode) # Remove slashes etc
	revhex = reverse(hexclean) # Reverse the string endianess
	hexzeroMin = calc(revhex,"wrap")
	print "0 - passed Hex = " + hexzeroMin
	loosevalues = split(hexzeroMin)
	chunks = sub(loosevalues)
	newchunks = subtable(chunks)
	print "Doing test to revert"
	for chunk in newchunks:
		print chunk
	
	if not str(test(newchunks)) == str("0x"+revhex):
		print "This is not good ..."
		print "0x"+revhex
		print str(test(newchunks))
		exit()

	#print test(newchunks)
