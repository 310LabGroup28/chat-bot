# ------------------------ POS tagging

from nltk import word_tokenize
from nltk import StanfordTagger
import nltk
import re
from spellchecker import SpellChecker
from textblob import TextBlob

class SpellCheckPosTag(object):

    # remove punctuations from unicode string except apostrophe
    # split sentence as words / tokenization
    def word_token(sentence):
      #text_tok = nltk.word_tokenize(text_example)
      sentence = re.sub(r"[^\w\d'\s]+",'',sentence)
      #print(sentence)
      words = sentence.split(' ')
      return words
     
    """
    # all tags with the abbreviations
    CC :	 conjunction, coordinating
    CD :	 numeral, cardinal
    DT :	 determiner
    EX :	 existential
    FW :	 foreign word
    IN :	 preposition
    JJ :	 adjective
    LS :	 list marker
    MD :	 modal auxiliary
    NN :	 noun
    PDT :	 pre-determiner
    POS :	 genitive marker
    PR :	 pronoun
    RB :	 adverb
    RP :	 particle
    SYM :	 symbol
    UH :	 interjection
    VB :	 verb
    WDT :	 WH-determiner
    WP :	 WH-pronoun
    WRB :	 Wh-adverb

    #nltk.help.upenn_tagset()
    # to print out all tag-set
    """
    # pos-tagging all words
    def pos_tagging(sentence):
      # there are different tags as above when using Stanford toolkit
      tags = {'CC': 'conjunction, coordinating', 'CD': 'numeral, cardinal', 'DT': 'determiner', 'EX': 'existential', 'FW': 'foreign word', 'IN': 'preposition', 'JJ': 'adjective', 'LS': 'list marker', 'MD': 'modal auxiliary', 'NN': 'noun', 'PDT': 'pre-determiner', 'POS': 'genitive marker', 'PR': 'pronoun', 'RB': 'adverb', 'RP': 'particle', 'SYM': 'symbol', 'TO': 'preposition or infinitive marker', 'UH': 'interjection', 'VB': 'verb', 'WD': 'WH-determiner', 'WP': 'WH-pronoun', 'WR': 'Wh-adverb'}
      words = SpellCheckPosTag.word_token(sentence)
      pos_tagged = nltk.pos_tag(words)
      dic = {}
      for w, tag in pos_tagged:
        tag = tag[:2]
        dic[w] = tags[tag]
      return dic

    #text_example = "Avengers: Endgame is a 2019 American superhero film based on the Marvel Comics superhero team the Avengers, produced by Marvel Studios and distributed by Walt Disney Studios Motion Pictures. The movie features an ensemble cast including Robert Downey Jr., Chris Evans, Mark Ruffalo, Chris Hemsworth, and others. (Source: wikipedia)."
    #pos_tagging(text_example)


    # ------------------------ spelling check


    def check_spelling(sentence):
      spell = SpellChecker()
      words = SpellCheckPosTag.word_token(sentence)
      mistakes = spell.unknown(words)
      dic = {}
      for w in mistakes:
        # spell.candidates(w)
        dic[w] = spell.correction(w)
      return dic
     
    def check_spelling_update(sentence):
      newSentence = sentence
      words = SpellCheckPosTag.word_token(sentence)
      dic = {}
      for w in words:
        cor = TextBlob(w)
        nw = cor.correct()
        nw = str(nw)    
        if nw!=w:
          newSentence = newSentence.replace(w, nw)
      return newSentence

    def check(sentence):
      d1 = check_spelling(sentence)
      d2 = check_spelling_update(sentence)
      dic = {}
      for w in d1:
        dic[w] = d1[w]
      for w in d2:
        dic[w] = d2[w]
      return dic  

    # find those words that may be misspelled
    #sentence = 'something is hapenning here, what do you abl about taht'
    #check_spelling(sentence)
    #check_spelling_update(sentence)
    #print(check('how fra is it from new yokr to london'))
    #print(pos_tagging('how fra is it from new yokr to london'))