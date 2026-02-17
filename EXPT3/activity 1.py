code for receipt
"""
Created on Tue Feb 17 10:43:57 2026

@author: sneha mali 
"""
#Input from user
copies = int(input("Enter number of receipt copies:"))
items = int(input("Enter number of items in each receipt:"))
#outer loop for receipt copies
for copy in range (1,copies + 1):
    print("\nReceipt copy:", copy)
    print("---------------------")
    
    #inner loop for items in each receipt
    for item in range(1, items + 1):
        print("Item Number:", item)
        
    print("--------------------")
print("\nAll receipts printed successfully!")
