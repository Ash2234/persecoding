amounts = []
for i in range(5):
    amount = int(input())
    amounts.append(amount)
lost_index = int(input()) - 1
remaining_amount = sum(amounts) - amounts[lost_index]
print(f"${remaining_amount}")
