from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

def send_to_google_drive():
    #set oauth
    gauth = GoogleAuth()
    drive = GoogleDrive(gauth)

    #create file within google drive
    document = drive.CreateFile({'title': 'Reliable Sources.doc'})

    #set content to update
    document.SetContentString('sources here will be printed to the document')

    #udpate file
    document.Upload()



### still to do:
### - create a doc once, then update the existing one
### - update to the doc should be the source, not a random string
