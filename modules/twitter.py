import tweepy

class Twitter:

    def __init__(self,client_id,client_secret,account_mention,keyword):
        self.api = self.get_api(client_id,client_secret)
        self.account_mention = account_mention
        self.keyword = keyword

    def get_api(self,client_id,client_secret):
        auth = tweepy.OAuthHandler(client_id, client_secret)
        return tweepy.API(auth)

    def search_tweets(self):
        return self.api.search(q=self.account_mention,
                                count = 500)
    @staticmethod
    def get_json(result):
        return result._json
    
    def contains_keyword(self,result):
        return self.keyword in result.text

    @staticmethod
    def get_user_id(resultJson):
        return resultJson['user']['id']

    @staticmethod
    def get_tweet_id(resultJSON):
        return resultJSON['id']

    def get_thread_url(self,resultJson):
        screen_name = self.get_user_handle(resultJson)
        id = self.get_tweet_id(resultJson)
        return f'https://twitter.com/{screen_name}/status/{id}'

    @staticmethod
    def get_user_tweet(resultJson):
        return resultJson['urls'][0]['url']

    @staticmethod
    def get_user_name(resultJson):
        return resultJson['user']['name']

    @staticmethod
    def get_user_handle(resultJSON):
        return resultJSON['user']['screen_name']
    
    def get_user_profile(self,resultJSON):
        handle = self.get_user_handle(resultJSON)
        return f"https://twitter.com/{handle}"

    def get_user(self,resultJSON):
        return dict( user_id = self.get_user_id(resultJSON),
                    name = self.get_user_name(resultJSON),
                    thread = self.get_thread_url(resultJSON),
                    profile = self.get_user_profile(resultJSON)
    )

    def return_user(self,result):
        resultJson = self.get_json(result)
        return self.get_user(resultJson)