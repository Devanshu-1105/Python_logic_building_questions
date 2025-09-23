# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.



n = int(input().strip()) #takes the userinput and strips the extra spaces around it.
scores = list(map (int, input().split())) #takes the input splits the string into smaller strings ,map will apply int to every item in the list turns each string to a integer.
unique_scores = sorted(set(scores)) #converts the scores where duplicates are removed and sorts it in order
print(unique_scores[-2])
