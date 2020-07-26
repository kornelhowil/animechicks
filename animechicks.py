from flask import Flask, render_template, url_for, session
import random, os, pickle

app = Flask(__name__)

def top_5():
	chicks = []
	for file in os.listdir('pickles'):
		if not file.startswith('.'):
			with open('pickles/'+file, 'rb') as dbfile:
				print(file)
				x = pickle.load(dbfile)
				chicks.append(x)

	sortedchicks = sorted(chicks, key=lambda i: i['count'], reverse=True)
	return sortedchicks[0], sortedchicks[1], sortedchicks[2], sortedchicks[3], sortedchicks[4]


@app.route('/vote/<direction>')
def click(direction):
	girl = session['girl1'] if direction == 'left' else session['girl2']

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

	session['girl1'] = girl1
	session['girl2'] = girl2

	with open('pickles/'+girl1, 'rb') as dbfile:
		chick1 = pickle.load(dbfile)
		print(chick1['count'])

	with open('pickles/'+girl2, 'rb') as dbfile:
		chick2 = pickle.load(dbfile)
		print(chick2['count'])

	top1, top2, top3, top4, top5 = top_5()

	return render_template('index.html', the_chick1=chick1,
										 the_chick2=chick2,
										 the_top1 = top1,
										 the_top2 = top2,
										 the_top3 = top3,
										 the_top4 = top4,
										 the_top5 = top5)

app.secret_key = 'hdwhi3682bjd2'

if __name__ == '__main__':
	app.run(debug=True)