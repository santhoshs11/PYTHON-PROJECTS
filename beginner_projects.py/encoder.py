
import art_encode
from art_encode import logo

print(logo)
    
def ceaser(text_word,shift_amount):

    direction = input("___encode/decode___ : ").lower()
    end_word = []
    for letter in text_word:
        position = alphapet.index(letter)
        if direction == 'encode':
          new_position = position + shift_amount
        elif direction =='decode':
            new_position = position + (shift_amount*-1)  

              
        else:
            print("""
                \/_______________\/
                |!!invalid choice!!|
                |  ______________  |
                \/              \/""") 
                
            break  
        end_word.append(alphapet[new_position])
    word=''.join(end_word)    
    print(f"your  result is : {word}")
repeat = False
while not repeat:  
    alphapet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    text = input("enter the word  : ").lower()
    shift = int(input("enter the no : "))
    shift = shift % 26      
    ceaser(text,shift)
    again = input('\n\nencrypt again ? yes/no : ').lower()
    if again == 'no':
        repeat = True
        print('\n   GOOD BYE !!')
    
    

'''def encode(text_word,shift_amount):
        for letter in text_word:
            position = alphapet.index(letter)
            new_position = position +shift_amount
            word.append(alphapet[new_position])
        encoded_word = ''.join(word)
        print(encoded_word)  ''' 

'''def decode(text_word,shift_amount):
    for letter in text_word:
        position = alphapet.index(letter)
        new_position = position - shift_amount
        word.append(alphapet[new_position])
    decoded_word = ''.join(word)
    print(decoded_word)'''

'''while True:
    direction = input("___encode/decode___ : ").lower()

    if direction == 'encode':
        text = input("enter the word to encode : ").lower()
        shift = int(input("enter the no : "))
        word = []
        encode(text,shift)
    elif direction ==  'decode':
        text = input("enter the word to encode : ").lower()
        shift = int(input("enter the no : "))
        word = []
        decode(text,shift)
    else:
        print("""
            \/_______________\/
            |!!invalid choice!!|
            |  ______________  |
             \/              \/""")   ''' 
