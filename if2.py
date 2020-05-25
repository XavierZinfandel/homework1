def type1(a,b):

    if a.isdigit() and b.isdigit():
       return ("0")
    elif len(a) == len(b):
       return ("1")
    elif len(a) != len(b) and len(a)>len(b):
       return("2")
    elif len(a) != len(b) and b == ("learn"):
       return("3")

while True:
      a = input("Введите строку 1: ")
      b = input("Введите строку 2: ")
      c = type1(a,b)
      print(c)








