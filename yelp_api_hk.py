from flask import Flask, render_template, request, app
app = Flask(__name__)


from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator

import os

# from dotenv import load_dotenv, find_dotenv
# load_dotenv(find_dotenv())

def get_business(location, type1):
	auth = Oauth1Authenticator(
	consumer_key=os.environ['CONSUMER_KEY'],
	consumer_secret=os.environ['CONSUMER_SECRET'],
	token=os.environ['TOKEN'],
	token_secret=os.environ['TOKEN_SECRET']
	)

	client = Client(auth)

	params = {
		'term': type1,
		'lang': 'en',
		'limit': 3
	}

	response = client.search(location, **params)

	businesses = []

	# print("In {} we find the following top 10 {} businesses with ratings: ".format (location,type1))
	for business in response.businesses:
		businesses.append({"name": business.name,
		 "rating": business.rating,
		  "phone": business.phone})

		# print (business.name, business.rating)
	return businesses


@app.route('/')
def index():
	city_nbiz = None
	city_nbiz = request.values.get('city_nbiz')
	bizrecs = None
	if city_nbiz:
		if len(city_nbiz.split()) == 2:
			city_nbiz,type1 = city_nbiz.split(" ")
			bizrecs = get_business(city_nbiz,type1)
	return render_template('index.html', city_nbiz=city_nbiz, bizrecs=bizrecs)


@app.route('/about')
def about():
	return render_template('about.html')

if __name__ == "__main__":
	port = int(os.environ["Port", 5000])
	app.run(host="0.0.0.0", port=port)

# location = input ("What is your city: ")
# type1 = input ("What type of business? ")

# businesses = get_business(location,type1)

# name = 'name'
# rating = 'rating'
# phone = 'phone'

# print (businesses[0][name])


# for numb in range(0,3):
# 	print ("{} : {} : {}" .format (businesses[numb][name],
# 		businesses[numb][rating], 
# 		businesses[numb][phone])
# 	)

	

# print (businesses)



