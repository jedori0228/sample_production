import os

channel = "MajoranaNeutrinoToMuMuMu"
masses = [5, 10, 20, 30, 40, 50, 60, 70, 90, 100, 150, 200, 300, 400, 500, 700, 1000]
#masses = [40]
#masses = [60]
#masses = [5, 10, 20, 30, 50, 70, 90, 100, 150, 200, 300, 400, 500, 700, 1000]

for mass in masses:
  os.system('mkdir crab_'+channel+'_'+str(mass))

  cfg_skleton = open('skeletons/GEN-SIM_crab_skeleton.py').readlines()
  output_cfg = open('crab_'+channel+'_'+str(mass)+'/GEN-SIM_crab_'+channel+'_'+str(mass)+'.py', 'w')
  for line in cfg_skleton:
    if "LHE_INPUTS_ARE_HERE" in line:
      for lheindex in range(0, 1):
        output_cfg.write("      'root://cluster142.knu.ac.kr//store/user/jskim/lhe/"+channel+"_M-"+str(mass)+"/cmsgrid_final_00"+str(lheindex)+".lhe',\n")
    else:
      output_cfg.write(line)
  output_cfg.close()

  crabpy_skeleton = open('skeletons/crab_skeleton.py').readlines()
  output_crabpy = open('crab_'+channel+'_'+str(mass)+'/crab_'+channel+'_'+str(mass)+'.py', 'w')
  for line in crabpy_skeleton:
    if "##requestName##" in line:
      output_crabpy.write("config.General.requestName = '"+channel+"_M-"+str(mass)+"_CMSSW_7_1_18_GEN-SIM'\n")
    elif "##psetName##" in line:
      output_crabpy.write("config.JobType.psetName = 'GEN-SIM_crab_"+channel+"_"+str(mass)+".py'\n")
    elif "##outputPrimaryDataset##" in line:
      output_crabpy.write("config.Data.outputPrimaryDataset = '"+channel+"_M-"+str(mass)+"'\n")
    else:
      output_crabpy.write(line)
  output_crabpy.close()
