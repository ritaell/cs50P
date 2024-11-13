#convert input to lowercase and display it to the screen
def convert_lowercase(user_input):
    user_input_lowercase = user_input.casefold().strip()
    print(user_input_lowercase)

user_input = input()
convert_lowercase(user_input)

