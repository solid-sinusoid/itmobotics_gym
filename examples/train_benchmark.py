import subprocess

program_list = ['ur5e_peginholeDDPG.py', 'ur5e_peginholePPO.py', 'ur5e_peginholeSAC.py', 'ur5e_peginholeTD3.py']

for program in program_list:
    subprocess.call(['python', program])
    print("Finished:" + program)