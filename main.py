from customer.customer import Customer
from restaurant.restaurant import Restaurant

# Create customers
customer1 = Customer("Gilbert", "Williams")
customer2 = Customer("Jane", "Darius")
customer3 = Customer("Michael", "Johnson")

# Create restaurants
restaurant1 = Restaurant("Pizza Palace")
restaurant2 = Restaurant("Burger Haven")
restaurant3 = Restaurant("Sushi Spot")

# Add reviews
customer1.add_review(restaurant1, 4)
customer1.add_review(restaurant2, 5)
customer2.add_review(restaurant1, 3)
customer2.add_review(restaurant3, 4)
customer3.add_review(restaurant2, 2)

# Test methods
print("All customers:")
for customer in Customer.instances:
    print(customer.get_full_name())

print("Average rating for Restaurant 2:", restaurant2.average_star_rating())

print("Restaurant 2 reviews:")
for review in restaurant2.get_reviews():
    print(f"  Rating: {review.get_rating()} stars")

print("Customers who reviewed Restaurant 2:")
for customer in restaurant2.get_customers():
    print("  " + customer.get_full_name())

print("Number of reviews by Customer 2:", customer2.num_reviews())

found_customer = Customer.find_by_name("Jane Darius")
print("Found customer by name:", found_customer.get_full_name() if found_customer else "Not found")

customers_with_given_name = Customer.find_all_by_given_name("Jane")
print("Customers with given name 'Jane':")
for customer in customers_with_given_name:
    print("  " + customer.get_full_name())

# Additional tests
print("\nAdditional Tests:")
print("Average rating for Restaurant 1:", restaurant1.average_star_rating())

print("Restaurant 1 reviews:")
for review in restaurant1.get_reviews():
    print(f"  Rating: {review.get_rating()} stars")

print("Customers who reviewed Restaurant 1:")
for customer in restaurant1.get_customers():
    print("  " + customer.get_full_name())

print("Number of reviews by Customer 1:", customer1.num_reviews())

found_customer = Customer.find_by_name("Michael Johnson")
print("Found customer by name:", found_customer.get_full_name() if found_customer else "Not found")

customers_with_given_name = Customer.find_all_by_given_name("Gilbert")
print("Customers with given name 'Gilbert':")
for customer in customers_with_given_name:
    print("  " + customer.get_full_name())
