num1=0;
while num1 < 100:
     num1 += 1
     if ((num1 % 7 == 0) or (num1 % 10 == 7) or (num1 // 10 == 7)):
         continue
     else:
         print(num1)
