var1 = 'Hello'
var2 = 'Vishwajeet'

message1 = var1+', '+var2 +'. How are you?'
print(message1)

message2 = '{}, {}. How are you?'.format(var1,var2)
print(message2)

message3 = f'{var1}, {var2}. How are you?'
print(message3)

message4 = "Knowledge Shelf"
print(message4)
print(type(message4))
print(message4.lower())
print(message4.upper())
print(message4.__len__())
print(len(message4))
print(message4.count('e'))
print(message4.find('Shelf'))
print(message4[10])
print(message4[0:10])