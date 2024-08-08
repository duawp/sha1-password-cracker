import hashlib
import time


print(r"""______            _     _  ______                 _           _ 
 _______   __    __   ______   __       __  _______  
|       \ |  \  |  \ /      \ |  \  _  |  \|       \ 
| $$$$$$$\| $$  | $$|  $$$$$$\| $$ / \ | $$| $$$$$$$\
| $$  | $$| $$  | $$| $$__| $$| $$/  $\| $$| $$__/ $$
| $$  | $$| $$  | $$| $$    $$| $$  $$$\ $$| $$    $$
| $$  | $$| $$  | $$| $$$$$$$$| $$ $$\$$\$$| $$$$$$$ 
| $$__/ $$| $$__/ $$| $$  | $$| $$$$  \$$$$| $$      
| $$    $$ \$$    $$| $$  | $$| $$$    \$$$| $$      
 \$$$$$$$   \$$$$$$  \$$   \$$ \$$      \$$ \$$      
                                                   """)
print("\n****************************************************************")
print("\n* Copyright of Malek, 2024                              *")
print("\n* https://x.com/FrankZane95                                  *")
print("\n* https://www.youtube.com/@duawp                          *")
print("\n****************************************************************")




def convert_text_to_sha1(text):
    digest = hashlib.sha1(
        text.encode()
    ).hexdigest()

    return digest


def main():
    user_sha1 = input("Enter SHA1 to crack: \n")
    cleaned_user_sha1 = user_sha1.strip().lower()
    with open("./passwords.txt") as f:
        for line in f:
            password = line.strip()
            converted_sha1 = convert_text_to_sha1(
                password)

            if cleaned_user_sha1 == converted_sha1:
                print(f"Password found: {password}")
                return
    print("Could not find the password")



if __name__ == "__main__":
    main()
input("Press Enter to exit...")



