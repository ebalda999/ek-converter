import pandas as pd


import tkinter as tk
from tkinter.filedialog import askopenfilename
import pandas as pd

#GUI Interface
root = tk.Tk()
root.withdraw() #Prevents the Tkinter window to come up
csv_file_path = askopenfilename()
root.destroy()
print(csv_file_path)
df = pd.read_csv(csv_file_path)
    
#Delete Unwanted Columns
df = df.drop(["DNI", "Take off", "Landing", "Landing Only", "T/O only","SDC", "PIC CREW", "Block", "SIC CREW", "DE Time"], axis=1)
#Expand Crew Names Column into PIC/SIC etc...
df = df.join(df['Crew Name'].str.split(',', expand=True).add_prefix('Crew Name'))
#Rename Columns For LogTen Pro Import
df_new= df.rename(columns={'Date':'Date','Type':'Type','Flight #':'Flight #',
                    'Aircraft ID':'Aircraft ID','From':'From','To':'To',
                    'Out':'Out','In':'In','Stick':'Total Time','PF':'Pilot Flying',
                    'PIC':'PIC','SIC':'SIC','Crew Name':"No Import",'Crew Name0':'PIC/P1 Crew',
                    'Crew Name1':'SIC/P2 Crew','Crew Name2':"Relief Crew",'Crew Name3':'Relief Crew 2',	
                    'Crew Name4':'Relief Crew 3','Crew Name5':'Relief Crew 4'})


#Generates LogTen Pro Import Ready CSV
df_new.to_csv('Emirates_Logbook_Converted.csv', encoding='utf8')

