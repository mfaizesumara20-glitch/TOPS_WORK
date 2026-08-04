# points  = int(input("Enter your team points: "))

# if points > 800:
#     print("Champion")
#     if points > 500 or points < 800:
#         print("Top Performer-up")
# else:
#     print("Keep Trying!")



points = int(input("Enter your team points: "))

if points > 800:
    print("Champion")
else:
    if points >= 500 and points <= 800:
        print("Top Performer")
    else:
        print("Keep Trying")