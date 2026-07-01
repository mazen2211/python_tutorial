# Week 5 - Tutorial 5 Documentation

## 1. Problem Analysis

### 1.1 Problem Statement
A small café currently calculates customer bills manually, which is slow and prone to human error. The café needs a Python program that automatically calculates the total bill based on the quantity of each item (coffee, tea, sandwich) a customer orders, and prints a clear receipt.

### 1.2 Inputs
- Customer name (text)
- Quantity of coffee ordered (number)
- Quantity of tea ordered (number)
- Quantity of sandwich ordered (number)

### 1.3 Outputs
- A printed receipt showing:
  - Customer name
  - Quantity of each item ordered
  - Total bill amount (in RM)

### 1.4 Typical Process Flow
1. Program starts and asks the cashier/customer for their name
2. Program asks for the quantity of coffee, tea, and sandwich
3. Program calculates the cost of each item (quantity × price)
4. Program sums up all item costs to get the total
5. Program prints a formatted receipt with all the details and the total

### 1.5 Constraints
- Prices are fixed: Coffee = RM8.50, Tea = RM6.00, Sandwich = RM12.00
- Quantities must be whole numbers (cannot order negative or fractional items)
- The program only handles these three menu items (no other products)

## 2. Problem Decomposition

The problem can be broken down into these smaller tasks:
1. **Input task** – Collect customer name and item quantities
2. **Calculation task** – Calculate the total cost based on quantities and fixed prices (`calculate_total` in utils.py)
3. **Output task** – Format and print the receipt (`print_receipt` in utils.py)
4. **Coordination task** – Tie everything together by calling input, calculation, and output functions in order (`main.py`)

## 3. Pseudocode

```
START
  DEFINE prices: coffee_price = 8.50, tea_price = 6.00, sandwich_price = 12.00

  FUNCTION calculate_total(coffee, tea, sandwich):
      total = (coffee * coffee_price) + (tea * tea_price) + (sandwich * sandwich_price)
      RETURN total

  FUNCTION print_receipt(name, coffee, tea, sandwich, total):
      PRINT "===== RECEIPT ====="
      PRINT "Customer :", name
      PRINT "Coffee   :", coffee
      PRINT "Tea      :", tea
      PRINT "Sandwich :", sandwich
      PRINT "-------------------"
      PRINT "Total = RM", total

  MAIN:
      GET name FROM user
      GET coffee_qty FROM user
      GET tea_qty FROM user
      GET sandwich_qty FROM user

      total = CALL calculate_total(coffee_qty, tea_qty, sandwich_qty)
      CALL print_receipt(name, coffee_qty, tea_qty, sandwich_qty, total)
END
```
