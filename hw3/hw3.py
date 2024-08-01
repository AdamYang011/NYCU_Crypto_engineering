import sys
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
freq = [0.08167, 0.01492, 0.02782, 0.04253, 0.12702, 0.02228, 0.02015,
        0.06094, 0.06966, 0.00153, 0.00772, 0.04025, 0.02406, 0.06749,
        0.07507, 0.01929, 0.00095, 0.05987, 0.06327, 0.09056, 0.02758,
        0.00978, 0.02360, 0.00150, 0.01974, 0.00074]

def cal_IC(text):
    text_num = len(text)
    number = {}
    tmp = 0

    for i in sorted(text):
        number[i] = text.count(i)

    for i in number.keys():
        tmp += number[i] * (number[i]-1)
    IC = tmp / (text_num * (text_num-1))

    return IC

def get_frequency(text):
    frequency = []
    for i in alphabet:
        frequency.append(text.count(i)/len(text))
    return frequency

def get_group_word(key_len,text):
    block_list = []
    tmp = ""
    for m in range(key_len):
        j = m
        while(j < len(text)):
            tmp += text[j]
            j = j + key_len
        block_list.append(tmp)
        tmp = ""
    return block_list

def find_key_length(text):
    max_IC = 0
    key_len = 0
    tmp = ""
    IC = 0

    for i in range(2,8):
        tmp = ""
        IC = 0
        for m in range(i):
            j = m
            while(j<len(text)):
                tmp += str[j]
                j = j + i
            IC += cal_IC(tmp)
            tmp = ""
        IC = IC / i
        if(IC > max_IC):
            max_IC = IC
            key_len = i
    print("key length: ",key_len)
    return key_len

def find_keyword2(text):
    L = len(text)
    min_sum = 1000000
    min_index = -1
    for i in range(26):
        sum = 0
        for j in range(26):
            index = (j + i) % 26
            obj = text.count(alphabet[index])
            Exp = freq[j]*L
            sum += ((obj - Exp)**2)/Exp
        #print(sum)
        if min_sum > sum:
            min_sum = sum
            min_index = i
    return alphabet[min_index]

str = ""

print("請輸入欲解密的文字:")
for line in sys.stdin.readlines():
    str += line
str = str.replace(" ","").replace("\n", "")  #輸入ctrl+z，視為終止輸入
#print(str)

key_len = find_key_length(str)

block_list = get_group_word(key_len,str)

key = ""
for i in range(key_len):
    a = find_keyword2(block_list[i])
    key += a
print("keyword: ",key)

plaintext = ""
for i in range(len(str)):
    key_index = alphabet.index(key[i % key_len])
    E_index = alphabet.index(str[i])
    D_index = (E_index - key_index + 26) % 26
    plaintext += alphabet[D_index]
#print(plaintext)

with open('311605012_message1_out.txt', 'w') as f:
    f.write(plaintext)