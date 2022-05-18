# Program name: CD INVENTORY
# Author: Memory Bethel
# Date: 5/1/2022
# Summary: CD Inventory list of popular 90s R&B and HipHop Album log
# Variable:
#   searchType = how to to navigate the program (int)
#   CD_list = list containing the CD inventory (str)
#   infile_CD = open the files for the list (str)

import os
import random

def main():

    try:
        # Open files and read them into lists
        infile_CD = open("cdList.txt", "r")
        CD_list = infile_CD.readlines() # reads file lines into a list

        # Ask for type of search
        searchType = -1
        while searchType != 9:
            searchType = int(input("Enter 1 for full printed list, 2 for album search, 3 for artist search,\n"+
                                   "4 for the year, 5 for the genre, 6 for a random album or 9 to quit: "))
            
            if searchType == 1:
                printFile(CD_list)
            elif searchType == 2:
                searchByAlbum(CD_list)
            elif searchType == 3:
                searchByArtist(CD_list)
            elif searchType == 4:
                searchByYear(CD_list)           
            elif searchType == 5:
                searchByGenre(CD_list)
            elif searchType == 6:
                searchRandom(CD_list)
            elif searchType != 9:
                print("ERROR...your choices are 1, 2, 3, 4, 5, or 9.")

        print("End of program.")

    except IOError:
        print("File name error.")
        os._exit(0)
    

    # Close files
    infile_CD.close()
    
# print the file cd list
def printFile(CD_list):
    print()
    print("%-35s%-25s%-10s%-10s" % ("Album","Artist","Year","Genre"))
    
    for i in range(len(CD_list)):
        CD_list[i] = CD_list[i].rstrip('\n')

        #num = random.randint(0, len(CD_list))
        item = CD_list[i]
        itemParts = item.split(',')
        
        album = itemParts[0]
        artist = itemParts[1]
        year = itemParts[2]
        genre = itemParts[3]

        print("%-35s%-25s%-10s%-10s" %(album, artist, year, genre))

# Function called to search the list by album name.    
def searchByAlbum(CD_list):

    another = "Y"
    while another.upper() == "Y":
        searchKey = input("Enter an album name: ")
        print()
        print("%-35s%-25s%-10s%-10s" % ("Album","Artist","Year","Genre"))
        
        for i in range(len(CD_list)):
            CD_list[i] = CD_list[i].rstrip('\n')

            #num = random.randint(0, len(CD_list))
            item = CD_list[i]
            itemParts = item.split(',')
            
            album = itemParts[0]
            artist = itemParts[1]
            year = itemParts[2]
            genre = itemParts[3]
            
            
            if searchKey.upper() in album.upper():
                print("%-35s%-25s%-10s%-10s" %(album, artist, year, genre))

        print("Would you like to continue searching or return to the main menu?")
        another = input("Y for yes and and N to return to menu.")
           

        

# Function called to search list by Artist            
def searchByArtist(CD_list):

    another = 'Y'
    while another.upper() == "Y":
        searchKey = input("Enter an artist name: ")
        print()
        print("%-35s%-25s%-10s%-10s" % ("Album","Artist","Year","Genre"))

        for i in range(len(CD_list)):
            CD_list[i] = CD_list[i].rstrip('\n')

            #num = random.randint(0, len(CD_list))
            item = CD_list[i]
            itemParts = item.split(',')
            
            album = itemParts[0]
            artist = itemParts[1]
            year = itemParts[2]
            genre = itemParts[3]

            if searchKey.upper() in artist.upper():
                print("%-35s%-25s%-10s%-10s" %(album, artist, year, genre))

        print("Would you like to continue searching or return to the main menu?")
        another = input("Y for yes and and N to return to menu.")
           

# Function called to search list by Year
def searchByYear(CD_list):
    another = 'Y'
    while another.upper() == "Y":
        searchKey = input("Enter a year between 1990 and 1999: ")
        while searchKey < "1990" or searchKey > "1999":
            searchKey =input("ERROR... Please enter a year between 1990-1999: ")
        print()
        print("%-35s%-25s%-10s%-10s" % ("Album","Artist","Year","Genre"))

        for i in range(len(CD_list)):
            CD_list[i] = CD_list[i].rstrip('\n')

            #num = random.randint(0, len(CD_list))
            item = CD_list[i]
            itemParts = item.split(',')
            
            album = itemParts[0]
            artist = itemParts[1]
            year = itemParts[2]
            genre = itemParts[3]

            if year.upper() == searchKey.upper():
                print("%-35s%-25s%-10s%-10s" %(album, artist, year, genre))

        print("Would you like to continue searching or return to the main menu?")
        another = input("Y for yes and and N to return to menu.")

# Function called to search by Genre
def searchByGenre(CD_list):

    another = 'Y'
    while another.upper() == "Y":
        searchKey = input("Enter R&B or HIPHOP to see the list genre: ")
        print()
        print("%-35s%-25s%-10s%-10s" % ("Album","Artist","Year","Genre"))

        for i in range(len(CD_list)):
            CD_list[i] = CD_list[i].rstrip('\n')

            #num = random.randint(0, len(CD_list))
            item = CD_list[i]
            itemParts = item.split(',')
            
            album = itemParts[0]
            artist = itemParts[1]
            year = itemParts[2]
            genre = itemParts[3]

            if genre.upper() == searchKey.upper():
                print("%-35s%-25s%-10s%-10s" %(album, artist, year, genre))

        print("Would you like to continue searching or return to the main menu?")
        another = input("Y for yes and and N to return to menu.")


# Function called to give a random printout from the list
def searchRandom(CD_list):

    another = 'Y'
    while another.upper() == "Y":
        print()
        print("%-35s%-25s%-10s%-10s" % ("Album","Artist","Year","Genre"))

        num = random.randint(0, len(CD_list))

        for i in range(len(CD_list)):
            CD_list[i] = CD_list[i].rstrip('\n')

            if num == i:
                
                item = CD_list[num]
                itemParts = item.split(',')
                
                album = itemParts[0]
                artist = itemParts[1]
                year = itemParts[2]
                genre = itemParts[3]

                
                print("%-35s%-25s%-10s%-10s" %(album, artist, year, genre))
        print("Would you like to continue searching or return to the main menu?")
        another = input("Y for yes and and N to return to menu.")


main()
    


