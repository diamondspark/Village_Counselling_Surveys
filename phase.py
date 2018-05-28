from abc import ABCMeta, abstractmethod
import sys
sys.path.append('./Connection')
from connection import Connection

class Phase(object):
     ''' Phase abstract class for ph1,2, all phases and no phase
     '''

     __metaclass__ = ABCMeta

     def __init__(self,concat=False):
          conn = Connection()
          self.report = conn.retrieve_reports(concat)

     def sort_repo(self,criteria):
          df= self.report
          return df.sort_values(by=criteria)
     
     def consolidate_repo(self):
          '''
          Put all records for same email in same row.
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
          

