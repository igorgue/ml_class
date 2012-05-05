ML Master Class
===============

This is my code for **An Introduction to Machine Learning with Web Data** by **Hilary Mason**

## Classifying Web Documents

### NYTimes API

Searching it:

	http GET http://api.nytimes.com/svc/search/v1/article\?query\=jazz\&api-key\=####

This is supervised learning, we provide some known labels so we can guest what labels belong to other training data we want to predict.
	
Use Naive Bayes to predict what kind of article is certain article.

#### Naive Bayes Algorithm

    	    ab
	-------------------
	ab + (1 - a)(1 - b)


    		 (.60)(.72)
	-------------------------------
	(.60)(.72) + (1 - .60)(1 - .72)

#### Stemming

Reduce words to linguistic stems. It can be used instead of complex natural language analysis.

	program = programming = programmer
	
#### Wordnet

Lexical database every word in english is in wordnet. And it can decide if something can be used as a noun or not, or a verb or not. You can use the Wordnik API for increasing your data set.

#### K Nearest Neighbors

Metaphor of distance. Find the K nearest points near an unlabeled point and infer the label.

- Good for image analysis
- Face recognition
- If you can imagine it in space then you can use it
- Anything you can plot

Euclidean distance, good algorithm.

#### SVM

Support Vector Machine calculates a divided hyperbole between two sets.

libsvm, is a good library.

#### Boosting

Take week learners and make them stronger by combining them.

#### Active Learning

User a classifier to label items that we understand.

Bring unknown items to an alternative system for labeling.

Re-train classifiers.