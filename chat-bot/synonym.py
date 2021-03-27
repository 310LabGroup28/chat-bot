from nltk.corpus import wordnet

class SynonymReplacer(object):
	def replaceSynonyms(question):
		for word in question.split():
			for syn in wordnet.synsets(word):
				for l in syn.lemmas():
					if(l.name() == "weather"):
						question = question.replace(word, "weather")

					if(l.name() == "distance"):
						question = question.replace(word, "distance")

					if(l.name() == "time"):
						question = question.replace(word, "time")

		return question
