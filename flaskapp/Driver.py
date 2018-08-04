import sys
sys.path.append('./../Connection/')
from connection import Connection
sys.path.append('./../Phase')
from phase1 import Phase1
from phase2 import Phase2
sys.path.append('./../Output')
from output import Output
import datetime
import numpy as np

def sort_ph1(test_case_removal):
    current_date =  str(datetime.datetime.now().strftime("%Y-%m-%d"))

    ph = Phase1(bool(test_case_removal),concat=True)
    ph.filterPhaseReports()
    ph.report=ph.sort_repo('email')
    df=ph.consolidate_repo()
    both_survey_completed= ph.both_survey_completed(df)
    print "Phase 1 both survey completed "+ str(len(both_survey_completed))
    single_survey_completed = ph.single_survey_completed(df)
    print "Phase 1 single survey completed "+ str(len(single_survey_completed))
    res=ph.percent_difference(df,both_survey_completed)
    
    output = Output(res[0],'1')
    output.do_it_all()
    output.df.to_csv('/var/www/html/flaskapp/Output/Phase1 '+current_date+'.csv',index=False)
    output.df.to_excel('/var/www/html/flaskapp/Output/Phase1 '+current_date+'.xlsx',index=False)

def sort_ph2(test_case_removal):
    current_date = str(datetime.datetime.now().strftime("%Y-%m-%d"))

    ph = Phase2(bool(test_case_removal),concat=True)
    ph.filterPhaseReports()
    ph.report=ph.sort_repo('email')
    df=ph.consolidate_repo()
    both_survey_completed= ph.both_survey_completed(df)
    print "Phase 2 both survey completed "+ str(len(both_survey_completed))
    single_survey_completed = ph.single_survey_completed(df)
    print "Phase 2 single survey completed "+ str(len(single_survey_completed))
    res=ph.percent_difference(df,both_survey_completed)

    output = Output(res[0],'2')
    output.do_it_all()
    output.df.to_csv('/var/www/html/flaskapp/Output/Phase2 '+current_date+'.csv',index=False)
    output.df.to_excel('/var/www/html/flaskapp/Output/Phase2 '+current_date+'.xlsx',index=False)
