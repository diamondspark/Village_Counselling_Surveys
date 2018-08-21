from phase import Phase

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
