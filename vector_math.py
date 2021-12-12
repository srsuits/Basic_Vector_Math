# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 13:59:06 2021

@author: shelb
"""

import numpy as np


#vec1 = np.array([1,1,1])

#vec2 = np.array([1,1,1])


# Get vector(s) from user input
def get_vectors(num_v, size_v):
    
    # Create list to hold return vectors
    vectors = []
    
    # For each vector 
    for vec in range(0, num_v):
        
        # Create empty list for individual vector
        vector_list = []
        
        # For each element in vector
        for i in range(0,size_v):
            
            # Get the element 
            element = input("enter value number " + str(i + 1) + " for vector " + str(vec + 1) + ": ")
            
            # Check that input is numerical
            if element.isdigit():
                
                # Add new element to vector
                vector_list.append(float(element))
            else:
                print("please enter a numerical value")
            
        # Add finish vector to vectors 
        vectors.append(vector_list)
        
    return(vectors)
            
            
    

# Perform the operation chosen by user
def do_math(text):
    '''
    Parameters
    ----------
    text : string
        user input to choose which vector operation to perform
    Returns
    -------
    new_vec : np array or number
        result of vector operation

    '''
    # Ignore all capitalization
    text = text.lower()
    
    vec_size = input("Enter the size(dimension) of your vector(s): ")
    
    try:
        vec_size = int(vec_size)
    except:
        print("ERROR: please enter an integer value")
    
    
    if text == 'addition':
        # Get vectors from user input
        vectors = get_vectors(2, vec_size)

        # Separate vector lists and cast to np array
        vec1 = np.array(vectors[0])
        vec2 = np.array(vectors[1])
        
        # Math
        new_vec = vec1 + vec2
        
    elif text == 'subtraction':
        # Get vectors from user input
        vectors = get_vectors(2, vec_size)

        # Separate vector lists and cast to np array
        vec1 = np.array(vectors[0])
        vec2 = np.array(vectors[1])
        
        # Math
        new_vec = vec1 - vec2

    elif text == 'multiplication':
        # Get vectors from user input
        vectors = get_vectors(2, vec_size)

        # Separate vector lists and cast to np array
        vec1 = np.array(vectors[0])
        vec2 = np.array(vectors[1])
        
        # Math        
        new_vec = vec1 * vec2
        
    elif text == 'scalar multiplication':
        # Get vector and scalar from user input
        scalar = float(input("Enter the scalar to multiply your vector by: "))
        vec1 = np.array(get_vectors(1, vec_size)[0])
        
        # Math
        new_vec = vec1 * scalar
        
    elif text == 'dot product':
        # Get vectors from user input
        vectors = get_vectors(2, vec_size)

        # Separate vector lists and cast to np array
        vec1 = np.array(vectors[0])
        vec2 = np.array(vectors[1])
        
        # Math
        new_vec = np.dot(vec1,vec2)
        
    elif text == 'constant addition':
        # Get vector and constant from user input
        constant = float(input("Enter the constant to add to your vector: "))
        vec1 = np.array(get_vectors(1, vec_size)[0])
        
        # Math
        new_vec = vec1 + constant
    else:
        print("\nERROR: incorrect input \nEnter only letters \nChoose one of the options listed\n")
    
    # Return the result of the vector operation
    return new_vec
    
    

print("Operations: \n\t Addition \n\t Subtraction \n\t Multiplication \n\t Scalar Multiplication \n\t Dot Product \n\t Constant Addition")
operation = input("Choose a vector operation from the list above: ")

new_vec = do_math(operation)

print("The result is: " + str(new_vec))


