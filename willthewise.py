import praw
import config
import time
import os

def bot_login():
    print ("Loggin in...")
    r = praw.Reddit(
            username = config.username,
            password = config.password,
            client_id = config.client_id,
            client_secret = config.client_secret,
            user_agent = "Will the Wise bot"
            )
    print ('Logged in.')
    return r

def run_bot(r, comments_replied_to):
    print ("Obtaining 10 comments...")

    for comment in r.subreddit('StrangerThings').comments(limit=10):
        if ("zombie boy" in comment.body or "Zombie Boy" in comment.body) and comment.id not in comments_replied_to: 
            print ("String with 'Zombie boy' found in comment " + str(comment.id))
            comment.reply("He's here.")
            print ("Replied to comment " + str(comment.id))
            comments_replied_to.append(comment.id)
            with open("comments_replied_to.txt", "a") as f:
                f.write(comment.id + "\n")

        elif ("will the wise" in comment.body or "Will the Wise" in comment.body) and comment.id not in comments_replied_to: 
            print ("String with 'Will the Wise' found in comment " + str(comment.id))
            comment.reply("Want to play D&D?")
            print ("Replied to comment " + str(comment.id))
            comments_replied_to.append(comment.id)
            with open("comments_replied_to.txt", "a") as f:
                f.write(comment.id + "\n")
    
    print ("Sleeping for 2 seconds...")
    #Sleep for 2 secs
    time.sleep(2)

def get_saved_comments():
    if not os.path.isfile("comments_replied_to.txt"):
        comments_replied_to = []
    else:   
        with open("comments_replied_to.txt", "r") as f:
            comments_replied_to = f.read()
            comments_replied_to = comments_replied_to.split("\n")
            #comments_replied_to = filter(None, comments_replied_to)
    return comments_replied_to

r = bot_login()
comments_replied_to = get_saved_comments()
print (comments_replied_to)

while True:
    run_bot(r, comments_replied_to)