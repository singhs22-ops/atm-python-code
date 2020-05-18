import os
import string
#open a file

print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
def getword_a(test_str,n):

    # printing original string
    #print("Original_String : " + test_str)

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

f.writelines("101 Santosh maths 35\n")
f.writelines("101 Santosh Hindi 30\n")
f.writelines("102 Hina English 41\n")
n = int(input("Enter the number of data to be entered:"))
for i in range(n):
    text = input("Add remaning contents")
    f.writelines(text)
    f.write("\n")

f.close()
total_marks= dict()
name = dict()
over = dict()
arr_final =""
dict_filen = dict()
file_txt =open("student.txt","r+")

for line in file_txt:

    res1 = line
    print("lines", line)
    res=res1[:3]
    word1 = getword_a(res1,4)
    if (res in total_marks):
        total_marks[res] = total_marks[res]+int(word1)
        #total marks
        print("totalmarks::",total_marks[res])
        arr_final = over[res] + res1

        over.pop(res)
        over[res] = arr_final


    else:
        total_marks[res] = int(word1)
        name[res] = getword_a(res1,2)
        over[res] = res1


        dict_filen[res] = name[res]+"."+res+".txt"
        fnew =open(dict_filen[res],"w")



for result in total_marks:
    fileher = open(dict_filen[result], "w")
    fileher.write(over[result])
    fileher.write("\t\t\tTotal ")
    fileher.write(str(total_marks[result]))
    print(result)

file_txt.close()
