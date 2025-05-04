def count_words(text):
    num_words = len(text.split())
    return f"Found {num_words} total words"

def get_characters_counts(text):
    stats = {}

    for character in text:
        character = character.lower()

        if character in stats:
            stats[character] += 1
        if character not in stats:
            stats[character] = 1

    return stats

def get_sorted_list_of_characters(characters_stats):
    list_of_characters = [
        {"char": char, "num": num}
        for char, num in characters_stats.items()
    ]

    list_of_characters.sort(key=lambda char: char.get("num"), reverse=True)

    return list_of_characters