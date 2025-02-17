import base64
import os

def decrypt_and_eval(user_input):
    try:
        decoded = base64.b64decode(user_input).decode()
        result = eval(decoded, {"__builtins__": {}})  # Dangerous eval!
        return result
    except Exception as e:
        return str(e)

def main():
    FLAG = "ifmCTF{d3crpts_is_easy}"
    print("Welcome to the decryption challenge!")
    user_input = input("Enter encoded payload: ")
    output = decrypt_and_eval(user_input)
    print("Output:", output)
    if output == "give_me_the_flag":
        print("Congrats! Here is your flag:", FLAG)
    else:
        print("Try again!")

if __name__ == "__main__":
    main()
