from phase import Phase

class Phase1(Phase):
     '''Subclass of Phase.vThis deals with methods to do with working of phase 1 reports
     '''

     def filterPhaseReports(self):
          '''Get participants who have done phase 1
          '''
          df = self.report
          self.report= df[df['Phase1'].notnull()]
