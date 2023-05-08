#!/usr/bin/env python
# coding: utf-8

# ### Taking the input from command line

# In[1]:


import numpy as np
import pandas as pd


# In[105]:


import traceback


# In[133]:


# 23 23 28 28 13 5 21 25 31 5  
print('Please enter the number of dishes , n : ')
num_dish = input()
print('Please enter the total Time , M : ')
max_time_threshold = input()
print('Please enter the time for '+str(num_dish) + ' dishes in a single line')
time_list = input()
 # strip any white space in the extreme left & right ; then split by space
dish_list =np.array(time_list.strip().split())
dish_list = list(map(int, dish_list))
print('the total no of time periods entered is '+str(len(dish_list)))
dish_list_copy = dish_list.copy()
if int(num_dish) != len(dish_list) :
    print('the no of dishes n & the time/effort list you entered do not have the same count. Please retry')


# In[134]:


dish_list


# # Part 1 - Heapsort

# In[135]:


# since in Python index starts at 0, hence the two children of root A[0] are A[1] and A[2] ; children of A[1] are A[3] & A[4]; 
# children of A[2] are A[5] & A[6] i.e. the left & right children index are - 2i+1 & 2i+2 respectively.
def get_left_child_index(index):
    return 2*index +1
def get_right_child_index(index):
    return 2*index +2


# In[136]:


def max_heapify(input_array, heapsize, current_index):
    """
    max_heapify assumes the two children left & right are Max-heaps themselves- but the root itself ( A[i]) might not be 
    the largest element in the initial stage. - Thus the condition of max heap might not be satisfied. 
    
    It remedies the situation by putting the value at the root A[i] at the appropriate place in the Binary Heap.
    ------
    Input Parameters
    ------
    array : nd array 
        the n dimensional array containing all the heap elements
    input_array_heapsize : int
        we need to check for the max element only in the heapsize range & ignore everything outside it.
    current_index : int
        root element in a heap
    """
    
    
    right = get_right_child_index(current_index)
    left = get_left_child_index(current_index)
    largest_element_index = current_index #initialise largest index. Later compared with left & right child
    if  heapsize > right:
        if arr[current_index] < input_array[right]: # if right child > largest-so-far
            # consider right to be largest-so-far ( out of current/root & right)
            largest_element_index = right     
    if heapsize > left :
        if input_array[largest_element_index] < input_array[left]: # if the left child> root
            # consider left to be largest-so-far  ( out of current/root, left & right)
            largest_element_index = left
  

        
    if  current_index != largest_element_index : 
        # if root is not the largest element, it violates max-heap property
        # so swap the root with the largest of the 3 ( out of current/root, left & right)
        input_array[current_index], input_array[largest_element_index] = input_array[largest_element_index], input_array[current_index]
        #now the older root element is in the older A[largest] position i.e. either left or right child position. 
        #But it might not be the largest in the child tree . So, continue recursively till it is max-heapified
        max_heapify(input_array, heapsize, largest_element_index)


# In[137]:


def build_max_heap(input_array, heapsize):
    '''
    Converts input_array into a max-heap in a Bottom -Up fashion, starts with 1 -sized heaps & runs for Each node.
    If heapsize is even --Starts with (heapsize/2) which has two children heapsize+1 & heapsize+2 -- none of these exist.
    NOTE - if heapsize is odd, floor(heapsize/2) has a child and these 2 need to be max-heapified.
    Then we move on to (heapsize/2)-1, the children are left = (heapsize-2+1), right = (heapsize-2+2). These 3 elements are max -heapified. 
    This contnues till we reach A[0] - the global root/last element of the array - i.e. max heapify it too
    ---
    Input Params 
    input_array : nd array
        the whole input array
    heapsize : int
        we need to check for the max element only in the heapsize range & ignore everything outside it.
    ----
    Returns : no return params. Inplace.
    '''
    for i in reversed(range(0,int(np.floor(heapsize/2+1)))): # iterate backwards- from floor(heapsize/2) to 0 ( both inclusive)
          max_heapify(input_array, heapsize, i)
  


# In[139]:


def solveGreedy(input_array, max_time_threshold):
    '''
    -------------HEAPSORT + Greedy Solving -----------------
    Create an ascending sorted array, by extracting the root element ( which is largest) & placing at the end.
    Now discard the last element i.e. reduce the heap-size & re-heapify to get the second largest element as the new Root element. 
    Repeat the process till only 2 elements left in the heap
    After sorting gets the max possible score from the sorted list
    ---
    Input Params
    ---
    input_array : nd array
    max_time_threshold : int
        max time allowed for finishing all dishes
    ----
    Returns : no return params. Inplace.
    '''
    max_heapsize = len(input_array)
    build_max_heap(input_array, max_heapsize)# create a max heap from the input array
    #for i in reversed(range(1,heapsize)):# iterate backwards- from (heapsize-1) to 1 i.e. 2nd element
    for heapsize in range(max_heapsize-1, 0, -1):# iterate backwards- from (heapsize-1) to 1 i.e. 2nd element
        # since A[0] is the largest , and we want to sort in ascending way, we need to swap A[0] with the last element
        input_array[heapsize], input_array[0] = input_array[0], input_array[heapsize] #swapping
        # Now discard the last element by reducing the heap-size &  re -maxheapify to get the second largest element & repeat
        max_heapify(input_array, heapsize, 0)#max heapify with heap size = heapsize 
    #heap sorting done -in place 
    effort_sum = 0
    chosen_effort_list = []
    for effort in input_array:
        # if adding the new value exceeds the threshold of max time allowed M; ignore it & exit the loop 
        if effort_sum + effort > int(max_time_threshold):
            break
        effort_sum = effort_sum + effort
        chosen_effort_list.append(effort)
    print('Maximum Effort = '+str(effort_sum) +' i.e. the following efforts :'+ str(chosen_effort_list))


# In[140]:


dish_list_copy


# In[142]:


arr = dish_list_copy.copy() #[1, 12, 9, 5, 6, 10]
solveGreedy(arr, max_time_threshold)
print('sorted array')
print(arr)


# # Dynamic Programming

# In[2]:


# 23 23 28 28 13 5 21 25 31 5  
print('DP- Please enter the number of dishes , n : ')
num_dish = input()
print('Please enter the total Time , M : ')
max_time_threshold = input()

print('Please enter the Point for '+str(num_dish) + ' dishes in a single line')
point_list = input()
 # strip any white space in the extreme left & right ; then split by space
point_list =np.array(point_list.strip().split())
point_list = list(map(int, point_list))
print('Please enter the Effort/ time for '+str(num_dish) + ' dishes in a single line')
effort_time_list = input()
 # strip any white space in the extreme left & right ; then split by space
effort_time_list =np.array(effort_time_list.strip().split())
effort_time_list = list(map(int, effort_time_list))

print('the total no of time periods entered is '+str(len(effort_time_list)))
#dish_list_copy = time_list.copy()
if int(num_dish) != len(effort_time_list) :
    print('the no of dishes n & the time/effort list you entered do not have the same count. Please retry')


# In[148]:


#sum(effort_time_list)


# In[143]:


#P
all_points_sum = sum(point_list)
print(all_points_sum)

dp_table = np.array([[-99.0 for point in range(int(num_dish))] for num in range(int(max_time_threshold))])
dp_table.shape

# In[5]:



#fill_dp_table(dp_table,dish_list_copy, point_list ):
#dp_table  


# In[189]:


def solveDP(max_time_threshold, effort_time_list, point_list, num_dish):
    '''returns the required efforts/time in table[num_dishes][points scored] format
    ---------
    Input Parameters
    ----
    max_time_threshold - int
     M - the max time the chef can take
    effort_time_list - array
    list of all the effort/time for each dish
    point_list - array
    list of all the effort/time for each dish
    num_dish -int
    total no of dishes
    -------
    Returns
    the DP_table dataframe containing the required efforts in table[num_dishes][points scored] format
    
    '''
    all_points_sum = sum(point_list)
    # stores the required efforts in table[num_dishes][points scored] format
    dp_table = np.array([[np.inf for point in range(int(all_points_sum)+1)] for num in range(int(num_dish)+1)])
    dp_table= pd.DataFrame(data = dp_table)
    
    #print(dp_table.shape)
    #  if no dish is prepared, boudary condition violated. Hence time set to Infinity
    dp_table.iloc[0,:] = np.inf 
    # time required for scoring 0 points is -> 0 
    dp_table.iloc[:,0] =0 
    for dish_count in range(int(num_dish)+1):
        for points_scored in range(int(all_points_sum)+1):
            try :
                if dish_count ==0 or points_scored ==0:
                    pass
                elif  points_scored < point_list[dish_count-1]:
                    #in python index starts at 0..hence 0...num_dish elements
                    #cannot attempt the i-th dish
                    prev_time = dp_table.iloc[dish_count-1,points_scored]
                    dp_table.iloc[dish_count,points_scored] = prev_time
                else:
                    prev_time = dp_table.iloc[dish_count-1,points_scored]
                    # time taken if he attempts the i-th dish, when the sum of points remains same
                    new_time = effort_time_list[dish_count-1]+ dp_table.iloc[dish_count-1, points_scored-point_list[dish_count-1]]
                    if new_time> int(max_time_threshold): # if the new effort crosses the threshold, discard it
                        dp_table.iloc[dish_count, points_scored] = prev_time
                    else:
                        dp_table.iloc[dish_count, points_scored] = min(prev_time, new_time)
            except Exception as e:
                print(dish_count, points_scored)
                print(e)
                print(traceback.format_exc())


# In[191]:


def solveDP(max_time_threshold, effort_time_list, point_list, num_dish):
    '''returns the required efforts/time in table[num_dishes][points scored] format
    ---------
    Input Parameters
    ----
    max_time_threshold - int
     M - the max time the chef can take
    effort_time_list - array
    list of all the effort/time for each dish
    point_list - array
    list of all the effort/time for each dish
    num_dish -int
    total no of dishes
    -------
    Returns
    the DP_table dataframe containing the required efforts in table[num_dishes][points scored] format
    
    '''
    all_points_sum = sum(point_list)
    # stores the required efforts in table[num_dishes][points scored] format
    dp_table = np.array([[np.inf for point in range(int(all_points_sum)+1)] for num in range(int(num_dish)+1)])
    dp_table= pd.DataFrame(data = dp_table)
    
    #print(dp_table.shape)
    #  if no dish is prepared, boudary condition violated. Hence time set to Infinity
    dp_table.iloc[0,:] = np.inf 
    # time required for scoring 0 points is -> 0 
    dp_table.iloc[:,0] =0 
    for dish_count in range(int(num_dish)+1):
        for points_scored in range(int(all_points_sum)+1):
            try :
                if dish_count ==0 or points_scored ==0:
                    pass
                elif  points_scored < point_list[dish_count-1]:
                    #in python index starts at 0..hence 0...num_dish elements
                    #cannot attempt the i-th dish
                    prev_time = dp_table.iloc[dish_count-1,points_scored]
                    dp_table.iloc[dish_count,points_scored] = prev_time
                else:
                    prev_time = dp_table.iloc[dish_count-1,points_scored]
                    # time taken if he attempts the i-th dish, when the sum of points remains same
                    new_time = effort_time_list[dish_count-1]+ dp_table.iloc[dish_count-1, points_scored-point_list[dish_count-1]]
                    if new_time> int(max_time_threshold): # if the new effort crosses the threshold, discard it
                        dp_table.iloc[dish_count, points_scored] = prev_time
                    else:
                        dp_table.iloc[dish_count, points_scored] = min(prev_time, new_time)
            except Exception as e:
                print(dish_count, points_scored)
                print(e)
                print(traceback.format_exc())
    dishes_remaining = int(num_dish)-1
    final_selection_effort = []
    final_selection_point =[]
    #print(dp_table.min(axis =0))
    print('max_time_threshold '+str(max_time_threshold))
    for points_scored in range(int(all_points_sum),0,-1):#iterate from max to min
        if dp_table.iloc[:, points_scored].min() <= float(max_time_threshold) :       
           
            min_effort = dp_table.iloc[:, points_scored].min()# for a given point check the minimum effort possible
            print('minimum effort for Maximum Points under time constraint p:='+str(points_scored)+' is -> '+str(min_effort))
            print(dp_table.iloc[:, points_scored].argmin())#first match
            break
    #print(point_list[dp_table.iloc[:, points_scored].argmin()])
    return dp_table
dp_table = solveDP(max_time_threshold, effort_time_list, point_list, num_dish) #dp_table
#dp_table

