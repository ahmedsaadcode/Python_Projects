while True :
    enter = input("Enter some thing: ").lower()
    if enter == "done" :
      break
    elif len(enter)== 0 :
       continue
    elif enter.startswith("#") :
       continue
    else:
       print(enter)
print("Done!")