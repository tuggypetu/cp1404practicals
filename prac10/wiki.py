"""Wikipedia API and Python Library"""

import warnings
import wikipedia


def main():
    """Get wiki summary of input title"""
    warnings.catch_warnings()

    warnings.simplefilter("ignore")
    title = input("Enter title of Wikipedia page: ").lower()
    while title != "":
        try:
            page = wikipedia.page(title, auto_suggest=False)
            print(page.title)
            print(page.url)
            print(page.summary)

        except wikipedia.exceptions.DisambiguationError as error:
            print(f"\nThe options for title '{title.title()}' are:\n", error.options, '\n')
            new_page_name = wikipedia.page(error.options[0], auto_suggest=False)
            print(f"Page title is assumed to be '{new_page_name.title}'. It could possibly need a more specific title.")
            print(new_page_name.url, '\n', wikipedia.summary(error.options[0]))
        except wikipedia.exceptions.PageError:
            print("No such Wikipedia page.")

        print()
        title = input("Enter title of Wikipedia page: ").lower()
    print("The end.")


main()
