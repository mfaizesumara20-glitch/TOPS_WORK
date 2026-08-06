# princes = [200,500,100,0]

# total = 0
# for price in princes:
#     total = total + price
#     if price == 0:
#         continue
        
#     elif total >2000:
#         break
#     else:
#         print("Total : " ,total)



prices = [200, 500, 100, 0, 800, 700]

total = 0

for price in prices:
    if price == 0:
        continue

    total = total + price

    if total > 2000:
        break

print("Final Total:", total)