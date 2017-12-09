# 4grams

The program defines the following functions

a. processSentence(sentence,posLex,negLex,tagger):  The parameters of this function are a sentence (a string), a set positive words, a set of negative words, and a POS tagger.  The function returns a list with all the 4-grams in the sentence that have the following structure:                                                   

not <any word> <pos/neg word> <noun>. 

For example: not a good idea


b. getTop3(D): The only parameter of this function is a dictionary D.  All the values in the dictionary are integers. The function returns a list of the keys with the 3 largest values in the dictionary.

 
