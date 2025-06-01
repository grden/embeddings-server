def normalize_spaces(text: str) -> str:
    # Replace non-breaking spaces and zero-width spaces with regular space, and strip
    return text.replace('\u00A0', ' ').replace('\u200B', '').strip()