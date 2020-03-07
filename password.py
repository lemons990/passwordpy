import hashlib
def main():
    FN = input("Enter file location: ")
    file = open(FN, "r")
    text = input("Input your text here: ")
    salt = input("Enter Salt: ")
    options = ["[1] Encode Text", "[2] Match Text"]
    optionsIn = [0,1,2]
    a = optionsIn[1]
    b = optionsIn[2]
    print(options[0] + " " + options[1])
    input1 = input("Slect an option: ")
    enc = text + salt
    h = hashlib.sha512()
    h.update(enc.encode('utf-8'))
    hash = h.hexdigest()
    if optionsIn[int(input1)] == a:
        opt1(FN,file,text,salt,options,optionsIn,a,b,input1,enc,h,hash)
    elif optionsIn[int(input1)] == b:
        opt2(FN,file,text,salt,options,optionsIn,a,b,input1,enc,h,hash)
    else:
        print("Exit Code 1")
        exit()
def opt1(FN,file,text,salt,options,optionsIn,a,b,input1,enc,h,hash):
    print(hash)
    file = open(FN, "w")
    file.write(h.hexdigest())
    file.close()
def opt2(FN,file,text,salt,options,optionsIn,a,b,input1,enc,h,hash):
    file = open(FN, "r")
    phash = file.read()
    file.close()
    if hash == phash:
        print("Success, the password is: " + text)
    else:
        print("Incorrect Text")
main()
