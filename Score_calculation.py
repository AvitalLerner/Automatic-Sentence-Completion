import re
from Levenshtein import editops
import Levenshtein as lev


def find_closest_substring(sentence: str, query: str) -> str:
    # Initialize
    best_match = None
    min_distance = float('inf')

    # Iterate over all possible substrings of the sentence
    for i in range(len(sentence)):
        for j in range(i, len(sentence) + 1):
            substring = sentence[i:j]
            # Skip substrings that are too different in length
            if abs(len(substring) - len(query)) > 1:
                continue
            # Calculate the Levenshtein distance
            distance = lev.distance(substring, query)
            # Check if this is the best match so far with at most one edit
            if distance <= 1 and distance < min_distance:
                best_match = substring
                min_distance = distance

    # If no match found within edit distance 1, return None
    return best_match


def calculate_score(sentence: str, query: str) -> int:
    # Normalize input: remove punctuation and extra spaces
    def normalize(text):
        return re.sub(r'\s+', ' ', re.sub(r'[^\w\s]', '', text.lower())).strip()

    query = normalize(query)
    sentence = normalize(sentence)

    # print("\n")
    # print(query)
    # print(sentence)

    best_substring = find_closest_substring(sentence, query)
    # print(best_substring)
    matching_chars = sum(1 for a, b in zip(best_substring, query) if a == b)
    base_score = matching_chars * 2
    # print(base_score)

    # Get edit operations
    operations = editops(query, best_substring)

    # Calculate score reductions
    score_reduction = 0
    for op, pos_query, pos_sentence in operations:
        if op == 'replace':
            if pos_query < 5:
                score_reduction += 5 - pos_query
            else:
                score_reduction += 1
        elif op in ('insert', 'delete'):
            if pos_query < 4:
                score_reduction += 10 - 2 * pos_query
            else:
                score_reduction += 2

    # print(base_score, '-', score_reduction)
    # Calculate final score
    final_score = max(0, base_score - score_reduction)

    return final_score
