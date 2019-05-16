from bs4 import BeautifulSoup
import requests
import re

class followertracker(object):
    def __init__(self, twitter_username = None, instagram_username = None, meetup_username = None):

        self.twitter_username = twitter_username
        self.instagram_username = instagram_username
        self.meetup_username = meetup_username
        
        #TODO meetup base url
        self.base_url = {"twitter":"https://www.twitter.com/",
                        "instagram": "https://www.instagram.com/", 
                        "meetup": "https://www.meetup.com/tr-TR/"
                        }
    
    def twitter(self):
        twitter_url = self.base_url['twitter'] + self.twitter_username
        soup = BeautifulSoup(requests.get(twitter_url).content, features="html5lib")
        self.twitter_follower = int(soup.find('li', class_ = "ProfileNav-item--followers").find('a')['title'].split(' ')[0].replace('.',''))
        return self.twitter_follower

    def instagram(self):
        instagram_url = self.base_url['instagram'] + self.instagram_username
        soup = BeautifulSoup(requests.get(instagram_url).content,features="html5lib")
        metaContentTags = soup.select("meta[content]")
    
        for tags in metaContentTags:
            strContent = tags.get("content").replace(",", "")
        
            if strContent.find("Follow") != -1:
                self.instagram_follower = int(re.findall(r'\d+', strContent)[0])
        return self.instagram_follower        

    def meetup(self):
        meetup_url = self.base_url['meetup'] + self.meetup_username
        soup = BeautifulSoup(requests.get(meetup_url).content,features="html5lib")
        temp = soup.find('a', class_ = "groupHomeHeaderInfo-memberLink").find('span')
        self.meetup_follower = int(str(temp).split('>')[1].split('<')[0].split(' ')[0].replace('.', ''))
        return self.meetup_follower