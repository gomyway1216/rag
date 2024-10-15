# Natural Language Processing Basics
Here, I explain how natural language processing works in the most basic form. 

**NLP** stands for Natural Language Processing. This is an area of study in which the language humans speak interacts with computing machines. (We call human languages such as English, Japanese, Hindi, etc **natural languages**, as opposed to **programming languages** such as Python, Java, C, etc.) 

NLP has a long history, even before we had huge GPUs and the recent emergence of chatGPT.
One of the earliest methods is called n-grams, where we look for word (string) matches and calculate probabilities so that the computer speaks human language somewhat fluently. Then, we have neural networks that take over the earliest simplest methods as we gain larger computation power. The evolution of neural networks was very rapid; RNN/LSTM represents many developed forms. As we gain so much more computation power thanks to computer architecture developers and the invention of attention models thanks to machine learning researchers, we now have generative models represented by GPT models.

I will dig into **n-grams** (and their neural network expression), **RNN/LSTM**, and **attention mechanisms** in this article.


## Natural Language Processing Tasks
What do natural language processing models do? What can we do with them? \
Some of the most common tasks are: 
- next word prediction: Given a sequence of words, predict what word(s) will come next.
- fill in the blank: Given a sequence of words with a blank, predict what word(s) will fill the blank.
- sentiment classification: Given a text, classify it into types of opinions (happy, unsatisfied, etc) stated.
- language translation: Given a text in a language, translate it into another language.
- summarization: Given a text, make it more concise (shorter).
- Q&A: Given a question text, answer to the question.
- text generation: Create texts.

<p align="center">
<img width="633" alt="Screenshot 2024-10-15 at 12 49 36" src="https://github.com/user-attachments/assets/063c4b09-50c9-41e5-8576-cf7483d7e446">
</p>
<p align="center">
Figure 1. Illustration of next word prediction using a language model
</p>
