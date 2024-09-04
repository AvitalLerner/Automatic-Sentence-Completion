from initialization_data import parse_sentences_from_file
import AutoCompleteData


def main():
    print("Loading the files and preparing the system...")

    # private case
    file_path = 'docs-aiohttp-org-en-v3.0.1.txt'
    result = parse_sentences_from_file(file_path)

    print("The system is ready. Enter your text:")

    query = ""
    while True:
        user_input = input()

        if user_input == '#':
            query = ""
        else:
            query = user_input + query

    list_five_best_completions = get_best_k_completions(query)
    print("Here are 5 suggestions:")
    for index, item in enumerate(list_five_best_completions, start=1):
        print(f"{index}. {item}")


if __name__ == "__main__":
    main()
