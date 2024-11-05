#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install python-Levenshtein')


# In[2]:


import Levenshtein  
string1 = "kitten"  
string2 = "sitting"  
edit_distance = Levenshtein.distance(string1, string2)  
print("The edit distance between '{}' and '{}' is: {}".format(string1, string2, edit_distance))  


# In[2]:


def edit_distance(str1, str2):  
    m, n = len(str1), len(str2)  
    # Create a matrix of size (m + 1) x (n + 1)
    dp = [[0] * (n + 1) for _ in range(m + 1)]  
    
    # Initialize the matrix
    for i in range(m + 1):  
        for j in range(n + 1):  
            if i == 0:  
                dp[i][j] = j  # If str1 is empty, insert all characters of str2
            elif j == 0:  
                dp[i][j] = i  # If str2 is empty, remove all characters of str1
            elif str1[i - 1] == str2[j - 1]:  
                dp[i][j] = dp[i - 1][j - 1]  # No operation needed
            else:  
                dp[i][j] = 1 + min(dp[i - 1][j],    # Deletion
                                   dp[i][j - 1],    # Insertion
                                   dp[i - 1][j - 1])  # Substitution  

    return dp, dp[m][n]  # Return the matrix and the edit distance

# Function to print the distance matrix with labeled rows and columns
def print_matrix(matrix, str1, str2):
    # Print header
    print("\t", end="")
    for char in str2:
        print(char, end="\t")
    print()

    # Print each row with the corresponding character from str1
    for i in range(len(matrix)):
        if i == 0:
            print(" ", end="\t")  # Top-left corner
        else:
            print(str1[i - 1], end="\t")  # Row label
        for j in range(len(matrix[i])):
            print(matrix[i][j], end="\t")
        print()

# Main function to test the edit distance function
def main():
    str1 = "kitten"  
    str2 = "sitting"  
    matrix, distance = edit_distance(str1, str2)  
    
    print(f"Edit Distance between '{str1}' and '{str2}': {distance}")  
    print("Distance Matrix:")
    print_matrix(matrix, str1, str2)

# Run the program
if __name__ == "__main__":
    main()


# In[ ]:




