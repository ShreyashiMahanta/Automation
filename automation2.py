#Personal assistant
import time
import datetime
import dropbox
import pandas as pd
import plotly.express as px

current_time = datetime.datetime.now() 
class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

answer = input("Hi! I am your personal assistant. What can I do for you today?  ")


if (answer == "Can you tell me the time"):
    print(current_time)

elif (answer == "Can you show me the number of coronavirus cases?"):
    cd = pd.read_csv("data - data.csv")
    fig  =   px.line(cd, x="Date" ,  y="Cases"  ,color="Country" ,  title="No. of cases")
    fig.show()

elif (answer == "Can you upload files to dropbox?"):
   def main():
       access_token = 'sl.AfgfRI77b7QrwiIM7koT_hvX-inAnKX23ktldFLRZvSlaH4VOpf3NMmaCAvclYS9jt17W1UZB9u8h-o5j96IY-CbiTgEVCa6gwQFOFVR7USsJPMc10sekuT6WvecZF1xvcmG71U'
       transferData = TransferData(access_token)
       file_from = input("Certainly! Please enter the file path to transfer :-  ")
       file_to = input("Enter the full path to upload to dropbox:-  ")
       transferData.upload_file(file_from, file_to)
       print("file has been moved !!!")

       if __name__ == '__main__':
           main()   
else:
    print("Sorry, but I am not programmed to answer this question yet.")


