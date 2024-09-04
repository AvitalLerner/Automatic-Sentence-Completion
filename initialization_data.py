from typing import List


def parse_sentences_from_file(file_path: str) -> List[str]:
    sentences: List[str] = []

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                cleaned_sentence = line.strip()
                if cleaned_sentence:
                    sentences.append(cleaned_sentence)

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except IOError:
        print(f"Error: There was an issue reading the file '{file_path}'.")

    return sentences

