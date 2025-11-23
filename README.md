def open\_diary():

&nbsp;   print("\\n \_\_\_PERSONAL DIARY\_\_\_ ")

&nbsp;   print("Type your diary entries below.")

&nbsp;   print("Type EXIT to save and close.\\n")



&nbsp;   diary = \[]

&nbsp;   while True:

&nbsp;       text = input()

&nbsp;       if text.upper() == "EXIT":

&nbsp;           break

&nbsp;       diary.append(text)



&nbsp;   print("\\n \_\_\_YOUR SAVED DIARY\_")

&nbsp;   for line in diary:

&nbsp;       print(line)

&nbsp;   print("\_")



def main():

&nbsp;   # Step 1: Set password each time

&nbsp;   set\_pwd = input("Set a password for this session: ")



&nbsp;   # Step 2: Ask to confirm password

&nbsp;   check\_pwd = input("Enter password to unlock diary: ")



&nbsp;   if set\_pwd == check\_pwd:

&nbsp;       open\_diary()

&nbsp;   else:

&nbsp;       print("Wrong password! Access denied.")



main()

