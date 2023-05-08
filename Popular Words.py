def popular_words(text: str, words: list) -> dict:
    # your code here
    result = {word: 0 for word in words}

    for word in text.lower().split():
        if word in words:
            result[word] += 1
    return result


print("Example:")
print(
    popular_words(
        """
When I was One
I had just begun
When I was Two
I was nearly new
""",
        ["i", "was", "three", "near"],
    )
)
