from io import BytesIO
from flask import Flask, jsonify
import os

import tweepy
from dotenv import load_dotenv
from flask import request,jsonify
import snscrape.modules.twitter as snstwitter
import requests
from goose3 import Goose
from wordcloud import WordCloud, STOPWORDS
import plotly.graph_objs as go
import json
import plotly
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import base64
import pandas as pd
# from flask import send_file
from flask import send_file


app = Flask(__name__)


@app.route('/twitter')
def index():
    query = "anna"
    retweet = 0
    likecount = 0
    hashtags = set([])
    i=0
    for tweet in snstwitter.TwitterSearchScraper(query).get_items(): 
        likecount += tweet.likeCount
        retweet += tweet.retweetCount + tweet.quoteCount
        if(tweet.hashtags != None):
            for h in tweet.hashtags:
                hashtags.add(h)
        
        i+= 1
        
        if(i==200):
            break
        
    tweets = [{"likecount":likecount,"retweet":retweet,"hashtags":list(hashtags),"count":i}]
    
    return jsonify({'result':tweets})


@app.route('/xyz')
def xyz():
    query = "AksNema"
    tweets = []
    for tweet in snstwitter.TwitterProfileScraper(query).get_items():
        tweets.append(tweet.date)
    return 



API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
headers = {"Authorization": "Bearer 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"}
API_URL_PROP = "https://api-inference.huggingface.co/models/valurank/distilroberta-propaganda-2class"



def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

def queryprop(payload):
	response = requests.post(API_URL_PROP, headers=headers, json=payload)
	return response.json()



@app.route('/sentiment')
def sentiment():
    query = request.args['query']
    retweet = 0
    likecount = 0
    hashtags = []
    senti=[]
    i=0
    positive=0
    negative=0
    neutral=0

    for tweet in snstwitter.TwitterSearchScraper(query).get_items(): 
        if tweet.lang=="en":
            i+=1
            if(i==200):
                break
            sentence= tweet.rawContent
            print(sentence)
            sid_obj = SentimentIntensityAnalyzer()
            sentiment_dict = sid_obj.polarity_scores([sentence])
            print(sentiment_dict['neg']*100, "% Negative")
            print(sentiment_dict['pos']*100, "% Positive")
            print("Review Overall Analysis", end = " ") 
            if sentiment_dict['compound'] >= 0.05 :
                positive+=1
            elif sentiment_dict['compound'] <= -0.05 :
                negative+=1
            else :
                neutral+=1
    senti=[positive, negative, neutral]
            
        
    return jsonify({"result":senti})
            
@app.route('/sentiment_article')
def sentiment_article():
    url = request.args['url']
    goose = Goose()
    articles = goose.extract(url)
    output = articles.cleaned_text


    for tweet in snstwitter.TwitterSearchScraper(query).get_items(): 
        if tweet.lang=="en":
            i+=1
            if(i==200):
                break
            sentence= tweet.rawContent
            print(sentence)
            sid_obj = SentimentIntensityAnalyzer()
            sentiment_dict = sid_obj.polarity_scores([sentence])
            print(sentiment_dict['neg']*100, "% Negative")
            print(sentiment_dict['pos']*100, "% Positive")
            print("Review Overall Analysis", end = " ") 
            if sentiment_dict['compound'] >= 0.05 :
                positive+=1
            elif sentiment_dict['compound'] <= -0.05 :
                negative+=1
            else :
                neutral+=1
    senti=[positive, negative, neutral]
            
        
    return jsonify({"result":senti})

    






@app.route('/news')
def news():
    url = request.args['url']
    goose = Goose()
    articles = goose.extract(url)
    output = query({
	"inputs":  articles.cleaned_text
    })
    print(output)
    
    return output[0]['summary_text']

@app.route('/cloud2')
def plotly_wordcloud2():
    url = request.args['url']
    goose = Goose()
    articles = goose.extract(url)
    text = articles.cleaned_text
    wordcloud = WordCloud(width=1280, height=853, margin=0,
                      colormap='Blues').generate(text)
    wordcloud.to_file("./wordcloud.png")
    # plt.imshow(wordcloud, interpolation='bilinear')
    # plt.axis('off')
    # plt.margins(x=0, y=0)
    # # plt.show()
    # # img = BytesIO()

    # plt.savefig("./wordcloud.png", format='png')
    # plt.imsave("./wordcloud.png", format='png')
    # img.seek(0)
    # # nimg = Image.frombytes("RGBA", (128, 128), img, 'raw')
    # nimg = Image.frombuffer(img)
    # nimg.save("./wordcloud.png")
    # plot_url = base64.b64encode(img.getvalue()).decode('utf8')
    return send_file("./wordcloud.png", mimetype='image/png')
    # return render_template('plot.html', plot_url=plot_url)

# @app.route('/cloud')
# def plotly_wordcloud():
#     url = 'https://blogs.jayeshvp24.dev/dive-into-web-design'
#     goose = Goose()
#     articles = goose.extract(url)
#     text = query({
# 	"inputs":  articles.cleaned_text
#     })
#     wc = WordCloud(stopwords = set(STOPWORDS),
#                    max_words = 200,
#                    max_font_size = 100)
#     wc.generate(text[0]['summary_text'])
@app.route('/propaganda')
def propaganda():
    url = request.args['url']
    goose = Goose()
    articles = goose.extract(url)
    output = queryprop({
	"inputs":  articles.cleaned_text[0:600]
    })
    
    num = str(output[0][0]['score'])
    return num

	

@app.route('/cloud')
def plotly_wordcloud():
    url = request.args['url']
    goose = Goose()
    articles = goose.extract(url)
    text = query({
	"inputs":  articles.cleaned_text
    })
    wc = WordCloud(stopwords = set(STOPWORDS),
                   max_words = 200,
                   max_font_size = 100)
    wc.generate(text[0]['summary_text'])
    
#     word_list=[]
#     freq_list=[]
#     fontsize_list=[]
#     position_list=[]
#     orientation_list=[]
#     color_list=[]

#     for (word, freq), fontsize, position, orientation, color in wc.layout_:
#         word_list.append(word)
#         freq_list.append(freq)
#         fontsize_list.append(fontsize)
#         position_list.append(position)
#         orientation_list.append(orientation)
#         color_list.append(color)
        
#     # get the positions
#     x=[]
#     y=[]
#     for i in position_list:
#         x.append(i[0])
#         y.append(i[1])
            
#     # get the relative occurence frequencies
#     new_freq_list = []
#     for i in freq_list:
#         new_freq_list.append(i*100)
#     new_freq_list
    
#     trace = go.Scatter(x=x, 
#                        y=y, 
#                        textfont = dict(size=new_freq_list,
#                                        color=color_list),
#                        hoverinfo='text',
#                        hovertext=['{0}{1}'.format(w, f) for w, f in zip(word_list, freq_list)],
#                        mode='text',  
#                        text=word_list
#                       )
    
#     layout = go.Layout({'xaxis': {'showgrid': False, 'showticklabels': False, 'zeroline': False},
#                         'yaxis': {'showgrid': False, 'showticklabels': False, 'zeroline': False}})
    
#     fig = go.Figure(data=[trace], layout=layout)
#     graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
#     print(graphJSON)
#     print(type(fig))
#     return graphJSON

@app.route('/authenticity')
def auth():
    name = request.args['name']
    lis = []
    df = pd.read_csv('blacklist.csv')
    for i in range(len(df)):
        lis.append(i)
    
    if name in lis:
        return {
            "result": True  
        }

    return { "result": False }


if __name__ == '__main__':
    app.run(debug=True)
