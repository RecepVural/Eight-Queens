#libraries are imported
import numpy as np
import random

# Chess table is created
a=['|',' ','|',' ','|',' ','|',' ','|',' ','|',' ','|',' ','|',' ','|']
chart= np.array([a,a,a,a,a,a,a,a],dtype=object)
chart2= chart.copy()
list1=[]
# possible columns are listed and first random selection is performed
columns_list=[1,3,5,7,9,11,13,15]
n_column=random.choice(columns_list)
chart[0][n_column]='Q'
list1.append(n_column)
columns_list.remove(n_column)# used column is removed from column list
i=1

while i<8:
    y,p=0,0
    while True:
        y=0
        # column is randomly chosen from column list
        n_column=random.choice(columns_list)
        #Diagonals of randomly chosen column is checked if they match with other queens
        for j in list1:  
            w=i-list1.index(j)
            if n_column!=j-(2*w) and n_column!=j+(2*w):
                y=y
            else:
                y=y+1
                p=p+1
        # if unsolvable situation is occured ,queens are take back and leaved from for loop with break
            if p>4:
                mask=chart=='Q'
                chart[mask]=' '
            comp1=chart==chart2
            if comp1.all():
                i=1
                break
        # leaved from while loop with break
        if comp1.all():
                break
        # if conditions are proper. Q is placed. Placed colums is removed
        if y==0 :
            chart[i][n_column]='Q' 
            list1.append(n_column)
            columns_list.remove(n_column)
            i=i+1 
            break
    # selection is start again here, with continue function go back to start of while loop.    
    if comp1.all():
       mask=chart=='Q'
       chart[mask]=' '
       list1=[]
       columns_list=[1,3,5,7,9,11,13,15]
       n_column=random.choice(columns_list)
       chart[0][n_column]='Q'      
       list1.append(n_column)
       columns_list.remove(n_column)
       i=1
       continue   

#cheess table is printed.
for i in range(8):
    print(''.join(chart[i]))
    
    
    
    
    

