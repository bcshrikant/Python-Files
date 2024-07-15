ls=[{"id":11,"name":"Arun"},{"id":12,"name":"siva"}]
ls1=[]
ls2=[] 

for item in ls:
    ls1.append(item["id"])
    ls2.append(item["name"])

    print([ls1,ls2])


   