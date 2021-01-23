import imdb as imdb  # to access imdb API
import pandas as pd  # for data array handling
from bs4 import BeautifulSoup  # for website parsing and scraping (rotten tomatoes)
import requests  # for http access
import re  # for regular expressions
# from ggplot import *  # for plotting
# import urllib2  # for accessing url object (movie covers)
import urllib

import matplotlib.pyplot as plt  # for plotting
from matplotlib.offsetbox import (OffsetImage, AnnotationBbox)


ia = imdb.IMDb()  # create imdb API object


# all_rudds = ia.search_person('Paul Rudd')
# for i in range(len(all_rudds)): 
#     print(all_rudds[i]['name'] + " : " + all_rudds[i].personID  ) 

paul_rudd_id = '0748620'

person_id = paul_rudd_id

actor = ia.get_person(person_id)
#actor.infoset2keys

#get films
filmography_super = ia.get_person_filmography(actor.personID)  
filmography_dict = filmography_super['data']['filmography'] # the role in the film. (other keys in data are #birth info', 'headshot', 'akas', 'filmography', 'imdbID', 'name', 'imdbIndex')




#some movie
filmography_dict['actor'] #list of the movies!
print(f"{actor['name']} acted in {len(filmography_dict['actor'])} movies")

movie_id = filmography_dict['actor'][5].movieID
movie = ia.get_movie(movie_id) ####
movie.current_info
print('\n\n')
movie.infoset2keys
movie['original title']

print('\n\n')

info_list = ['kind', 'rating', 'runtimes']
movie['kind'] #tv series vs...
'rating', 'runtimes',
#movie['cast']
movie['plot']
movie['year']
movie['rating']

#tv
movie['imdbID']
movie['series years']
movie['seasons']

#cast credit ordering is sometimes alphabetical or in order of appearance.  I can check for the former but not the latter (easily... maybe I can check if the famous folks are at the top -- famous = # of entries in their filmography)

[a['name'] for a in movie['cast']]

movie = ia.get_movie(movie_id,page=2) ###############brokeded
ia.update(movie, 'full credits') #request the API to update with the full credits if you cant find your actor

cast = [cast_member['name'] for cast_member in  movie['cast']]
alphabetical = all(cast[i] <= cast[i+1] for i in range(len(cast)-1)) #check if its sorted

idx = [idx for idx, cast_member in enumerate(movie['cast']) if cast_member['name']==actor['name']][0] #rank in the list of credits

#if the movie is a tv series we can fetch all the data for individual episodes!
ia.update(movie, 'episodes')
movie['episodes']

ia.update(actor, 'episodes')
actor.infoset2keys
actor['biography']['headshot']

actor['filmography']['actor'][5]