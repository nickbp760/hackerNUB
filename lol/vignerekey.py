# This function decrypts the
# encrypted text and returns
# the original text
def key(cipher_text, kata):
guest_key = []
for i in range(len(kata)-1):
key=0;
cipher=ord(cipher_text[i])-97+26
#print(cipher)
origin=ord(kata[i])-97
#print(origin)
key=cipher-origin;
if(key>=26):
key=key-26
#print(key)
key += ord('a')
guest_key.append(chr(key))
return("" . join(guest_key))
print(key("kgtisomm","gemastik")) #echiave
