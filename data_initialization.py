

import nltk
import zipfile
from pygtrie import Trie
import os


def parse_zip_and_populate_trie(zip_file_path):
    """Parses a ZIP file, extracts sentences from text files, and builds a Trie.

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
                    sentences = nltk.sent_tokenize(text)  # Tokenize into sentences
                    for sentence in sentences:
                        # Add sentences to the Trie
                        trie[sentence.lower()] = 1  # Using '1' as a placeholder value

                #break # check at the start only one txt file

    return trie


def main():
    zip_file_path = os.path.join("data", "Archive (2).zip")
    trie_tree = parse_zip_and_populate_trie(zip_file_path)
    print(trie_tree)
