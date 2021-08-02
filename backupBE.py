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
        mcpath = (os.environ["APPDATA"].replace("Roaming","")+"Local/"+"packages/")

        mcpath = mcpath.replace("\\","/")
        
        for name in glob.glob(f'{mcpath}*'):
            name = (name.replace("\\","/"))
            name = (name.replace(mcpath,""))
            name_path = "MinecraftUWP" in name
            if(name_path==True):
                break

        mcpath = (mcpath+name+"/LocalState/games/com.mojang/")

        return mcpath

    def getmcworldpath():

        path = mcfunction.getmcpath()
                
        mcworldpath=path+"minecraftWorlds/"
        
        return mcworldpath


def main():

    confirm = input("バックアップを開始しますか？\n1.開始する\n2.キャンセルする\n>")

    if confirm=="1":

        mc = mcfunction

        mcpath = (mc.getmcpath())

        worldpath = mc.getmcworldpath()

        files = os.listdir(worldpath)

        for worldfile in files:
            try:        
                print(f"\r{worldpath+worldfile}\nバックアップ中...")
                shutil.copytree(worldpath,f'{backuppath}/BE/backup_{dt_now.strftime("%Y_%m_%d_%H_%M_%S")}')
                print(f"\rバックアップ中...")

            except Exception as e:
                pass


        print(f'\nワールドデータは{backuppath}/BE/backup_{dt_now.strftime("%Y_%m_%d_%H_%M_%S")}に保存されました。')
    elif confirm==2:
        print("キャンセルしました。")


if __name__ == "__main__":

    if(os.path.exists(mcfunction.getmcpath())==True):
        print("Minecraft:インストール済み")
    else:
        print("Minecraftがインストールされていません。")
        confirm = input("Enterキーで終了")
        sys.exit()
    try:
        main()
        confirm = input("Enterキーで終了")
    except Exception as e:
        print("予期せぬエラーが発生しました。")
        print(e)
        confirm = input("Enterキーで終了")
        sys.exit()
    except KeyboardInterrupt:
        print("バックアップをキャンセルしました。")