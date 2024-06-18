from components.Sheets_Manager.module.sheets_manager import Sheets_Manager
from utils.read_env import *
from components.Meta_Manager.module.meta_class import Social_Manager
from components.Twitter_Manager.module.scraping_twt import Twitter_Manager

def get_face_essencial(social_man: Social_Manager, dates: list)->list:        
        model = social_man.face_description(dates)
        result =[]
        for post in model[0]:
                result.append(
                        {
                         'date_created': post['created_time'],
                         'description': post['message'],
                         'link_url': post['permalink_url']
                         }
                )
        return result

def get_insta_essencial(social_man: Social_Manager, dates: list)->list:
        model = social_man.insta_description(dates)
        result =[]
        for post in model[0]:
                result.append(
                        {
                         'date_created': post['timestamp'],
                         'description': post['caption'],
                         'link_url': post['permalink']
                        }
                )
        return result

def get_twitter_essencial(twitter_man: Twitter_Manager, dates: list)->list:
        model = twitter_man.standard_procedure(dates)
        result =[]
        for post in model:
                result.append(
                        {
                         'date_created': post['extra'],
                         'description': post['texts'],
                         'link_url': post['effective_link']
                        }
                )
        return result