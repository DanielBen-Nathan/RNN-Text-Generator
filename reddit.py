import praw
import sys
import re
import pickle
import numpy as np
import random
name = "KerbalSpaceProgramTop"
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
reddit = praw.Reddit(client_id='NtEQAjxGg5jzCQ',
                     client_secret='ld-uLjfXSltKeln2vm7Vh_Cmpg4',
                     
                     username='deeplearningdatabot',
                     password='gnomed',
                     user_agent='deeplearning'
                     )
#deeplearningdatabot
#gnomed
title=True
subreddit = reddit.subreddit('KerbalSpaceProgram')
hot = subreddit.top(limit=10000)
data = []
count=0

for submission in hot:
    if(title):

        try:

            data.append(submission.title)
            count += 1
        except:
            pass
    else:
        #print(submission.title)
        #print(submission.comments.list)
        if not submission.stickied:
            comments = submission.comments
            for comment in comments:
                try:
                    #print(comment.body)
                    #data[count] = comment.body

                    data.append(comment.body.translate(non_bmp_map))
                    count += 1

                except:
                    pass
            #for y int x.comments:
                #print(y.)

#regex = re.compile('[^a-z|[[:space:]]]')
print(count)
pickle_out=open("text/"+name+".txt", "wb")
pickle.dump(data,pickle_out)


