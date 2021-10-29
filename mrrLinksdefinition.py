#Links, Apps and work environment definition
# Only for MRR product

from tkinter import *
import subprocess, os 
from shutil import copy , copyfile
#from ShortcutsProductEngineering import open_MRR

def action_BTDB():
    os.system("BTDB")
def action_SAP():
    os.system("saplogon")
def action_ECAM():
    os.system("ECAM")
def action_Actividades():
    subprocess.Popen(r'explorer /open, "https://bosch-my.sharepoint.com/personal/goa7ju_bosch_com/Documents/ActividadesDiariasAdrian_.xlsx?web=1"')
def action_ProdEngWeb():
    os.system("paginaweb")
def action_mws():
    os.system("mws")
def action_oisnet():
    os.system("oisnet")

def OpenLink0():
    subprocess.Popen(r'explorer /open,"\\bosch.com\dfsrb\DfsUS\loc\JU1\Projects\MSE1\MOE2\05_MRR\MFQ2"')
    copy("\\bosch.com\dfsrb\DfsUS\loc\JU1\Projects\MSE1\MOE2\05_MRR\MFQ2")
def OpenLink1():
    subprocess.Popen(r'explorer /open, "\\bosch.com\dfsrb\DfsUS\LOC\JU1\Projects\MSE1\MOE2\05_MRR\MFQ2\40_Q_incidents"')
    copy("\\bosch.com\dfsrb\DfsUS\LOC\JU1\Projects\MSE1\MOE2\05_MRR\MFQ2\40_Q_incidents")
def OpenLink2():
    subprocess.Popen(r'explorer /open, "\\bosch.com\dfsrb\DfsUS\LOC\JU1\Projects\MSE1\MOE2\05_MRR\MFQ2\40_Q_incidents\10 Q events" ') 
    copy("\\bosch.com\dfsrb\DfsUS\LOC\JU1\Projects\MSE1\MOE2\05_MRR\MFQ2\40_Q_incidents\10 Q events" )
def OpenLink3():
    subprocess.Popen(r'explorer /open, "\\bosch.com\dfsrb\DfsUS\LOC\JU1\Projects\MSE1\MOE2\05_MRR\MFQ2\30 Failure analysis"')
    copy("\\bosch.com\dfsrb\DfsUS\LOC\JU1\Projects\MSE1\MOE2\05_MRR\MFQ2\30 Failure analysis")
def OpenLink4():
    subprocess.Popen(r'explorer /open, "\\bosch.com\dfsrb\DfsUS\LOC\JU1\Projects\MSE1\MOE2\05_MRR\MFQ2\10 Planning\60 Q criteria\10_CriterioLiberacion"')
    copy("\\bosch.com\dfsrb\DfsUS\LOC\JU1\Projects\MSE1\MOE2\05_MRR\MFQ2\10 Planning\60 Q criteria\10_CriterioLiberacion")
def OpenLink5():
    subprocess.Popen(r'explorer /open,"\\bosch.com\dfsrb\DfsUS\LOC\JU1\Projects\MSE1\MOE2\05_MRR\MFQ2\50 PQA\ "')
    copy("\\bosch.com\dfsrb\DfsUS\LOC\JU1\Projects\MSE1\MOE2\05_MRR\MFQ2\50 PQA\ ")
def OpenLink6():
    subprocess.Popen(r'explorer /open, "\\bosch.com\dfsrb\DfsUS\LOC\JU1\Projects\MSE1\MOE2\05_MRR\MFQ2\20 Product validation"')
    copy("\\bosch.com\dfsrb\DfsUS\LOC\JU1\Projects\MSE1\MOE2\05_MRR\MFQ2\20 Product validation")
def OpenLink7():
    subprocess.Popen(r'explorer /open, "\\bosch.com\dfsrb\DfsUS\LOC\JU1\Projects\MSE1\MOE2\05_MRR\140_Quality\06_Concessions"')
    copy("\\bosch.com\dfsrb\DfsUS\LOC\JU1\Projects\MSE1\MOE2\05_MRR\140_Quality\06_Concessions")
def OpenLink8():
    subprocess.Popen(r'explorer /open, "\\bosch.com\dfsrb\DfsUS\LOC\JU1\Projects\MSE1\MOE2\05_MRR\MFQ2\50 PQA\10 QI"')
    copy("\\bosch.com\dfsrb\DfsUS\LOC\JU1\Projects\MSE1\MOE2\05_MRR\MFQ2\50 PQA\10 QI")
def OpenLink9():
    subprocess.Popen(r'explorer /open, "\\bosch.com\dfsrb\DfsUS\LOC\JU1\Projects\MSE1\MOE2\05_MRR\MFQ2\10 Planning\70_Work_instruction_PQI\ "')
    copy("\\bosch.com\dfsrb\DfsUS\LOC\JU1\Projects\MSE1\MOE2\05_MRR\MFQ2\10 Planning\70_Work_instruction_PQI\ ")
def OpenReportesAnalisis():
    subprocess.Popen(r'explorer /open, "\\bosch.com\dfsrb\DfsUS\loc\JU1\Projects\MSE1\MOE2\05_MRR\MFQ2\30 Failure analysis\60 Eventos\01. Formato\Formato_eventos_MFQ4_V3.5.xlsm "')
def OpenQISupport():
    subprocess.Popen(r'explorer /open, "\\bosch.com\dfsrb\DfsUS\loc\JU1\Projects\MSE1\MOE2\05_MRR\MFQ2\50 PQA\PQA QAM\SupportPS_PQAfiles\SuportFileForPQAEvents_v01.xlsm" ')
    subprocess.Popen(r'explorer /open,"\\bosch.com\dfsrb\DfsUS\LOC\JU1\Projects\MSE1\MOE2\05_MRR\MFQ2\50 PQA\ "')
def OpenCheckListAnalista_MRR():
    subprocess.Popen(r'explorer /open, "\\bosch.com\dfsrb\DfsUS\loc\JU1\Projects\MSE1\MOE2\05_MRR\MFQ2\30 Failure analysis\ChecklistInicioTurno\CheckListInicioTurnoAnalista_MRR.xlsm"')
def OpenPQA_QAM():
    subprocess.Popen(r'explorer /open, "\\bosch.com\dfsrb\DfsUS\loc\JU1\Projects\MSE1\MOE2\05_MRR\MFQ2\50 PQA\PQA QAM\01_MRR_PQA_QAM.xlsx"')

############# RVC LINKS SEGMENT

def rvcOpenLink0():
    subprocess.Popen(r'explorer /open, "\\bosch.com\dfsrb\DfsUS\LOC\JU1\Projects\MSE1\MOE2\02_Rear_View_Camera\145_MFQ2"')
    copy("\\bosch.com\dfsrb\DfsUS\LOC\JU1\Projects\MSE1\MOE2\02_Rear_View_Camera\145_MFQ2")
def rvcOpenLink1():
    subprocess.Popen(r'explorer /open, "\\bosch.com\dfsrb\DfsUS\LOC\JU1\Projects\MSE1\MOE2\02_Rear_View_Camera\145_MFQ2\40 Q incidents"')
    copy("\\bosch.com\dfsrb\DfsUS\LOC\JU1\Projects\MSE1\MOE2\02_Rear_View_Camera\145_MFQ2\40 Q incidents")
def rvcOpenLink2():
    subprocess.Popen(r'explorer /open, "\\bosch.com\dfsrb\DfsUS\LOC\JU1\Projects\MSE1\MOE2\02_Rear_View_Camera\145_MFQ2\40 Q incidents\10 Q events"')
    copy("\\bosch.com\dfsrb\DfsUS\LOC\JU1\Projects\MSE1\MOE2\02_Rear_View_Camera\145_MFQ2\40 Q incidents\10 Q events")
def rvcOpenLink3():
    subprocess.Popen(r'explorer /open, "\\bosch.com\dfsrb\DfsUS\LOC\JU1\Projects\MSE1\MOE2\02_Rear_View_Camera\145_MFQ2\30 Failure analysis"')
    copy("\\bosch.com\dfsrb\DfsUS\LOC\JU1\Projects\MSE1\MOE2\02_Rear_View_Camera\145_MFQ2\30 Failure analysis")
def rvcOpenLink4():
    subprocess.Popen(r'explorer /open, "\\bosch.com\dfsrb\DfsUS\LOC\JU1\Projects\MSE1\MOE2\02_Rear_View_Camera\145_MFQ2\10_Planning\60 Q Criteria\10_CriterioLiberacion"')      
    copy("\\bosch.com\dfsrb\DfsUS\LOC\JU1\Projects\MSE1\MOE2\02_Rear_View_Camera\145_MFQ2\10_Planning\60 Q Criteria\10_CriterioLiberacion")
def rvcOpenLink5():
    subprocess.Popen(r'explorer /open, "\\bosch.com\dfsrb\DfsUS\LOC\JU1\Projects\MSE1\MOE2\02_Rear_View_Camera\145_MFQ2\50 PQA"')
    copy("\\bosch.com\dfsrb\DfsUS\LOC\JU1\Projects\MSE1\MOE2\02_Rear_View_Camera\145_MFQ2\50 PQA")
def rvcOpenLink6():
    subprocess.Popen(r'explorer /open, "\\bosch.com\dfsrb\DfsUS\LOC\JU1\Projects\MSE1\MOE2\02_Rear_View_Camera\100_Process\001_Validations"')
    copy("\\bosch.com\dfsrb\DfsUS\LOC\JU1\Projects\MSE1\MOE2\02_Rear_View_Camera\100_Process\001_Validations")
def rvcOpenLink7():
    subprocess.Popen(r'explorer /open, "\\bosch.com\dfsrb\DfsUS\LOC\JU1\Projects\MSE1\MOE2\02_Rear_View_Camera\140_Quality\3_Concessions"')
    copy("\\bosch.com\dfsrb\DfsUS\LOC\JU1\Projects\MSE1\MOE2\02_Rear_View_Camera\140_Quality\3_Concessions")
def rvcOpenLink8():
    subprocess.Popen(r'explorer /open, "\\bosch.com\dfsrb\DfsUS\LOC\JU1\Projects\MSE1\MOE2\02_Rear_View_Camera\145_MFQ2\50 PQA\10 QI"')
    copy("\\bosch.com\dfsrb\DfsUS\LOC\JU1\Projects\MSE1\MOE2\02_Rear_View_Camera\145_MFQ2\50 PQA\10 QI")
def rvcOpenLink9():
    subprocess.Popen(r'explorer /open, "\\bosch.com\dfsrb\DfsUS\LOC\JU1\Projects\MSE1\MOE2\02_Rear_View_Camera\145_MFQ2\10_Planning\07_Work instruction, PQI"')
    copy("\\bosch.com\dfsrb\DfsUS\LOC\JU1\Projects\MSE1\MOE2\02_Rear_View_Camera\145_MFQ2\10_Planning\07_Work instruction, PQI")

def rvc_OpenReportesAnalisis():
    subprocess.Popen(r'explorer /open, "\\bosch.com\dfsrb\DfsUS\loc\JU1\Projects\MSE1\MOE2\05_MRR\MFQ2\30 Failure analysis\60 Eventos\01. Formato\Formato_eventos_MFQ4_V3.5.xlsm "')
def rvc_OpenQISupport():
    subprocess.Popen(r'explorer /open, "\\bosch.com\dfsrb\DfsUS\loc\JU1\Projects\MSE1\MOE2\02_Rear_View_Camera\145_MFQ2\50 PQA\PQA QAM\SupportPS_PQAfiles\SuportFileForPQAEvents_v01.xlsm ')
    subprocess.Popen(r'explorer /open,"\\bosch.com\dfsrb\DfsUS\loc\JU1\Projects\MSE1\MOE2\02_Rear_View_Camera\145_MFQ2\50 PQA\ "')
def rvc_OpenCheckListAnalista_MRR():
    subprocess.Popen(r'explorer /open, "\\bosch.com\dfsrb\DfsUS\loc\JU1\Projects\MSE1\MOE2\02_Rear_View_Camera\145_MFQ2\30 Failure analysis\CheckListInicioTurnoAnalista_RVC.xlsm"')
def rvc_OpenPQA_QAM():
    subprocess.Popen(r'explorer /open, "\\bosch.com\dfsrb\DfsUS\loc\JU1\Projects\MSE1\MOE2\02_Rear_View_Camera\145_MFQ2\50 PQA\PQA QAM\01_RVC_PQA_QAM.xlsx"')


################# PP LINKS SEGMENT

def ppOpenLink0():
    subprocess.Popen(r'explorer /open, "\\bosch.com\dfsrb\DfsUS\LOC\JU1\Projects\MSE1\MOE2\04_ParkPilot\145_MFQ"')
    copy("\\bosch.com\dfsrb\DfsUS\LOC\JU1\Projects\MSE1\MOE2\04_ParkPilot\145_MFQ")
def ppOpenLink1():
    subprocess.Popen(r'explorer /open, "\\bosch.com\dfsrb\DfsUS\LOC\JU1\Projects\MSE1\MOE2\04_ParkPilot\145_MFQ\40_Q_incidents"')
    copy("\\bosch.com\dfsrb\DfsUS\LOC\JU1\Projects\MSE1\MOE2\04_ParkPilot\145_MFQ\40_Q_incidents")
def ppOpenLink2():
    subprocess.Popen(r'explorer /open, "\\bosch.com\dfsrb\DfsUS\LOC\JU1\Projects\MSE1\MOE2\04_ParkPilot\145_MFQ\40_Q_incidents\10 Q events"')
    copy("\\bosch.com\dfsrb\DfsUS\LOC\JU1\Projects\MSE1\MOE2\04_ParkPilot\145_MFQ\40_Q_incidents\10 Q events")
def ppOpenLink3():
    subprocess.Popen(r'explorer /open, "\\bosch.com\dfsrb\DfsUS\LOC\JU1\Projects\MSE1\MOE2\04_ParkPilot\145_MFQ\30 Failure analysis"')
    copy("\\bosch.com\dfsrb\DfsUS\LOC\JU1\Projects\MSE1\MOE2\04_ParkPilot\145_MFQ\30 Failure analysis")
def ppOpenLink4():
    subprocess.Popen(r'explorer /open, "\\bosch.com\dfsrb\DfsUS\LOC\JU1\Projects\MSE1\MOE2\04_ParkPilot\145_MFQ\10 Planning\60 Q criteria\10_CriterioLiberacion"')
    copy("\\bosch.com\dfsrb\DfsUS\LOC\JU1\Projects\MSE1\MOE2\04_ParkPilot\145_MFQ\10 Planning\60 Q criteria\10_CriterioLiberacion")
def ppOpenLink5():
    subprocess.Popen(r'explorer /open, "\\bosch.com\dfsrb\DfsUS\LOC\JU1\Projects\MSE1\MOE2\04_ParkPilot\145_MFQ\50 PQA"')
    copy("\\bosch.com\dfsrb\DfsUS\LOC\JU1\Projects\MSE1\MOE2\04_ParkPilot\145_MFQ\50 PQA")
def ppOpenLink6():
    subprocess.Popen(r'explorer /open, "\\bosch.com\dfsrb\DfsUS\LOC\JU1\Projects\MSE1\MOE2\04_ParkPilot\100 Process\21 Validaciones\Ppilot"')
    copy("\\bosch.com\dfsrb\DfsUS\LOC\JU1\Projects\MSE1\MOE2\04_ParkPilot\100 Process\21 Validaciones\Ppilot")
def ppOpenLink7():
    subprocess.Popen(r'explorer /open, "\\bosch.com\dfsrb\DfsUS\LOC\JU1\Projects\MSE1\MOE2\04_ParkPilot\140_Quality\100_Concession"')
    copy("\\bosch.com\dfsrb\DfsUS\LOC\JU1\Projects\MSE1\MOE2\04_ParkPilot\140_Quality\100_Concession")
def ppOpenLink8():
    subprocess.Popen(r'explorer /open, "\\bosch.com\dfsrb\DfsUS\LOC\JU1\Projects\MSE1\MOE2\04_ParkPilot\145_MFQ\50 PQA\10 QI"')
    copy("\\bosch.com\dfsrb\DfsUS\LOC\JU1\Projects\MSE1\MOE2\04_ParkPilot\145_MFQ\50 PQA\10 QI")
def ppOpenLink9():
    subprocess.Popen(r'explorer /open, "\\bosch.com\dfsrb\DfsUS\LOC\JU1\Projects\MSE1\MOE2\04_ParkPilot\145_MFQ\10 Planning\70 Work instruction, PQI"')
    copy("\\bosch.com\dfsrb\DfsUS\LOC\JU1\Projects\MSE1\MOE2\04_ParkPilot\145_MFQ\10 Planning\70 Work instruction, PQI")

def pp_OpenReportesAnalisis():
    subprocess.Popen(r'explorer /open, "\\bosch.com\dfsrb\DfsUS\loc\JU1\Projects\MSE1\MOE2\04_ParkPilot\145_MFQ\30 Failure analysis\60_Eventos\00. Formato\Formato_eventos_MFQ4_V3.4.xlsm')
def pp_OpenQISupport():
    subprocess.Popen(r'explorer /open, "\\bosch.com\dfsrb\DfsUS\loc\JU1\Projects\MSE1\MOE2\04_ParkPilot\145_MFQ\50 PQA\PQA_QAM\SupportPS_PQAfiles\SuportFileForPQAEvents_v01.xlsm" ')
    subprocess.Popen(r'explorer /open,"\\bosch.com\dfsrb\DfsUS\loc\JU1\Projects\MSE1\MOE2\04_ParkPilot\145_MFQ\50 PQA\PQA_QAM')
def pp_OpenCheckListAnalista():
    subprocess.Popen(r'explorer /open, "\\bosch.com\dfsrb\DfsUS\loc\JU1\Projects\MSE1\MOE2\04_ParkPilot\145_MFQ\30 Failure analysis\CheckListInicioTurnoAnalista_ParkPilot.xlsm"')
def pp_OpenPQA_QAM():
    subprocess.Popen(r'explorer /open, "\\bosch.com\dfsrb\DfsUS\loc\JU1\Projects\MSE1\MOE2\04_ParkPilot\145_MFQ\50 PQA\PQA_QAM\01_PP_PQA_QAM.xlsx"')
