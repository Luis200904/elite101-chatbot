def chatbot():
    print("Welcome to the Elite 101 Chatbot!")

name = input("Please enter your name: ")
print(f"Nice to meet you, {name}!")

age = input("How old are you? ")
print(f"Welcome {name}! Oh,being {age} is the greatest years of my life! How can I help you today?")

print("\nPlease choose from the following options:")
print("1. Placeholder Option 1")
print("2. Placeholder Option 2")
print("3. Placeholder Option 3")
print("4. Exit the conversation")

choice = input("Enter the number of your choice: ")

if choice == "4":
    print(f"Goodbye, {name}! Have a great day!")
else:
    print("This is a placeholder for the selected option. Goodbye for now!")

chatbot()

