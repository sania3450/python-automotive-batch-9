# Base Class
class Discount:
    def apply_discount(self, amount):
        return amount

# Derived class seasonal discount
class SeasonalDiscount(Discount):
    def apply_discount(self, amount):
        return amount - (amount * 0.30)

# Derived class festival discount
class FestivalDiscount(Discount):
    def apply_discount(self, amount):
        return amount - 1000

# Derived class coupon discount
class CouponDiscount(Discount):
    def apply_discount(self, amount):
        return amount - 200


# User input
amount = float(input("Enter total amount: "))

print("\nChoose type of discount you want:")
print("1. Seasonal Discount")
print("2. Festival Discount")
print("3. Coupon Discount")

choice = int(input("Enter choice (1-3): "))

if choice == 1:
    discount = SeasonalDiscount()
elif choice == 2:
    discount = FestivalDiscount()
elif choice == 3:
    discount = CouponDiscount()
else:
    print("Invalid choice")
    exit()

final_amt = discount.apply_discount(amount)

print("Final Amount Payable:", final_amt)
