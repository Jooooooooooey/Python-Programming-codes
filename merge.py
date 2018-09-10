#encoding:utf-8


### Calculate category probs from fasttext model and store them into dictionary
dct={}
with open('model_fasttext.txt') as file:
    lines=file.readlines()
    for line in lines:
        lst=line.strip('\n').split('\t')
        if not dct.has_key(lst[1]):
            dct.setdefault(lst[1],[0,0]) 
        else:
            dct[lst[1]][0]+=1
            if lst[1]==lst[2]:
                dct[lst[1]][1]+=1
probs={}
for key in dct.keys():
    if dct[key][1]==0:
        probs[key]=0
    else:
        probs[key]=float(dct[key][1])/dct[key][0]      

### Extract accurate data from fasttext model based on threshold value
dict_fasttext={}
num=0
with open('model_fasttext.txt') as file:
    lines=file.readlines()
    for line in lines:
        num+=1
        lst=line.strip('\n').split('\t')
        #if float(lst[-1])>=0.85 and float(probs[lst[1]])>=0.59:  # 0.85,0.59
        dict_fasttext[num]=[lst[0],lst[1],lst[2],float(lst[-1]),float(probs[lst[1]])]
"""
for x, y in dict_fasttext.items():
    print(x,y)
"""
### Extract accurate data from CNN model based on threshold value
dict_cnn={}
num=0
with open('report_cnn.txt') as file:
    lines=file.readlines()
    for line in lines:
        num+=1
        lst=line.strip('\n').split('\t')
        #if float(lst[-3])>=0.91 and float(lst[-1])>=0.71:   # 0.91,0.71
        dict_cnn[num]=[lst[0],lst[1],lst[2],float(lst[-3]),float(lst[-1])]
"""
for x, y in dict_cnn.items():
    print(x,y)
"""
### Calculate category probs from RNN model and store them into dictionary
dct1={}
with open('predicted1.txt') as file:
    lines=file.readlines()
    for line in lines:
        lst=line.strip('\n').split('\t')
        if not dct1.has_key(lst[1]):
            dct1.setdefault(lst[1],[0,0])
        else:
            dct1[lst[1]][0]+=1
            if lst[1]==lst[2]:
                dct1[lst[1]][1]+=1
probs1={}
for key in dct1.keys():
    if dct1[key][1]==0:
        probs1[key]=0
    else:
        probs1[key]=float(dct1[key][1])/dct1[key][0]


### Extract accrate data from RNN model based on threshold value
dict_rnn={}
num=0
with open('predicted1.txt') as file:
    lines=file.readlines()
    for line in lines:
        num+=1
        lst=line.strip('\n').split('\t')
        #if float(lst[-1])>=0.96 and float(probs1[lst[1]])>=0.6: # 0.96, 0.6
        dict_rnn[num]=[lst[0],lst[1],lst[2],float(lst[-1]),float(probs1[lst[1]])]

### Merge three models
list1=[]
list2=[]
list3=[]
for num1 in dict_fasttext.keys():
    list1.append(num1)
for num2 in dict_cnn.keys():
    list2.append(num2)
for num3 in dict_rnn.keys():
    list3.append(num3)
list_merged=list(set().union(list1,list2,list3))
print "Fasttext: ", len(dict_fasttext.keys())
print "CNN: ", len(dict_cnn.keys())
print "RNN: ", len(dict_rnn.keys())
print "Merged: ", len(list_merged)

"""
import pdb
### Print outcomes
from itertools import chain
from collections import defaultdict
dict_combine={}
for i, j in chain(dict_fasttext.items(),dict_cnn.items()):
    dict_combine.setdefault(i, [])
    dict_combine[i].append(j)


dict_combine2={}
for i, j in chain(dict_combine.items(),dict_rnn.items()):
    dict_combine2.setdefault(i, [])
    dict_combine2[i].append(j)

for i, j in dict_combine2.items():
    print i, j
"""
"""
total=0
count=0
for i in dict_combine2.keys():
    total+=1
    print len(dict_combine2[i])
"""
"""
    if len(dict_combine2)==3:
        if dict_combine2[i][1]==dict_combine2[i][2]:
            count+=1
    elif len(dict_combine2)==6:
        if dict_combine2[i][1]==dict_combine2[i][2] or
"""
"""
combined={}
for i in list(set().union(list1,list2,list3)):
    if dict_fasttext.has_key(i):
        if dict_cnn.has_key(i):
            if dict_rnn.has_key(i):
                combined[i]=[dict_fasttext[i],dict_cnn[i],dict_rnn[i]]
            else:
                combined[i]=[dict_fasttext[i],dict_cnn[i]]
        else:
            if dict_rnn.has_key(i):
                combined[i]=[dict_fasttext[i],dict_rnn[i]]
            else:
                combined[i]=[dict_fasttext[i]]
    elif dict_fasttext.has_key(i)==False:
        if dict_cnn.has_key(i):
            if dict_rnn.has_key(i):
                combined[i]=[dict_cnn[i],dict_rnn[i]]
            else: 
                combined[i]=[dict_cnn[i]]
        else:
            if dict_rnn.has_key(i):
                combined[i]=[dict_rnn[i]]
for i ,j in combined.items():
    for m in j:
        print j

total=0
count=0
for i in combined.keys():
    total+=1
    if len(combined[i])==1:
        if combined[i][0][1]==combined[i][0][2]:
            count+=1
    elif len(combined[i])==2:
        if combined[i][0][1]==combined[i][0][2] or combined[i][1][1]==combined[i][1][2]:
            count+=1
    #elif len(combined[i])==3:
        #if combined[i][0][1]==combined[i][0][2] or combined[i][1][1]==combined[i][1][2] or combined[i][2][1]==combined[i][2][2]:
            #count+=1
            
print('total: ',total)
print('count: ',count)
print('accuracy: ',float(count)/total)
"""

dictdict={}

### Voting first!
for i in list(set().union(list1,list2,list3)):
    if i>62500:
        break
    if dict_fasttext[i][1]==dict_cnn[i][1]==dict_rnn[i][1]:
        if dict_fasttext[i][-2]>=dict_cnn[i][-2] and dict_fasttext[i][-2]>=dict_rnn[i][-2]:
            dictdict[i]=dict_fasttext[i]
        elif dict_cnn[i][-2]>=dict_fasttext[i][-2] and dict_cnn[i][-2]>=dict_rnn[i][-2]:
            dictdict[i]=dict_cnn[i]
        elif dict_rnn[i][-2]>=dict_fasttext[i][-2] and dict_rnn[i][-2]>=dict_cnn[i][-2]:
            dictdict[i]=dict_rnn[i]
    elif dict_fasttext[i][1]==dict_cnn[i][1]:
        if dict_fasttext[i][-2]>=dict_cnn[i][-2]:
            dictdict[i]=dict_fasttext[i]
        else:
            dictdict[i]=dict_cnn[i]
    elif dict_fasttext[i][1]==dict_rnn[i][1]:
        if dict_fasttext[i][-2]>=dict_rnn[i][-2]:
            dictdict[i]=dict_fasttext[i]
        else:
            dictdict[i]=dict_rnn[i]
    elif dict_cnn[i][1]==dict_rnn[i][1]:
        if dict_cnn[i][-2]>=dict_rnn[i][-2]:
            dictdict[i]=dict_cnn[i]
        else:
            dictdict[i]=dict_rnn[i]
    else:
        if dict_fasttext[i][-2]>=dict_cnn[i][-2] and dict_fasttext[i][-2]>=dict_rnn[i][-2]:
            dictdict[i]=dict_fasttext[i]
        elif dict_cnn[i][-2]>=dict_fasttext[i][-2] and dict_cnn[i][-2]>=dict_rnn[i][-2]:
            dictdict[i]=dict_cnn[i]
        elif dict_rnn[i][-2]>=dict_fasttext[i][-2] and dict_rnn[i][-2]>=dict_cnn[i][-2]:
            dictdict[i]=dict_rnn[i]

for i in range(62501,62512):
    if dict_fasttext[i][-2]>=dict_cnn[i][-2]:
        dictdict[i]=dict_fasttext[i]
    else:
        dictdict[i]=dict_cnn[i]
"""
# Merge three models by voting!
for i in list(set().union(list1,list2,list3)):
    if dict_fasttext.has_key(i) and dict_cnn.has_key(i) and dict_rnn.has_key(i):
        if dict_fasttext[i][1]==dict_cnn[i][1] or dict_fasttext[i][1]==dict_rnn[i][1] or dict_fasttext[i][1]==dict_cnn[i][1]==dict_rnn[i][1]:
            dictdict[i]=dict_fasttext[i]
        elif dict_cnn[i][1]==dict_rnn[i][1]:
            dictdict[i]=dict_cnn[i]
        elif dict_fasttext[i][1]!=dict_cnn[i][1]!=dict_rnn[i][1]:
            if dict_fasttext[i][-2]>=dict_cnn[i][-2] and dict_fasttext[i][-2]>=dict_rnn[i][-2]:
                dictdict[i]=dict_fasttext[i]
            elif dict_cnn[i][-2]>=dict_fasttext[i][-2] and dict_cnn[i][-2]>=dict_rnn[i][-2]:
                dictdict[i]=dict_cnn[i]
            else:
                dictdict[i]=dict_rnn[i]
    elif dict_fasttext.has_key(i)==False and dict_cnn.has_key(i) and dict_rnn.has_key(i):
        if dict_cnn[i][-2]>=dict_rnn[i][-2]:
            dictdict[i]=dict_cnn[i]
        else:
            dictdict[i]=dict_rnn[i] 
    elif dict_fasttext.has_key(i) and dict_cnn.has_key(i)==False and dict_rnn.has_key(i):
        if dict_fasttext[i][-2]>=dict_rnn[i][-2]:
            dictdict[i]=dict_fasttext[i]
        else:
            dictdict[i]=dict_rnn[i]
    elif dict_fasttext.has_key(i) and dict_cnn.has_key(i) and dict_rnn.has_key(i)==False:
        if dict_fasttext[i][-2]>=dict_cnn[i][-2]:
            dictdict[i]=dict_fasttext[i]
        else:
            dictdict[i]=dict_cnn[i] 
    elif dict_fasttext.has_key(i) and dict_cnn.has_key(i)==False and dict_rnn.has_key(i)==False:
        dictdict[i]=dict_fasttext[i]
    elif dict_fasttext.has_key(i)==False and dict_cnn.has_key(i) and dict_rnn.has_key(i)==False:
        dictdict[i]=dict_cnn[i]
    elif dict_fasttext.has_key(i)==False and dict_cnn.has_key(i)==False and dict_rnn.has_key(i):
        dictdict[i]=dict_rnn[i]

"""
"""
# Merge three models by keeping the one with the highest case prob
for i in list(set().union(list1,list2,list3)):
    if dict_fasttext.has_key(i) and dict_cnn.has_key(i) and dict_rnn.has_key(i):
        if dict_fasttext[i][-2]>=dict_cnn[i][-2] and dict_fasttext[i][-2]>=dict_rnn[i][-2]:
            dictdict[i]=dict_fasttext[i]
        elif dict_cnn[i][-2]>=dict_fasttext[i][-2] and dict_cnn[i][-2]>=dict_rnn[i][-2]:
            dictdict[i]=dict_cnn[i]
        elif dict_rnn[i][-2]>=dict_fasttext[i][-2] and dict_rnn[i]>=dict_cnn[i][-2]:
            dictdict[i]=dict_rnn[i]
    elif dict_fasttext.has_key(i)==False and dict_cnn.has_key(i) and dict_rnn.has_key(i):
        if dict_cnn[i][-2]>=dict_rnn[i][-2]:
            dictdict[i]=dict_cnn[i]
        else:
            dictdict[i]=dict_rnn[i] 
    elif dict_fasttext.has_key(i) and dict_cnn.has_key(i)==False and dict_rnn.has_key(i):
        if dict_fasttext[i][-2]>=dict_rnn[i][-2]:
            dictdict[i]=dict_fasttext[i]
        else:
            dictdict[i]=dict_rnn[i]
    elif dict_fasttext.has_key(i) and dict_cnn.has_key(i) and dict_rnn.has_key(i)==False:
        if dict_fasttext[i][-2]>=dict_cnn[i][-2]:
            dictdict[i]=dict_fasttext[i]
        else:
            dictdict[i]=dict_cnn[i] 
    elif dict_fasttext.has_key(i) and dict_cnn.has_key(i)==False and dict_rnn.has_key(i)==False:
        dictdict[i]=dict_fasttext[i]
    elif dict_fasttext.has_key(i)==False and dict_cnn.has_key(i) and dict_rnn.has_key(i)==False:
        dictdict[i]=dict_cnn[i]
    elif dict_fasttext.has_key(i)==False and dict_cnn.has_key(i)==False and dict_rnn.has_key(i):
        dictdict[i]=dict_rnn[i]
"""
"""
# Merge Two models by keeping the one with the highest case prob
for i in list(set().union(list2,list3)):
    if dict_cnn.has_key(i) and dict_rnn.has_key(i):
        if dict_cnn[i][-2]>=dict_rnn[i][-2]:
            dictdict[i]=dict_cnn[i]
        else:
            dictdict[i]=dict_rnn[i]
    elif dict_cnn.has_key(i) and dict_rnn.has_key(i)==False:
        dictdict[i]=dict_cnn[i]
    elif dict_cnn.has_key(i)==False and dict_rnn.has_key(i):
        dictdict[i]=dict_rnn[i]   
"""
#for i in dictdict.keys():
    #print '\t'.join([dictdict[i][0],dictdict[i][1],dictdict[i][2],str(dictdict[i][3]),"i",str(dictdict[i][4])])

total=0
count=0
for i in dictdict.keys():
    total+=1
    if dictdict[i][1]==dictdict[i][2]:
        count+=1
print 'total: ',total
print 'count: ',count
print 'accuracy: ',float(count)/total

for i in range(1,len(dictdict)+1):
    print '\t'.join([dictdict[i][0],dictdict[i][1],dictdict[i][2],str(dictdict[i][3]),'hhh',str(dictdict[i][4])])
