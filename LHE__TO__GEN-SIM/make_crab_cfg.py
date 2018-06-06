import os

## write sample alias and lhe path, starting with /store/
## e.g.,
## PairProduction_MuMu_ZR3000_N200_WR5000_NLO /store/user/jskim/SE_UserHome/lhe/LRSM/PairProduction_MuMu_ZR3000_N200_WR5000_NLO/events.lhe

txtfilename = 'filelist.txt'
samples = open(txtfilename).readlines()

for AAA in samples:

  if "#" in AAA:
    continue

  words = AAA.split()

  sample = words[0]
  lhefilepath = words[1]

  dirname = 'crab_'+sample
  os.system('mkdir -p '+dirname)

  cfg_skleton = open('skeletons/LHE__TO__GEN-SIM.py').readlines()
  output_cfg = open(dirname+'/LHE__TO__GEN-SIM__'+sample+'.py','w')
  for line in cfg_skleton:
    if "##INPUT_HERE##" in line:
      for lheindex in range(0, 1):
        output_cfg.write("      'root://cluster142.knu.ac.kr/"+lhefilepath+"',\n")
    else:
      output_cfg.write(line)
  output_cfg.close()

  crabpy_skeleton = open('skeletons/crab_skeleton.py').readlines()
  crab_file_name = 'crab_'+sample+'.py'
  output_crabpy = open(dirname+'/'+crab_file_name, 'w')
  for line in crabpy_skeleton:
    if "##requestName##" in line:
      output_crabpy.write("config.General.requestName = '"+sample+"_CMSSW_9_3_4_GEN-SIM'\n")
    elif "##psetName##" in line:
      output_crabpy.write("config.JobType.psetName = 'LHE__TO__GEN-SIM__"+sample+".py'\n")
    elif "##outputPrimaryDataset##" in line:
      output_crabpy.write("config.Data.outputPrimaryDataset = '"+sample+"'\n")
    else:
      output_crabpy.write(line)
  output_crabpy.close()

  print '## '+sample
  print 'cd '+dirname
  print 'crab submit -c '+crab_file_name
  print 'cd -'
