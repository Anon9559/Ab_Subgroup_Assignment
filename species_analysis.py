#%%
def check_species_assignment(in_file,out_file):
    """
    Summary:
    Works out MCC for a species.
    
    Args:    
    in_file = combined full results file 
        Produced by a species' sequences against a hsubgroup datafile 
        containing all subgroup profiles for all species. Each full results file
        produced for each species is the joined together. The final column 
        of this file contains the actual organism. This is compared to 
        hsubgroup's assignment to derive an MCC
    out_file = named output file (.csv)
    
    Desc:
    /
    
    """
    import csv
    import sys
    sys.stdout = open(out_file,'a+')
    with open(in_file) as csv_in:
        reader = csv.reader(csv_in)
        
        organisms = ['Homo sapiens','Mus musculus','Oryctolagus cuniculus',
                        'Macaca mulatta','Oncorhynchus mykiss']
        
        
        
        for organism in organisms:
            csv_in.seek(0)
            TP = 0 
            FP = 0 
            FN = 0 
            TN = 0 
            
            for row in reader:
               actual_org = str(row[8]) 
               predicted_org = str(row[1])
                
               if organism in predicted_org and \
               organism in actual_org:
                   TP+=1

               elif organism not in predicted_org and \
               organism in actual_org:
                   FN+=1

               elif organism in predicted_org and \
               organism not in actual_org:
                   FP+=1

               elif organism not in predicted_org and \
               organism not in actual_org:
                   TN+=1

               else:
                   continue
               
               try:
                   org_MCC = float((TP * TN) - (FP * FN))/ \
                   float(((TP+FP)*(TP+FN)*(TN+FP)*(TN+FN)) ** 0.5)
               except:
                   continue
                   
            print(organism,'MCC:', org_MCC)
            print('TP:',TP,'FP:',FP,'FN:', FN ,'TN:', TN )
            print(TP+FP+FN+TN,'\n')




def determine_species_misassignment_master(in_file):
    """Works out which species were assigned as which"""

    query_organisms =['Homo sapiens', 'Mus musculus','Macaca mulatta',
                        'Oryctolagus cuniculus','Oncorhynchus mykiss']
    for organism in query_organisms:
        determine_species_misassignment_FNs(in_file,organism)
        
    for organism in query_organisms:
        determine_species_misassignment_FPs(in_file,organism)

def determine_species_misassignment_FNs(in_file, organism):
    """Determines which species get misclassified as the other, FNs only
    
    Outputs to console. No need for dedicated output file
    
    """
    import csv
    with open(in_file) as csv_in:
        reader = csv.reader(csv_in)
        macaca = 0 
        mouse = 0 
        oryctolagus = 0 
        homo = 0
        mykiss = 0  
        for row in reader:
            assigned_org = str(row[1])
            actual_org = str(row[8]) 
                        
            if organism not in assigned_org and organism in actual_org:
                if 'Macaca mulatta' in assigned_org:
                    macaca +=1
                elif 'Mus musculus' in assigned_org:
                    mouse+=1
                elif 'Oryctolagus cuniculus' in assigned_org:
                    oryctolagus+=1
                elif 'Homo sapiens' in assigned_org:
                    homo+=1
                elif 'Oncorhynchus mykiss' in assigned_org:
                    mykiss+=1
                    
    print('FALSE NEGATIVES')
                    
    print('Query organism:', organism)
    print('Macaca:',macaca,'Mouse:', mouse,'Oryctolagus:', oryctolagus, 
            'Homo:',homo,'Mykiss: ',mykiss)
    print('Sum:',macaca+mouse+oryctolagus+homo+mykiss)
    print('\n')
    
def determine_species_misassignment_FPs(in_file,organism):
    """Determines which species get misclassified as the other, FPs only
    
    Outputs to console. No need for dedicated output file
    
    """
    import csv
    with open(in_file) as csv_in:
        reader = csv.reader(csv_in)
        macaca = 0 
        mouse = 0 
        oryctolagus = 0 
        homo = 0
        mykiss = 0  
        for row in reader:
            assigned_org = str(row[1])
            actual_org = str(row[8]) 
                        
            if organism in assigned_org and organism not in actual_org:
                if 'Macaca' in actual_org:
                    macaca +=1
                elif 'Mus' in actual_org:
                    mouse+=1
                elif 'Oryctolagus' in actual_org:
                    oryctolagus+=1
                elif 'Homo' in actual_org:
                    homo+=1
                elif 'Oncorhynchus' in actual_org:
                    mykiss+=1
                    
    
    print('FALSE POSITIVES')
    print('Query organism:', organism)
    print('Macaca:',macaca,'Mouse:', mouse,'Oryctolagus:', oryctolagus, 
            'Homo:',homo,'Mykiss: ',mykiss)
    print('Sum:',macaca+mouse+oryctolagus+homo+mykiss)
    print('\n')