#!/usr/bin/env python3

# The Hash Slinging Slasher!
# A python script which hashes a file using one of three algorithims.
# Written by Brian T. Carr
# briantcarr.com
# brian@briantcarr.com

# BE SURE TO DOWNLOAD THE HASHLIB METHOD PRIOR TO RUNNING THE SCRIPT
# BE SURE TO RUN THIS FILE IN THE SAME DIRECTORY WHICH THE FILE YOU WISH TO HASH IS LOCATED.
# OTHERWISE YOU MAY HAVE TO SPECIFY FILE PATH 


import hashlib
import sys

def md5_hash_it():
    hasher = hashlib.md5()

    selected_file = input("Please enter the file you wish to hash...: ")

    with open (selected_file) as afile:
        buf = afile.read()
        hasher.update(buf.encode('utf-8'))
    print("The MD5 hash value of", selected_file, "is", hasher.hexdigest())

def sha256_hash_it():
    hasher = hashlib.sha256()

    selected_file = input("Please enter the file you wish to hash...: ")

    with open (selected_file) as afile:
        buf = afile.read()
        hasher.update(buf.encode('utf-8'))
    print("The SHA256 hash value of", selected_file, "is", hasher.hexdigest())

def sha1_hash_it():
    hasher = hashlib.sha1()

    selected_file = input("Please enter the file you wish to hash...: ")

    with open (selected_file) as afile:
        buf = afile.read()
        hasher.update(buf.encode('utf-8'))
    print("The SHA1 hash value of", selected_file, "is", hasher.hexdigest())
#Select hash function
add_file = input("Would you like to hash a file?(Y/N): ")
while add_file == "Y":
    print("Available hash algorithms, 1: MD5   2: SHA256    3: SHA1")
    hash_type = input("Which hash algorithm would you like to use?: ")
    print("you have selected:", hash_type)
    if hash_type == "1":
        md5_hash_it()
        add_file = input("Would you like to hash a file?(Y/N): ")
    elif hash_type == "2":
        sha256_hash_it()
        add_file = input("Would you like to hash a file?(Y/N): ")
    elif hash_type ==  "3":
        sha1_hash_it()
        add_file = input("Would you like to hash a file?(Y/N): ")
    else: 
        print("Please enter a valid choice...")
        sys.exit()
#for when they dont want to hash a file        
else:
    print("See you soon!")
    sys.exit()

