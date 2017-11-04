#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
#Nahaangard - Feb17

from telegram.ext import Updater, CommandHandler, Job
import logging
from TwitterAPI import TwitterAPI
import time

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

#Twitter Credentials
consumer_key='TOMgP9u0C0rd7zo51qLbmszbz'
consumer_secret='VgzJC60lPcwqBK69MnY3Sb1Rx7ypK0Edi8MwReoj5rym3p6FIz'
access_token='780211428061872128-f9DQB1tv4yC3njpjy0Z8vaf4Efh9Duu'
access_secret='8cbSymWatNbrqjZhMEqft1lY0vjdR2kTXlaK8qwGFYsyX'

api = TwitterAPI(consumer_key,
                 consumer_secret,
                 access_token,
                 access_secret)

#Required favstar and bot paramters
keyword_to_search = ('[]')
counts = 500 # number of tweets to be assessed
default_fav = 250 # favs counts to be a favstar - first criteria
ret_limit = 10 # ret counts to be a favstar - second criteria
result_alg = 'recent'
fav_limit = 0
id_list = []
default_time = 60
follower_count = 20000

#Just a quick warm-up
def start(bot, update):
    update.message.reply_text('''Hey! good to see you here :) ''' + '\n'
                                 '''type /run to begin your bot.''')

#Definning help parameters
def help(bot, update):
    update.message.reply_text('''Hey, Nahaangard's here :)''' + '\n' + '\n' +
                            '''To RUN your bot, with fav threshold and time interval, simply just type:''' +'\n' + '\n' +
                            '''/run (favs} {seconds} ''' + '\n' +
                            '''For example: /run 60 300''' + '\n' +'\n' +
                            '''Keep it in mind:''' + '\n' +
                            '''{seconds} a value between (60 - 3000)''' + '\n' +
                            '''{favs} has to be a value between (150 - 3000)''' + '\n' + '\n' +
                            '''To STOP your bot, type "/stop" ''' + '\n' +
                            '''To get some HELP, type "/help" ''' + '\n' + '\n'
                            '''That's it! enjoy :)''')

#The main run_bot module
def run(bot, update,args, job_queue, chat_data):
    global fav_limit
    chat_id = '@nahaangard'
    print ('\n')
    print ('Running now...')
    # chat_id = update.message.chat_id

    if args:

        if len(args) > 2:
            print ('please set your values again')
            pass

        if len(args) == 1:

            print ('Time: ' + args[0])
            print ('Favs: ' + str(default_fav))
            try:
                Timer_set = int(args[0])
                if Timer_set < 61:
                    Timer_set = default_time
                if Timer_set > 3601:
                    Timer_set = 3600
                fav_limit = default_fav
                job = Job(twitel, Timer_set, repeat=True, context=chat_id)
                chat_data['job'] = job
                job_queue.put(job)

            except (IndexError, ValueError):
                pass
        if len(args) == 2:
            print ('Time: ' + args[0])
            print ('Favs: ' + args[1])
            try:
                Timer_set = int(args[0])
                if Timer_set < 61:
                    Timer_set = default_time
                if Timer_set > 3601:
                    Timer_set = 3600

                fav_limit = int(args[1])
                if fav_limit < 101:
                    fav_limit = 100
                if fav_limit > 3001:
                    fav_limit  = 3000

                job = Job(twitel, Timer_set, repeat=True, context=chat_id)
                chat_data['job'] = job
                job_queue.put(job)

            except (IndexError, ValueError):
                pass
    if not args:
        print ('Time: ' + str(default_time))
        print ('Favs: ' + str(default_fav))
        try:
            fav_limit = default_fav
            job = Job(twitel, default_time, repeat=True, context=chat_id)
            chat_data['job'] = job
            job_queue.put(job)

        except (IndexError, ValueError):
            pass

#Stop module : it'll take a while perhaps to clear-up the cache, stopping module happens gradually
def stop(bot, update, chat_data):
    print ('stopped.')
    if 'job' not in chat_data:
        update.message.reply_text('You have already stopped the bot.')
        return

    job = chat_data['job']
    job.schedule_removal()
    del chat_data['job']

    update.message.reply_text('''Ok. I stop here,''' + '\n' +
                              '''if you want me to run again, simply type: /run''' + '\n' + '\n' +
                              '''I'll be waiting for you :)''')

#Returns the error
def error(bot, update, error):
    logger.warning('Update "%s" caused error "%s"' % (update, error))

#Twitter favstar filtering for the streaming tweets, firsrt by language then favs and finally the tweet's id
def favstar():

    error_note = True
    for item in api.request('search/tweets', {'q': keyword_to_search, 'lang': 'fa', 'count': counts, 'result_type': result_alg}):

        if 'retweeted_status' in item:
            if item['retweeted_status']['user']['followers_count'] <= follower_count:
                if item['retweeted_status']['favorite_count'] >=  fav_limit and item['retweeted_status']['retweet_count'] >= ret_limit:
                    if not item['retweeted_status']['id'] in id_list:

                        id_list.append(item['retweeted_status']['id'])
                        twpack = (item['retweeted_status']['text'] + '\n' + '\n'
                                  + '[' + item['entities']['user_mentions'][0]['name'] + ']'+ '\n'
                                  + u"\u2764" + str(item['retweeted_status']['favorite_count']) + '\n'
                                  + u'\U0001f501' + ' ' + str(item['retweeted_status']['retweet_count']) + '\n' + '\n'
                                  + 'twitter.com/' + item['entities']['user_mentions'][0]['screen_name'] + '\n')

                        print (twpack)

                        # clean-up the id-list
                        # print id_list
                        if len(id_list) > 3000:
                            del id_list[:]

                        return twpack
                        error_note = False

        if not 'retweeted_status' in item:
            if item['favorite_count'] >= fav_limit:
                if not item['id'] in id_list:

                    id_list.append(item['id'])
                    twpack = (item['text'] + '\n' + '\n'
                              + item['user']['name'] +'\n'
                              + u'\u2764' + str(item['favorite_count']) + '\n'
                              + u'\U0001f501' + ' ' + str(item['retweet_count']) + '\n' + '\n'
                              # + 'twitter.com/' + item['entities']['user_mentions'][0]['screen_name'] + '\n'
                              + str(item['id']))
                    # print twpack
                    return twpack
                    error_note = False

    if error_note == True:
        return None

#Telegram-Twitter bridge, if it couldn't find anything, it'll give a 120 s delay, then it'll retry.
def twitel(bot, job):
    txt = favstar()
    if txt:
        bot.sendMessage(job.context, text=txt)
        time.sleep(120)
    elif txt is None:
        time.sleep(120)
        print ('''couldn't find anything''')
        pass
    else:
        pass

#The main module, the telegram token will be implemented here; current and future commands will be managed here as well
def main():
    updater = Updater("325108031:AAEtMYjMumRjsQJn1_6jJwUOqvaEeHzePlw")
    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("run", run,
                                  pass_args=True,
                                  pass_job_queue=True,
                                  pass_chat_data=True))
    dp.add_handler(CommandHandler("stop", stop, pass_chat_data=True))

    dp.add_error_handler(error)

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()