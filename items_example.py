# Items ==> List Comprehension

item = {
     'a' : 10, 
     'b' : 12, 
     'c' : 22
}

temp = list();
for k, v in item.items() : 
    temp.append((v, k))
    
print(sorted(temp))


## Shorthand

c = {'a':10, 'b':12, 'c':22}
print(sorted([ (v, k) for k, v in c.items() ]))
