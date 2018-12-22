
# coding: utf-8

# In[ ]:


COUNT = 4
import numpy as np
a2 = np.array(list('.'*100))
a2.shape = (10,10)


# In[ ]:


def is_filled_below(array,point):
    if array[point[0]+1,point[1]] == 'x' or  array[point[0]+1,point[1]] == '0':
        return True
    else:
        return False


# In[ ]:


def get_left_diagonal(array,point):
    left_diagonal = []
    for i in range(COUNT-1,-COUNT,-1):
        try:
            row,col = point[0]-i,point[1]+i
            if row>=0 and col>=0 and (row,col) != point:
                value = array[row,col]
                if value == '.' and is_filled_below(array,(row,col)) == False:
                    value = '?'
                left_diagonal.append(value)
        except:
            pass
    return left_diagonal


# In[ ]:


def get_right_diagonal(array,point):
    right_diagonal = []
    for i in range(COUNT-1,-COUNT,-1):
        try:
            row,col = point[0]-i,point[1]-i
            if row>=0 and col>=0 and (row,col) != point:
                value = array[row,col]
                if value == '.' and is_filled_below(array,(row,col)) == False:
                    value = '?'
                right_diagonal.append(value)
        except:
            pass
    return right_diagonal


# In[ ]:


def get_upper_lower(array,point):
    upper_lower = []
    for i in range(COUNT-1,-COUNT,-1):
        try:
            row,col = point[0]-i,point[1]
            if row>=0 and col>=0 and (row,col) != point:
                value = array[row,col]
                if value == '.' and is_filled_below(array,(row,col)) == False:
                    value = '?'
                upper_lower.append(value)
        except:
            pass
    return upper_lower


# In[ ]:


def get_left_right(array,point):
    left_right = []
    for i in range(COUNT-1,-COUNT,-1):
        try:
            row,col = point[0],point[1]-i
            if row>=0 and col>=0 and (row,col) != point:
                value = array[row,col]
                if value == '.' and is_filled_below(array,(row,col)) == False:
                    value = '?'
                left_right.append(value)
        except:
            pass
    return left_right


# In[ ]:


def break_group(l):
    all_group = []
    length = len(l)
    for i in range(length-COUNT+2):
        sub_list = []
        for j in range(COUNT-1):
            sub_list.append(l[i+j])
        all_group.append(sub_list)
    return all_group


# In[ ]:


def get_all_group(array,point):
    return {'left_diagonal': break_group(get_left_diagonal(array,point)) , 'right_diagonal':break_group(get_right_diagonal(array,point)) ,
           'upper_lower':break_group(get_upper_lower(array,point)) , 'left_right':break_group(get_left_right(array,point))}


# In[ ]:


def get_point_priority(array,point,char):
    group_dict = get_all_group(array,point)
    if char == '0':
        priority_dict = {
         ('.', '.', '.') : 0,
         ('.', '.', '0') : 12,
         ('.', '.', '?') : 4,
         ('.', '.', 'x') : 2,
         ('.', '0', '0') : 210,
         ('.', '0', '?') : 18,
         ('.', '0', 'x') : 1,
         ('.', '?', '?') : 8,
         ('.', '?', 'x') : 4,
         ('.', 'x', 'x') : 24,
         ('0', '0', '0') : 80001,
         ('0', '0', '?') : 1000,
         ('0', '0', 'x') : 4,
         ('0', '?', '?') : 25,
         ('0', '?', 'x') : 2,
         ('0', 'x', 'x') : 1,
         ('?', '?', '?') : 15,
         ('?', '?', 'x') : 8,
         ('?', 'x', 'x') : 220,
         ('x', 'x', 'x') : 5000
        }
    else:
        priority_dict = {
         ('.', '.', '.') : 0,
         ('.', '.', '0') : 2,
         ('.', '.', '?') : 4,
         ('.', '.', 'x') : 12,
         ('.', '0', '0') : 24,
         ('.', '0', '?') : 4,
         ('.', '0', 'x') : 1,
         ('.', '?', '?') : 8,
         ('.', '?', 'x') : 18,
         ('.', 'x', 'x') : 210,
         ('0', '0', '0') : 5000,
         ('0', '0', '?') : 210,
         ('0', '0', 'x') : 1,
         ('0', '?', '?') : 8,
         ('0', '?', 'x') : 2,
         ('0', 'x', 'x') : 4,
         ('?', '?', '?') : 15,
         ('?', '?', 'x') : 25,
         ('?', 'x', 'x') : 1000,
         ('x', 'x', 'x') : 80001
        }
    sum_value = 0
    for key in group_dict.keys():
        for group in group_dict[key]:
                group.sort()
                priority_dict_key = tuple(group)
                sum_value += priority_dict[priority_dict_key]
    return sum_value


# In[ ]:


def add(array,char,column):
    column_array = array.T[column]
    row = (len(column_array)-list(column_array)[::-1].index('.'))-1
    array[row,column] = char


# In[ ]:


def get_fall_point(array,column):
    column_array = array.T[column]
    row = (len(column_array)-list(column_array)[::-1].index('.'))-1
    return (row,column)


# In[ ]:


def print_box(array):
    print('\n ',end = '')
    count = len(array[0])
    for i in range(1,count+1):
        print('',i,' ',end = '')
    print('')
    for row in array:
        print('|',end = '')
        for element in row:
            print(' '+str(element)+' |',end = '')
        print('\n',end = '')
    print('-'*(4*len(array[0])+1))


# In[ ]:


def has_won(array,point,char):
    group_dict = get_all_group(array,point)
    group_flat_list = []
    for key in group_dict.keys():
        for group in group_dict[key]:
            group_flat_list.append(group)
    if ([char]*(COUNT-1) in group_flat_list) and (array[point] == char):
        return True
    else:
        return False


# In[ ]:


char = 'x'
while '.' in a2.flatten():
    print_box(a2)
    ask = int(input("Enter the column number : "))-1
    add(a2,char,ask)
    point = get_fall_point(a2,ask)
    if has_won(a2,(point[0]+1,point[1]),char):
        print(char+' has won !')
        break
    if char == 'x':
        char = '0'
    else:
        char = 'x'
else:
    print("game is draw!")

