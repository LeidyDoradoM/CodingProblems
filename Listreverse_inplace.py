# write a function that takes a list of characters and reverses the letter in place 

# In a greedy approach, we can loop through the list and switch the current first and last 
# characters at each iteration; and then update the first and last positions. I am using a temp
# variable to save the first character and then place it to the last position.
def reverse(list_of_chars,start_idx,end_idx):
    while start_idx < end_idx:
        temp = list_of_chars[start_idx]
        list_of_chars[start_idx] = list_of_chars[end_idx]
        list_of_chars[end_idx] = temp
        start_idx = start_idx+1
        end_idx = end_idx-1
#for further use of this function, we can add as input variables the first and last indeces, so
#we have the flexibility to reverse only one portion of the list, if desired
#--- there is not return because the reversed chars are in the same input variable ---


# Second problem related to the previous function:
# You're working on a secret team solving coded transmissions.  Your team is scrambling to decipher
# a recent message, worried it's a plot to break into a major European National Cake Vault. The
# message has been mostly deciphered, but all the words are backward! Your colleagues have handed
# off the last step to you. Write a function reverse_words() that takes a message as a list of
# characters and reverses the order of the words in place.

# We can use twice the above function, first for reversing all the characters in the message, and
# for reversing each word.  For example: message = ['c','a','k','e','','i','s','','t','h','i','s']
# after the first reversing, we got ->['s','i','h','t','','s','i','','e','k','a','c'], and after
# reversing each word: ['t','h','i','s','','i','s','','c','a','k','e'].
# when reversing each word, we need to keep track of ''(space) that are the separators of words,
# in order to get the indices i and n that we need to interchange positions of the letters.
def reverse_words(message):
    reverse(message,0,len(message)-1) #reversing all from 0 to the length of the message
    str_i = 0
    for end_i in range(0,len(message)):
        item = message[end_i]
        if (item == ' '):
            reverse(message,str_i,end_i-1)
            str_i = end_i+1
        if (end_i == len(message)-1):
            reverse(message,str_i,end_i)

message = list('yummy is cake bund chocolate')
reverse_words(message)
print(message)