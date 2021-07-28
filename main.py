import yaml
from modules.gsheets import WorkSheet
from modules.twitter import Twitter
from modules.discord import Discord
from apscheduler.schedulers.blocking import BlockingScheduler




CONFIG_PATH = "config.yml"

def load_config():
    with open(CONFIG_PATH,'r') as config_yml:
        config = yaml.load(config_yml)
    config_yml.close()
    return config

def initailize_class(config):
    worksheet = WorkSheet(config['gsheet_cred_path'],
                          config['gsheet_sheet_name'])
    

    discord = Discord(config['discord_webhook'])

    twitter = Twitter(config['twitter_client_id'],
                      config['twitter_secret_key'],
                      config['mention_name'],
                      config['keyword'])
    
    return (worksheet, discord, twitter)

def run_it(worksheet, discord, twitter):
    #iterating through resultObjects
    for result in twitter.search_tweets():
        #testing if result object contains keyword
        if twitter.contains_keyword(result):
            #getting user information 
            user = twitter.return_user(result)
            #seeing if the user is new 
            new_user = worksheet.proccess_user(user)
            #sending discord message if new user 
            if new_user:
                discord.send_message(user)


sched = BlockingScheduler()

config = load_config()
worksheet, discord, twitter = initailize_class(config)


@sched.scheduled_job('interval', minutes=10)
def timed_job():
    print('Starting Job 🥳')
    run_it(worksheet, discord, twitter)
    print('Job Over 🥳')

if __name__ == "__main__":
    sched.start()


    

    





