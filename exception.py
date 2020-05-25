def ask_user(a):
  while True:  
    try:
        if a == "хорошо":
           break 
        else:
           a = input("Как дела? ")    
    except KeyboardInterrupt:
      print("Пока") 
      break
a = input("Как дела? ") 

if __name__ == "__main__":
    ask_user(a)
