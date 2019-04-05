import flask
from flask import jsonify ,request,render_template
import google.cloud.translate as translate
import google.cloud.datastore as datastore
import os
import emoji 
from wtforms import Form, TextAreaField, validators
import pickle
import numpy as np

app = flask.Flask(__name__)

######## Preparing the Classifier
cur_dir = os.path.dirname(__file__)
#pkl_dir = os.path.join(cur_dir, 'pkl_objects')

try:
    d = open(os.path.join(cur_dir, 'label_encoder.p'), 'rb')
    le = pickle.load(d)
finally:
    d.close()

try:
    d = open(os.path.join(cur_dir, 'countv.p'), 'rb')
    vect = pickle.load(d)
finally:
    d.close()

try:
    d = open(os.path.join(cur_dir, 'clf_countv.p'), 'rb')
    clf = pickle.load(d)
finally:
    d.close()

def classify(document):
	x_vect = vect.transform([document])
	proba = np.max(clf.predict_proba(x_vect))
	pred = clf.predict(x_vect)
	label = le.inverse_transform(pred)
	return label, proba
	
######## Flask
class ReviewForm(Form):
	lyrics = TextAreaField('',[validators.DataRequired(), validators.length(min=15)])

@app.route('/api')
def home():
	form = ReviewForm(request.form)
	return render_template("home.html",form=form)
	
@app.route('/api/lyrics',methods=['POST'])
def api_lyrics():
	form = ReviewForm(request.form)
	if request.method == 'POST' and form.validate():
		text=request.form['lyrics']
		lyricsgiven=request.form['lyrics']
		abc=lyrics_translate(text)
		y, proba = classify(abc)
	else:
		return "lyrics empty"
	
	return render_template("home.html",form=form,y=y,probability=np.round(proba*100))

def lyrics_translate(lyrics):
	os.environ["GOOGLE_APPLICATION_CREDENTIALS"]= u"PRIVATE.json"
	client = datastore.Client()
	translate_client = translate.Client()
	target = 'En'
	translation = translate_client.translate(lyrics,target_language=target)
	translated_lyrics=u'Translation: {}'.format(translation['translatedText'])
	return translated_lyrics
	
	
if __name__ == '__main__':
	app.run(debug=True)