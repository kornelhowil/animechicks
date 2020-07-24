import pickle

Makise = {	'name': 'Makise Kurisu',
			'url': 'https://myanimelist.net/character/34470/Kurisu_Makise',
			'image': '/static/images/1.jpg',
			'count': 0}

Rem = {	'name': 'Rem',
			'url': 'https://myanimelist.net/character/118763/Rem',
			'image': '/static/images/2.jpg',
			'count': 0}

Mikasa = {	'name': 'Mikasa Ackerman',
			'url': 'https://myanimelist.net/character/40881/Mikasa_Ackerman',
			'image': '/static/images/3.jpg',
			'count': 0}

Hitagi = {	'name': 'Hitagi Senjougahara',
			'url': 'https://myanimelist.net/character/22037/Hitagi_Senjougahara',
			'image': '/static/images/4.jpg',
			'count': 0}

Yuno = {	'name': 'Yuno Gasai',
			'url': 'https://myanimelist.net/character/4963/Yuno_Gasai',
			'image': '/static/images/5.jpg',
			'count': 0}

Megumin = {	'name': 'Megumin',
			'url': 'https://myanimelist.net/character/117225/Megumin',
			'image': '/static/images/6.jpg',
			'count': 0}

Taiga = {	'name': 'Taiga Aisaka',
			'url': 'https://myanimelist.net/character/12064/Taiga_Aisaka',
			'image': '/static/images/7.jpg',
			'count': 0}


Saber = {	'name': 'Saber',
			'url': 'https://myanimelist.net/character/497/Saber',
			'image': '/static/images/8.jpg',
			'count': 0}

Shinobu = {	'name': 'Shinobu Oshino',
			'url': 'https://myanimelist.net/character/23602/Shinobu_Oshino',
			'image': '/static/images/9.jpg',
			'count': 0}

Asuna = {	'name': 'Asuna Yuuki',
			'url': 'https://myanimelist.net/character/36828/Asuna_Yuuki',
			'image': '/static/images/10.jpg',
			'count': 0}

Holo = {	'name': 'Holo',
			'url': 'https://myanimelist.net/character/7373/Holo',
			'image': '/static/images/11.jpg',
			'count': 0}

Yukinoshita = {	'name': 'Yukino Yukinoshita',
			'url': 'https://myanimelist.net/character/67067/Yukino_Yukinoshita',
			'image': '/static/images/12.jpg',
			'count': 0}

Homura = {	'name': 'Homura Akemi',
			'url': 'https://myanimelist.net/character/38005/Homura_Akemi',
			'image': '/static/images/13.jpg',
			'count': 0}

ZeroTwo = {	'name': 'Zero Two',
			'url': 'https://myanimelist.net/character/155679/Zero_Two',
			'image': '/static/images/14.jpg',
			'count': 0}

with open('pickles/makise.pickle', 'ab') as dbfile:
	pickle.dump(Makise, dbfile)  
	
with open('pickles/rem.pickle', 'ab') as dbfile:
	pickle.dump(Rem, dbfile) 

with open('pickles/mikasa.pickle', 'ab') as dbfile:
	pickle.dump(Mikasa, dbfile)      

with open('pickles/hitagi.pickle', 'ab') as dbfile:
	pickle.dump(Hitagi, dbfile)             

with open('pickles/yuno.pickle', 'ab') as dbfile:
	pickle.dump(Yuno, dbfile)  

with open('pickles/megumin.pickle', 'ab') as dbfile:
	pickle.dump(Megumin, dbfile) 

with open('pickles/taiga.pickle', 'ab') as dbfile:
	pickle.dump(Taiga, dbfile)

with open('pickles/saber.pickle', 'ab') as dbfile:
	pickle.dump(Saber, dbfile)                            

with open('pickles/shinobu.pickle', 'ab') as dbfile:
	pickle.dump(Shinobu, dbfile)     

with open('pickles/asuna.pickle', 'ab') as dbfile:
	pickle.dump(Asuna, dbfile)     

with open('pickles/holo.pickle', 'ab') as dbfile:
	pickle.dump(Holo, dbfile)     

with open('pickles/yukinoshita.pickle', 'ab') as dbfile:
	pickle.dump(Yukinoshita, dbfile)    

with open('pickles/homura.pickle', 'ab') as dbfile:
	pickle.dump(Homura, dbfile) 

with open('pickles/zerotwo.pickle', 'ab') as dbfile:
	pickle.dump(ZeroTwo, dbfile)   
