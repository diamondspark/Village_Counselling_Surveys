from phase import Phase

class Phase2(Phase):
     '''Subclass of Phase.vThis deals with methods to do with working of phase2 reports
     '''

     def filterPhaseReports(self):
          '''Get participants who have done phase 2
          '''
          df = self.report
          self.report= df[df['Phase2'].notnull()]
