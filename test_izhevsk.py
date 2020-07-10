# Python 3.7.4
import re
text_body = input('Введите текст:\n')
search_text = list(map(str, input('Введите поисковую строку:\n').split()))


# Find all words that match the words in search_text
def get_search_matches(search_words, text_content):
    search_matches = [
        re.findall(rf'[-\w]*{search_word}[-\w]*', text_content)
        for search_word in search_words
    ]

    # Flat the list of lists of matching words (word groups).
    # Each list in search_matches is the group of words from text_body
    # that match a single word from search_matches.
    search_matches = [
        word
        for matching_group in search_matches
        for word in matching_group
    ]
    return set(search_matches)  # Some words are found twice and being repeated. Take one of each match.


# Replace each found match with word wrapped in a tag.
def add_tags(words_to_wrap, text_content, tag='b'):
    for word in words_to_wrap:
        text_content = re.sub(rf'\b{word}\b', f'<{tag}>{word}</{tag}>', text_content)
    return text_content


matches = get_search_matches(search_text, text_body)
text_body = add_tags(matches, text_body)

print(text_body)
