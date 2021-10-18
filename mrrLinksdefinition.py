#Links, Apps and work environment definition
# Only for MRR product

from tkinter import *
import os 
#from ShortcutsProductEngineering import open_MRR

link0_MRR = "\\bosch.com\dfsrb\DfsUS\LOC\JU1\Projects\MSE1\MOE2\05_MRR\MFQ2"
link1_MRR = "\\bosch.com\dfsrb\DfsUS\LOC\JU1\Projects\MSE1\MOE2\05_MRR\MFQ2\40_Q_incidents"
link2_MRR = "\\bosch.com\dfsrb\DfsUS\LOC\JU1\Projects\MSE1\MOE2\05_MRR\MFQ2\40_Q_incidents\10 Q events"
link3_MRR = "\\bosch.com\dfsrb\DfsUS\LOC\JU1\Projects\MSE1\MOE2\05_MRR\MFQ2\30 Failure analysis"
link4_MRR = "\\bosch.com\dfsrb\DfsUS\LOC\JU1\Projects\MSE1\MOE2\05_MRR\MFQ2\10 Planning\60 Q criteria\10_CriterioLiberacion"
link5_MRR = "\\bosch.com\dfsrb\DfsUS\LOC\JU1\Projects\MSE1\MOE2\05_MRR\MFQ2\50 PQA"
link6_MRR = "\\bosch.com\dfsrb\DfsUS\LOC\JU1\Projects\MSE1\MOE2\05_MRR\MFQ2\20 Product validation"
link7_MRR = "\\bosch.com\dfsrb\DfsUS\LOC\JU1\Projects\MSE1\MOE2\05_MRR\140_Quality\06_Concessions"
link8_MRR = "\\bosch.com\dfsrb\DfsUS\LOC\JU1\Projects\MSE1\MOE2\05_MRR\MFQ2\50 PQA\10 QI"
link9_MRR = "\\bosch.com\dfsrb\DfsUS\LOC\JU1\Projects\MSE1\MOE2\05_MRR\MFQ2\10 Planning\70_Work_instruction_PQI"

def action_0():
    os.system("firefox")

def action_1():
    print("alguna accion")

def action_2():
    os.system("gedit")

def action_BTDB():
    os.system("BTDB")

def action_SAP():
    os.system("SAP")

def action_ECAM():
    os.system("ECAM")

def action_Actividades():
    os.system("Actividades")

def action_ProdEngWeb():
    os.system("paginaweb")

def action_mws():
    os.system("mws")

def action_oisnet():
    os.system("oisnet")

def OpenLink():
    os.system("explorer", link0_MRR)

def OpenLink():
    os.system("explorer", link1_MRR)
