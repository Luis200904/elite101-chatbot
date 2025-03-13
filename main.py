def restaurant_chatbot():
    print("Welcome to the Elite 101 Restaurant Chatbot!")
    name = input("Please enter your name: ")
    print(f"Hello {name}, how can I assist you today?")
    
    while True:
        print("\nPlease choose from the following options:")
        print("1. Place an order")
        print("2. Track an order")
        print("3. Request a refund")
        print("4. Contact customer service")
        print("5. Exit")
        
        choice = input("Enter the number of your choice: ")
        
        if choice == "1":
            order = input("What would you like to order? ")
            print(f"Thank you, {name}. Your order for {order} has been successfully placed.")
        
        elif choice == "2":
            order_id = input("Please enter your order ID: ")
            print(f"Your order {order_id} is currently being processed and will be delivered shortly.")
        
        elif choice == "3":
            order_id = input("Please enter your order ID for the refund request: ")
            print(f"Your refund request for order {order_id} has been submitted. Our team will review it and get back to you soon.")
        
        elif choice == "4":
            issue = input("Please describe your issue: ")
            print(f"Thank you for reaching out, {name}. Our customer service team will contact you shortly.")
        
        elif choice == "5":
            print(f"Goodbye, {name}. Have a great day!")
            break
        
        else:
            print("Invalid choice, please try again.")

restaurant_chatbot()