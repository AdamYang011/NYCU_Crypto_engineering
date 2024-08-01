import numpy as np
from itertools import permutations
#print(list(permutations("ABCD",2)))
#ECDTM ECAER AUOOL EDSAM MERNE NASSO DYTNR VBNLC RLTIQ LAETR IGAWE BAAEI HOR
word_list = ['ER','EN','TH','HE','AN']  #TH HE AN RE ER IN ON AT ND ST ES EN OF TE ED OR TI HI AS TO
rec_row = 9     #從第一題結果推斷為9*7的長方形
rec_column = 7

def find_prime_factor(num):
    cnt = {}
    while num != 1:
        for i in range(2,num+1):
            if (num % i) == 0:
                if i in cnt:
                    cnt[i] += 1
                else:
                    cnt[i] = 1
                num = int(num / i)
                break
    return cnt

def find_num_pair(dict, cipher_num):
    x1 = []
    x2 = []
    for i in num_cnt.keys():
        for j in range(1,dict[i]+1):
            tmp = int(int(i) ** int(j))
            if tmp in x1:
                continue
            x1.append(tmp)
            x2.append(int(cipher_num/tmp))
            x1.append(int(cipher_num/tmp))
            x2.append(tmp)
    x1.insert(0,1)
    x2.insert(0,cipher_num)
    x1.append(cipher_num)
    x2.append(1)
    return x1,x2

def cal_diff(x1,x2,cipher_num):
    diff = [0]*len(x1)
    for i in range(len(x1)):
        expect_num = x2[i] * 0.4
        vowel_num = [0]*x1[i]
        index = 0
        for j in range(cipher_num):
            if (cipher_txt[j] == "A" or cipher_txt[j] == "E" or cipher_txt[j] == "I" or cipher_txt[j] == "O" or cipher_txt[j] == "U"):
                vowel_num[j % x1[i]] += 1
            index +=1
        for k in vowel_num:
            diff[i] += abs(k - expect_num)
    return diff

def output_Q1(x1,x2,diff):
    for i in range(len(x1)):
        print("For {0}*{1} triangle, the sum of the difference is {2}".format(x1[i],x2[i],round(diff[i],2)))

def keep_finding(p,ok_list,empty_array,last_k,times):
    f = []
    tt = 0
    for i in range(rec_column):
        if i not in ok_list:
            f.append(i)
    #print("f:",f)

    cal_array1 = np.empty([rec_row, rec_column-2], dtype= str)
    cal_array2 = np.empty([rec_row, rec_column-2], dtype= str)
    w = 0
    for j in range(rec_column-2):
        
        for m in ok_list:
            if m == w:
                w+=1
        for i in range(rec_row):
                cal_array1[i][j] = empty_array[i][w]
        w+=1

    for t in permutations(range(0,len(f)),len(f)):
        #print(t)
        for j in range(rec_column-2):
            for i in range(rec_row):
                    cal_array2[i][j] = cal_array1[i][t[j]]

        for i in range(rec_row):
            for j in range(rec_column-2):
                if j == rec_column - 2 - 1:
                    break
                for k in range(last_k+1, len(word_list)): 
                    if cal_array2[i][j] + cal_array2[i][j+1] == word_list[k]:
                        #print(cal_array2)
                        #print(word_list[k])
                        #print(j,j+1)
                        ok_list.append(f[j])
                        ok_list.append(f[j+1])
                        #print("OK:",ok_list)
                        list = keep_finding2(f,ok_list,empty_array,last_k)
                        return list
                        tt = 1
                        break
                if tt == 1:
                    break
            if tt == 1:
                break
        if tt == 1:
            break

def keep_finding2(f,ok_list,empty_array,last_k):
    h = []
    tt = 0
    for i in range(rec_column):
        if i not in ok_list:
            h.append(i)
    #print(h)

    cal_array1 = np.empty([rec_row, rec_column-4], dtype= str)
    cal_array2 = np.empty([rec_row, rec_column-4], dtype= str)
    w = 0
    for j in range(rec_column-4):
        
        for m in ok_list:
            if m == w:
                w+=1
        for i in range(rec_row):
                cal_array1[i][j] = empty_array[i][w]
        w+=1

    for t in permutations(range(0,len(h)),len(h)):
        #print(t)
        for j in range(rec_column-4):
            for i in range(rec_row):
                    cal_array2[i][j] = cal_array1[i][t[j]]

        for i in range(rec_row):
            for j in range(rec_column-4):
                if j == rec_column - 2 -2 - 1:
                    break
                for k in range(last_k+1, len(word_list)): 
                    if cal_array2[i][j] + cal_array2[i][j+1] == word_list[k]:
                        #print(cal_array2)
                        #print(word_list[k])
                        #print(j,j+1)
                        ok_list.append(h[j])
                        ok_list.append(h[j+1])
                        #print("OK:",ok_list)
                        return ok_list
                        tt = 1
                        break
                if tt == 1:
                    break
            if tt == 1:
                break
        if tt == 1:
            break

def encrypt(cipher_txt):
    times = 0
    empty_array = np.empty([rec_row, rec_column], dtype= str)
    k = 0
    for j in range(rec_column):
        for i in range(rec_row):
            empty_array[i][j] = cipher_txt[k]
            k+=1
    #print(empty_array)
    array_tmp = empty_array.copy()
    tt = 0
    ok_list = []
    cal_array = np.empty([rec_row, rec_column], dtype= str)
    for p in permutations(range(0,len(empty_array[0])),len(empty_array[0])):
        print(p)
        for j in range(rec_column):
            for i in range(rec_row):
                    cal_array[i][j] = empty_array[i][p[j]]
        
        for i in range(rec_row):
            for j in range(rec_column):
                if j == rec_column - 1:
                    break
                for k in range(len(word_list)):                    
                    if cal_array[i][j] + cal_array[i][j+1] == word_list[k]:
                        print(cal_array)
                        ok_list.append(j)
                        ok_list.append(j+1)
                        
                        print(cal_array[i][j])
                        list = keep_finding(p,ok_list,empty_array,k,times+1)
                        return list
                        tt =1
                        break
                if tt == 1:
                    break
            if tt == 1:
                break            
        if tt == 1:
            break


cipher = input("Please input your cipher text:\n")
cipher_array = cipher.split(" ")
cipher_txt = cipher.replace(" ","")
cipher_num = len(cipher_txt)
num_cnt = find_prime_factor(cipher_num)
x1,x2 = find_num_pair(num_cnt,cipher_num)
diff = cal_diff(x1,x2,cipher_num)
output_Q1(x1,x2,diff)
print(encrypt(cipher_txt))


