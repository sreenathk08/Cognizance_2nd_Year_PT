h=int(input())
m=int(input())
words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
                 "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", 
                 "nineteen", "twenty", "twenty one", "twenty two", "twenty three", "twenty four", "twenty five", 
                 "twenty six", "twenty seven", "twenty eight", "twenty nine"]
if m == 0:
    print(f"{words[h]} o' clock")
elif m == 15:
    print(f"quarter past {words[h]}")
elif m == 30:
    print(f"half past {words[h]}")
elif m == 45:
    print(f"quarter to {words[(h % 12) + 1]}")
elif m < 30:
        if m == 1:
            print(f"one minute past {words[h]}")
        else:
            print(f"{words[m]} minutes past {words[h]}")
else:
    m1= 60 - m
    if m1== 1:
        print(f"one minute to {words[(h % 12) + 1]}")
    else:
        print(f"{words[m1]} minutes to {words[(h % 12) + 1]}")
