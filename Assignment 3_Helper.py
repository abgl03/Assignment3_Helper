import hashlib
response = "f239c8dd1b1cbdd5e5663bf12809b2b7"

text_file = open("output.txt", "r")
lines = text_file.read().split('\n')
text_file.close()

for word in lines:
    ha1_plain_text = "6326415:Mordor:"+word
    ha1 = hashlib.md5(ha1_plain_text.encode('utf-8')).hexdigest()
    my_response_plain_text = ha1+":03e2abb8a924e966bee59d41cef32851:80e33c06ee081829a3e2988489e9abc6"
    my_response = hashlib.md5(my_response_plain_text.encode('utf-8')).hexdigest()
    if my_response == response:
        print(word)

