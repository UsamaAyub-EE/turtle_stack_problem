def sum(l,a):
    we=0
    a+=1
    while a<len(l):
        we+=l[a][2]
        a+=1
    return we
def cap_check(t,w):
    r=True
    for i in range(len(t)):
        if sum(t,i)>=t[i][1]:
            r=False
    return r
l=[];lst=[];count=0;c_w_ratio=[];copy=[]
print("This program solves the turtles all the way down problem")
while True:
    c=float(input("Enter the capacity of the turtle.Enter -1 to stop entering\n"))
    if c==-1:
        break
    w=float(input("Enter the weight of this turtle\n"))
    count+=1
    c=c-w
    c_w_ratio.append([count,c/w])
    l.append([count,c,w])
    copy.append([count,c,w])
print("The cap to weight ratios are ",c_w_ratio)
for i in range(len(l)):
    print("Turtle number ",l[i][0]," is [ ",l[i][1]," , ",l[i][2]," ]")
for i in range(len(l)):
    for j in range(len(l)-i-1):
        if l[j][1]<l[j+1][1]:
            temp=l[j]
            l[j]=l[j+1]
            l[j+1]=temp
        if c_w_ratio[j][1]<c_w_ratio[j+1][1]:
            temp=c_w_ratio[j]
            c_w_ratio[j]=c_w_ratio[j+1]
            c_w_ratio[j+1]=temp
print("After sorting,")
for i in range(len(l)):
    print("Turtle number ",l[i][0]," is [ ",l[i][1]," , ",l[i][2]," ]")
print("The cap to weight ratios are ",c_w_ratio)
stack=1;i=1;cap=l[0][1];ans=[]
for d in range(1,len(l)):
    stack=1;cap=l[0][1];lst=[]
    lst.append(l[0])
    j=d
    while True:
        if cap>l[j][2]and(cap_check(lst,l[j][2])):
            cap=cap-l[j][2]
            lst.append(l[j])
            stack+=1
        j+=1
        if j==len(l):
            j=1
        if j==d:
            break
    ans.append(stack)
stack=1;cap=l[0][1];lst=[]
lst.append(l[0])
for j in range(len(c_w_ratio)):
    if c_w_ratio[j][0]==l[0][0]:
        continue
    if cap>copy[c_w_ratio[j][0]-1][2]and(cap_check(lst,copy[c_w_ratio[j][0]-1][2])):
        cap=cap-copy[c_w_ratio[j][0]-1][2]
        lst.append(copy[c_w_ratio[j][0]-1])
        stack+=1
print("So,here stack is ",stack)
ans.append(stack)
max=ans[0]
for i in range(len(ans)):
    if ans[i]>max:
        max=ans[i]
print("The maximum number of turtles in stack is ",max)
