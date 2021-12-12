# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 13:59:06 2021

@author: shelb
"""

import numpy as np


vec1 = np.array([1,1,1])

vec2 = np.array([1,1,1])



def get_vectors(num_vectors, size_vectors):
    
    
    for vec in range(0, num_vectors):
        
        vector_list = []

        for i in range(0,size_vectors):
            
            element = input("enter value number " + str(i + 1) + " for vector " + str(vec + 1) + ": ")
            
            if element.isdigit():
                vector_list.append(float(element))
            else:
                print("please enter a numerical value")
            

            print(element)
            
            
    

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
    
    if text == 'addition':
        
        vectors = get_vectors(2, 3)
        
        new_vec = vec1 + vec2
        
        
    elif text == 'subtraction':
        new_vec = vec1 - vec2
    elif text == 'multiplication':
        new_vec = vec1 * vec2
    elif text == 'scalar multiplication':
        scalar = float(input("Enter the scalar to multiply your vector by: "))
        new_vec = vec1 * scalar
    elif text == 'dot product':
        new_vec = np.dot(vec1,vec2)
    elif text == 'constant addition':
        constant = float(input("Enter the constant to add to your vector: "))
        new_vec = vec1 + constant
    else:
        print("\nERROR: incorrect input \nEnter only letters \nChoose one of the options listed\n")
    
    # Return the result of the vector operation
    return new_vec
    
    

print("Operations: \n\t Addition \n\t Subtraction \n\t Multiplication \n\t Scalar Multiplication \n\t Dot Product \n\t Constant Addition")
operation = input("Choose a vector operation from the list above: ")

new_vec = do_math(operation)

print("The result is: " + str(new_vec))


