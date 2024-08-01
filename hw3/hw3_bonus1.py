import hashlib
HASH = ['5f4dcc3b5aa765d61d8327deb882cf99','5a105e8b9d40e1329780d62ea2265d8a']

PASSLIST = ['test','name','hello','password','goodbye',
            '12345','1234567','123456789','123456','test1',
            '12345678','zinch','g_czechout','asdf','qwerty',
            'picture1','111111','123123','1234567890','senha',
            'qwerty123']

            

#需要輸入HASH values時使用
'''while(True):
        HASH1 = input("Please input the HASH values: ")
        if HASH1 == "finish":
               break

        finding = 0
        print("HASH: ",HASH1)
        for word in PASSLIST:
                guess = hashlib.md5(word.encode('utf-8')).hexdigest()
                if guess.upper() == HASH1 or guess.lower() == HASH1:
                        print(f'[+] Password found: {word}')
                        finding = 1
                        break
                else:
                        print(f'[-] Guess: {word} incorrect... {guess}')
        if finding == 0:
                print(f'Password not found in wordlist...')
        print("----------------------------------------------")'''


#預設文本還原
for i in range(len(HASH)):
    finding = 0
    print("HASH: ",HASH[i])
    for word in PASSLIST:
            guess = hashlib.md5(word.encode('utf-8')).hexdigest()
            if guess.upper() == HASH[i] or guess.lower() == HASH[i]:
                    print(f'[+] Password found: {word}')
                    finding = 1
                    break
            else:
                    print(f'[-] Guess: {word} incorrect... {guess}')
    if finding == 0:
        print(f'Password not found in wordlist...')
    print("---------------------------------------------")