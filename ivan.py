# Count Words Longer Than Five Characters

def words_counter(a):
    words = a.split()
    count = 0
    for word in words:
        if len(word) > 4:
            count += 1
    return print(f"Number of words longer than five characters: {count}")

a = input("Please enter your text: ")
words_counter(a)