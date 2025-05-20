from datetime import datetime 
import re
import os
mart_name = "Charlie shopping mart"
heading = "BILL RECEIPT"

def generate_receipt(name,items,total,discount_amt,gst_amt,final_total, now):
    lines = []
    lines.append("="*40)
    lines.append(mart_name.center(40))
    lines.append(heading.center(40))
    lines.append(now.strftime("date:%d:%m:%Y  time:%H:%M:%S").center(40))
    lines.append("="*(40))
    lines.append(f"Customer name:{name}")
    lines.append("-"*40)
    lines.append(f"{'Item':<15}{'Price':<9}{'Qty':<8}{'Total'}")
    lines.append("-"*40)
    for item_name,amount, quantity, item_total in items:
        lines.append(f"{item_name:<15}{amount:<9.2f}{quantity:<8.2f}{item_total:.2f}")
    
    lines.append("="*40)
    lines.append(f"{'Total_amount':>32}:₹{total:.2f}")
    lines.append(f"{'Discount(10%)':>32} : -₹{discount_amt:.2f}")
    lines.append(f"{'Gst(5%)':>32} : +₹{gst_amt:.2f}")
    lines.append(f"{'Final total':>32}:₹{final_total:.2f}")
    lines.append("=" *40)
    lines.append("*****Thank you, visit Again!*****")
    lines.append("="*40)

    return "\n".join(lines)


while True:
    now= datetime.now()
    print("="*40)
    print(mart_name.center(40))
    print(heading.center(40))
    print(now.strftime("date:%d:%m:%Y  time:%H:%M:%S").center(40))
    print("="*(40))


    name=input("Enter your name:").title()
    total=0
    items=[]


    while True:
        print("\nEnter item details:")
        print("enter the amount and quantity:")
        item_name=input(" enter item name:")
        amount=float(input("enter amount: (₹)"))
        quantity=float(input("enter number of items:"))
        item_total = amount * quantity
        total += item_total
        items.append((item_name, amount, quantity, item_total))
        repeat=input("do you want to add more items(yes/no):").lower()
        if repeat == "no" or repeat=="no":
            break
    print("="*40) 
    print(name)
    print(f"₹{total:.2f}")
    print("="*40)
 
    discount= 0.10
    gst= 0.05
    discount_amt=total*discount
    gst_amt= total*gst
    final_total= total-discount_amt+gst_amt

    
  
    receipt_text= generate_receipt(name,items,total,discount_amt,gst_amt,final_total, now)
    print(receipt_text)
    
    save_path = "C\\Billing_receipts"
    os.makedirs(save_path, exist_ok=True)
    safe_name=re.sub(r'[^\w\s-]','',name).strip().replace(" " , "_")
    file_name = f"{safe_name}_{now.strftime('%d%m%y')}.txt"
    full_path = os.path.join(save_path, file_name)
    with open(full_path, 'w') as f:
        f.write(receipt_text)
    print(f"\n Receipt saved to file:{file_name}")

      
    repeat=input("do you want to go next costumer(yes/no):")
    if repeat=="no":
        print("\n Thank you billing system closed.")
        break


   
