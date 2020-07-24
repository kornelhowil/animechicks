from flask import Flask, render_template, url_for
import random, os, pickle

app = Flask(__name__)


@app.route('/chick1/<girl>')
def click(girl):
	with open('pickles/'+girl, 'rb') as dbfile:
		chick = pickle.load(dbfile)
		chick['count'] += 1

	with open('pickles/'+girl, 'wb') as dbfile:
		pickle.dump(chick, dbfile)   

	return entry_page()
		

@app.route('/')
def entry_page():
	files = os.listdir('pickles')
	while True:
		girl1 = random.choice(files)
		if girl1 != '.DS_Store':
			break
	while True:
		girl2 = random.choice(files)
		if girl2 != '.DS_Store' and girl2 != girl1:
			break

	with open('pickles/'+girl1, 'rb') as dbfile:
		chick1 = pickle.load(dbfile)
		print(chick1['count'])

	with open('pickles/'+girl2, 'rb') as dbfile:
		chick2 = pickle.load(dbfile)
		print(chick2['count'])

	return render_template('index.html', the_title='Anime Chicks',
										 the_chick1=chick1,
										 the_chick2=chick2,
										 the_girl1=girl1,
										 the_girl2=girl2)



if __name__ == '__main__':
	app.run(debug=True)