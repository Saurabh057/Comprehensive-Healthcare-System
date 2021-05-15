

def shuffle(o1,o2, s1,s2):
    f1=[]
    f2=[]
    # print(s1)
    # print(s2)
    for i in range(len(o1)):
        # print(s1)
        # print(len(s1))

        # print(s2)
        q1=s1[0]
        q2=s2[0]
        # print(s1)
        # print(s2)
        # print(q1)
        # print(q2)
        if(len(q1)<len(q2)):
            # print("in")
            if(q1[0] in q2):
                # print("equal")
                a=q1[0]
                f1.append(a)
                f2.append(a)
                s1[0].remove(a)
                s2[0].remove(a)
                # print(s1)
                # print(s2)
            else:
                for k in range(len(q2)):
                    # if(i+len(q2)>=)
                    if(q2[k] not in o1[i+1:i+len(q2)]):
                        f1.append(q1[0])
                        f2.append(q2[k])
                        del s1[0][0]
                        del s2[0][k]
                        break
        else:
            if(q2[0] in q1):
                a=q2[0]
                f1.append(a)
                f2.append(a)
                s1[0].remove(a)
                s2[0].remove(a)
            else:
                for k in range(len(q1)):
                    # if(i+len(q2)>=)
                    if(q1[k] not in o2[i+1:i+len(q1)]):
                        f1.append(q1[k])
                        f2.append(q2[0])
                        del s1[0][k]
                        del s2[0][0]
                        break
        if(s1[0]==[]):
            del s1[0]
        if(s2[0]==[]):
            del s2[0]
    # print(f1)
    # print(f2) 
    return f1,f2

# o1=['a','b','c','d','e','g']
# o2=['a','g','d','b','c','e']
# s1=[['a','b','c'],['d'],['g','e']]
# s2=[['a','g','d','b'],['e','c']]
# shuffle(o1,o2,s1,s2)


