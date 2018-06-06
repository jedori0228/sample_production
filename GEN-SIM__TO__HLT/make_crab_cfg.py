import os
from random import randint

## write sample das name
## e.g.,
## /TEST_CRAB/jskim-CMSSW_9_3_4_GEN-SIM-93765d8a8aae3b1e637eb3e94c7ca04e/USER

txtfilename = 'filelist.txt'
samples = open(txtfilename).readlines()

for AAA in samples:

  AAA = AAA.strip('\n')

  if "#" in AAA:
    continue

  words = AAA.split('/')

  sample = words[1]

  dirname = 'crab_'+sample
  os.system('mkdir -p '+dirname)

  cfg_skleton = open('skeletons/GEN-SIM__TO__HLT.py').readlines()
  output_cfg = open(dirname+'/GEN-SIM__TO__HLT__'+sample+'.py','w')
  for line in cfg_skleton:

    ## https://hypernews.cern.ch/HyperNews/CMS/get/computing-tools/3859/1/1/1/1/1.html
    if "##MINBIAS_HERE##" in line:

      lines = open('MinBias.txt').readlines()
      total_pu_lines=143891
      #for line in lines:
      #  total_pu_lines+=1
      for i in range(0,15):
        pickrand = lines[randint(0,total_pu_lines)].strip()
        output_cfg.write("    '"+pickrand+"',\n")
    else:
        output_cfg.write(line)
  output_cfg.close()

  crabpy_skeleton = open('skeletons/crab_skeleton.py').readlines()
  crab_file_name = 'crab_'+sample+'.py'
  output_crabpy = open(dirname+'/'+crab_file_name, 'w')
  for line in crabpy_skeleton:
    if "##requestName##" in line:
      output_crabpy.write("config.General.requestName = '"+sample+"_CMSSW_9_4_0_patch1_HLT'\n")
    elif "##psetName##" in line:
      output_crabpy.write("config.JobType.psetName = 'GEN-SIM__TO__HLT__"+sample+".py'\n")
    elif "##inputDataset##" in line:
      output_crabpy.write("config.Data.inputDataset = '"+AAA+"'\n")
    else:
      output_crabpy.write(line)
  output_crabpy.close()

  print '## '+sample
  print 'cd '+dirname
  print 'crab submit -c '+crab_file_name
  print 'cd -'
