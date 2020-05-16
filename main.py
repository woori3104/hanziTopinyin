import pinyin
import requests
from flask  import Flask, render_template, request
from googletrans import Translator


app = Flask('중국어 단어')

numberic_word = {}
pinyins = []
terms = {'Korean':'ko','English':'en','Chinese-Hans':'zh-Hans','Chinese-TW':'zh-TW','Japanese':'ja','Spanish':'ex'}

translator = Translator()
@app.route('/')
def home():
  numberic_word.clear()
  return render_template('home.html',terms=terms)

@app.route('/convert')
def convert():
  numberic_word.clear()
  word = request.args.get('word')
  term = request.args.get('term')
  chars = list(word)
  for char in chars:
    numberic = pinyin.get(char, format="numerical")
    try:
      if 0<int(numberic[-1]) and 5>int(numberic[-1]):
        numberic_word[char] = (pinyin.get(char), int(numberic[-1]))
        print (numberic_word[char])
      else:
        numberic_word[char] = (pinyin.get(char), 0)
        print (numberic_word[char][0])

    except :
      numberic_word[char] = '0'
      numberic_word[char] = (pinyin.get(char), 0)
  trans = translator.translate(word, dest=terms[term]).text
  src_lang = translator.detect(word).lang
  return render_template('convert.html', words=numberic_word,  trans = trans, dest = terms[term], src = src_lang )


app.run(host='0.0.0.0')