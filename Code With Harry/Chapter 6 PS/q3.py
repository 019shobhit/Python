# 3. A spam comment is defined as a text containing following keywords: “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program to detect these spams.

message = input("Enter your Message: ")
if("Make a lot of money" in message or "buy now" in message or "subscribe this" in message or "click this" in message):
    print("This is a Spam Message, So be Aware from this")
else:print("Their is not any kind of spam content")