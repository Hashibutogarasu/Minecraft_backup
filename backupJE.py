import sys
import os
import glob
import shutil
import datetime


dt_now = datetime.datetime.now()

try:
    backuppath=os.path.expanduser('~/mcbackup').replace("\\","/")
    os.mkdir(backuppath)
except:
    pass

class mcfunction():
    def getmcpath():
        mcpath = (os.environ["APPDATA"]+"/.minecraft/saves/")

        mcpath = mcpath.replace("\\","/")        

        return mcpath


def main():

    
    mc = mcfunction
    
    mcpath = (mc.getmcpath())

    mode=input(f"どこのファイルをバックアップしますか？\n1.{mcpath}\n2.任意のパス\n3.キャンセル\n>")

    if mode=="1":
        
        print(f"バックアップ中...{mcpath}")

        files = os.listdir(mcpath)

        for worldfile in files:
            try:
                shutil.copytree(mcpath, f'{backuppath}/JE/backup_{dt_now.strftime("%Y_%m_%d_%H_%M_%S")}')
            except Exception as e:
                pass
        print(f'\nワールドデータは{backuppath}/JE/backup_{dt_now.strftime("%Y_%m_%d_%H_%M_%S")}に保存されました。')
    
    elif mode=="2":

        mcpath=input("savesまでのパスを入力してください。\n>")
        confirm = input(f"パスは{mcpath}でよろしいですか？\n1.続行\n2.キャンセル\n>")
            
        if(mcpath.endswith("/saves/") == True):
            
            if confirm=="1":
                files = os.listdir(mcpath)

                print(f"バックアップ中...{mcpath}")

                for worldfile in files:
                    try:        
                        shutil.copytree(mcpath, f'{backuppath}/JE/backup_{dt_now.strftime("%Y_%m_%d_%H_%M_%S")}')
                    except Exception as e:
                        pass
                print(f'\nワールドデータは{backuppath}/JE/backup_{dt_now.strftime("%Y_%m_%d_%H_%M_%S")}に保存されました。')
            else:
                print("キャンセルしました。")
        else:
            print("正しい形式で入力してください。")
    elif mode=="3":
        print("キャンセルしました。")
    
    
if __name__ == "__main__":
    try:
        main()
        confirm = input("Enterキーで終了")
    except Exception as e:
        print("予期せぬエラーが発生しました。")
        print(e)
        confirm = input("Enterキーで終了")
        sys.exit()
    except KeyboardInterrupt:
        print("\nバックアップをキャンセルしました。")