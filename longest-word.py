def longest_word(sentence):
    words = sentence.split(" ")
    longest = ""
    for w in words:
        if len(w) >= len(longest):
            longest = w
    return longest


sentence = "Hola amigos de youtube"

longest = longest_word(sentence)
print(longest)
