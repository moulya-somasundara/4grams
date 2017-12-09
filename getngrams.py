#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 19:50:59 2017

@author: Moulya
"""

import nltk
from nltk.util import ngrams
import re
from nltk.tokenize import sent_tokenize
from nltk import load
import codecs
from collections import Counter

#function that loads a lexicon of positive words to a set and returns the set
def loadLexicon(fname):
   newLex=set()
   lex_conn= codecs.open(fname, encoding='utf8')
   #add every word in the file to the set
   for sentence in lex_conn:
       newLex.add(sentence.strip())# remember to strip to remove the lin-change character
   lex_conn.close()

   return newLex

# return all the terms that belong to a specific POS type
def getPOSterms(terms,POStags,tagger):
   #print (terms)
   tagged_terms=tagger.tag(terms)#do POS tagging on the tokenized sentence

   POSterms={}
   for tag in POStags:POSterms[tag]=set()

   #for each tagged term
   for pair in tagged_terms:
       for tag in POStags: # for each POS tag 
           if pair[1].startswith(tag): POSterms[tag].add(pair[0])

   return POSterms

def processSentence(sentence,posLex,negLex,tagger):

   noungrams=[]

   terms = nltk.word_tokenize(sentence)#tokenize the sentenc
   #print terms
   fourgrams =ngrams(terms,4) #compute 4-grams

   POStags=['NN'] # POS tags of interest =>Nouns
   #tagged_terms=tagger.tag(terms)#do POS tagging on the tokenized sentence

   POSterms=getPOSterms(terms,POStags,tagger)
   nouns=POSterms['NN']

   for tg in fourgrams:
       #print tg
       if tg[0]=='not' and tg[3] in nouns and (tg[2] in posLex or tg[2] in negLex): noungrams.append(tg) #and (tg[2] in posLex or tg[2] in negLex) and tg[3] in nouns: tg[0]=='not'
       return noungrams

_POS_TAGGER = 'taggers/maxent_treebank_pos_tagger/english.pickle'
tagger = load(_POS_TAGGER)
sentence='not a good idea'
posLex=loadLexicon('positive-words.txt')
negLex=loadLexicon('negative-words.txt')

def getTop3(D):
   Cdict = Counter(D)
   Cdict.most_common()
   for k, v in Cdict.most_common(3):
       print(k)

data = {'a': 2, 'and': 23, 'this': 14, 'only.': 21, 'is': 2, 'work': 2, 'will': 2, 'as': 2, 'test': 4}
getTop3(data)


print (processSentence(sentence,posLex,negLex,tagger))