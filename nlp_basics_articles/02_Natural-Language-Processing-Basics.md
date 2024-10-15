# Natural Language Processing Basics
Here, simple applications and basic concepts used in natural language processing are explained.

**NLP** stands for Natural Language Processing. This is an area of study in which the language humans speak interacts with computing machines. (We call human languages such as English, Japanese, Hindi, etc **natural languages**, as opposed to **programming languages** such as Python, Java, C, etc.) 

NLP has a long history, even before we had huge GPUs and the recent emergence of chatGPT.
One of the earliest methods is called n-grams, where we look for word (string) matches and calculate probabilities so that the computer speaks human language somewhat fluently. Then, we have neural networks that take over the earliest simplest methods as we gain larger computation power. The evolution of neural networks was very rapid; RNN/LSTM represents many developed forms. As we gain so much more computation power thanks to computer architecture developers and the invention of attention models thanks to machine learning researchers, we now have generative models represented by GPT models.
I will dig into n-grams (and their neural network expression), RNN/LSTM, and attention mechanisms in the next article. 
The focus of this article is on **NLP tasks** and **basic concepts**.


## Natural Language Processing Tasks
What do natural language processing models do? What can we do with them? \
**Some of the most common tasks** are next-word prediction, fill-in-the-blank, sentiment classification, language translation, summarization, and Q&A. Each task is illustrated below.

1. **Next-word prediction**: Given a sequence of words, predict what word(s) will come next.
<p align="center">
<img width="633" alt="Screenshot 2024-10-15 at 12 49 36" src="https://github.com/user-attachments/assets/063c4b09-50c9-41e5-8576-cf7483d7e446">
</p>
<p align="center">
Figure 1. Next-word prediction
</p>
<br>
<br>


2. **Fill-in-the-blank**: Given a sequence of words with a blank, predict what word(s) will fill the blank.
<p align="center">
<img width="633" alt="Screenshot 2024-10-15 at 15 12 53" src="https://github.com/user-attachments/assets/9d0ffbc8-4d9b-4c48-b38f-f4bfeb401787">
</p>
<p align="center">
Figure 2. Fill-in-the-blank
</p>
<br>
<br>

3. **Sentiment classification**: Given a text, classify it into types of opinions (happy, unsatisfied, etc) stated.
<p align="center">
<img width="633" alt="Screenshot 2024-10-15 at 15 13 03" src="https://github.com/user-attachments/assets/0adbe38c-9931-42cd-bdd7-124cfdfce379">
</p>
<p align="center">
Figure 3. Sentiment classification
</p>
<br>
<br>

4. **Language translation**: Given a text in a language, translate it into another language.
<p align="center">
<img width="633" alt="Screenshot 2024-10-15 at 15 13 13" src="https://github.com/user-attachments/assets/d5ec2eb7-6d97-46f5-951d-bd39e7930123">
</p>
<p align="center">
Figure 4. Language Translation
</p>
<br>
<br>

5. **Summarization**: Given a text, make it more concise (shorter).
<p align="center">
<img width="712" alt="Screenshot 2024-10-15 at 15 13 27" src="https://github.com/user-attachments/assets/f73a1eed-3520-494c-9877-c681bec5d424">
</p>
<p align="center">
Figure 5. Summarization
</p>
<br>
<br>

6. **Q&A**: Given a question text, answer to the question.
<p align="center">
<img width="712" alt="Screenshot 2024-10-15 at 15 13 39" src="https://github.com/user-attachments/assets/aded9844-38ae-400c-8366-97c46dadd8d2">
</p>
<p align="center">
Figure 6. Q&A
</p>
<br>
<br>

<!---
## Basic concepts in NLP
The basic concepts used in NLP are tokens, 
--->
