def count_characters(s):
    return len(s)


def count_words(s):
    return len(s.split())


def average_word_length(s):
    words = s.split()
    if not words:
        return 0
    return sum(len(word) for word in words) / len(words)


if __name__ == "__main__":
    text = "this is a test"
    print("Character count:", count_characters(text))
    print("Word Count:", count_words(text))
    print("Average word length:", average_word_length(text))
