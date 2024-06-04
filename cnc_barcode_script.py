import os
from pathlib import Path
import csv

def main():
    project = input("Project Name: ")
    target_file_name = project+".R41"
    script_directory = os.path.dirname(os.path.abspath(__file__))
    
    isFound = False
    file = ""
    project_dir = ""
    
    for root, dirs, files in os.walk(script_directory):
        if target_file_name in files:
            file = os.path.join(root, target_file_name)
            project_dir = root
            print("Project Found:", file)
            isFound = True
            break
        
    if (isFound == False):
        print("Project was not found!")
        return
    
    
    if os.path.isfile(file):
        with open(file,'r') as file:
            filedata = file.read()
            filedata_arr= filedata.split('\n')
            barcode_set = set()
            for item in filedata_arr:
                if (item.startswith("DRAWING") or item.startswith("EXT18")):
                    barcode = item.split("=")[1].strip()
                    barcode_set.add(barcode)
                    
                    
        
    output_dir = project_dir+"/cnc"
    os.makedirs(output_dir, exist_ok=True)
    csv_file_name = 'output_cnc_barcodes_' + project
    csv_file = os.path.join(output_dir, csv_file_name+'.csv')
    
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([project])  
        writer.writerow(["========="])  
        for barcode in barcode_set:
            writer.writerow([barcode])    
    
    txt_file = os.path.join(output_dir, csv_file_name+'.txt')
    with open(txt_file, 'w') as file:
        file.write(project + '\n')  
        file.write("=========" + '\n') 
        for barcode in barcode_set:
            file.write(barcode + '\n')             
                                
    
    print(csv_file_name +'.csv' + " created successfully!")         
    print(csv_file_name +'.txt' + " created successfully!")         
    print(str(len(barcode_set)) + " different barcodes were found!")         
    input("Press enter to exit;")
            

    
    
    
    
    
    
    
    
    
    
if __name__ == "__main__":
    main()