import os
import string
#open a file

print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
def getword_a(test_str,n):

    # printing original string
    print("Original_String : " + test_str)

    # initializing N
    N = n

    # Get Nth word in String
    # using loop
    count = 0
    res = ""
    for ele in test_str:
        if ele == ' ':
            count = count + 1
            if count == N:
                break
            res = ""
        else:
            res = res + ele

    # printing result
    print("Nth word : " + res)
    return res


print(os.getcwd())
f = open("student.txt","w")
text ="qwerty"
f.writelines("101 Santosh maths 35\n")
f.writelines("101 Santosh Hindi 30\n")
f.writelines("102 Hina English 41")
f.writelines(text)
file_txt =open("student.txt","r")
d= dict()
tot = dict()
over = dict()
for line in file_txt:

    res1 =line
    res=res1[:3]
    word1 = getword_a(res1,4)
    if (res in d):
        d[res] = d[res]+int(word1)
        #total marks

    else:
        d[res] = int(word1)
        tot[res] = getword_a(res1,2)
        over[res] = res1

        print("word",tot )
        strt = tot[res]+"."+res+".txt"
        fnew =open(strt,"w")
        fnew.write(res1)
        fnew.write("Total ")
        fnew.write(str(d[res]))

file_txt.close()
