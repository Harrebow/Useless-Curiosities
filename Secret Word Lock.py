exit_word = "test"
count = 0
user_word = 0

while user_word != exit_word:
    if user_word == exit_word:
        print("You've successfully left the loop.")
        break
    else:
        count += 1
        if count <= 3:
            user_word = (input("Please enter the Secret exit word: "))
        else:
            print("You've entered the Secret word incorrectly 3 times. You have now been locked out of the system.")
            break

print("Goodbye")
