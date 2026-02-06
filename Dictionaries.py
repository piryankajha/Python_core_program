 '''_________________________________||  DICTIONARY   ||__________________________________________________'''

'''DICTIONARY - Dictionary is a collection of non repitative elements it is always written with the pair of  
                keys and values .
               and it also store multiple elements in dict. 
               written in curly brackets.

1->  written in curly brackets with part of keys and values.  
2->  dict are ordered .
3->  dict are mutable or changable .
4->  dict are not indexed .   
5->  dict not allow duplicate keys .
6-.  it also support multiple typpe of Data.  
_________________________________________________________________________________________________________

GET-->  its extract values base of Keys from dict.
kEY-->  Its return array where show entire keys of dictionary.  
VALUES-> Its return arry where show entire values from dict.
_________________________________________________________________________________________________________'''

''' how to create a dict.'''
x={}
x=dict()
print(type(x))
#-----------------------------------------------


D={"Brand":"TATA",
   "Model":"xyz",
   "Color":"Black",
   "year":2000}

print(D)
print(type(D))    #dict
print(len(D))     #4
#-----------------------------------------------------------
'''extract the name of students whose rollni is 3'''
st={1:"nman",
    2:"ashis",
    3:"mayank",
    4:"rajiv"}
x=st.get(3)  #extract the value base of key
print(x)
#---------
x=st[3]       #with out formula
print(x)


'''Create A Dictionary with the Help of user input'''

x=int(input("  :- "))
z=dict()
for i in range(x):
       a=input("enter key__")
       b=input("enter value : ")
       z[a]=b
print(z)
#-------------------------------------------
length= int(input("enter Length of dict :- "))
dic=dict()
for i in range(length):
    key=input("Enter Key :- ")
    val=input("Enter Values :- ")
    dic[key]=val
print(dic)



