percentages = {"100%": "1/1", "50%": "1/2", "25%": "1/4"}
percentage = input("please enter a percentage")
fraction = []
for word in percentage:
    if word in percentages:
        fraction.append(percentages[word])
    else:
        fraction.append(word)
print("the fraction is", " ".join(fraction))