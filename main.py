import backend

def main(): 
    user_name = input("enter name:")
    greet = backend.hello_world(user_name)
    print(greet)

main()
