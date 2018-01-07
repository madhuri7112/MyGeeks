#Find the smallest window in a string containing all characters of another string

#http://www.geeksforgeeks.org/find-the-smallest-window-in-a-string-containing-all-characters-of-another-string/

"""
Given two strings string1 and string2, find the smallest substring in string1 containing all characters of string2 efficiently.
For Example:

Input :  string = "this is a test string"
         pattern = "tist"
Output :  Minimum window is "t stri"
Explanation: "t stri" contains all the characters
              of pattern.

Input :  string = "geeksforgeeks"
         pattern = "ork" 
Output :  Minimum window is "ksfor"
"""

def  main():
   find_smallest_window("adobecodebanc", "abc")

def  find_smallest_window(testString, pattern):
     pattern_hash = {}
     for c in range(ord('a'), ord('z')):
        pattern_hash[chr(c)] = 0

     for c in pattern:
         pattern_hash[c] = 1


     start_index = 0
     end_index = 0
     matched_characters = 0
     min_length = len(testString) + 1   #So that this is the max
     pattern_length = len(pattern)

     while(1):
         
          if (matched_characters == pattern_length):
                window_length = end_index - start_index
                if (window_length < min_length):
                     min_length = window_length
                if (pattern_hash[testString[start_index]] == 2):
                         matched_characters = matched_characters - 1
                         pattern_hash[testString[start_index]] = pattern_hash[testString[start_index]] -1
                start_index = start_index + 1
          else:
                if (end_index == len(testString) ):
                      break
                if (pattern_hash[testString[end_index]] !=0):
                      if (pattern_hash[testString[end_index]] == 1):
                           matched_characters = matched_characters + 1
                      pattern_hash[testString[end_index]] = pattern_hash[testString[end_index]] + 1
                end_index = end_index + 1

     print min_length

main()
