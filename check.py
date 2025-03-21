# def get_first_element(lst):  
#     print(lst[0])  # List ka pehla element print kar raha hai

# # User se input lena
# user_list = []  # Khaali list banayi
# n = int(input("Kitne elements daalne hain? "))  # User se poocha kitne elements chahiye

# for i in range(n):  
#     element = input(f"Element {i+1} likho: ")  # Har element input karwa rahe hain
#     user_list.append(element)  # List me add kar rahe hain

# print("List before:", user_list)  
# get_first_element(user_list)  # Function call kiya  


MAX_LENGTH = 3

def shorten(list):
    
    while len(list) > MAX_LENGTH:
        remove_element = list.pop()
        print(f"Removed Element: {remove_element}")
        
        
def user_input():
    
    user_list = []
    
    user_input = int(input("Kitne Elements Add karne hai list may: "))
    
    for i in range(user_input):
        
        element = input(f"Element {i + 1} Likho")
        user_list.append(element)
        

print(f"List before shortening: {user_list}")

shorten(user_list)

print(f"List after shortening: {user_list}")