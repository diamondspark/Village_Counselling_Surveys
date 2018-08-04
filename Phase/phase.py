from abc import ABCMeta, abstractmethod
import sys
sys.path.append('./Connection')
from connection import Connection
from dateutil.parser import parse


class Phase(object):
     ''' Phase abstract class for ph1,2, all phases and no phase
     '''

     __metaclass__ = ABCMeta

     def __init__(self,test_case_removal,concat=False):
          conn = Connection()
          self.report = conn.retrieve_reports(test_case_removal,concat)

     def sort_repo(self,criteria):
          df= self.report
          return df.sort_values(by=criteria)
     
     def consolidate_repo(self):
          '''
          Put all records for same email in same row. The input report must is of  concatenated type
          '''
          df= self.report
          df=df.applymap(str)
          for i in range(len(df)):
              
              if i == len(df)-1:
                  for j in range(0,17):
                      df.iat[i,17+j]=''
                  break
              else:
                  
                  if df.iat[i,7]== df.iat[i+1,7]:
                      for j in range(0,17):
                          df.iat[i,j+17]= df.iat[i+1,j]
                          df.iat[i+1,j]=''
                  else:
                      for j in range(0,17):
                          df.iat[i,17+j]=''
          return df

     def both_survey_completed(self,df):
          ''' If email and email_1 is same in a row then both_survey_completed.
              If only one survey is taken then email_1 would be empty anyways.
          '''
          both_survey_completed_index=[]
          email_1_col_index = df.columns.get_loc("email_1")
          for i in range(len(df)):
               if df.iat[i,email_1_col_index] != '':
                    both_survey_completed_index.append(i)
          return both_survey_completed_index

     def single_survey_completed(self,df):
          '''If email is present and email_1 is absent then only one phase is completed.
             Which phase is completed is dependent on which phase(phase1 or phase2) object is being dealt with
          '''
          email_1_col_index = df.columns.get_loc("email_1")
          email_col_index = df.columns.get_loc("email")
          single_survey_completed_index=[]
          for i in range(len(df)):
               if df.iat[i,email_col_index]!='' and df.iat[i,email_1_col_index]=='':
                    single_survey_completed_index.append(i)
          return single_survey_completed_index

     def percent_difference(self,df,both_repo_completed):
          ''' Drop %_difference column coz it's old miscalculated data.
              For all participants who have completed both survey, insert into %_difference_1, their
              score difference between survey taken later - survey taken before (chronologically)
              Also return a list of scores of surveys taken later and list of scores of survey taken before
          '''

          df.drop('%_difference',axis=1,inplace=True)

          date_col_index = df.columns.get_loc("date")
          time_col_index = df.columns.get_loc("time")
          date1_col_index = df.columns.get_loc("date_1")
          time1_col_index = df.columns.get_loc("time_1")
          emq_col_index = df.columns.get_loc("emq")
          emq1_col_index = df.columns.get_loc("emq_1")
          percent_diff1_col_index = df.columns.get_loc('%_difference_1')


          former_scores=[]
          later_scores=[]
          
          for i in range(len(both_repo_completed)):
               
               date_time = df.iat[both_repo_completed[i],date_col_index]+' '+df.iat[both_repo_completed[i],time_col_index]
               date_time_1 = df.iat[both_repo_completed[i],date1_col_index]+' '+df.iat[both_repo_completed[i],time1_col_index]
               date_time = parse(date_time)
               date_time_1 = parse(date_time_1)
          
               if date_time < date_time_1:
                    df.iat[both_repo_completed[i],percent_diff1_col_index]= int(df.iat[both_repo_completed[i],emq1_col_index])- int(df.iat[both_repo_completed[i],emq_col_index])
                    later_scores.append(int(df.iat[both_repo_completed[i],emq1_col_index]))
                    former_scores.append(int(df.iat[both_repo_completed[i],emq_col_index]))
               elif date_time > date_time_1:
                    df.iat[both_repo_completed[i],percent_diff1_col_index]= int(df.iat[both_repo_completed[i],emq_col_index])-int(df.iat[both_repo_completed[i],emq1_col_index])
                    later_scores.append(int(df.iat[both_repo_completed[i],emq_col_index]))
                    former_scores.append(int(df.iat[both_repo_completed[i],emq1_col_index]))
     

          return df, later_scores,former_scores
                    
               

                    



     @abstractmethod
     def filterPhaseReports(self):
          '''Each kind of phase has it's own version of filtering just that phase's reports
          '''
          pass



