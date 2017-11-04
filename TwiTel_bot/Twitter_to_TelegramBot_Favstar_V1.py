<!DOCTYPE html>

<html lang="en">
    <head>
        <meta charset="utf-8">
        <title>test_telbot_5.py : /home/aminhb/test_telbot_5.py : Editor : aminhb : PythonAnywhere</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta name="description" content="test_telbot_5.py : /home/aminhb/test_telbot_5.py : Editor : aminhb : PythonAnywhere">
        <meta name="author" content="PythonAnywhere LLP">
        <meta name="google-site-verification" content="O4UxDrfcHjC44jybs2vajc1GgRkTKCTRgVzeV6I9V14" />


        <!-- Le styles -->
        <link rel="stylesheet" href="/static/CACHE/css/afa5e20fceeb.css" type="text/css" media="screen" />
        <link rel="stylesheet" href="/static/CACHE/css/ad9d1f2ab435.css" type="text/css" media="screen" />

        <!-- Le javascript -->
        <script type="text/javascript">
            var Anywhere = {};
            Anywhere.urls = {};
            Anywhere.csrfToken = "uIKOLEW9SCFHC92zkklQiWvvU8qE9HFc";
        </script>
        <script type="text/javascript" src="/static/CACHE/js/4c6fed4396b4.js"></script>
        

        <script type="text/javascript" src="/static/CACHE/js/b13f6a2104a0.js"></script>
        
    <script type="text/javascript">
      $(document).ready(function() {
        $.extend(Anywhere.urls, {
          save: "/user/aminhb/files/home/aminhb/test_telbot_5.py",
          check_hash: "/user/aminhb/files/home/aminhb/test_telbot_5.py",
          run: "/user/aminhb/files/home/aminhb/test_telbot_5.py" + "?run",
          update_editor_mode_preference: "/user/aminhb/account/update_editor_mode_preference",
        });
        var filename = "/home/aminhb/test_telbot_5.py";
        var hash = "5ec5917c9ac42372eab56d7a3401e14a";
        var interpreter = "/usr/bin/python2.7";

        
            Anywhere.Editor.InitialiseAce(ace, Anywhere.urls, filename, hash, interpreter);
            $("#id_keybinding_mode_select").val("normal");
            $("#id_keybinding_mode_select").trigger("change");
        
        var consoleVisible = true;
        Anywhere.Editor.splitPanes(consoleVisible);

        Anywhere.WebAppControl.initialize();
        Anywhere2.initializeFileSharingOptions(
          $('#id_file_sharing_options')[0],
          {
            url: "/api/v0/user/aminhb/files/sharing/",
            csrfToken: "uIKOLEW9SCFHC92zkklQiWvvU8qE9HFc",
            path: "/home/aminhb/test_telbot_5.py"
          }
        );

      });
    </script>

        

        <!-- Le fav and touch icons -->
        <link rel="apple-touch-icon" href="images/apple-touch-icon.png">
        <link rel="apple-touch-icon" sizes="72x72" href="images/apple-touch-icon-72x72.png">
        <link rel="apple-touch-icon" sizes="114x114" href="images/apple-touch-icon-114x114.png">



    </head>

     <body>
        
    <nav class="navbar" role="banner">
        <div id="id_internal_nav_bar_container" class="container fluid">

            <div class="navbar-header">
                <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target=".right_hand_links" aria-expanded="false">
                  <span class="sr-only">Toggle navigation</span>
                  <span class="icon-bar"></span>
                  <span class="icon-bar"></span>
                  <span class="icon-bar"></span>
                </button>
                <a class="navbar-brand" href="/"><img id="id_logo" src="/static/anywhere/images/logo-234x35.png" height="35" title="PythonAnywhere logo" alt="PythonAnywhere logo" /></a>
            </div>

            <div class="collapse navbar-collapse right_hand_links">
                <div class="row">
                    <ul id="id_header_links" class="nav navbar-nav navbar-right ">
                        <li><a id="id_feedback_link" class='feedback_link' href="">Send feedback</a></li>
                        <li><a id="id_forums_link" href="/forums/">Forums</a></li>
                        <li><a href="https://help.pythonanywhere.com/" id="id_help_link">Help</a></li>
                        <li><a href="https://blog.pythonanywhere.com/" id="id_blog_link">Blog</a></li>
                        
                        
                            <li><a href="/user/aminhb/" id="id_dashboard_nav_link">Dashboard</a></li>
                            <li><a href="/user/aminhb/account/" id="id_account_link">Account</a></li>
                            <li>
                            <form class="navbar-form" action="/logout/" method="POST">
                              <input type='hidden' name='csrfmiddlewaretoken' value='uIKOLEW9SCFHC92zkklQiWvvU8qE9HFc' />
                              <button type="submit" class="btn btn-link" id="id_logout_link">Log out</button>
                            </form>
                            </li>
                        
                    </ul>
                </div>

                
                    <div class="row nice_dropdown header_second_row">

                        

                        

                        
                        

                        

                        

                    </div>
                
            </div>
        </div>
    </nav>

    



        
    


        

<div>

    <div id="id_editor_toolbar">

      <div id="id_editor_messages">
        

      </div>

      <span id="id_breadcrumbs_div"><a class="breadcrumbs_link breadcrumb_entry" href="/user/aminhb/files/">/</a><a class="breadcrumbs_link breadcrumb_entry" href="/user/aminhb/files/home">home</a><span class="breadcrumb_entry">/</span><a class="breadcrumbs_link breadcrumb_entry" href="/user/aminhb/files/home/aminhb">aminhb</a><span class="breadcrumb_entry">/</span><span class="breadcrumb_entry breadcrumb_terminal">test_telbot_5.py</span></span>

      <span>
        <span id="id_unsaved_changes_spacer">
          <span id="id_unsaved_changes" class="pa_hidden muted">(unsaved changes)</span>
        </span>
      </span>
      <img src="/static/anywhere/images/spinner-small.gif" class="pa_hidden" id="id_save_spinner" />
      <div id="id_editor_buttons_right" class="form-inline">
          <span id="id_save_error" class="pa_hidden alert alert-danger">Error saving.</span>
          
              <span id="id_keyboard_shortcuts"><a href="#">Keyboard shortcuts:</a></span>
              <select id="id_keybinding_mode_select" class="form-control input-sm">
                  <option value="normal">Normal</option>
                  <option value="vim">Vim</option>
              </select>
          
          <button id="id_display_sharing_options" class="btn btn-sm btn-default" data-toggle="modal" data-target="#id_file_sharing_modal" title="Get a URL to share this file">
            <span class="glyphicon glyphicon-paperclip" aria-hidden="true"></span>
            Share
          </button>
          
            <button id="id_save" class="btn btn-sm btn-success" title="Save (Ctrl + S)">
              <span class="glyphicon glyphicon-floppy-disk" aria-hidden="true"></span>
              Save
            </button>
            <button id="id_save_as" class="btn btn-sm btn-default" title="Save As">Save as...</button>
          
          
          <button class="btn btn-sm btn-info run_button" title="Save &amp; Run (Ctrl + R)">
            <span><code>&gt;&gt;&gt;</code></span>
            Run
          </button>
          

          
          
          


        </div>
        <div class="clear"></div>
    </div>

    <div id="id_ide_split_panes">

        
            <div id="id_editor">#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
#Nahaangard

from telegram.ext import Updater, CommandHandler, Job
import logging
from TwitterAPI import TwitterAPI
import time

# Enable logging
logging.basicConfig(format=&#39;%(asctime)s - %(name)s - %(levelname)s - %(message)s&#39;,
                    level=logging.INFO)
logger = logging.getLogger(__name__)

#Twitter Credentials
consumer_key=&#39;TOMgP9u0C0rd7zo51qLbmszbz&#39;
consumer_secret=&#39;VgzJC60lPcwqBK69MnY3Sb1Rx7ypK0Edi8MwReoj5rym3p6FIz&#39;
access_token=&#39;780211428061872128-f9DQB1tv4yC3njpjy0Z8vaf4Efh9Duu&#39;
access_secret=&#39;8cbSymWatNbrqjZhMEqft1lY0vjdR2kTXlaK8qwGFYsyX&#39;

api = TwitterAPI(consumer_key,
                 consumer_secret,
                 access_token,
                 access_secret)

#Required favstar and bot paramters
keyword_to_search = (&#39;[]&#39;)
counts = 250 # number of tweets to be assessed
default_fav = 100 # favs counts to be a favstar
fav_limit = 0
result_alg = &#39;recent&#39;
id_list = []
default_time = 60

#Just a quick warm-up
def start(bot, update):
    update.message.reply_text(&#39;&#39;&#39;Hey! good to see you here :) &#39;&#39;&#39; + &#39;\n&#39;
                                 &#39;&#39;&#39;type /run to begin your bot.&#39;&#39;&#39;)

#Definning help parameters
def help(bot, update):
    update.message.reply_text(&#39;&#39;&#39;Hey, Nahaangard&#39;s here :)&#39;&#39;&#39; + &#39;\n&#39; + &#39;\n&#39; +
                            &#39;&#39;&#39;To RUN your bot, with fav threshold and time interval, simply just type:&#39;&#39;&#39; +&#39;\n&#39; + &#39;\n&#39; +
                            &#39;&#39;&#39;/run (favs} {seconds} &#39;&#39;&#39; + &#39;\n&#39; +
                            &#39;&#39;&#39;For example: /run 30 300&#39;&#39;&#39; + &#39;\n&#39; +&#39;\n&#39; +
                            &#39;&#39;&#39;Keep it in mind:&#39;&#39;&#39; + &#39;\n&#39; +
                            &#39;&#39;&#39;{seconds} a value between (30 - 3600)&#39;&#39;&#39; + &#39;\n&#39; +
                            &#39;&#39;&#39;{favs} has to be a value between (50 - 2000)&#39;&#39;&#39; + &#39;\n&#39; + &#39;\n&#39; +
                            &#39;&#39;&#39;To STOP your bot, type &quot;/stop&quot; &#39;&#39;&#39; + &#39;\n&#39; +
                            &#39;&#39;&#39;To get some HELP, type &quot;/help&quot; &#39;&#39;&#39; + &#39;\n&#39; + &#39;\n&#39;
                            &#39;&#39;&#39;That&#39;s it! enjoy :)&#39;&#39;&#39;)

#The main run_bot module
def run(bot, update,args, job_queue, chat_data):
    global fav_limit
    chat_id = &#39;@nahaangard&#39;
    print &#39;running&#39;
    # chat_id = update.message.chat_id
    print len(args)
    if args:

        if 2 &lt; len(args):
            print &#39;please set your values agains.&#39;
            pass

        if len(args) == 1:

            print &#39;args&#39; + args
            try:
                Timer_set = int(args[0])
                if Timer_set &lt; 31:
                    Timer_set = 30
                if Timer_set &gt; 3601:
                    Timer_set = 3600
                fav_limit = default_fav
                job = Job(twitel, Timer_set, repeat=True, context=chat_id)
                chat_data[&#39;job&#39;] = job
                job_queue.put(job)

            except (IndexError, ValueError):
                pass
        if len(args) == 2:
            print &#39;args&#39; + &#39; &#39; + args[0] + &#39; &#39; +args[1]
            try:
                Timer_set = int(args[0])
                if Timer_set &lt; 31:
                    Timer_set = 30
                if Timer_set &gt; 3601:
                    Timer_set = 3600

                fav_limit = int(args[1])
                if fav_limit &lt; 51:
                    fav_limit = 50
                if fav_limit &gt; 2001:
                    fav_limit  = 2000

                job = Job(twitel, Timer_set, repeat=True, context=chat_id)
                chat_data[&#39;job&#39;] = job
                job_queue.put(job)

            except (IndexError, ValueError):
                pass
    if not args:
        print &#39;no args&#39;
        try:
            fav_limit = default_fav
            job = Job(twitel, default_time, repeat=True, context=chat_id)
            chat_data[&#39;job&#39;] = job
            job_queue.put(job)

        except (IndexError, ValueError):
            pass

#Stop module : it&#39;ll take a while perhaps to clear-up the cache, stopping module happens gradually
def stop(bot, update, chat_data):
    print &#39;stopped.&#39;
    if &#39;job&#39; not in chat_data:
        update.message.reply_text(&#39;You have already stopped the bot.&#39;)
        return

    job = chat_data[&#39;job&#39;]
    job.schedule_removal()
    del chat_data[&#39;job&#39;]

    update.message.reply_text(&#39;&#39;&#39;Ok. I stop here,&#39;&#39;&#39; + &#39;\n&#39; +
                              &#39;&#39;&#39;if you want me to run again, simply type: /run&#39;&#39;&#39; + &#39;\n&#39; + &#39;\n&#39; +
                              &#39;&#39;&#39;I&#39;ll be waiting for you :)&#39;&#39;&#39;)

#Returns the error
def error(bot, update, error):
    logger.warning(&#39;Update &quot;%s&quot; caused error &quot;%s&quot;&#39; % (update, error))

#Twitter favstar filtering for the streaming tweets, firsrt by language then favs and finally the tweet&#39;s id
def favstar():

    error_note = True
    for item in api.request(&#39;search/tweets&#39;, {&#39;q&#39;: keyword_to_search, &#39;lang&#39;: &#39;fa&#39;, &#39;count&#39;: counts, &#39;result_type&#39;: result_alg}):

        if &#39;retweeted_status&#39; in item:
            if item[&#39;retweeted_status&#39;][&#39;favorite_count&#39;] &gt;=  fav_limit:
                if not item[&#39;retweeted_status&#39;][&#39;id&#39;] in id_list:

                    id_list.append(item[&#39;retweeted_status&#39;][&#39;id&#39;])
                    twpack = (item[&#39;retweeted_status&#39;][&#39;text&#39;] + &#39;\n&#39; + &#39;\n&#39;
                              + item[&#39;entities&#39;][&#39;user_mentions&#39;][0][&#39;name&#39;] + &#39;\n&#39;
                              + u&quot;\u2764&quot; + &#39; &#39; + str(item[&#39;retweeted_status&#39;][&#39;favorite_count&#39;]) + &#39;\n&#39;
                              + u&#39;\U0001f501&#39; + &#39; &#39; + str(item[&#39;retweeted_status&#39;][&#39;retweet_count&#39;]) + &#39;\n&#39;
                              + &#39;twitter.com/&#39; + item[&#39;entities&#39;][&#39;user_mentions&#39;][0][&#39;screen_name&#39;] + &#39;\n&#39;+ &#39;@nahaangard&#39;)
                    print twpack
                    return twpack
                    error_note = False

        if not &#39;retweeted_status&#39; in item:
            if item[&#39;favorite_count&#39;] &gt;= fav_limit:
                if not item[&#39;id&#39;] in id_list:

                    id_list.append(item[&#39;id&#39;])
                    twpack = (item[&#39;text&#39;] + &#39;\n&#39; + &#39;\n&#39;
                              + item[&#39;user&#39;][&#39;name&#39;] +&#39;\n&#39;
                              + u&quot;\u2764&quot; + &#39; &#39; + str(item[&#39;favorite_count&#39;]) + &#39;\n&#39;
                              + u&#39;\U0001f501&#39; + &#39; &#39; + str(item[&#39;retweet_count&#39;]) + &#39;\n&#39; + &#39;@nahaangard&#39;)
                              # + &#39;twitter.com/&#39; + item[&#39;entities&#39;][&#39;user_mentions&#39;][0][&#39;screen_name&#39;] + &#39;\n&#39; + &#39;@nahaangrad&#39;)
                    print twpack
                    return twpack
                    error_note = False

    if error_note == True:
        return None

#Telegram-Twitter bridge, if it couldn&#39;t find anything, it&#39;ll give a 5 s delay, then it&#39;ll retry.
def twitel(bot, job):
    txt = favstar()
    if txt:
        bot.sendMessage(job.context, text=txt)
    elif txt is None:
        time.sleep(5)
        print &#39;&#39;&#39;couldn&#39;t find anything&#39;&#39;&#39;
        pass
    else:
        pass

#The main module, the telegram token will be implemented here; current and future commands will be managed here as well
def main():
    updater = Updater(&quot;325108031:AAEtMYjMumRjsQJn1_6jJwUOqvaEeHzePlw&quot;)
    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler(&quot;start&quot;, start))
    dp.add_handler(CommandHandler(&quot;help&quot;, help))
    dp.add_handler(CommandHandler(&quot;run&quot;, run,
                                  pass_args=True,
                                  pass_job_queue=True,
                                  pass_chat_data=True))
    dp.add_handler(CommandHandler(&quot;stop&quot;, stop, pass_chat_data=True))

    dp.add_error_handler(error)

    updater.start_polling()

    updater.idle()


if __name__ == &#39;__main__&#39;:
    main()</div>
        

        <div id="id_ide_console">
            
                <div id="id_ide_console_pane_buttons">
                    <center>
                        
                            <button class="btn btn-large btn-info run_button" title="Save &amp; Run (Ctrl + R)">&gt;&gt;&gt; Run this file</button>
                            <button class="btn btn-large btn-info bash_console_here" title="Start a Bash console in this folder">$ Bash console here</button>
                        
                    </center>
                </div>
                <iframe style="display: none" id="id_console" name="console" class="soft_keyboard_sensitive">
                </iframe>
                <div style="display: none;" class="console_limit_reached">
                    <div class="container">
    <div class="row">
        <div class="col-md-5 col-md-offset-3 well">
            <h1>Console limit reached :-/</h1>

            <p>
            With your current PythonAnywhere account you can have up to
            2 consoles.  You can
            have more if you
            <a href="/user/aminhb/account/">upgrade your account</a>!

            <p>
            Alternatively, if you don't feel like paying us more money, you
            can <a href="/user/aminhb/consoles/">kill some consoles on your Consoles page</a>.
        </div>
    </div>
</div>


                </div>
            
        </div>

    </div>

    <div id="id_go_to_line_dialog" class="pa_hidden">
        <p class="form-inline">Line number: <input id="id_go_to_line_dialog_input" /></p>
        <div class="dialog_buttons">
            <button class="btn btn-default" id="id_go_to_line_dialog_ok_button">Go</button>
            <button class="btn btn-default" id="id_go_to_line_dialog_close_button">Close</button>
        </div>
    </div>

    <div id="id_file_changed_on_disk" class="pa_hidden">
        <p>Are you sure you want to save it?  Alternatively, you could re-open it in a new tab to check differences</p>
        <div class="dialog_buttons">
            <button id="id_force_save" class="btn btn-danger">Force Save</button>
            <button id="id_cancel_save" class="btn btn-default">Cancel</button>
        </div>
    </div>

    <div id="id_save_as_dialog" class="pa_hidden">
        <form class="form-inline">
            <div class="form-group">
                <label for="id_save_as_path">Please enter a path:</label>
                <input id="id_save_as_path" class="form-control" style="width: 100%;" />
            </div>
            <img id="id_save_as_spinner" class="spinner pa_hidden" src="/static/anywhere/images/spinner-small.gif" />
            <p>
                <span id="id_save_as_error" class="error_message"></span>
            </p>
            <div class="dialog_buttons">
                <button id="id_save_as_ok" type="submit" class="btn btn-primary">Save</button>
                <button id="id_save_as_cancel" type="button" class="btn btn-default">Cancel</button>
            </div>
        </form>
    </div>

    <div class="modal fade" id="id_file_sharing_modal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title" id="myModalLabel">File Sharing options</h4>
          </div>
          <div class="modal-body">
            <div id="id_file_sharing_options"></div>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
          </div>
        </div>
      </div>
    </div>

</div>


        

        


        <div id="id_feedback_dialog" title="Help us improve" style="display:none">
    <div id="id_feedback_dialog_blurb_big" class="dialog_blurb_big">
        It's always a pleasure to hear from you!
    </div>
    <div id="id_feedback_dialog_blurb_small">
        Ask us a question, or tell us what you love or hate about PythonAnywhere.<br/>
        We'll get back to you over email ASAP.
    </div>
    <textarea id="id_feedback_dialog_text" rows="6"></textarea>
    <input id="id_feedback_dialog_email_address" type="text" placeholder="Email address (optional - only necessary if you would like us to contact you)"/>
    
    <div id="id_feedback_dialog_error" class="pa_hidden">
        Sorry, there was an error connecting to the server. <br/>Please try again in a few moments...
    </div>
    <div class="dialog_buttons">
        <img id="id_feedback_dialog_spinner" src="/static/anywhere/images/spinner-small.gif" />
        <button class="btn btn-primary" id="id_feedback_dialog_ok_button">OK</button>
        <button class="btn btn-default" id="id_feedback_dialog_cancel_button">Cancel</button>
    </div>
</div>


        
            <script>
                (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
                (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
                m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
                })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

                ga('create', 'UA-18014859-6', 'auto');
                ga('send', 'pageview');
            </script>
        

        
        <!-- preload font awesome fonts to avoid glitch when switching icons -->
        <div style="width: 0; height: 0; overflow: hidden"><i class="fa fa-square-o fa-3x" ></i></div>
    </body>
</html>
