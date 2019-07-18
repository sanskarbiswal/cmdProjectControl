@ECHO OFF
cd /d F:
ECHO =====================================
ECHO ======= AUTO-INIT PROJECT ===========
ECHO =====================================

python initProject.py %1
cd /d %1
python ../initGitRepo.py %1

