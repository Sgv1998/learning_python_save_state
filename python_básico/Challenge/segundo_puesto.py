"""Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given
scores. Store them in a list and find the score of the runner-up.

Input Format

The first line contains. The second line contains an array of integers each separated by a space. """

n=5
arr= [2, 3, 6, 6, 5]

arr_dictionary=set(arr)
arr_sorted=sorted(arr_dictionary)
print(arr_sorted[-2])