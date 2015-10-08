

## 0. Copia un texto largo como variable string texto.
texto = """
Founded as a Roman city, in the Middle Ages Barcelona became the capital of the County of Barcelona. After merging with the Kingdom of Aragon, Barcelona continued to be an important city in the Crown of Aragon as an economical and administrative center of this Crown and the capital of the Principality of Catalonia. Besieged several times during its history, Barcelona has a rich cultural heritage and is today an important cultural center and a major tourist destination. Particularly renowned are the architectural works of Antoni Gaudí and Lluís Domènech i Montaner, which have been designated UNESCO World Heritage Sites. The headquarters of the Union for the Mediterranean is located in Barcelona. The city is known for hosting the 1992 Summer Olympics as well as world-class conferences and expositions and also many international sport tournaments.

Barcelona is one of the world's leading tourist, economic, trade fair and cultural centers, and its influence in commerce, education, entertainment, media, fashion, science, and the arts all contribute to its status as one of the world's major global cities. It is a major cultural and economic center in southwestern Europe, 24th in the world (before Zürich, after Frankfurt) and a financial center. In 2008 it was the fourth most economically powerful city by GDP in the European Union and 35th in the world with GDP amounting to €177 billion. In 2012 Barcelona had a GDP of $170 billion; it is leading Spain in both employment rate and GDP per capita change. In 2009 the city was ranked Europe's third and one of the world's most successful as a city brand. In the same year the city was ranked Europe's fourth best city for business and fastest improving European city, with growth improved by 17% per year, but it has since been in a full recession with declines in both employment and GDP per capita, with some recent signs of the beginning of an economic recovery. Since 2011 Barcelona is a leading smart city in Europe. Barcelona is a transport hub with the Port of Barcelona being one of Europe's principal seaports and busiest European passenger port, an international airport, Barcelona–El Prat Airport, which handles above 35 million passengers per year, an extensive motorway network and a high-speed rail line with a link to France and the rest of Europe.
"""

## 1. Normaliza texto: elimina accentos y caracteres estraños y todas minusculas
#Normalizacion
texto = texto.lower()
sentences = texto.strip().split('.')[:-1]

for i in range(len(sentences)):
    sentences[i] = sentences[i].strip().split(' ')

## 2. Estadisticas de palabas
count = {}
for sentence in sentences:
    for word in sentence:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1


## 3. Estadisticas de transicion de palabras (2-gram model)
from sklearn.feature_extraction.text import CountVectorizer


sentences = sentences = texto.strip().split('.')[:-1]
bigram_vectorizer = CountVectorizer(ngram_range=(1,2), min_df=1)
X_2 = bigram_vectorizer.fit_transform(sentences).toarray()


## 4. Using NLTK do a Part of Speech tagging (POS tagging)
tokens = nltk.word_tokenize(sentence)
tagged = nltk.pos_tag(tokens)

## 5. Dibuja un arbol lexico-gramatical con la ayuda de NLTK
from nltk.corpus import treebank

t = treebank.parsed_sents('wsj_0001.mrg')[0]
t.draw()



