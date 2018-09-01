import pandas as pd

class Output(object):
     '''Base class to make changes to final output dataframe as per client requirement
     '''
     def __init__(self,df,phase):
          self.df = df
          self.phase = phase

     def do_it_all(self,later_former_indices=None):
          self.drop_redundant_cols()
          self.replace_nan_with_blank_string()
          if self.phase!='3':
               self.switch_later_former_score(later_former_indices)
          self.remove_blank_rows()
          

     def drop_redundant_cols(self):
          self.df.drop(['user_1', 'email_1','age_1','email_1','gender_1','marital_status_1','sexual_orientation_1','professional_designation_1',
                        'years_in_practice_1'], axis=1, inplace=True)
          if self.phase =='1':
               self.df.drop(['Phase2','Phase2_1','short','short_1','redo','redo_1'],axis=1,inplace=True)
          elif self.phase =='2':
               self.df.drop(['Phase1','Phase1_1','short','short_1','redo','redo_1'],axis=1,inplace=True)
          elif self.phase =='3':
               self.df.drop(['short','short_1'],axis=1,inplace=True)

     def replace_nan_with_blank_string(self):
          self.df.replace('nan','',regex=True,inplace=True)

     def remove_blank_rows(self):
          '''Remove empty rows. If email col is empty then that row must be empty
          '''
          df=self.df
          self.df= df[df['email']!='']

     def switch_later_former_score(self,later_former_indices):
          '''If the details for survey taken later is first, we move it later in the row
             and move the former taken score before
          '''
          df = self.df
          for i in range(len(later_former_indices)):
              temp = df.iat[later_former_indices[i],0]
              df.iat[later_former_indices[i],0]= df.iat[later_former_indices[i],13]
              df.iat[later_former_indices[i],13]= temp
              
              temp = df.iat[later_former_indices[i],2]
              df.iat[later_former_indices[i],2]= df.iat[later_former_indices[i],15]
              df.iat[later_former_indices[i],15]= temp
              
              temp = df.iat[later_former_indices[i],3]
              df.iat[later_former_indices[i],3]= df.iat[later_former_indices[i],16]
              df.iat[later_former_indices[i],16]= temp
              
              temp = df.iat[later_former_indices[i],12]
              df.iat[later_former_indices[i],12]= df.iat[later_former_indices[i],17]
              df.iat[later_former_indices[i],17]= temp

          self.df=df


