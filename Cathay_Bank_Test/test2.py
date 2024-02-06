def count_characters(text):
    character_count = {}

    for char in text:
        if char.isalnum():
            char_upper = char.upper()
            character_count[char_upper] = character_count.get(char_upper, 0) + 1
    return character_count


text = "Hello welcome to Cathay 60th year anniversary"

result = count_characters(text)

for char, count in sorted(result.items()):
    print(char + " " + str(count))
