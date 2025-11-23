def open_diary():
    print("\n ____PERSONAL DIARY____ ")
    print("Type your diary entries below.")
    print("Type EXIT to save and close.\n")

    diary = []
    while True:
        text = input()
        if text.upper() == "EXIT":
            break
        diary.append(text)

    print("\n ____YOUR SAVED DIARY____")
    for line in diary:
        print(line)
    print("_________________________")

def main():
    # Step 1: Set password each time
    set_pwd = input("Set a password for this session: ")

    # Step 2: Ask to confirm password
    check_pwd = input("Enter password to unlock diary: ")

    if set_pwd == check_pwd:
        open_diary()
    else:
        print("Wrong password! Access denied.")

main()