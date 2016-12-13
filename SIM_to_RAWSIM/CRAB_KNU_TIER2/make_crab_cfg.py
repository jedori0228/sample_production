import os
from random import randint

channel = "MajoranaNeutrinoToMuMuMu"
masses = [5, 10, 20, 30, 40, 50, 60, 70, 90, 100, 150, 200, 300, 400, 500, 700, 1000]

import csv
from urllib import urlopen

for mass in masses:
  os.system('mkdir crab_'+channel+'_'+str(mass))

  cfg_skleton = open('skeletons/SIM_to_RAWSIM_skeleton.py').readlines()
  output_cfg = open('crab_'+channel+'_'+str(mass)+'/SIM_to_RAWSIM_crab_'+channel+'_'+str(mass)+'.py', 'w')
  for line in cfg_skleton:
    if "##MINBIAS_HERE##" in line:

      lines = open('/pnfs/knu.ac.kr/data/cms/store/user/jskim/filelist_MinBias.txt').readlines()
      total_pu_lines=-1
      for line in lines:
        total_pu_lines+=1
      for i in range(0,15):
        pickrand = lines[randint(0,total_pu_lines)].strip()
        output_cfg.write("    '"+pickrand+"',\n")
    else:
      output_cfg.write(line)
  output_cfg.close()

  crabpy_skeleton = open('skeletons/crab_skeleton.py').readlines()
  output_crabpy = open('crab_'+channel+'_'+str(mass)+'/crab_'+channel+'_'+str(mass)+'.py', 'w')
  for line in crabpy_skeleton:
    if "##requestName##" in line:
      output_crabpy.write("config.General.requestName = '"+channel+"_M-"+str(mass)+"_CMSSW_8_0_21_RAWSIM'\n")
    elif "##psetName##" in line:
      output_crabpy.write("config.JobType.psetName = 'SIM_to_RAWSIM_crab_"+channel+"_"+str(mass)+".py'\n")
    elif "##inputDataset##" in line:

      ## Fill DBS like below!
      ## shared link : https://docs.google.com/spreadsheets/d/1aUoEq40MjpZ4LpcEoxXdd9-prrDmJkWWgeKPLPsmBhk/edit#gid=0
      ## publish your spreadsheet to csv foramt, and put the link below (url = '<LINK>')

      url = 'https://docs.google.com/spreadsheets/d/1aUoEq40MjpZ4LpcEoxXdd9-prrDmJkWWgeKPLPsmBhk/pub?gid=0&single=true&output=csv'
      cr = csv.reader(urlopen(url).readlines())
      for row in cr:
        if row[0] == channel+"_M-"+str(mass):
          output_crabpy.write("config.Data.inputDataset = '"+row[1]+"'\n")
    else:
      output_crabpy.write(line)
  output_crabpy.close()
