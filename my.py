def calculate_total_cost(item1_price, item2_price, item3_price):
    item1_cost = item1_price
    item2_cost = item2_price
    item3_cost = item3_price
    # calculate the cost of combo packs with discounts
    combo1_cost = (item1_price + item2_price) * 0.9  # 10% discount
    combo2_cost = (item1_price + item3_price) * 0.9  # 10% discount
    combo3_cost = (item2_price + item3_price) * 0.9  # 10% discount
    combo4_cost = (item1_price + item2_price + item3_price) * \
        0.75  # 25% discount
    print("Welcome to Jessica Stores:")
    print("_______________________")
    print("product(s)  price")
    print(f"item 1        {item1_cost:.1f}")
    print(f"item 2        {item2_cost:.1f}")
    print(f"item 3        {item3_cost:.1f}")
    print(f"combo 1(item 1 + 2)   {combo1_cost:.1f}")
    print(f"combo 2(item 1 + 3)   {combo2_cost:.1f}")
    print(f"combo 3(item 2 + 3)   {combo3_cost:.1f}")
    print(f"combo 4(item 1 + 2 + 3)   {combo4_cost:.1f}")
    print("For delivery contact:+192263568")


# Example usage:
item1_price = 200.0
item2_price = 300.0
item3_price = 600.0

calculate_total_cost(item1_price, item2_price, item3_price)
