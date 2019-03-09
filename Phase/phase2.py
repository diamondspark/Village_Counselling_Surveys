from phase import Phase
from dateutil.parser import parse

class Phase2(Phase):
     '''Subclass of Phase.vThis deals with methods to do with working of phase2 reports
     '''

     def filterPhaseReports(self):
          '''Get participants who have done phase 2
          '''
          df = self.report
          self.report= df[df['Phase2'].notnull()]

     def averagePercentDiff(self,scorelist1,scorelist2):
          '''For Phase 1 scorelist1 is list of all scores taken before
             and scorelist2 is list of all scores taken later
          '''
          former_sum = sum(scorelist1)
          later_sum = sum(scorelist2)
          total_participants = len(self.report)
          average_former = former_sum/total_participants
          average_later = later_sum/total_participants
 
          return former_sum,later_sum,average_former,average_later,total_participants

     def average_difference(self,list1,list2):
          if len(list1)==0 or len(list2)==0:
               return 0

          sum_scores_list_1 = sum([float(x[1]) for x in list1])
          sum_scores_list_2 = sum([float(x[1]) for x in list2])
          return float((sum_scores_list_1-sum_scores_list_2)/len(list1))


     def get_people_and_scores(self,df, both_repo_completed):
          date_col_index = df.columns.get_loc("date")
          time_col_index = df.columns.get_loc("time")
          date2_col_index = df.columns.get_loc("date_2")
          time2_col_index = df.columns.get_loc("time_2")
          emq1_col_index = df.columns.get_loc("emq_1")
          emq2_col_index = df.columns.get_loc("emq_2")
          emq_type_col_index = df.columns.get_loc("quiz_1")

          bgf,bdf,bgs,bds=[],[],[],[]

          for i in range(len(both_repo_completed)):
               date_time = df.iat[both_repo_completed[i],date_col_index]+' '+df.iat[both_repo_completed[i],time_col_index]
               date_time_1 = df.iat[both_repo_completed[i],date2_col_index]+' '+df.iat[both_repo_completed[i],time2_col_index]
               date_time = parse(date_time)
               date_time_1 = parse(date_time_1)

               if date_time < date_time_1:
                    if df.iat[both_repo_completed[i],emq_type_col_index]=='Bagging Groceries':
                         bgf.append([both_repo_completed[i],df.iat[both_repo_completed[i],emq1_col_index]])
                         bds.append([both_repo_completed[i],df.iat[both_repo_completed[i],emq2_col_index]])
                    elif df.iat[both_repo_completed[i],emq_type_col_index]=="Boss' Dinner":
                         bdf.append([both_repo_completed[i],df.iat[both_repo_completed[i],emq1_col_index]])
                         bgs.append([both_repo_completed[i],df.iat[both_repo_completed[i],emq2_col_index]])

               else:
                    if df.iat[both_repo_completed[i],emq_type_col_index]=='Bagging Groceries':
                         bgs.append([both_repo_completed[i],df.iat[both_repo_completed[i],emq1_col_index]])
                         bdf.append([both_repo_completed[i],df.iat[both_repo_completed[i],emq2_col_index]])
                    elif df.iat[both_repo_completed[i],emq_type_col_index]=="Boss' Dinner":
                         bds.append([both_repo_completed[i],df.iat[both_repo_completed[i],emq1_col_index]])
                         bgf.append([both_repo_completed[i],df.iat[both_repo_completed[i],emq2_col_index]])

          return bgf,bdf,bgs,bds

     def calculate_improvement(self, bgf, bdf,bgs,bds ):
          improved_sum_first_scores = 0
          improved_sum_second_scores= 0
          total_improved_scores=[]

          for i in range(max(len(bgf),len(bdf))):
               try:
                    if float(bgf[i][1])<float(bds[i][1]):
                         improved_sum_first_scores = improved_sum_first_scores+float(bgf[i][1])
                         improved_sum_second_scores= improved_sum_second_scores+float(bds[i][1])
                         total_improved_scores.append(i)
               except Exception as e:
                    pass

               try:
                    if float(bdf[i][1])<float(bgs[i][1]):
                         improved_sum_first_scores = improved_sum_first_scores+float(bdf[i][1])
                         improved_sum_second_scores= improved_sum_second_scores+float(bgs[i][1])
                         total_improved_scores.append(i)

               except Exception as e:
                    pass

          avg_improvement_diff = improved_sum_second_scores - improved_sum_first_scores
          avg_improvement_per_subj = float(avg_improvement_diff/len(total_improved_scores))
          percent_improvement = float(avg_improvement_diff/improved_sum_first_scores)

          return len(total_improved_scores),percent_improvement

     def single_bag_boss_list(self,df):
          '''If email is present and email_1 is absent then only one phase is completed.
             Which phase is completed is dependent on which phase(phase1 or phase2) object is being dealt with
          '''
          email_2_col_index = df.columns.get_loc("email_2")
          email_col_index = df.columns.get_loc("email")
          emq_type_col_index = df.columns.get_loc("quiz_1")

          bg_only_ppl=[]
          bd_only_ppl=[]
          for i in range(len(df)):
               if df.iat[i,email_col_index]!='' and df.iat[i,email_2_col_index]=='':
                    if df.iat[i,emq_type_col_index]== 'Bagging Groceries':
                         bg_only_ppl.append(i)
                    elif df.iat[i,emq_type_col_index]== "Boss' Dinner":
                         bd_only_ppl.append(i)

          return bg_only_ppl,bd_only_ppl









