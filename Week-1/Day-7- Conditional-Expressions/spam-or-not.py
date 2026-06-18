# write a code to check msg is spam or not 

message = input("Enter message: ").lower()

if "free" in message or "win" in message or "lottery" in message or "prize" in message:
    print("Spam")
else:
    print("Not Spam")
