import sys
sys.path.append('./../Connection/')
from connection import Connection
sys.path.append('./../Phase')
from phase1 import Phase1
from phase2 import Phase2


def sort_ph1():
    ph = Phase1(concat=True)
    ph.report=ph.sort_repo('email')
    df=ph.consolidate_repo()
    both_survey_completed= ph.both_survey_completed(df)
    print "Phase 1 both survey completed "+ str(len(both_survey_completed))
    single_survey_completed = ph.single_survey_completed(df)
    print "Phase 1 single survey completed "+ str(len(single_survey_completed))
    res=ph.percent_difference(df,both_survey_completed)
    res[0].to_csv('ph1.csv')
    res[0].to_excel('ph1.xlsx')

def sort_ph2():
    ph = Phase2(concat=True)
    ph.report=ph.sort_repo('email')
    df=ph.consolidate_repo()
    both_survey_completed= ph.both_survey_completed(df)
    print "Phase 2 both survey completed "+ str(len(both_survey_completed))
    single_survey_completed = ph.single_survey_completed(df)
    print "Phase 2 single survey completed "+ str(len(single_survey_completed))
    res=ph.percent_difference(df,both_survey_completed)
    res[0].to_csv('ph2.csv')
    res[0].to_excel('ph2.xlsx')
