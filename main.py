from typing import List

from Score_calculation import calculate_score
from initialization_data import parse_zip_and_populate_trie
from AutoCompleteData import AutoCompleteData
from search import search_trie
import os

NUM_COMPLETIONS = 5
sentence_database = []


def get_top_auto_completions(data: List[AutoCompleteData]) -> List[AutoCompleteData]:
    top = sorted(data, key=lambda x: (-x.score, x.source_text))[:NUM_COMPLETIONS]
    return top


def get_best_k_completions(prefix: str) -> List[AutoCompleteData]:
    # חיפוש כל ההתאמות
    all_completions = search_trie(sentence_database, prefix)  # מחזירה רשימה של AutoCompleteData
    print("len list all completion:", len(all_completions))

    # ניקוד
    for sentence in all_completions:
        score = calculate_score(sentence.completed_sentence, prefix)
        sentence.score = score

    # מיון ובחירת 5 הכי מתאימים
    # Sort the dictionary items by value in descending order
    all_completions_sort = AutoCompleteData.sort_autocomplete_data(all_completions)
    top_five = get_top_auto_completions(all_completions_sort)
    return top_five


def main():
    print("Loading the files and preparing the system...")

    # private case
    """
    file_path = 'docs-aiohttp-org-en-v3.0.1.txt'
    result = parse_sentences_from_file(file_path)
    """

    zip_file_path = "C://Excellenteam//google project//Automatic-Sentence-Completion//data//Archive.zip"
    global sentence_database
    sentence_database = parse_zip_and_populate_trie(zip_file_path)

    print("The system is ready. Enter your text:")

    query = ""
    while True:
        user_input = input()

        if user_input == '#':
            query = ""
            continue
        else:
            query = user_input + query

        list_five_best_completions = get_best_k_completions(query)

        print("Here are 5 suggestions:")
        for index, item in enumerate(list_five_best_completions, start=1):
            print(f"{index}. {item}")


if __name__ == "__main__":
    main()
