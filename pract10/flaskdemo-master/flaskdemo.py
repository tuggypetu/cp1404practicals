from flask import Flask, render_template, request, redirect, url_for, session
import wikipedia

app = Flask(__name__)
# Set the secret key. Keep this really secret:
app.secret_key = 'IT@JCUA0Zr98j/3yXa R~XHH!jmN]LWX/,?RT'


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/search', methods=['POST', 'GET'])
def search():
    if request.method == 'POST':
        session['search_term'] = request.form['search']
        return redirect(url_for('results'))
    return render_template("search.html")


@app.route('/results')
def results():
    search_term = session['search_term']
    page = get_page(search_term)
    return render_template("results.html", page=page)


def get_page(search_term):
    try:
        page = wikipedia.page(search_term, auto_suggest=False)
        print(page.title)
        print(page.url)
        # print(page.summary)

    except wikipedia.exceptions.DisambiguationError:

        page_titles = wikipedia.search(search_term)
        if page_titles[0] != search_term.title():
            title_new = page_titles[0]
        elif page_titles[1].lower() == page_titles[0].lower():
            title_new = page_titles[2]
        else:
            title_new = page_titles[1]
        # print(title_new)
        print(f"\nThe options for title '{search_term.title()}' are:\n", page_titles, '\n')
        page = wikipedia.page(title_new, auto_suggest=False)
        print(f"Page title is assumed to be '{page.title}'. It could possibly need a more specific title.")
        # print(page.url, '\n', wikipedia.summary(title_new))
    except wikipedia.exceptions.PageError:
        page = wikipedia.page(wikipedia.random())
    # try:
    #     page = wikipedia.page(search_term, auto_suggest=False)
    # except wikipedia.exceptions.DisambiguationError:
    #     # this is a disambiguation page, get the first real page (close enough)
    #     page_titles = wikipedia.search(search_term)
    #     print(page_titles)
    #     print(search_term.title())
    #     # sometimes the next page has the same name (different caps), so don't try the same again
    #     if page_titles[0] != search_term.title():
    #         title = page_titles[0]
    #     elif page_titles[1].lower() == page_titles[0].lower():
    #         title = page_titles[2]
    #     else:
    #         title = page_titles[1]
    #     print(title)
    #     print(wikipedia.page(title, auto_suggest=False))
    #     page = get_page(wikipedia.page(title, auto_suggest=False))
    # except wikipedia.exceptions.PageError:
    #     # no such page, return a random one
    #     page = wikipedia.page(wikipedia.random())
    print()
    return page


if __name__ == '__main__':
    app.run()
