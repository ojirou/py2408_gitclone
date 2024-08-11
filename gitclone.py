import subprocess
import os
def main():
    repository= input('githubで作成したレポジトリ名 （例 py2305_〇〇）>> ')  
    path=r'C:\\Users\\user\\anaconda3\\Scripts\\gitclone_xxxxx.bat'
    with open(path) as f:
        s=f.read()
        print(type(s))
        print(s)    
    s=s.replace('xxxxx', repository)
    path_w='C:\\Users\\user\\anaconda3\\Scripts\\'+repository+'.bat'
    with open(path_w, mode='w') as f:
        f.write(s)
    with open(path_w) as f:
        print(f.read())
#   subprocess.Popen(["notepad", path_w])
    subprocess.run(path_w, shell=True)
#    os.remove(path_w)
# def run_windows_shell_script(script_path):
#     try:
#         # シェルスクリプトを実行
#         subprocess.run(script_path, shell=True)
#     except Exception as e:
#         print("シェルスクリプトの実行中にエラーが発生しました:", str(e))
if __name__ == "__main__":
    main()