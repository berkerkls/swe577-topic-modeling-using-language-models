# Classical Topic Modeling — Survey Notes

**Sources:** LSA, NMF, LDA notes + Towards Data Science comparison article

[What is Topic Modelling? and definitions of Bag of Words and Document Term Matrix concepts](https://www.ibm.com/think/topics/latent-dirichlet-allocation#:~:text=Simply%20put%2C%20LDA%20is%20a,terms%20derived%20from%20those%20documents)
[What is Bag of Words?][https://www.ibm.com/think/topics/bag-of-words]
--- 

## 1. What is Topic Modeling?
> Topic modelling is an unsupervised machine learning technique that scans all the documents and analyzes the engineering patterns of words used in them. By doing this, it groups
> the words of a document into different themes. As a general definition of its process, topic modelling groups words that are used together frequently without naming the concepts of the words.

---

## 2. What is Bag of Words?
> Bag of Words is a frequently used technique in Natural Language Processing (NLP). Simply put, it enables us to compute the words in a document within a vector space and stores all the words in an unstructured way.
> Dimension of the vector space depends on the unique word count in the entire dataset. It is very useful technique for standard text classification, however it has some major limitations such as word correlation, compound words and
> multiple meanings. To give some examples of these limitations:
> Word Correlation: It assumes that words are highly independent. It cannot recognize that "president" and "election" are familiar words.
> Compound Words: It cannot recognize compound words. It evaluates Mr.Berker are seperate words as "Mr" and "Berker".
> Multiple Meanings: Some words have multiple meaning but BoW cannot recognize it because it ignores surronding context around the word.

---

## 3. What is Document-Term Matrix?
> A Document-Term Matrix is a mathematical table or grid used to track and model how often words appear across a collection of documents. We can explain Document Term Matrix as next step
> that is used after Bag of Words. It organizes the extracted data into a better-structured format to enable algorithms, such as the LDA topic model, to process and understand the text.
