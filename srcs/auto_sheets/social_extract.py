from components.Sheets_Manager.module.sheets_manager import Sheets_Manager
from components.Thread_Manager.module.scraping_threads import Threads_Manager
from components.Meta_Manager.module.meta_class import Social_Manager
from components.Twitter_Manager.module.scraping_twt import Twitter_Manager, BeautifulSoup
from srcs.utils import *
from utils.read_env import *

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
			 'description': post.get('caption'),
			 'link_url': post['permalink']
			}
		)
	return result

def getTwitterAndThreads(dates: list)->list:
	twitter_man = Twitter_Manager(TWITTER_ACC, BROWSER_DATA_PATH, USER_AGENT,"Default",other_options=False,disable_graphics=False, remote_connection=False)
	model = twitter_man.standard_procedure(dates)
	result =[]
	for post in model:
		result.append(
			{
			 'date_created': post['extra_1'],
			 'metrics': post['extra_2'],
			 'description': post['texts'],
			 'link_url': post['effective_link']
			}
		)
	twitter_man.driver.quit()
	threads_man = Threads_Manager(THREADS_ACC, BROWSER_DATA_PATH, USER_AGENT,"Default",other_options=False,disable_graphics=False, remote_connection=False)
	model = threads_man.standard_procedure(dates)
	for post in model:
		result.append(
			{
			 'date_created': post['extra_1'],
			 'description': post['texts'],
			 'link_url': post['effective_link']
			}
		)
	threads_man.driver.quit()
	return result
	
def get_threads_essencial(threads_man: Threads_Manager, dates: list)->list:
	model = threads_man.standard_procedure(dates)
	result = []
	for post in model:
		result.append(
			{
			 'date_created': post['extra_1'],
			 'description': post['texts'],
			 'link_url': post['effective_link']
			}
		)
	return result