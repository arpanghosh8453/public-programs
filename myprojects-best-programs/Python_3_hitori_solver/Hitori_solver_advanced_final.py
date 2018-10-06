
#--------------------------------------------------------------------Written in Python 3---------------------------------------------------------------------------------


#----------------------------------------------------------------------Essential imports---------------------------------------------------------------------------------
import numpy as np#importing numpy
import datetime#importing datetime for time calculation

#----------------------------------------------------------------------Introductions---------------------------------------------------------------------------------------
print( u'''
                            ©  Copyright : Arpan Ghosh  ©
               * This hitori solver is programmed by Arpan Ghosh  *
                    
----------------------------- < INSTRUCTIONS >----------------------------------

How to create a hitori file :
* create a blank text file and write the values of the hitori as space
   seperated values for each row in a seperate line.No comma after row ending
   number
   
* No blank line initially or midway, start from top left corner
  No spaces in between numbers and comma(s)

* New line only when a row completes.No space in terminal
   position.No space is required anywhere in file

''')

next_ = input("Enter to proceed : ")

print(u'''
Example :

    1,7,1,6,1,8,1,2                                 1  7  1  6  1  8  1  2
    2,2,1,3,5,4,7,8                                 2  2  1  3  5  4  7  8
    4,3,7,8,1,3,2,6         (conversion)            4  3  7  8  1  3  2  6
    3,8,6,2,4,2,1,2      <<---------------          3  8  6  2  4  2  1  2
    6,3,2,4,7,3,8,5                                 6  3  2  4  7  3  8  5
    4,4,7,7,8,6,2,1                                 4  4  7  7  8  6  2  1
    5,1,8,7,2,3,6,1                                 5  1  8  7  2  3  6  1
    2,2,7,1,1,5,4,3                                 2  2  7  1  1  5  4  3
    (file content)                                    (real hitori problem)

Output :
* The circled values will appear as 'O' in place of values( in Prompt )
  the circled values will appear as 'o' in place of values( in solution file )
  
* The darkened values will appear as 'X' in place of darkened values
  the darkened values will appear as '.' in place of values( in solution file )

* If it cannot determine whether it will be circled or darkened, it places
  '?' as blank marking ( rare case )
--------------------------------------------------------------------------------
''')
next_ = input("Enter to Start : ")

#--------------------------------------------------------------------Definitions----------------------------------------------------------------------------------------------

# marks all the values as circle which are unique in both of its row and column(useful but not required)
def mark_unique(cell_id):
    #Checking for row and column uniqueness
    if (value_array[cell_id[0],...].tolist().count(value_array[cell_id]) == 1) and (value_array[...,cell_id[1]].tolist().count(value_array[cell_id]) == 1):

        mark_array[cell_id] = 'circle'#unique in row and column can not be darken, so they will be circled

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#returns True if the cell lies in the border side of the game box
def is_border_cell(cell_id):
    
    if (cell_id[0] == 0 or cell_id[1] == 0) or (cell_id[0] == row_count-1 or cell_id[1] == column_count-1):
        return True
    else:
        return False

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Checks for whether the given id indicates a valid cell_id
def id_exists(cell_id):
    
    if (cell_id[0]>=0 and cell_id[0]<row_count) and (cell_id[1]>=0 and cell_id[1]<column_count):#true for valid id(s)
        return True
    else:
        return False

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#returns the diagonal neighborer's(of the cell_id) cell id(s) as a list
#if the only_dark flag is True, returns only the list of available dark neighbor's id(s)
def get_diagonal_neighbour(cell_id,mark_array_copy,only_dark = False):
    
    #all diagonal values(may contain invalid id(s))
    all_diagonal_id = [(cell_id[0]+1,cell_id[1]-1),(cell_id[0]+1,cell_id[1]+1),(cell_id[0]-1,cell_id[1]-1),(cell_id[0]-1,cell_id[1]+1)]
    result = []
    for _id in all_diagonal_id:
        if id_exists(_id):#sorting the valid id values
            if only_dark:#checking for dark flag
                if mark_array_copy[_id] == 'dark':#only darks will pass
                    result.append(_id)
            else:#all diagonals(without dark checking)
                result.append(_id)  
    return result
        
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#marks a cell as circle in mark_array and fulfill the other consequents
def mark_circle(cell_id):
    
    if mark_array[cell_id] != 'blank' :
        return None
    
    mark_array[cell_id] = 'circle'#marks a cell as 'circle' in mark_array
    circled_value = value_array[cell_id]
    
    #effect of that value circling
    
    for num in range(column_count):
        id_1 = (cell_id[0],num)
        if mark_array[id_1] == 'blank':
            if value_array[id_1] == circled_value:#value matched in same row of circled value
                mark_dark(id_1)#horizontal same values of circled value are darken(by rule)
    
    for num_1 in range(row_count):
        id_2 = (num_1,cell_id[1])
        if mark_array[id_2] == 'blank':
            if value_array[id_2] == circled_value:#value matched in same column of circled value
                mark_dark(id_2)#vertical same values of circled value are darken(by rule)
    
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#marks a cell as dark in mark_array and fulfill the other consequents
def mark_dark(cell_id):
    
    if mark_array[cell_id] != 'blank' :
        return None
    
    mark_array[cell_id] = 'dark'#marks a cell as 'dark' in mark_array
    
    #effect of that value darkening
    
    row_column_neighbour = [(cell_id[0],cell_id[1]-1),
                           (cell_id[0],cell_id[1]+1),
                           (cell_id[0]-1,cell_id[1]),
                           (cell_id[0]+1,cell_id[1])]#all row and column neighbors(may contain invalid id(s))
    
    for _id in row_column_neighbour:
        if id_exists(_id):#pass for valid id only
            mark_circle(_id)#surrounding row column neighbors are circled as they cannot be darken(by rule)
        
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#marks a cell as circle in virtual_mark_array and fulfill the other consequents to check it's effect(whether it causes error or not)
def mark_virtual_circle(cell_id):
    
    if virtual_mark_array[cell_id] != 'blank' :
        return None
    
    virtual_mark_array[cell_id] = 'circle'#marks a cell as 'circle' in virtual_mark_array
    circled_value = value_array[cell_id]
    
    #effect of that value circling
    
    for num in range(column_count):
        id_1 = (cell_id[0],num)
        if virtual_mark_array[id_1] == 'blank':
            if value_array[id_1] == circled_value:#value matched in same row of circled value
                mark_virtual_dark(id_1)#horizontal same values of circled value are darken in virtual_mark_array(by rule)
    
    for num_1 in range(row_count):
        id_2 = (num_1,cell_id[1])
        if virtual_mark_array[id_2] == 'blank':
            if value_array[id_2] == circled_value:#value matched in same column of circled value
                mark_virtual_dark(id_2)#vertical same values of circled value are darken in virtual_mark_array(by rule)
    
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#marks a cell as dark in virtual_mark_array and fulfill the other consequents to check it's effect(whether it causes error or not)
def mark_virtual_dark(cell_id):
    
    if virtual_mark_array[cell_id] != 'blank' :
        return None
    
    virtual_mark_array[cell_id] = 'dark'#marks a cell as 'dark' in virtual_mark_array
    
    #effect of that value darkening
    
    row_column_neighbour = [(cell_id[0],cell_id[1]-1),
                           (cell_id[0],cell_id[1]+1),
                           (cell_id[0]-1,cell_id[1]),
                           (cell_id[0]+1,cell_id[1])]#all row and column neighbors(may contain invalid id(s))
    
    for _id in row_column_neighbour:
        if id_exists(_id):#pass for valid id only
            mark_virtual_circle(_id)#surrounding row column neighbors are circled in virtual_mark_array as they cannot be darken(by rule)
        
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Checks for every error that may occur in the virtual_mark_array for wrong circling or darkening
def virtual_error_occured():
    
    for _id in all_id_list:
        if loop_form_if_darken(_id,virtual_mark_array) and virtual_mark_array[_id] == 'dark':# already a complete dark loop formed(circled values are not continuous)
            return True #Error occurred
        
        if virtual_mark_array[_id] == 'dark':#pass for a dark cell
            row_column_neighbour = [(_id[0],_id[1]-1),
                           (_id[0],_id[1]+1),
                           (_id[0]-1,_id[1]),
                           (_id[0]+1,_id[1])]#all row and column neighbors(may contain invalid id(s))
            for id_ in row_column_neighbour:
                if id_exists(id_):
                    if virtual_mark_array[id_] == 'dark':#surrounding cell of that dark cell is also dark
                        return True #Error occurred
    
    for index in range(column_count):
        column_value_array = value_array[...,index]#index column 
        column_mark_array = virtual_mark_array[...,index]#markings of that column
        column_circled_values = column_value_array[column_mark_array == 'circle']#circled value list of that column
        if len(column_circled_values.tolist()) != len(set(column_circled_values.tolist())):#repetition(circled values are not unique) in same circled value in same column
            return True#Error occurred
    for index in range(row_count):
        row_value_array = value_array[index,...]#index row
        row_mark_array = virtual_mark_array[index,...]#markings of that row
        row_circled_values = row_value_array[row_mark_array == 'circle']#circled value list of that row
        if len(row_circled_values.tolist()) != len(set(row_circled_values.tolist())):#repetition(circled values are not unique) in same circled value in same row
            return True#Error occurred
    
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Checks whether a cell cannot be circled , and makes it dark 
def check_for_dark(cell_id):
    
    if mark_array[cell_id] != 'blank' :
        return None
    
    cell_value = value_array[cell_id]#value of cell_id
    
    #LOGIC : There are same values adjacent in same row(horizontal) which is equal to cell_value .if the cell is circled,there will be 
        #   two adjacent dark cells in same row; which is invalid,so it must be darken
    for i in range(column_count-1):
        id_1 = (cell_id[0],i)#for each id in every row
        id_right = (cell_id[0],i+1)#for id right of that id in every row
        if id_1 == cell_id or id_right == cell_id :#if id_1 or id_right matches with cell under calculation...
            pass#,nothing happens
        else:
            if (mark_array[id_1] == 'blank') and (mark_array[id_right] == 'blank'):#checks if two adjacent s are blank in same row
                if (value_array[id_1] == cell_value) and (value_array[id_right] == cell_value):# and they carries the same value that of cell_value
                    mark_dark(cell_id)#marks the cell as dark
                
    #LOGIC : There are same values adjacent in same column(vertical) which is equal to cell_value .if the cell is circled,there will be 
        #   two adjacent dark cells in same column; which is invalid,so it must be darken
    for j in range(row_count-1):
        id_2 = (j,cell_id[1])#for each id in every column
        id_down = (j+1,cell_id[1])#for id right of that id in every column
        if id_2 == cell_id or id_down == cell_id :#if id_2 or id_down matches with cell under calculation...
            pass#nothing happens
        else:
            if (mark_array[id_2] == 'blank') and (mark_array[id_down] == 'blank'):#checks if two adjacent s are blank in same column
                if (value_array[id_2] == cell_value) and (value_array[id_down] == cell_value):# and they carries the same value that of cell_value
                    mark_dark(cell_id)#marks the cell as dark
                
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Checks whether a cell cannot be circled in the virtual_mark_array , and makes it dark in real mark_array
def check_for_dark_advanced(cell_id):
    
    if mark_array[cell_id] != 'blank' :
        return None
    
    for _id in all_id_list:
        virtual_mark_array[_id] = mark_array[_id]#Re-initiating the virtual_mark_array as a copy of real mark_array
        
    mark_virtual_circle(cell_id)#virtual circling for checking 
    
    if virtual_error_occured():#circling that value causes error
        mark_dark(cell_id)#it must be a dark cell as circling that value causes error
        
    for _id in all_id_list:
        #Second step checking
        if loop_form_if_darken(_id,virtual_mark_array) and virtual_mark_array[_id] == 'blank':#such condition formed that darkening one cell causes a loop
            mark_virtual_circle(_id)#so, it must be circled
            
        if virtual_error_occured():#but circling that must circled value causes error
            mark_dark(cell_id)#the cell under checking(which was circled randomly) must be darken as it gives a error rising condition
        

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Checks whether a cell cannot be darken in the virtual_mark_array , and makes it circle in real mark_array
def check_for_circle_advanced(cell_id):
    
    if mark_array[cell_id] != 'blank' :
        return None
    
    for _id in all_id_list:
        virtual_mark_array[_id] = mark_array[_id]#Re-initiating the virtual_mark_array as a copy of real mark_array
        
    mark_virtual_dark(cell_id)#virtual darkening for checking 
    
    if virtual_error_occured():#darkening that value causes error
        mark_circle(cell_id)#it must be a circle cell as darkening that value causes error
        
    for _id in all_id_list:
        #Second step checking
        if loop_form_if_darken(_id,virtual_mark_array) and virtual_mark_array[_id] == 'blank':#such condition formed that darkening one cell causes a loop
            mark_virtual_circle(_id)#so, it must be circled
            
        if virtual_error_occured():#but circling that must circled value causes error
            mark_circle(cell_id)#the cell under checking(which was darkened randomly) must be circled as it gives a error rising condition
        
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#checks whether circled values are discontinuous by darkened cells in mark_array_copy if the cell_id is darkened
def loop_form_if_darken(cell_id,mark_array_copy):
    
    connected_blacks = [cell_id]
    checked_cells = []
    border_flag = is_border_cell(cell_id)
    
    while len(connected_blacks) > 0:
        new_black_connections = []#newer connections with connected_blacks
        for black_id in connected_blacks:
            neighbours = get_diagonal_neighbour(black_id,mark_array_copy,True)#fetch the black diagonal neighbors(as they cannot be adjacent in row/column)
            for _id in neighbours:
                if _id not in checked_cells:#already taken in connection
                    new_black_connections.append(_id)#newer connections with connected_blacks are added
                    
        for id_ in new_black_connections:
            if is_border_cell(id_):#one border cell found in connection
                if border_flag:#if already contains one border cell
                    return True#connection of dark cells contains two different border cells
                else:
                    border_flag = True#one border cell is present in connection
            if new_black_connections.count(id_) >= 2:#meets to a common point,so loop formed
                return True
            
        checked_cells += connected_blacks#checked cells are added to checked_cells
        connected_blacks = new_black_connections#only new black cells will proceed the process of connecting, so replaced
        
    return False#Don't for any dark loop if darkened , don't make circle marked cells discontinuous
        
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------		
#Checks whether a cell cannot be darked , and makes it circle
def check_for_circle(cell_id):
    
    if mark_array[cell_id] != 'blank' :
        return None
    #all neighboring cell(s) ( valid or invalid) in horizontal and vertical directions
    left_cell = (cell_id[0],cell_id[1]-1)
    right_cell = (cell_id[0],cell_id[1]+1)
    up_cell = (cell_id[0]-1,cell_id[1])
    down_cell = (cell_id[0]+1,cell_id[1])
    
    #the cell is surrounded by same valued cells horizontally. If it is darken, two same value in a row will become circled; that's invalid
    if id_exists(left_cell) and id_exists(right_cell):#both right and left values exists
        if value_array[left_cell] == value_array[right_cell]:#both right and left contains same value
            mark_circle(cell_id)#the cell is circled
            
    #the cell is surrounded by same valued cells vertically. If it is darken, two same value in a column will become circled; that's invalid
    if id_exists(up_cell) and id_exists(down_cell):#both up and down values exists
        if value_array[up_cell] == value_array[down_cell]:#both up and down contains same value
            mark_circle(cell_id)#the cell is circled
            
    if loop_form_if_darken(cell_id,mark_array):#Check if forms a dark loop if the cell_id is darkened , it will make circle marked cells discontinuous
        mark_circle(cell_id)#the cell is circled

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#takes a text(comma seperated) hitori file and makes the value_array of hitori
def take_input():
    print("--------------------------------------------------------------------------------")
    infile = open(input("\nEnter the hitori input file (full path) : "),'r')#taking the file input
    list_data = []
    
    part = infile.readline()#reading first line of that [csv] file
    while part:
        list_data.append(list(map(int,part.strip().split(','))))#splitting the text w.r.t. comma , converting them into integer and appending the listed value to list_data
        part = infile.readline()#reading the next line
    infile.close()
    
    all_value_array = np.array(list_data)#making numpy array from list_data
    return all_value_array

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#function for printing result
def print_solution():
   outfile = open('D:\hitori_solution.txt','a')
   solution_string = '\n'#result string
   print("\nSolution : \n")
   for sub_list in mark_array:
        for mark in sub_list:#for every marking in mark_array
           if mark == 'dark':
               print(u' X ',end = '')#printing ' X ' mark
               solution_string += u' • '#adding ' • ' mark in solution string for dark marked cells
           elif mark == 'circle':
               print(' O ',end = '')#printing ' O ' mark
               solution_string += ' o '#adding ' o ' mark in solution string for circle marked cells
           else:
               print(' ? ',end = '')#printing ' ? ' mark
               solution_string += ' ? '#adding ' ? ' mark in solution string for unknown marked cells
        print('')#printing newline
        solution_string += '\n'#adding newline
   print ("\nTime taken to solve : ",time_diff)
   #for writing solution to file
   while True:#loop till file is written properly without error
       try:#trying to store the result in 'D:\hitori_solution.txt'
           outfile_path = input("\nEnter a file path to store result ( defalut : D:\hitori_solution.txt ) : ")
           if outfile_path == '':
               outfile_path = 'D:\hitori_solution.txt'
           outfile = open(outfile_path, 'a')
           outfile.write("\nSOLUTION OF CURRENT HITORI : \n"+solution_string)#writing the solution
           outfile.close()
           print("\nSolution Written to output file : ",outfile_path)
           break
       except Exception as error:#error occured in file opening or writing or accessing
           print("\nUnable to Write solution file : ",outfile_path," due to  --> ",error)
           ask = input("\nRetry ( y/n) : ")#Error recovery option
           if ask == 'n' or ask == 'N':#user don't want to store result
               break

#---------------------------------------------------------------------------------main program starts---------------------------------------------------------------------------

#Given hitori Example(s) : 
'''
value_array = np.array([[5,2,8,8,3,4,7,1],[2,1,6,4,6,5,5,7],[8,4,5,4,7,3,4,1],[3,4,4,6,6,2,3,8],[6,2,7,2,1,4,8,3],[1,6,6,3,8,7,5,2],[5,3,1,4,4,2,6,3],[4,5,8,7,8,1,3,4]])
#value_array = np.array([[2,2,1,3,5,6,1,5],[3,4,7,6,2,5,8,1],[7,2,5,3,1,4,6,8],[3,6,1,4,8,1,5,1],[5,1,2,8,7,3,8,6],[6,5,6,7,8,1,2,4],[4,2,8,8,6,8,7,1],[8,8,4,3,5,2,3,7]])
'''
value_array = take_input()#taking hitori input from file
row_count = value_array.shape[0]#row from value array shape
column_count = value_array.shape[1]#column from value array shape
mark_array = np.array([['blank']*column_count]*row_count, dtype = '<U6')#initial mark array with all 'blank' marking
virtual_mark_array = np.array(mark_array)#creating initial virtual_mark_array for later advanced calculations 
#creating a list of all available cell_id(s)
all_id_list = []
for i in range(row_count):
    for j in range(column_count):
        all_id_list.append((i,j))#appending all cell_id


#Calling the pre-defined functions
start_time = datetime.datetime.now()
#marking circle for all unique values
for i in all_id_list:
    mark_unique(i)
while True:
    print("\nSOLVING >> ....")
    prev_mark_array = np.array(mark_array)#creating a copy of mark_array for checking any change occurrence
    stop_flag = True
    #calling every pre-defined solving functions one by one for every cell id
    for i in all_id_list:
        check_for_circle(i)#checking for circling
    for i in all_id_list:
        check_for_dark(i)#Checking for darkening
    for i in all_id_list:
        check_for_dark_advanced(i)#advance checking for darkening
    for i in all_id_list:
        check_for_circle_advanced(i)#advance checking for circling
    #checking any change occurrence in mark_array
    for i in all_id_list:
        if prev_mark_array[i] != mark_array[i]:
            stop_flag = False
            break
    if stop_flag:#No further change occurred in mark_array for running all above methods of solving
        break#end of calculations
    if 'blank' not in mark_array.flatten().tolist():#No blank cells left in mark_array for further calculations
        break#end of calculations
        
time_diff = datetime.datetime.now()-start_time#time taken to solve

print('')#for newline
print_solution()#printing result

#----------------------------------------------------------End of program------------------------------------------------------------------

pause = input("\nEnter to Exit : ")#to pause the script from exiting
