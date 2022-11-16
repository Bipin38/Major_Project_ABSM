# Python 3 code to rename multiple
# files in a directory or folder
 
# importing os module
import os
 
# Function to rename multiple files
def main():
    folder ="not_cobra"
    # folder = ["konasana", "padmasan" , "vrksasana" , "bhujangasana","not_cobra"]
    # for i in folder:
    for count, filename in enumerate(os.listdir(folder)):
            dst = f"{folder}_{str(count)}.mp4"
            src =f"{folder}/{filename}"  # foldername/filename, if .py file is outside folder
            dst =f"{folder}/{dst}"
            
            # rename() function will
            # rename all the files
            os.rename(src, dst)
 
# Driver Code
if __name__ == '__main__':
     
    # Calling main() function
    main()