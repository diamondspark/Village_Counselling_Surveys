from phase import Phase

class Phase3(Phase):
     '''Subclass of Phase. This deals with methods to do wih working of
        no phase designated report
     '''

     def filterPhaseReports(self):
          '''Get Participant whose both Phase1 and Phase2 are empty
          '''
          df = self.report
          self.report= df[(df['Phase1'].isnull() & df['Phase2'].isnull()) | df['redo'].notnull()]

     
     def redoScoreIndices(self):
          df= self.report
          return df.index[df['redo'].notnull()].tolist()

     def percent_difference(self, redo_index):
          '''Fill %_differnce column with redo score - emq score
          '''
          df= self.report
          for i in range(len(redo_index)):
               index=redo_index[i]
               df.loc[index,'%_difference'] = df.loc[index,'redo']-df.loc[index,"emq"]
          self.report= df


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
