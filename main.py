
message = input("Type in the message to encrypt: ") 
newMessage = "" 

for i in range(len(message)):
  ASCII = ord(message[i]) 
  newMessage += str(ASCII) + " " 

print(newMessage) 
print()

message = input("Type in the message to encrypt: ") 
key = int(input('Type in the key you want to use: ')) 
newMessage = "" 

for i in range(len(message)):
  ASCII = ord(message[i]) + key 
  newMessage += str(ASCII) + " " 

print(newMessage) 
print()
