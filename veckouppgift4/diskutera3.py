#1h om ord har 5-7 bokstäver, lägg till i lista found, returnera found
def average_words(strings):
    found = []
    for item in strings:
        if 4 < len(item) < 8:
            found.append(item)
    return found

#average_words(["sup", "how's", "it", "going", "reflecting", "on", "programs", "and", "coding"])

print(average_words((["sup", "how's", "it", "going", "reflecting", "on", "programs", "and", "coding"])))