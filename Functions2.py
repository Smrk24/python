def get_name (firstname, lastname):
    """Return a nice format name"""
    fullname = f"{firstname} {lastname}"  
    return fullname.title ()

#print (get_name ("John", "Franče")

while True:
    print("Please tell me your name")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name:")
    if f_name == 'q':
        break

    l_name = input("Last name:")
    if l_name == 'q':
        break

    formatted_name = formatted_name(f_name, l_name)
    print(f"Hello, {formatted_name}!")


