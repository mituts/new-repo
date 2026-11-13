x = 1
list = []
while x > 0:
    price = int(input("Enter: "))
    if price < 0:
        continue
    elif price > 0:
        list.append(price)
        total = sum(list)
    else:
        x = 0

print(total)
if total > 5000:
    discount = total * (20/100)
elif total > 1000:
    discount = total * (10/100)
subtotal = total - discount
gst = (18/100)*subtotal
total_final = subtotal + gst
print("Subtotal = ", total)
print("Discount = ", discount)
print("GST = ", gst)
print("Total = ", total_final)
