import tweepy, json, requests
from secrets import *
from tweepy.api import API
from tweepy import OAuthHandler
from tweepy import Stream
import time

auth = OAuthHandler(C_KEY, C_SECRET)
auth.secure = True
auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)
api = API(auth)


class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api=None):
        self.api = api or API()
        
        
    def on_conect(self):
    	print("Conectado")

    """    
    ->>>> Sirve para leer los twits en tiempo real de mi tl:
    def on_status(self, status):
    	try:
    		print("Imprimir tweets del tl\n\n\n")
    		print(status.text.encode('utf8'))
    		print("\n\n\n")
    		return True

    	except BaseException as e:
        	print("Fallo al enviar el tweets", str(e))
	"""
    def on_direct_message(self, data):
    	

    	print("\n")
    	nombre = data._json['direct_message']['sender']['name']
    	user_name = data._json['direct_message']['sender']['screen_name']
    	dm = data._json['direct_message']['text']
    	if user_name != 'anonymous_tuits':
    		try:
		    	print(nombre)
		    	print(user_name)
		    	longitud = len(str(dm))
		    	print("Longitud: ", longitud)
		    	print("Publicacion: ", dm)
		    	if longitud <= 140:
		    		api.send_direct_message(user_name, text="Thank you for using my service! Your tweet should appear in a minute")
		    		time.sleep(60)
		    		api.update_status(str(dm))
		    		print("Tweet sent")
		    		print("\n")
		    	else:
		    		api.send_direct_message(user_name, text="Your DM was longer than 140 chars, it won't be posted. Please send a DM shorter than 140 chars.")
		    		print("No se posteo, era más largo")
		    		time.sleep(15)
		    		print("\n")

    		except BaseException as e:
		    	print("Hubo un error al recibir un DM", e)
	    	


def main():
	try:
		
		print(api.me().name)

		stream = Stream(auth, MyStreamListener())
		stream.userstream()
	except BaseException as e:
		print("Error in main()", e)


if __name__ == '__main__':
	main()
