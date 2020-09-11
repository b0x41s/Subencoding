# subencoding
Script to create SUB instructions, to overcome badchars.
Example in base 16 (HEX):
0x0 - 0x01 = 0xffffffff 
Python: hex(0x0-0x01 & 0xFFFFFFFF)

As you can see instead of -1 it wraps around.
This technique can be used for exploit development.
First we need to zero out a register, EAX using AND instructions. 
(& AND	Sets each bit to 1 if both bits are 1)

AND EAX,554E4D4A
AND EAX,2A313235

When we take each of these values and convert them from hex to binary well get: 
01010101010011100100110101001010
00101010001100010011001000110101
=
00000000000000000000000000000000

After zeroing the EAX register we want to put a value there and push it to the stack
If we need a shellcode like: \xaf\x75\xea\xaf
0 – afea75af = 50158A51 # wrap it around, and make sure to take care of the endianness

To calculate the first part 0x50 take 3 numbers and subtract untill zero.
0x50 - 0x26 - 0x15 - 0x15 = 0  
This will create the first row from up to down, and to create 0x15,8A and 51 do the same. 
When taking care of all HEX numbers this wil result in the SUB encoding chunks.

SUB EAX,2613424F
SUB EAX,15014201
SUB EAX,15010601
PUSH EAX

I thought it might could come in handy for the OSCE course, since doing it manually takes a lot of time. 
Absolutely not sophisticated, but it does the job .. i hope :D

Nice read about restrictive char sets:
https://vellosec.net/blog/exploit-dev/carving-shellcode-using-restrictive-character-sets/

