@echo off
cd C:\Users\user\git\github
git clone https://github.com/ojirou/xxxxx.git
cd C:\Users\user\git\github\xxxxx
echo "#xxxxx" >> README.md
echo github�ɃA�b�v���[�h����t�@�C�����i�[������N���b�N���Ă�������
pause > nul
git add *
git commit -m "first commit"
git push origin main