import os
from random import randint

## write sample das name
## e.g.,
## /TEST_CRAB/jskim-CMSSW_9_3_4_GEN-SIM-93765d8a8aae3b1e637eb3e94c7ca04e/USER

txtfilename = 'filelist.txt'
samples = open(txtfilename).readlines()

for AAA in samples:

  AAA = AAA.strip('\n')

  words = AAA.split('/')

  sample = words[1]

  dirname = 'crab_'+sample
  os.system('mkdir -p '+dirname)

  cfg_skleton = open('skeletons/HLT__TO__AODSIM.py').readlines()
  output_cfg = open(dirname+'/HLT__TO__AODSIM__'+sample+'.py','w')
  for line in cfg_skleton:
    output_cfg.write(line)
  output_cfg.close()

  crabpy_skeleton = open('skeletons/crab_skeleton.py').readlines()
  crab_file_name = 'crab_'+sample+'.py'
  output_crabpy = open(dirname+'/'+crab_file_name, 'w')
  for line in crabpy_skeleton:
    if "##requestName##" in line:
      output_crabpy.write("config.General.requestName = '"+sample+"_CMSSW_9_4_0_patch1_AODSIM'\n")
    elif "##psetName##" in line:
      output_crabpy.write("config.JobType.psetName = 'HLT__TO__AODSIM__"+sample+".py'\n")
    elif "##inputDataset##" in line:
      output_crabpy.write("config.Data.inputDataset = '"+AAA+"'\n")
    else:
      output_crabpy.write(line)
  output_crabpy.close()

  print '## '+sample
  print 'cd '+dirname
  print 'crab submit -c '+crab_file_name
  print 'cd -'
