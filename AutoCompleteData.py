from dataclasses import dataclass
from typing import List


@dataclass
class AutoCompleteData:
    completed_sentence: str
    source_text: str
    offset: int
    score: int


def sort_autocomplete_data(data_list: List[AutoCompleteData]) -> List[AutoCompleteData]:
    # Sort the list in-place by the score field in descending order
    return sorted(data_list, key=lambda x: x.score, reverse=True)
