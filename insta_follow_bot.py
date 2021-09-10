from instapy import InstaPy 
from instapy import smart_run
from time import sleep
import sys
 
# credencials de la meva conta 
my_username = 'atlastrok'
my_password = 'libertad200821'

#variable session que permet obrir el insta segons les credencials
session = InstaPy(username = my_username,
                  password = my_password,
                  headless_browser = False)

#execució del log in i busqueda d'usuaris segons followers/following.... donar like, agregar i comentar post segons 'tags' n=20
with smart_run(session):
    session.set_relationship_bounds(enabled=True,
                                    delimit_by_numbers=True,
                                    max_followers=300,
                                    min_followers=30,
                                    min_following=30)

    session.set_do_follow(True, percentage=100)
    session.set_dont_like(['nsfw', 'loli', 'fight'])
    session.set_do_comment(enabled=True, percentage=100)
    session.set_comments(['This is awesome!', 'Really Cool :)', 'I like your stuff!', 'such a great illustration!'])

    session.like_by_tags(['artmash', 'digitalart', 'procreate', 'art', 'creativity'], amount=20)

#tancar algoritme
sys.exit()