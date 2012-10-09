#Encoding: UTF-8
import re

#Encode a text with base64
def base64Encode(text):
	alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","+","/"]
	bit_str=""	
	base64_str=""

	#Loop through all chars concatenate them as binary string
	for char in text:
		bin_char = bin(ord(char)).lstrip("0b")
		bin_char = (8-len(bin_char))*"0" + bin_char
		bit_str += bin_char

	#Add zero till text-length is divideable through 3
	while (((len(text)) % 3) != 0):
		bit_str += "00000000"	
		text += "0"
	
	#Split bit_str into 6bit long brackets
	brackets = re.findall('(\d{6})', bit_str)

	#Encode the brackets
	for bracket in brackets:
		if(bracket=="000000"):
			base64_str+="="
		else:
			base64_str+=alphabet[int(bracket,2)]
	return base64_str

#Decode a base64 chiffre
def base64Decode(chiffre):
	alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","+","/"]
	bit_str=""
	text_str=""
	
	#Loop through every char
	for char in chiffre:
		#Ignore characters, which are not in the alphabet. Concatenate the binary representation of alphabet index of char 
		if char in alphabet:
			bin_char = bin(alphabet.index(char)).lstrip("0b")
			bin_char = (6-len(bin_char))*"0" + bin_char
			bit_str += bin_char
	
	#Make 8bit - 2byte brackets
	brackets = re.findall('(\d{8})', bit_str)

	#Decode char binary -> asciii
        for bracket in brackets:
                        text_str+=chr(int(bracket,2))

        return text_str


to_encode="Gehaxelts Python base64"

print "String to be encoded:"+to_encode
print "Base64 encoded:"
encoded= base64Encode(to_encode)
print encoded

print "Base64 decoded:"
decoded= base64Decode(encoded)
print decoded
