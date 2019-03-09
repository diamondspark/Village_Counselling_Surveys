
# -*- coding: utf-8 -*-

import sys
##sys.path.append('var/www/html/flaskapp/Connection')
sys.path.append('./../Connection/')
from connection import Connection
##sys.path.append('var/www/html/flaskapp/Phase')
sys.path.append('./../Phase')
from phase1 import Phase1
from phase2 import Phase2
from phase3 import Phase3
##sys.path.append('var/www/html/flaskapp/Output')
sys.path.append('./../Output')
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
    bg_ppl,bg_scores,bd_ppl,bd_scores = ph.get_total_scores_and_people(df)
    res=ph.percent_difference(df,both_survey_completed)
    bg_scores = [float(x) for x in bg_scores]
    bd_scores = [float(x) for x in bd_scores]
    avg_bg_scores = float(sum(bg_scores)/len(bg_ppl))
    avg_bd_scores = float(sum(bd_scores)/len(bd_ppl))

    output = Output(res[0],'1')
    output.do_it_all(res[3])
    total_participants = len(output.df)
    
##    writer = pd.ExcelWriter('/var/www/html/flaskapp/Output/Phase1 '+current_date+'.xlsx',engine='xlsxwriter')
    writer = pd.ExcelWriter('./../Output/Phase1 '+current_date+'.xlsx',engine='xlsxwriter')
    output.df.to_excel(writer,startcol = 0, startrow = 11,index=False)
    worksheet = writer.sheets['Sheet1']
    worksheet.write_string(0, 0, 'EmQ Phase 1 Export – '+current_date)
    worksheet.write_string(1, 0, "Phase 1 both quizzes completed ")
    worksheet.write_string(1, 8, str(len(both_survey_completed)))
    worksheet.write_string(2, 0, "Total Phase1 Participants ")
    worksheet.write_string(2, 8, str(total_participants))
    worksheet.write_string(3, 0, "Total BG Participants ")
    worksheet.write_string(3, 8, str(len(bg_ppl)))
    worksheet.write_string(4, 0, "Total BD Participants ")
    worksheet.write_string(4, 8, str(len(bd_ppl)))
    worksheet.write_string(5, 0, "Total BG scores ")
    worksheet.write_string(5, 8, str(sum(bg_scores)))
    worksheet.write_string(6, 0, "Total BD scores ")
    worksheet.write_string(6, 8, str(sum(bd_scores)))
    worksheet.write_string(7, 0, "Average of Bagging Grocery scores ")
    worksheet.write_string(7, 8, str(avg_bg_scores))
    worksheet.write_string(8, 0, "Average of Boss' Dinner scores ")
    worksheet.write_string(8, 8, str(avg_bd_scores))
    worksheet.write_string(9, 0, "Average Difference (BG - BD) ")
    worksheet.write_string(9, 8, str(avg_bg_scores- avg_bd_scores ))
    writer.save()


def sort_ph2(test_case_removal):
    current_date = str(datetime.datetime.now().strftime("%Y-%m-%d"))

    ph = Phase2(bool(test_case_removal),concat=True)
    ph.filterPhaseReports()
    ph.report=ph.sort_repo('email')
    df=ph.consolidate_repo()
    both_survey_completed= ph.both_survey_completed(df)
    res=ph.percent_difference(df,both_survey_completed)
    bgf,bdf,bgs,bds = ph.get_people_and_scores(df, both_survey_completed)
    total_improved_scores, percent_improvement= ph.calculate_improvement( bgf, bdf,bgs,bds )
    bg_only_ppl, bd_only_ppl = ph.single_bag_boss_list(df)

    output = Output(res[0],'2')
    output.do_it_all(res[3])
    total_participants = len(output.df)

##    writer = pd.ExcelWriter('/var/www/html/flaskapp/Output/Phase2 '+current_date+'.xlsx', engine='xlsxwriter')
    writer = pd.ExcelWriter('./../Output/Phase2 '+current_date+'.xlsx',engine='xlsxwriter')
    output.df.to_excel(writer,startcol = 0, startrow = 15,index=False)
    worksheet = writer.sheets['Sheet1']
    worksheet.write_string(0, 0, 'EmQ Phase 2 Export – '+current_date)
    worksheet.write_string(2, 0, "Phase 2 both quizzes completed ")
    worksheet.write_string(2, 8, str(len(both_survey_completed)))
    worksheet.write_string(3, 0, "Bagging Grocery only people ")
    worksheet.write_string(3, 8, str(len(bg_only_ppl)))
    worksheet.write_string(4, 0, "Boss' Dinner only people ")
    worksheet.write_string(4, 8, str(len(bd_only_ppl)))
    
    worksheet.write_string(5, 0, "Both surveys done - Bagging Grocery first")
    worksheet.write_string(5, 8, str(len(bgf)))
    worksheet.write_string(6, 0, "Both surveys done - Boss' Dinner Second")
    worksheet.write_string(6, 8, str(len(bds)))
    worksheet.write_string(7, 0, "BGF, BDS - Average Difference")
    worksheet.write_string(7, 8, str(ph.average_difference(bgf,bds)))
    worksheet.write_string(8, 0, "Both surveys done - Boss' Dinner first")
    worksheet.write_string(8, 8, str(len(bdf)))
    worksheet.write_string(9, 0, "Both surveys done - Bagging Grocery Second")
    worksheet.write_string(9, 8, str(len(bgs)))
    worksheet.write_string(10, 0, "BDF, BGS - Average Difference")
    worksheet.write_string(10, 8, str(ph.average_difference(bdf,bgs)))
    worksheet.write_string(11, 0, "Total people with improved scores")
    worksheet.write_string(11, 8, str(total_improved_scores))
    worksheet.write_string(12, 0, "Average %  improvement")
    worksheet.write_string(12, 8, str(percent_improvement))
    worksheet.write_string(13, 0, "Average improvement")
    worksheet.write_string(13, 8, str(ph.average_difference(bgf,bds)-ph.average_difference(bdf,bgs)))



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






