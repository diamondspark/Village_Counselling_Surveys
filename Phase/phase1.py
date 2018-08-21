from phase import Phase

class Phase1(Phase):
     '''Subclass of Phase.vThis deals with methods to do with working of phase 1 reports
     '''

     def filterPhaseReports(self):
          '''Get participants who have done phase 1
          '''
          df = self.report
          self.report= df[df['Phase1'].notnull()]

     def averagePercentDiff(self,scorelist1,scorelist2,both_survey_completed):
          '''For Phase 1 scorelist1 is list of all scores of Bagging Grocery
             and scorelist2 is list of all Boss dinner scores
          '''
          scorelist1,scorelist2= self.getBagBossScores(both_survey_completed)
          bag_sum = sum(scorelist1)
          boss_sum = sum(scorelist2)
          total_participants = len(self.report)
          average_boss = boss_sum/total_participants
          average_bag = bag_sum/total_participants
 
          return bag_sum,boss_sum,average_bag,average_boss,total_participants

     def getBagBossScores(self,both_survey_completed):
          '''Create scorelist1 n scorelist2 of bagging n boss reports where both survey completed.
             as required for 

          '''
          bag_scores=[]
          boss_scores=[]
          df= self.report
          for i in range(len(both_survey_completed)):
               name1= df.iat[both_survey_completed[i],1]
               name2 =df.iat[both_survey_completed[i],17]
               score1= df.iat[both_survey_completed[i],14]
               score2=df.iat[both_survey_completed[i],30]
               if name1=="Bagging Groceries":
                    bag_scores.append(score1)
                    if name2=="Boss' Dinner":
                         boss_scores.append(score2)
               elif name1=="Boss' Dinner":
                    boss_scores.append(score1)
                    if name2=="Bagging Groceries":
                         bag_scores.append(score2)
          return bag_scores,boss_scores

     
                    
                    
                    

     
