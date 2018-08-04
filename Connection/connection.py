import pandas as pd
from bs4 import BeautifulSoup
import urllib2 
import requests

username = ''
password = ''
url = 'http://empathyworks.org/wp-admin/admin.php?page=dataexchange%2Freportspage.php'

class Connection(object):
     def __init__(self):
          self.payload = {
                        'log': username,
                        'pwd': password 
                    }

     def retrieve_reports(self,test_case_removal,concat=False):
          REQUEST_URL = url
          POST_LOGIN_URL = 'http://empathyworks.org/wp-login.php'
          with requests.Session() as session:
              post = session.post(POST_LOGIN_URL, data=self.payload)
              r = session.get(REQUEST_URL)
          soup = BeautifulSoup(r.content,"lxml")
          df= pd.read_html(r.content)[0]
          
          if concat:
               return self.__concat_repo(df,test_case_removal)
          else:          
               df.rename(columns={0:'short',1:'quiz',2:'Phase1',3:'Phase2',4:'date',5:'time',6:'user',7:'email',8:'age',9:'gender',10:'marital',11:'sexual_orientation',
                 12:'professional_designation',13:'years_in_practice',14:'emq',15:'redo',16:'%_difference'},inplace=True)
               return df


     def __concat_repo(self,df,test_case_removal):
          df.columns = [''] * len(df.columns)
          frames = [df,df]
          df_concat = pd.concat(frames,axis=1)
          df_concat.columns=['short','quiz','Phase1','Phase2','date','time','user','email','age','gender','marital_status','sexual_orientation','professional_designation','years_in_practice','emq','redo','%_difference',
                            'short_1','quiz_1','Phase1_1','Phase2_1','date_1','time_1','user_1','email_1','age_1','gender_1','marital_status_1','sexual_orientation_1','professional_designation_1','years_in_practice_1','emq_1','redo_1','%_difference_1']

          if test_case_removal:
               df_concat[df_concat.user.str.contains("test",case=False) == False]
               
          return df_concat






          
