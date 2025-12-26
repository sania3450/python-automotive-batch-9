# Base class
class Discount:
    def apply_discount(self, amount):
        return amount


class SeasonalDiscount(Discount):
    def apply_discount(self, amount):
        return amount * 0.90   # 10% off


class FestivalDiscount(Discount):
    def apply_discount(self, amount):
        return amount * 0.80   # 20% off


class CouponDiscount(Discount):
    def apply_discount(self, amount):
        return amount - 2000   # Flat ₹2000 off


class Store:
    def __init__(self):
        self.items = {
            1: ("Apple iPhone 17 (512 GB)", 102900),
            2: ("SONY BRAVIA 55 inch 4K TV", 57990),
            3: ("Mivi Fort H880 Soundbar", 9999),
            4: ("Wakefit Sofa Cum Bed", 12148),
            5: ("SONY PlayStation 5", 44990)
        }

    def show_items(self):
        print("\nAvailable Items:")
        for key, value in self.items.items():
            print(f"{key}. {value[0]} - ₹{value[1]}")

    def get_price(self, choice):
        return self.items[choice][1]


# ---------------- Checkout ----------------
store = Store()
total_price = 0

store.show_items()

while True:
    item_choice = int(input("\nEnter item number: "))
    total_price += store.get_price(item_choice)

    more = input("Do you want to add more items? (yes/no): ").lower()
    if more != "yes":
        break

print("\nChoose Discount Type:")
print("1. Seasonal Discount")
print("2. Festival Discount")
print("3. Coupon Discount")

discount_choice = int(input("Enter discount choice: "))

if discount_choice == 1:
    discount = SeasonalDiscount()
elif discount_choice == 2:
    discount = FestivalDiscount()
elif discount_choice == 3:
    discount = CouponDiscount()
else:
    discount = Discount()

final_price = discount.apply_discount(total_price)

if final_price < 0:
    final_price = 0

print(f"\nOriginal Price: ₹{total_price}")
print(f"Final Price after Discount: ₹{int(final_price)}")
