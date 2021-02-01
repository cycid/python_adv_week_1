def main():
    f=open('values_import.txt', 'r')
    content=f.read()
    list_of_lists=[]

    #making list by removing "/n"
    list_of_values=content.split("\n")

    #making listOflists by removing space in each row and change str on int
    for items in list_of_values:
        item=items.split(" ")
        new=[]
        for i in item:
            i=int(i)
            new.append(i)
        list_of_lists.append(new)

    return list_of_lists



def income_values(value):
    #protection from "no_value" input
    v=input("please input integer "+value+"\n")

    while v.isnumeric()==False and len(v)==0:
        v = input("please enter correct "+value+"\n")
    v=float(v)
    return int(v)