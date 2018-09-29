
# coding: utf-8

# In[47]:


import numpy as np#importing numpy


# In[49]:


#marks all the values as circle which are unique in both of its row and column
def mark_unique(cell_id):
    #Checking for row and column uniqueness
    if (value_array[cell_id[0],...].tolist().count(value_array[cell_id]) == 1) and (value_array[...,cell_id[1]].tolist().count(value_array[cell_id]) == 1):
        
        mark_array[cell_id] = 'circle'
                                                                                    


# In[50]:


#returns True if the cell lies in the border side of the game box
def is_border_cell(cell_id):
    if (cell_id[0] == 0 or cell_id[1] == 0) or (cell_id[0] == row_count-1 or cell_id[1] == column_count-1):
        return True
    else:
        return False


# In[51]:


#Checks for whether the given id indicates a valid cell_id
def id_exists(cell_id):
    if (cell_id[0]>=0 and cell_id[0]<row_count) and (cell_id[1]>=0 and cell_id[1]<column_count):#true for valid id(s)
        return True
    else:
        return False


# In[64]:


#returns the diagonal neighboure's(of the cell_id) cell id(s) as a list
#if the only_dark flag is True, returns only the list of available dark neighbour's id(s)
def get_diagonal_neighbour(cell_id,only_dark = False):
    #all diagonal values(may contain invalid id(s))
    all_diagonal_id = [(cell_id[0]+1,cell_id[1]-1),(cell_id[0]+1,cell_id[1]+1),(cell_id[0]-1,cell_id[1]-1),(cell_id[0]-1,cell_id[1]+1)]
    result = []
    for _id in all_diagonal_id:
        if id_exists(_id):#sorting the valid id values
            if only_dark:#checking for dark flag
                if mark_array[_id] == 'dark':#only darks will pass
                    result.append(_id)
            else:#all diagonals(without dark checking)
                result.append(_id)  
    return result
        


# In[53]:


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
    


# In[54]:


#marks a cell as dark in mark_array and fulfill the other consequents
def mark_dark(cell_id):
    if mark_array[cell_id] != 'blank' :
        return None
    
    mark_array[cell_id] = 'dark'#marks a cell as 'dark' in mark_array
    
    #effect of that value darkening
    
    row_column_neighbour = [(cell_id[0],cell_id[1]-1),
                           (cell_id[0],cell_id[1]+1),
                           (cell_id[0]-1,cell_id[1]),
                           (cell_id[0]+1,cell_id[1])]#all row and column neighbours(may contain invalid id(s))
    
    for _id in row_column_neighbour:
        if id_exists(_id):#pass for valid id only
            mark_circle(_id)#surrounding row column neighbours are circled as they cannot be darken(by rule)
        


# In[55]:


#Checks whether a cell cannot be circled , and makes it dark 
def check_for_dark(cell_id):
    if mark_array[cell_id] != 'blank' :
        return None
    
    cell_value = value_array[cell_id]#value of cell_id
    
    #LOGIC : There are same values adjacent in same row(horizontal) which is equal to cell_value .if the cell is circled,there will be 
        #   two adjacent dark cells in same row; which is invalid,so it must be darken
    for i in range(column_count-1):
        id_1 = (cell_id[0],i)
        id_right = (cell_id[0],i+1)
        if (mark_array[id_1] == 'blank') and (mark_array[id_right] == 'blank'):#checks if two adjacents are blank in same row
            if (value_array[id_1] == cell_value) and (value_array[id_right] == cell_value):# and they carries the same value that of cell_value
                mark_dark(cell_id)#marks the cell as dark
                
    #LOGIC : There are same values adjacent in same column(vertical) which is equal to cell_value .if the cell is circled,there will be 
        #   two adjacent dark cells in same column; which is invalid,so it must be darken
    for j in range(row_count-1):
        id_2 = (j,cell_id[1])
        id_down = (j+1,cell_id[1])
        if (mark_array[id_2] == 'blank') and (mark_array[id_down] == 'blank'):#checks if two adjacents are blank in same column
            if (value_array[id_2] == cell_value) and (value_array[id_down] == cell_value):# and they carries the same value that of cell_value
                mark_dark(cell_id)#marks the cell as dark


# In[59]:


#checks whether circled values are discontinuous by darkened cells if the cell_id is darkened
def loop_form_if_darken(cell_id):
    if mark_array[cell_id] != 'blank' :
        return False
    
    connected_blacks = [cell_id]
    checked_cells = []
    border_flag = is_border_cell(cell_id)
    
    while len(connected_blacks) > 0:
        new_black_connections = []#newer conncetions with connected_blacks
        for black_id in connected_blacks:
            neighbours = get_diagonal_neighbour(black_id,True)#fetch the black diagonal neighbours(as they cannot be adjacent in row/column)
            for _id in neighbours:
                if _id not in checked_cells:#already taken in connection
                    new_black_connections.append(_id)#newer conncetions with connected_blacks are added
                    
        for id_ in new_black_connections:
            if is_border_cell(id_):#one border cell found in connection
                if border_flag:#if alreany contains one border cell
                    return True#connection of dark cells contains two different border cells
                else:
                    border_flag = True#one border cell is present in connection
            if new_black_connections.count(id_) >= 2:#meets to a common point,so loop formed
                return True
            
        checked_cells += connected_blacks#checked cells are added to checked_cells
        connected_blacks = new_black_connections#only new black cells will proceed the process of connecting, so replaced
        
    return False#Don't for any dark loop if darkned , don't make circle marked cells discontinuous
        


# In[72]:


#Checks whether a cell cannot be darked , and makes it circle
def check_for_circle(cell_id):
    if mark_array[cell_id] != 'blank' :
        return None
    #all neighbouring cell(s) ( valid or invalid) in horizontal and vertical directions
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
            
    if loop_form_if_darken(cell_id):#Check if forms a dark loop if the cell_id is darkened , it will make circle marked cells discontinuous
        mark_circle(cell_id)#the cell is circled


# # CHECKING

# In[78]:


row_count = 8
column_count = 8
#A given hitori
value_array = np.array([[3,3,6,1,3,7,3,5],[2,5,6,9,1,8,3,4],[1,1,2,1,3,5,3,8],[2,9,9,3,4,7,2,5],[4,2,5,6,1,1,7,9],[4,4,6,8,5,2,6,1],[3,7,1,4,3,6,3,2],[2,8,8,7,6,4,1,3]])
mark_array = np.array([['blank']*column_count]*row_count, dtype = '<U6')
all_points = []
for i in range(row_count):
    for j in range(column_count):
        all_points.append((i,j))#appending all cell_id


# In[79]:


#Calling the pre-defined functions
for i in all_points:
    mark_unique(i)
for i in all_points:
    check_for_circle(i)
for i in all_points:
    check_for_dark(i)


# In[82]:


#printing result
for i in mark_array:
    print(i)

