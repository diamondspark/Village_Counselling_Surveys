import pandas as pd
from bs4 import BeautifulSoup
import requests

username = ''
password = ''
url = 'https://empathyworks.org/wp-admin/admin.php?page=dataexchange%2Freportspage.php'

class Connection(object):
     def __init__(self):
          self.payload = {
                        'log': username,
                        'pwd': password 
                    }

     def retrieve_reports(self,test_case_removal,concat=False):
          REQUEST_URL = url
          POST_LOGIN_URL = 'https://empathyworks.org/wp-login.php'
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
          df_concat.columns=['short','quiz_1','Phase1','Phase2','date','time','user','email','age','gender','marital_status','sexual_orientation','professional_designation','years_in_practice','emq_1','redo','%_difference',
                            'short_2','quiz_2','Phase1_2','Phase2_2','date_2','time_2','user_2','email_2','age_2','gender_2','marital_status_2','sexual_orientation_2','professional_designation_2','years_in_practice_2','emq_2','redo_2','%_difference_2']

          if test_case_removal:
               df_concat=df_concat[df_concat.user.str.contains("test",case=False) == False]
               
          return df_concat






          
