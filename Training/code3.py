class BusinessUtility:
    def calculate_margin(self, revenue, cost):
        return ((revenue - cost) / revenue) * 100


class SeasonalBusinessUtility(BusinessUtility):
    def calculate_margin(self, revenue, cost):
        regular_margin = super().calculate_margin(revenue, cost)
        return regular_margin + 10


class ProfitabilityChecker:
    def check_profitability(self, regular_margin):
        if regular_margin >= 10:
            print("Business is profitable.")
        else:
            print("Business is not profitable.")


def main():
    revenue = float(input("Enter Revenue: "))
    cost = float(input("Enter Cost: "))

    business = BusinessUtility()
    seasonal_business = SeasonalBusinessUtility()
    checker = ProfitabilityChecker()

    regular_margin = business.calculate_margin(revenue, cost)
    seasonal_margin = seasonal_business.calculate_margin(revenue, cost)

    print("Regular Profit Margin:", regular_margin)
    print("Seasonal Profit Margin:", seasonal_margin)

    checker.check_profitability(regular_margin)


if __name__ == "__main__":
    main()
