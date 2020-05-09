# Twitter RetweetBot

### a simple bot for twitter that retweets everything with a specified word.


## Getting started 

First of all, you need to create a "BOT" app on the link below.

https://developer.twitter.com/

After creating the app, you will need the app verification keys and tokens


| KEY                    | VALUE                          	|
|---------------------	|-------------------------------	|
| Consumer API 		| XXXXXXXXXXXXXXXXX             	|
| Consumer API Secret   | xxxxxxxxxxxxxxxxxxxxxxxxxxxxx 	|
| Access Token        	| xxxxxxxxxxxxxxxxx             	|
| Access Token Secret 	| xxxxxxxxxxxxxxxxxxxxxxxxxxxx  	|
| Access Level        	| Read and Write                	|



## Configuring the settings file

	
	// file: auth.json
	{
	    "access_token_key" : "YOUR_ACCESS_TOKEN_GOES_HERE",
	    "access_token_secret" : "YOUR_ACCESS_TOKEN_SECRET_GOES_HERE",
	    "client_key" : "YOUR_CONSUME_API_KEY_GOES_HERE",
	    "client_secret" : "YOUR_CONSUME_API_SECRET_KEY_GOES_HERE",
	    "query" : [
	        "CHOOSE A WORD"
	    ],
	    "count" : 50,
	    "result_type" : "recent",
	    "iso_language_code" : "pt"
	}
	


## Running

	
	$ pip install -r requirements.txt
	$ python app.py auth.json
	

### Output Example

	
	[RETWEETED -> 1258555422610534400] 'luciana - @_lula_silvestri' - 'Búscame cuando haya amorQue sólo por ti a Dios le...'
	[RETWEETED -> 1258555419896799232] 'A Sergio Marques B - @sergiomarquesb' - '@SF_Moro Como sempre, vale tudo para vc desde que ...'
	[RETWEETED -> 1258555418416230402] 'Seoade Lula - @Seoade' - 'RT @HGabrielaRM: @dilmabr Deveriam julgar cada emb...'
	[RETWEETED -> 1258555410925211656] 'claudio riso lopes - @claudiorisolope' - 'RT @EstevamReboucas: Lula: Essa gente ñ pode ficar...'
	[RETWEETED -> 1258555396857442305] 'Jesus Marte Fajardo - @martefajardo' - '@PedroMCasals @realDonaldTrump Trump  es la salvac...'
	[RETWEETED -> 1258555361897975809] 'Hugo Ricardo (ugO37) - @ugO377' - 'A admiração e fanatismo, louco e inconsequente por...'
	[RETWEETED -> 1258555341958254593] '𝘼𝙣𝙙𝙧𝙚® - @andrerezendef' - 'Pra mim quem aplaude Lula é tão burro quanto quem ...'
	

- used in: https://twitter.com/LulaBotOficial
- created by: https://twitter.com/nando_ferreira2
