
import time
from AutoCompleteData import AutoCompleteData



def search_trie(trie, search_string):
    """Searches the Trie for sentences containing the search string and returns
    a list of AutoCompleteData instances.

    Args:
        trie (Trie): The Trie object (already compressed with data).
        search_string (str): The string to search for.

    Returns:
        list: A list of AutoCompleteData instances containing the search string.
    """

    results = []
    start_time = time.time()

    for sentence, data in trie.items(search_string):
        # Assume sentence is a list of characters, join it into a string
        sentence = ''.join(sentence)
        source_text, offset = data
        results.append(AutoCompleteData(
            completed_sentence=sentence,
            source_text=source_text,
            offset=offset,
            score=0
        ))
    end_time = time.time()
    print(f"Trie Search: {end_time - start_time:.4f} seconds")

    return results