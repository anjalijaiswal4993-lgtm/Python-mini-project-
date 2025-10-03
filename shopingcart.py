def main():
    cart = []

    while True:
        print("\n welcome to the shopping cart program!")
        print("1.Add item to cart")
        print("2.Remove item from cart")
        print("3.View cart")
        print("4.Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            item = input("Enter the item you want to add: ")
            cart.append(item)
            print(f'Added "{item}" to the cart.')
        elif choice == '2':
            item = input("Enter the item you want to remove: ")

            if item in cart:
              cart.remove(item)
              print(f'Removed "{item}" from the card.')
            else:
             print(f'Item "{item}" not found in the cart.')

        elif choice == '3':
        
            if not cart:
             print("your cart is empty.")
            else:
             print("Items in your cart.")
             for item in cart:
                print(f'{item}')

        elif choice == '4':
         print("Thankyou for using the shopping cart program!")
        break

    else:
     print("Invalid choice. Please choose a valid option.")