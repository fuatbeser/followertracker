from util import followertracker

# You can change usernames as you wish or leave it None
twitter_username = "deeplearningtr"
instagram_username = "deeplearningtr"
meetup_username = "Deep-Learning-Turkiye"

tracker = followertracker(twitter_username, instagram_username, meetup_username)

print("Twitter Followers: ",tracker.twitter())
print("Instagram Followers: ",tracker.instagram())
print("Meetup Followers: ",tracker.meetup())