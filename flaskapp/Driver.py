
# -*- coding: utf-8 -*-

import sys
sys.path.append('var/www/html/flaskapp/Connection')
from connection import Connection
sys.path.append('var/www/html/flaskapp/Phase')
from phase1 import Phase1
from phase2 import Phase2
from phase3 import Phase3
sys.path.append('var/www/html/flaskapp/Output')
from output import Output
import datetime
import numpy as np
import pandas as pd

def sort_ph1(test_case_removal):
    current_date =  str(datetime.datetime.now().strftime("%Y-%m-%d"))

    ph = Phase1(bool(test_case_removal),concat=True)
    ph.filterPhaseReports()
    ph.report=ph.sort_repo('email')
    df=ph.consolidate_repo()
    both_survey_completed= ph.both_survey_completed(df)
    single_survey_completed = ph.single_survey_completed(df)
    res=ph.percent_difference(df,both_survey_completed)
    bag_sum,boss_sum,average_bag,average_boss,total_participants = ph.averagePercentDiff(res[1],res[2],both_survey_completed)

    output = Output(res[0],'1')
    output.do_it_all(res[3])

    writer = pd.ExcelWriter('/var/www/html/flaskapp/Output/Phase1 '+current_date+'.xlsx',engine='xlsxwriter')
    output.df.to_excel(writer,startcol = 0, startrow = 11,index=False)
    worksheet = writer.sheets['Sheet1']
    worksheet.write_string(0, 0, 'EmQ Phase 1 Export – '+current_date)
    worksheet.write_string(1, 0, "Phase 1 both survey completed ")
    worksheet.write_string(2, 0, "Phase 1 single survey completed ")
    worksheet.write_string(1, 1, str(len(both_survey_completed)))
    worksheet.write_string(2, 1, str(len(single_survey_completed)))
    worksheet.write_string(3, 0, "Sum of all Bagging Groceries surveys taken in Phase1")
    worksheet.write_string(3, 1, str(bag_sum))
    worksheet.write_string(4, 0, "Sum of all Boss' Dinner surveys taken in Phase1")
    worksheet.write_string(4, 1, str(boss_sum))
    worksheet.write_string(5, 0, "Total Phase1 Participants ")
    worksheet.write_string(5, 1, str(total_participants))
    worksheet.write_string(6, 0, "Average of Bagging Grocery scores ")
    worksheet.write_string(6, 1, str(average_bag))
    worksheet.write_string(7, 0, "Average of Boss' Dinner scores ")
    worksheet.write_string(7, 1, str(average_boss))
    worksheet.write_string(8, 0, "Average difference between  \n Bagging Groceries and Boss's Dinner scores")
    worksheet.write_string(8, 1, str(average_bag-average_boss))
    worksheet.write_string(9, 0, "Average % difference between  \n Bagging Groceries and Boss's Dinner scores")
    worksheet.write_string(9, 1, str((average_bag-average_boss)*100))
    writer.save()


def sort_ph2(test_case_removal):
    current_date = str(datetime.datetime.now().strftime("%Y-%m-%d"))

    ph = Phase2(bool(test_case_removal),concat=True)
    ph.filterPhaseReports()
    ph.report=ph.sort_repo('email')
    df=ph.consolidate_repo()
    both_survey_completed= ph.both_survey_completed(df)
    single_survey_completed = ph.single_survey_completed(df)
    res=ph.percent_difference(df,both_survey_completed)
    former_sum,later_sum,average_former,average_later,total_participants = ph.averagePercentDiff(res[1],res[2])

    output = Output(res[0],'2')
    output.do_it_all(res[3])

    writer = pd.ExcelWriter('/var/www/html/flaskapp/Output/Phase2 '+current_date+'.xlsx', engine='xlsxwriter')
    output.df.to_excel(writer,startcol = 0, startrow = 11,index=False)
    worksheet = writer.sheets['Sheet1']
    worksheet.write_string(0, 0, 'EmQ Phase 2 Export – '+current_date)
    worksheet.write_string(1, 0, "Phase 2 both survey completed ")
    worksheet.write_string(2, 0, "Phase 2 single survey completed ")
    worksheet.write_string(1, 1, str(len(both_survey_completed)))
    worksheet.write_string(2, 1, str(len(single_survey_completed)))
    worksheet.write_string(3, 0, "Sum of all Phase2 surveys taken before ")
    worksheet.write_string(3, 1, str(former_sum))
    worksheet.write_string(4, 0, "Sum of all Phase2 surveys taken later ")
    worksheet.write_string(4, 1, str(later_sum))
    worksheet.write_string(5, 0, "Total Phase2 Participants ")
    worksheet.write_string(7, 0, "Average of later scores ")
    worksheet.write_string(7, 1, str(average_later))
    worksheet.write_string(8, 0, "Average difference between before and after scores for Phase2  ")
    worksheet.write_string(8, 1, str(average_later-average_former))
    worksheet.write_string(9, 0, "Average % difference between before and after scores for Phase2  ")
    worksheet.write_string(9, 1, str((average_later-average_former)*100))
    writer.save()

 
def sort_ph3(test_case_removal):
    current_date = str(datetime.datetime.now().strftime("%Y-%m-%d"))
    ph = Phase3(bool(test_case_removal),concat=True)
    ph.filterPhaseReports()
    redo_index = ph.redoScoreIndices()
    ph.percent_difference(redo_index)
    df= ph.report
    redo_sum = df[df['redo'].notnull()]['emq'].sum()
    non_redo_sum = df[df['redo'].isnull()]['emq'].sum()
    ph.report=ph.sort_repo('email')
    df=ph.consolidate_repo()

    output = Output(df,'3')
    output.do_it_all()
    writer = pd.ExcelWriter('/var/www/html/flaskapp/Output/No_Phase '+current_date+'.xlsx',engine='xlsxwriter')
    output.df.to_excel(writer,startcol = 0, startrow = 10,index=False)
    worksheet = writer.sheets['Sheet1']
    worksheet.write_string(0, 0, 'EmQ No Phase/Redo Export – '+current_date)
    worksheet.write_string(1, 0, "Number of Redo Participants")
    worksheet.write_string(1, 1, str(len(redo_index)))
    worksheet.write_string(2, 0, "Sum of all redo participants ")
    worksheet.write_string(2, 1, str(redo_sum))
    worksheet.write_string(3, 0, "Sum of all non-phase  participants (except redo) ")
    worksheet.write_string(3, 1, str(non_redo_sum))
    worksheet.write_string(4, 0, "Average % Difference ")
    worksheet.write_string(4, 1, str('Insert number here'))
    writer.save()






