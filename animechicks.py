from flask import Flask, render_template
import random, os
import pickle

app = Flask(__name__)

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
		print(girl1)
		chick1 = pickle.load(dbfile)

	with open('pickles/'+girl2, 'rb') as dbfile:
		print(girl2)
		chick2 = pickle.load(dbfile)


	return render_template('index.html', the_title='Anime Chicks',
										 the_path1=chick1['image'],
										 the_path2=chick2['image'])

if __name__ == '__main__':
	app.run(debug=True)