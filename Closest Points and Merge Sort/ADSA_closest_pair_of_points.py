#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#ADSA Assignment 1 - Sauradeep Debnath


# In[1]:


import numpy as np
import math


# # Custom Merge Sort

# In[2]:


def checkif_index_exists(list_test, test_index):
    return (0 <= test_index< len(list_test))# Check if a List has a particular index 
def custom_merge_sort_tuple(series,tuple_index=0):
    """Returns the sorted output using Merge Sort. Time Complexity O(nlog n ) for input of length n 
    Parameters
    ----------
    series : str
        The input data. Could be either a list of int/float. Or. a list of tuples
    tuple_index : int, optional
        if the data is List of tuples, which element of the tuples to sort it by.
    Returns
    -------
    none. Sorts the input list inplace.
    """
    length =len(series)
    if length>1:
        mid = np.floor((length/2))# finding the midpoint of the array
        mid = mid.astype(int) 
        left_sub =series[:mid] # Left half of the series
        custom_merge_sort_tuple(left_sub,tuple_index)# recursive calling -LEFT half
        right_sub =series[mid:] # right half of the series
        custom_merge_sort_tuple(right_sub, tuple_index)# recursive calling -RIGHT half
        index,left_i,right_i =0,0,0# initialisation 
        for index in range(length):# running a loop for the length of the entire array    
            try:
                if any([isinstance(t, tuple) for t in series]):# if it is list of tuples
                    left_smaller_condition = (left_sub[left_i][tuple_index] < right_sub[right_i][tuple_index])
                    
                elif any([isinstance(t, (int, float)) for t in series]):# if it is list of integers or floats
                    left_smaller_condition = (left_sub[left_i] < right_sub[right_i])
            
                if (left_smaller_condition):
                    series[index] = left_sub[left_i] # if the left[i]<right[j], assigning left[i] to outout array & increment left[i]
                    left_i += 1
                else:
                    series[index] = right_sub[right_i]
                    right_i += 1
            except IndexError:# if Either of the left or right sub-array has already been traversed, but one is remaining
                # In that case, it throws List Index out of Bound error. We are handling that case below.
                if checkif_index_exists(right_sub, right_i):# if the right subarray still has elements remaining
                    series[index] = right_sub[right_i]
                    right_i += 1
                if checkif_index_exists(left_sub, left_i):# if the left subarray still has elements remaining
                    series[index] = left_sub[left_i]
                    left_i += 1
        


# ## TAKE THE TOTAL LENGTH & THE COORDINATES AS INPUT

# In[3]:


def get_input_points_2D():
    print('How many points are there on the 2D plane?')
    num_points = input()
    point_list_of_tuples =[]
    for i in range(int(num_points)):
        print('Enter the coordinates of Point '+str(i+1))
        print('the x co ordinate')
        x = input()
       
        print(' the y co ordinate')
        y = input()

        point_list_of_tuples.append((float(x),float(y),int(i))) #stored in the form (x_coordinate, y_coordinate, serial_no)
    
    print('You have entered'+str(point_list_of_tuples)+' where the 3 elements of tuple are :')
    print('(x -co ordinate ,y- co ordinate, Serial No/system generated Unique ID) ')
    return point_list_of_tuples
point_list_of_tuples = get_input_points_2D()
point_list_of_tuples_copy = point_list_of_tuples.copy()
#print(point_list_of_tuples_copy)


# In[ ]:




#worked for the below ---point_list_of_tuples =
#[(34.0, -56.0, 0), (23.0, 89.0, 1), (58.0, -56.0, 2), (67.89, -7.8, 3), (46.0, 28.0, 4), (78.0, 68.0, 5), (34.0, 49.0, 6), 
#(89.0, -0.89, 7), (47.0, -7.9, 8), (345.0, 68.0, 9), (98.0, 31.0, 10), (56.0, 77.0, 11)]
# In[4]:


x_sorted_points = point_list_of_tuples.copy()
custom_merge_sort_tuple(x_sorted_points,0)
print('x_sorted_points'+str(x_sorted_points))
y_sorted_points = point_list_of_tuples.copy()
custom_merge_sort_tuple(y_sorted_points,1)
print('y_sorted_points'+str(y_sorted_points))


# In[5]:


## CHECK ALL THE DISTANCE PAIRS USING BRUTE FORCE - USED IN VALIDATING OUR ALGO
## USED for co-ordinates of the form (x_coordinate, y_coordinate, serial_no)
mini =100000
for i in range(len(x_sorted_points)):
    for j in range(i+1, len(x_sorted_points)):
            temp = math.sqrt((x_sorted_points[i][0]- x_sorted_points[j][0])**2 + (x_sorted_points[i][1]- x_sorted_points[j][1])**2)
            if temp<mini:
                mini = temp
print('minimum distance from Brute force ( for validation)---> '+str(mini))
            


# In[6]:


#STEP 1 - Euclidean DIstance for tuples of the form (x_coordinate, y_coordinate, serial_no)
def euclidean_distance_tuples(point1, point2):
    """Returns the euclidean distance between two tuples of the form (x_coordinate, y_coordinate, serial_no)
    ----------
    point1 : tuple of float/int values
        The input point 1 of the form (x_coordinate, y_coordinate, serial_no)
    point2 : tuple of float/int values
        The input point 1 of the form (x_coordinate, y_coordinate, serial_no)
    Returns
    -------
    euclidean distance :float 
    """
    return math.sqrt((point1[0] - point2[0]) **2 +(point1[1] - point2[1]) **2)
#euclidean_distance_tuples((1,1),(3,3))


# # FINAL CLOSEST POINT CODE

# In[7]:


def findstrip(x_sorted_points, y_sorted_points, mid, mini):
    """Returns the y-sorted points whose x co ordinates are between the x -coordinate of the midpoint + /- DELTA ( minimum distance)
    ----------
    x_sorted_points : tuple of float/int values
        The input point 1 of the form (x_coordinate, y_coordinate, serial_no)
    y_sorted_points : tuple of float/int values
        The input point 1 of the form (x_coordinate, y_coordinate, serial_no)
    mid : int
         the mid point of the x_sorted_points
    mini : float
        the minimum distance so far
    Returns
    -------
    euclidean distance :float 
    """
    #step 1 - find the Serial No(s)/ Unique ID(s) ( i.e. the third element in our tuples)
    # for the points whose x -co-ordinate values lie between the x- value of the mid point +/- Minimum distance
    # NOTE - in each of the tuples in Point List, index[0]-> X, index[1]-> Y, index[2]-> Serial No/Unique ID
    x_strip_serial = [x[2] for x in x_sorted_points if (x_sorted_points[mid][0]-mini<x[0]) & (x[0]<x_sorted_points[mid][0]+ mini)]
    #step 2 -- From the y-sorted array , select the points with Serial No(s)/ Unique ID(s) ( i.e. the third element in our tuples)
    # in the list x_strip_serial. 
    y_strip = [y for y in y_sorted_points if y[2] in x_strip_serial]
    return y_strip
def brute_force(x_sorted_points):
    """Returns the euclidean distance between two tuples of the form (x_coordinate, y_coordinate, serial_no).
    THIS IS CALLED ONLY WHEN 2 or 3 points are remaining after recursive Divide & Conquer
    ----------
    x_sorted_points : points of the format (x_coordinate, y_coordinate, serial_no) sorted by x -coordinate
    Returns
    -------
    minimum distance calculated via bruteforce (for x<=3) 
    """
    min_val = float('inf')
    for i in range(len(x_sorted_points)):
        for j in range(i+1, len(x_sorted_points)):
            dist = math.sqrt((x_sorted_points[i][0]- x_sorted_points[j][0])**2 + (x_sorted_points[i][1]- x_sorted_points[j][1])**2)
            if dist<min_val:
                min_val = dist# if less than earlier minimum value, then replace
                min_xi= x_sorted_points[i][0]
                min_yi= x_sorted_points[i][1]
                min_xj=x_sorted_points[j][0]
                min_yj = x_sorted_points[j][1]
    return min_val, min_xi, min_yi, min_xj, min_yj

def closest_point_custom(x_sorted_points, y_sorted_points):
    """Returns the euclidean distance between two tuples of the form (x_coordinate, y_coordinate, serial_no)
    ----------
    x_sorted_points : tuple of float/int values
        The input point 1 of the form (x_coordinate, y_coordinate, serial_no).Sorted by x.
        for the LEFT & RIGHT subarrays -- only the left & right half of the array is step n 
        is sent as x_sorted_points of the next recursion step
    y_sorted_points : tuple of float/int values
        The input point 1 of the form (x_coordinate, y_coordinate, serial_no). Sorted by y.

    Returns
    -------
    minimum_distance :float 
    """
    length = len(x_sorted_points)
    
    if length>3:
        mid = np.floor((length/2))# finding the midpoint of the array
        mid = mid.astype(int) 
        left_sub =x_sorted_points[:mid] # Left half of the series
        left_minimum_distance, min_xil, min_yil, min_xjl, min_yjl = closest_point_custom(left_sub,y_sorted_points)# recursive calling
        
        right_sub =x_sorted_points[mid:] # right half of the series
        right_minimum_distance, min_xir, min_yir, min_xjr, min_yjr = closest_point_custom(right_sub, y_sorted_points)# recursive calling
        
        minimum_distance = min(left_minimum_distance,right_minimum_distance)
        if left_minimum_distance<right_minimum_distance:
            
            min_xi, min_yi, min_xj, min_yj = min_xil, min_yil, min_xjl, min_yjl
        else :
            min_xi, min_yi, min_xj, min_yj =min_xir, min_yir, min_xjr, min_yjr
        #NEXT find the y-sorted lists for the points whose x -co ordinates lie on the strip 
        #i.e. mid point x cordinates +/- delta ( minimum distance)
        y_sorted_strip = findstrip(x_sorted_points, y_sorted_points, mid, minimum_distance)
        for i in range(len(y_sorted_strip)):#x- coordinate range
            for j in range(i+1,len(y_sorted_strip)):
                if (y_sorted_strip[j][1]- y_sorted_strip[i][1])<minimum_distance:
                    try:
                        distance_iter_ij = euclidean_distance_tuples(y_sorted_strip[i],y_sorted_strip[j])
                        if distance_iter_ij <minimum_distance:
                            minimum_distance = distance_iter_ij
                            min_xi= y_sorted_strip[i][0]
                            min_yi= y_sorted_strip[i][1]
                            min_xj= y_sorted_strip[j][0]
                            min_yj = y_sorted_strip[j][1]
                    except IndexError: # if ether i th or j th index does not exist, Do nothing 
                        pass
                
                else:
                    break # SINCE the co ordinates are y sorted , as soon as yj -yi > DELTA --> Exit
    else :
        minimum_distance, min_xi, min_yi, min_xj, min_yj = brute_force(x_sorted_points)### BRUTE FORCE when only 2 or 3 points are remaining
    return minimum_distance, min_xi, min_yi, min_xj, min_yj
        
delta ,  min_xi, min_yi, min_xj, min_yj = closest_point_custom(x_sorted_points, y_sorted_points)

print('minimum distance as per Divide & Conquer algo is - ')
print('The closest pair of points are ({}, {}) and ({}, {}). The distance between them is {} units.'.format(min_xi, min_yi, min_xj, min_yj , str(round(delta,2))))


# In[ ]:





# In[ ]:




