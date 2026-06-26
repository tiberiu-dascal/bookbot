def get_num_words(text) -> int:
    words = text.split()
    return len(words)


def characters_count(text: str) -> dict[str:int]:
    characters_counter = {}
    characters = list(text)
    for char in characters:
        char = char.lower()
        if char not in characters_counter:
            characters_counter[char] = 1
        else:
            characters_counter[char] += 1
        # print(characters_counter)
    return characters_counter


def count_words(text):
    words = text.split()
    return len(words)
