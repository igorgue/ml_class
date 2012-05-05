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