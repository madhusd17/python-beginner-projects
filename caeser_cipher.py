alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def encrypt(plain_text,shift_no):
    cipher_text=""
    for char in plain_text: 
        if char in alphabets:
            position=alphabets.index(char)
            new_position=(position+shift_no)%26
            cipher_text+=alphabets[new_position]
        else:
            cipher_text+=char
    print(f"here's the encrypted result:{cipher_text}")
def decrypt(cipher_text,shift_no):
    plain_text=""
    for char in cipher_text:
        if char in alphabets:
            position=alphabets.index(char)
            new_position=(position-shift_no)%26
            plain_text+=alphabets[new_position]
        else:
            plain_text+=char
    print(f"here's the decrypted result:{plain_text}")
end=False    
while not end:
    choice=input("Type 'encrypt' for encryption and 'decrypt' for decryption :")
    text=input("type ur message: ").lower()
    shift=int(input("enter shift number:"))
    if choice=='encrypt':
        encrypt(plain_text=text,shift_no=shift)
    else:
        decrypt(cipher_text=text,shift_no=shift)
    x=input("type 'yes' if you want to go again,otherwise type'no':")
    if x=='no':
        end=True
        print("have a nice day !! byee...")
    
    
