#1 1 2 3 5 8 13 21 34

list1=[1,1]
new_num = 0

for i in range(23):
    new_num = list1[i]+list1[i+1]
    list1.append(new_num)

print(sum(list1))

#  2/1 + 3/2 + 5/3 + 8/5 + 13/8


list2=[]

temp = 0
under = 1
top = 2

for i in range(25):
    
    list2.append(top/under)
    temp = top
    top += under
    under = temp
    
print(sum(list2))


#0-1 1-3 3-6 6-10 10-14 

num = eval(input("請輸入最終數字:"))
list3 = [i for i in range(1,num+1)]
start=0
end = 0
count = 0
add = 0 

while add != :
    count+=1
    add+=count
    
for i in range(1,count+1):
    end+=i
    print(list3[start:end])
    start = end  
    

    
    

    

    
    
    
    
