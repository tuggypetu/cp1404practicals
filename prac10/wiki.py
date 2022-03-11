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

        except wikipedia.exceptions.DisambiguationError:

            page_titles = wikipedia.search(title)
            if page_titles[0] != title.title():
                title_new = page_titles[0]
            elif page_titles[1].lower() == page_titles[0].lower():
                title_new = page_titles[2]
            else:
                title_new = page_titles[1]
            # print(title_new)
            print(f"\nThe options for title '{title.title()}' are:\n", page_titles, '\n')
            new_page_name = wikipedia.page(title_new, auto_suggest=False)
            print(f"Page title is assumed to be '{new_page_name.title}'. It could possibly need a more specific title.")
            print(new_page_name.url, '\n', wikipedia.summary(title_new))
        except wikipedia.exceptions.PageError:
            print("No such Wikipedia page.")

        print()
        title = input("Enter title of Wikipedia page: ").lower()
    print("The end.")


main()
