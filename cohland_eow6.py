# Camryn Ohland
# 10/4/2026
# End of week assignment - week 6

# Exercise 1

# Create a list with the original employees
employees = ["Bob", "Carlos", "Alice"]

# Print the original employee list
print("Exercise 1")
print(employees)

# Add Dana to the end of the list
employees.append("Dana")
print(employees)

# Remove Bob because he left the organization
employees.remove("Bob")
print(employees)

# Add Evelyn to the beginning of the list
employees.insert(0, "Evelyn")
print(employees)

# Sort the employees into alphabetical order
employees.sort()
print(employees)

# Exercise 2

# Create the list of customer ratings
ratings = [5, 4, 3, 5, 5, 5, 2, 3, 3, 3, 3, 2, 5, 4, 3]

print("Exercise 2")

# Check if there is a 5-star rating in the list
print("There are 5-star ratings in the results:", 5 in ratings)

# Count how many 5-star ratings are in the list
print("Number of 5-star ratings:", ratings.count(5))

# Calculate the average by dividing the total by the number of ratings
average = sum(ratings) / len(ratings)
print("Average rating:", average)

# Check whether there is a 1-star rating
if 1 in ratings:
    print("Low rating exists.")
else:
    print("No 1-star ratings found")

# Exercise 3

# Create the inventory list
stock = [120, 45, 300, 53, 90, 6, 200, 108, 43, 2]

print("\nExercise 3")

# Sort the inventory from smallest to largest
stock.sort()
print("Ascending:", stock)

# Reverse the sorted list to put it in descending order
stock.reverse()
print("Descending:", stock)

# Create a list containing revenue for all 12 months
revenue = [
    12000,
    15000,
    14000,
    16000,
    18000,
    17000,
    20000,
    21000,
    19000,
    22000,
    23000,
    24000,
]

print("Exercise 4")

# Use slicing to separate the months into four quarters
q1 = revenue[0:3]
q2 = revenue[3:6]
q3 = revenue[6:9]
q4 = revenue[9:12]

# Print the revenue lists for each quarter
print("Q1:", q1)
print("Q2:", q2)
print("Q3:", q3)
print("Q4:", q4)

# Calculate the total and average revenue for Q1
q1_total = sum(q1)
q1_average = q1_total / len(q1)

# Calculate the total and average revenue for Q2
q2_total = sum(q2)
q2_average = q2_total / len(q2)

# Calculate the total and average revenue for Q3
q3_total = sum(q3)
q3_average = q3_total / len(q3)

# Calculate the total and average revenue for Q4
q4_total = sum(q4)
q4_average = q4_total / len(q4)

# Print the results with clear labels
print("\nQ1 Total:", q1_total, "Average:", q1_average)
print("Q2 Total:", q2_total, "Average:", q2_average)
print("Q3 Total:", q3_total, "Average:", q3_average)
print("Q4 Total:", q4_total, "Average:", q4_average)

# Exercise 5

# Import the copy module so we can make a deep copy
import copy

# Create the customer purchases list
customer_purchases = [
    "milk",
    ["milk", "bread", "eggs"],
    "bread",
    ["milk", "bread", "eggs", "tp"],
]

print("Exercise 5")

# Find the number of customers in the list
print("Number of customers:", len(customer_purchases))

# Start by assuming tp was not purchased
tp_purchased = False

# Loop through each customer's purchase
for purchase in customer_purchases:

    # Check if the purchase is a list with multiple items
    if isinstance(purchase, list):
        if "tp" in purchase:
            tp_purchased = True

    # Check if the purchase itself is tp
    elif purchase == "tp":
        tp_purchased = True

# Print whether tp was purchased
print("TP purchased:", tp_purchased)

# Make a deep copy so changes do not affect the original list
purchase_copy = copy.deepcopy(customer_purchases)

# Loop through the copied list
for purchase in purchase_copy:

    # Only look inside items that are lists
    if isinstance(purchase, list):

        # Check if tp is inside the nested list
        if "tp" in purchase:

            # Find where tp is located
            tp_index = purchase.index("tp")

            # Replace tp with butter
            purchase[tp_index] = "butter"

# Print both lists to show that only the copy changed
print("Original list:", customer_purchases)
print("Deep copy:", purchase_copy)
