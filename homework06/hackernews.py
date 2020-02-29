from bottle import (
    route, run, template, request, redirect
)

from scraputils_wtf import get_news
from db_ehh import News, session
from bayes import NaiveBayesClassifier
import string

def clean(s):
    translator = str.maketrans("", "", string.punctuation)
    return s.translate(translator)

@route("/news")
def news_list():
    s = session()
    rows = s.query(News).filter(News.label == None).all()
    return template('news_template', rows=rows)


@route("/add_label/")
def add_label():
    ids = request.query.get("id")
    labels = request.query.get("label")
    s = session()
    for item in s.query(News).filter(News.id == ids).all():
        item.label = labels
    s.commit()
    redirect("/news")


@route("/update")
def update_news():
    news_lst = get_news('https://news.ycombinator.com/newest', 11)
    s = session()
    for i in range(len(news_lst)):
        if len(s.query(News).filter(News.title == news_lst[i]['title']).filter(News.author == news_lst[i]['author']).all()) == 0:
            new_news = News(title = news_lst[i]['title'],
                            author = news_lst[i]['author'],
                            points = news_lst[i]['points'],
                            comments = news_lst[i]['comments'],
                            url = news_lst[i]['url'])
            s.add(new_news)
    s.commit()
    redirect("/news")


@route("/classify")
def classify_news():
    s = session()
    labeled_news = s.query(News).filter(News.label != None).filter(News.id < 1001).all()
    x = [clean(news.title) for news in labeled_news]
    y = [news.label for news in labeled_news]
    classifier = NaiveBayesClassifier(1)
    classifier.fit(x, y)
    rows = s.query(News).filter(News.label == None).all()
    good, maybe, never = [], [], []
    for row in rows:
        row.title = clean(row.title)
        prediction = classifier.predict([row.title])
        print(prediction)
        if prediction == ['good']:
            good.append(row)
        elif prediction == ['maybe']:
            maybe.append(row)
        else:
            never.append(row)
     return template('news_recommendations', good=good, maybe=maybe, never=never)

if __name__ == "__main__":
    run(host="localhost", port=8080)
