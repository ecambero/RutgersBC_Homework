from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars
import pymongo


app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

# connect to mongo db and collection
db = client.mars_scrape

# Or set inline
# mongo = PyMongo(app, uri="mongodb://localhost:27017/craigslist_app")


@app.route("/")
def index():
    scrape_mars.scrape()
    return render_template("scraping.html")

@app.route("/scrape")
def scraper():
    article = list(db.marsnews.find())
    feature_img = list(db.marsimg.find())
    print(article)
    return render_template("index.html", article=article, feature_img=feature_img)



if __name__ == "__main__":
    app.run(debug=True)
