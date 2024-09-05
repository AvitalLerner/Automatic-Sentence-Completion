from pygtrie import Trie
import zipfile
import nltk
"""
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
"""


def parse_zip_and_populate_trie(zip_file_path: str) -> Trie:
    """Parses a ZIP file, extracts sentences from text files, and builds a Trie,
    storing information about the file and line number for each sentence.

    Args:
        zip_file_path (str): Path to the ZIP file.

    Returns:
        Trie: The populated Trie tree.
    """

    trie = Trie()
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        for file_info in zip_ref.infolist():
            if file_info.filename.endswith(".txt"):  # Filter for text files
                with zip_ref.open(file_info) as file:
                    text = file.read().decode('utf-8')  # Decode to string
                    lines = text.splitlines()  # Split into lines
                    for line_number, line in enumerate(lines, 1):  # Start line numbers from 1
                        sentences = nltk.sent_tokenize(line)
                        for sentence in sentences:
                            # Store file and line number information
                            trie[sentence.lower()] = (file_info.filename, line_number)
                break
    return trie
