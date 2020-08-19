
import os
import shutil

# def move_files(source, destination):
#     shutil.move(source, destination)
# folders = os.listdir("G:\\adminstrator\GNS3")
# print(folders)

def check(extensions, newFileName , folder_name, file_name):
    ## Organize image into images folder
    os.chdir("G:")
    if newFileName.endswith(extensions):
        if not os.path.exists(folder_name):
            os.chdir("G:")
            os.mkdir(folder_name)
        #shutil.copy(file_name, folder_name)
        try:
            shutil.move(file_name, folder_name)
        except:
            print(Exception)
        #os.remove(file_name)
    print("Done")

# pdf_path = "G:\\files\\Pdf"


# for folder in folders:
#     folders_in_folder = os.listdir("G:\\adminstrator\\%".format(folder))
#     print(folders_in_folder)

current_folder_count = 0
subfolder_count = 0
files_count = 0

folder_names_backup = {}

for folderName, subfolders, filenames in os.walk('G:'):
    # print('The current folder is ' + folderName)
    current_folder_count += 1
    folder_names_backup[folderName] = subfolders + filenames

    # if folderName == "01-Learning":
    #     continue
    for subfolder in subfolders:
        # print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
        subfolder_count += 1

    for filename in filenames:
        # print('FILE INSIDE ' + folderName + ': '+ filename)
        files_count += 1
        new_file_name = filename.lower()
        # source = folderName+filename

        # if any([i in new_file_name for i in (".mp3", ".3ga")]):
        #     shutil.move(source, mp3_path)
        actual_path = folderName +"\\"+ filename
        # print("Actual Path: ", actual_path)
        ## Organize image into images folder
        check((".png", ".jpg", ".jpeg", ".gif"), new_file_name, "Images", actual_path)
        ## Organize codes files into Codes folder
        check((".css", ".html", ".bash", ".js", ".sh", ".xml"), new_file_name, "Codes", actual_path)
        ## Organize archives files into Archives folder
        check((".zip", ".rar", ".tar", ".iso", ".deb", ".gz", ".7z", ".bin", ".clie"), new_file_name, "Archives",actual_path)
        ## Organize codes files into Codes folder
        check((".pdf", ".docx", ".word", ".xlsx", ".txt", ".docs", ".log", ".odt", ".wbk", ".csv"), new_file_name, "Documents", actual_path)
        ## Organize Audio files into Audios folder
        check((".ogg", ".m4b", ".m4p", ".m4a", ".raw", ".wav", ".mp3", ".aac"), new_file_name, "Audios", actual_path)
        ## Organize Video files into Videos folder
        check((".mp4", ".mwv", ".mkv", ".webm", ".flv", ".mov", ".wmv", ".m4v", ".3gp"), new_file_name, "Videos", actual_path)
        ## Organize ExecutableFile files into Programs folder
        check((".exe"), new_file_name, "Programs", actual_path)



os.chdir("G:")
with open("fl_fldr_names_backup.txt", "a", encoding="utf-8") as file_folder_name:
    intro = "You have {} folders and {} subFolders and also {} files in the following file."
    intro = intro.format(current_folder_count, subfolder_count, files_count)
    file_folder_name.write("\n\n"+intro+"\n\n")

    for folderName, fileName in folder_names_backup.items():
        file_folder_name.write(str(folderName)+ ": "+ str(fileName)+"\n")

print("Number of folders and sub folders = ", current_folder_count + subfolder_count, "\n\n" )
print("Number of files = ", files_count, "\n\n" )
