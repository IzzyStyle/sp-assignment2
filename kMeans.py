# Name: Eugene Zhuravel, Ian Wodder, Israel Nolazco
# Date: 7/24/2019
# Course Name:CPSC-51100-003
# Semester: Summer 2018
# Assignment: Programming Assignment 2

import sys
import os

# Opens file in local directory, read each line and cast to a float
def openFile(filename):
    location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    location = location + "\\" + filename
    lines = [float(x.rstrip()) for x in open(location)]
    return lines

# initialized empty clusters with centroid as the 'key' value
def initializeClusters(num_clusters, points):
    clusters = {}
    
    index = 0
    for num in points:
        # make sure there are no more clusters than points
        if(index < num_clusters):
            index = index + 1
            clusters[str(num)] = {}
            

# Entry point of application
def main(argv):
    #Print header 
    print(
"""CPSC-51100, Summer 2019"
NAME: Eugene Zhuravel. Iam Wodder, Israel Nolazco"
PROGRAMMING ASSIGNMENT #2"
""")
        
    #read file
    points = openFile("prog2-input-data.txt")

 #function ensure that the user enters an integer
def inputNumber(number_clusters):
    while True:
        try:
            userInput = int(input(number_clusters))

        except ending:
            print("Not an integer! Try again.")
        else:
            return userInput
            break
            
    #get user name
number_clusters = float(inputNumber("Enter the number of clusters: "))    
    
clusters = initializeClusters(number_clusters, points)
    
    # TODO: write k-means algorithm
    
    # TODO: print result
    
pass

if __name__ == "__main__":
    main(sys.argv)

