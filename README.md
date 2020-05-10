# RetweetBot

[![Python Version](https://img.shields.io/badge/python-3.8-black)](https://python.com)

simple bot for twitter that retweets everything with a selected search term, specified in auth.json

<br>

## Dependecies:
	
- python >= 3.8
- tweepy >= 3.8.0


## Getting started 

First of all, you need to create an RetweetBot at <a href="https://www.developer.twitter.com">developer.twitter.com</a> after this your need the Consumer API keys and Access token & access token secret from you application.


<table style="border-collapse:collapse;border-spacing:0;table-layout: fixed; width: 295px" class="tg"><colgroup><col style="width: 161px"><col style="width: 134px"></colgroup><thead><tr><th style="border-color:inherit;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;font-weight:normal;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal">API Key</th><th style="border-color:inherit;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;font-weight:normal;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal">xxxx</th></tr></thead><tbody><tr><td style="border-color:inherit;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal">API Secret Key</td><td style="border-color:inherit;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal">xxxxxxxx</td></tr><tr><td style="border-color:inherit;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal">Access Token</td><td style="border-color:inherit;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal">xxxx</td></tr><tr><td style="border-color:inherit;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal">Access Token Secret</td><td style="border-color:inherit;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal">xxxxxxxx</td></tr><tr><td style="border-color:inherit;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal">Access Level</td><td style="border-color:inherit;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal">Read and Write</td></tr></tbody></table>


## Configuring the settings file

```json
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
```


## Running

	
	$ pip install -r requirements.txt
	$ python app.py auth.json
	

***Output Example***

	
	[RETWEETED -> 1258555422610534400] 'luciana - @_lula_silvestri' - 'Búscame cuando haya amorQue sólo por ti a Dios le...'
	[RETWEETED -> 1258555419896799232] 'A Sergio Marques B - @sergiomarquesb' - '@SF_Moro Como sempre, vale tudo para vc desde que ...'
	[RETWEETED -> 1258555418416230402] 'Seoade Lula - @Seoade' - 'RT @HGabrielaRM: @dilmabr Deveriam julgar cada emb...'
	Retweeted: 3 | remaining: 2
	
	[RETWEETED -> 1258555410925211656] 'claudio riso lopes - @claudiorisolope' - 'RT @EstevamReboucas: Lula: Essa gente ñ pode ficar...'
	[RETWEETED -> 1258555396857442305] 'Jesus Marte Fajardo - @martefajardo' - '@PedroMCasals @realDonaldTrump Trump  es la salvac...'
	Retweeted: 2 | remaining: 0
	
<br>

## References

- https://developer.twitter.com/en/docs
- https://developer.twitter.com/en/docs/api-reference-index
- https://developer.twitter.com/en/docs/tutorials
- https://developer.twitter.com/en/docs/changelog/enterprise
- https://api.twitterstat.us/
- http://docs.tweepy.org/en/latest/

<br>

## About
This code is used in https://twitter.com/LulaBotOficial
and created by https://twitter.com/nando_ferreira2	
