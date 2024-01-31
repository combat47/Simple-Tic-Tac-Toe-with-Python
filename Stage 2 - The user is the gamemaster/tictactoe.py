user_input = input()
game_display = [list(user_input[:3]), list(user_input[3:6]), list(user_input[6:9])]

print("---------")
for elem in game_display:
    print("|", " ".join(elem), "|")
print("---------")
