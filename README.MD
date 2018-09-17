
# Writing assistance tool

Resume
------

The goal of this project is to implement a writing assistance tool. The project is divided into 3 steps:
* Extraction of n-grams
* Language detection
* Writing assistance (TF-IDF and probability)

___
Execution
---------

Go into the src folder and launch:

    > python3.6 menu.py

___
Results
-------

For more details, you can read the report (French)

Language detection uses statistics, thanks to the n-grams we can detect the language of the document.

    > Ceci est une phrase pour tester la détection de la langue de la phrase.
    < Français
    > This is a sentence to test the language detection of the sentence.
    < Anglais
    > Esta es una oración para probar la detección del idioma de la oración.
    < Espagnol
    
Writing assistance works with the TF-IDF (term frequency-inverse document frequency), probabilities and statistics (using a dataset with 7 million sentences)

    > Je ne me sens vraiment pas très bien, je suis un petit peu triste en ce moment en allant chez 
    < ["j'irai chez moi",  'chez la femme',  'vais chez vous', "j'étais chez moi", 'venez chez moi']
    
    > Trouver l'itineraire de Paris a Pointoise en prenant la voiture electriq
    < électrique
