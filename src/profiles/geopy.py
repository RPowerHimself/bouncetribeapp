from geopy import geocoders

g = geocoders.GoogleV3()


def find():
	print "What would you like to search?"
	query = raw_input()

	place = g.geocode(query)

	return place