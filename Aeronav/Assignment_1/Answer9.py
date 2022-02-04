def rare(A,B):
    A1={};
    B1={};
    a1=A.split();
    b1=B.split();
    for i in a1:
        if(i in A1):
            A1[i]+=1;
        else:
            A1[i]=1;
    for i in b1:
        if(i in B1):
            B1[i]+=1;
        else:
            B1[i]=1;
    output=[];
    for i in A1:
        if(A1[i]==1 and i not in B1):
            output.append(i);
    for i in B1:
        if(B1[i]==1 and i not in A1):
            output.append(i);
    return output 
A = "apple banana mango"
B = "banana fruits mango"  
print(rare(A,B))