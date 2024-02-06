import nltk
from textblob import TextBlob
import tkinter as tk
from newspaper import Article


def summarize():
    url = utext.get("1.0", "end").strip()
    article = Article(url)

    article.download()
    article.parse()
    article.nlp()

    title.config(state="normal")
    author.config(state="normal")
    pub_date.config(state="normal")
    seentiment.config(state="normal")
    summary.config(state="normal")

    title.delete("1.0", "end")
    title.insert("1.0", article.title)

    author.delete("1.0", "end")
    author.insert("1.0", article.authors)

    pub_date.delete("1.0", "end")
    pub_date.insert("1.0", article.publish_date)

    summary.delete("1.0", "end")
    summary.insert('1.0', article.summary)

    analysis = TextBlob(article.text)
    seentiment.delete("1.0", "end")
    # seentiment.insert(f"sentiment" : "positive" if {analysis.polarity>0} else "negative" if {analysis.polarity<} else "neutral")

    title.config(state="disabled")
    author.config(state="disabled")
    pub_date.config(state="disabled")
    seentiment.config(state="disabled")
    summary.config(state="disabled")


root = tk.Tk()
root.title("Text summarizer tool")
root.geometry('1200x600')

tlabel = tk.Label(root, text="Title")
tlabel.pack()

title = tk.Text(root, height=2, width=140)
title.config(state="disabled", bg="#dddddd")
title.pack()

alabel = tk.Label(root, text="Author")
alabel.pack()

author = tk.Text(root, height=2, width=140)
author.config(state="disabled", bg="#dddddd")
author.pack()

plabel = tk.Label(root, text="Publication Date")
plabel.pack()

pub_date = tk.Text(root, height=2, width=140)
pub_date.config(state="disabled", bg="#dddddd")
pub_date.pack()

slabel = tk.Label(root, text="summary")
slabel.pack()
summary = tk.Text(root, height=8, width=140)
summary.config(state="disabled", bg="#dddddd")
summary.pack()
setlabel = tk.Label(root, text="Sentiment")
setlabel.pack()
seentiment = tk.Text(root, height=2, width=140)
seentiment.config(state="disabled", bg="#dddddd")
seentiment.pack()
ulabel = tk.Label(text="URL")
ulabel.pack()
utext = tk.Text(root, height=2, width=140)
utext.pack()
btn = tk.Button(root, text="Summarize",command=summarize)
btn.pack()
root.mainloop()

summarize()
