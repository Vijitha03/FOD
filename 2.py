item_prices = [2.5, 1.0, 3.0, 5.0]
item_quantities = [3, 4, 2, 1]
discount_rate = 10  # 10% discount
tax_rate = 7  # 7% tax
total_cost_before_discounts = sum(item_price * item_quantity for item_price, item_quantity in zip(item_prices, item_quantities))
total_discount = (discount_rate / 100) * total_cost_before_discounts
subtotal_after_discounts = total_cost_before_discounts - total_discount
total_tax = (tax_rate / 100) * subtotal_after_discounts
final_total_cost = subtotal_after_discounts + total_tax
print("Total cost before discounts and taxes: ", total_cost_before_discounts)
print("Total discount amount: ", total_discount)
print("Subtotal after discounts: ", subtotal_after_discounts)
print("Total tax amount: ", total_tax)
print("Final total cost with discounts and taxes: ", final_total_cost)
