 code for seat booking
"""
Created on Tue Feb 17 10:58:11 2026

@author: sneha mali
"""
rows = int(input("Enter number of rows:"))
seats_per_row = int(input("Enter number of seats in each row:"))

for row in range (1, rows + 1):
    print("Row", row,":" , end=" ")
    
    for seat in range(1, seats_per_row + 1):
        print(f"s{seat}", end=" ")
        
    print()
