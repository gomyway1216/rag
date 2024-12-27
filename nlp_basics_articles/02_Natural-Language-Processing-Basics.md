# Natural Language Processing Basics
Here, simple applications and basic concepts used in natural language processing are explained.

**NLP** stands for Natural Language Processing. This is an area of study in which the language humans speak interacts with computing machines. (We call human languages such as English, Japanese, Hindi, etc **natural languages**, as opposed to **programming languages** such as Python, Java, C, etc.) Here, the focus is on **NLP tasks** and **basic concepts**.


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


## Basic concepts in NLP
The basic concepts used in NLP are tokens, positional encoding, embedding, and encoder/decoder.

### One-hot encoding
This is a way of expressing non-numerical values such as YES/NO, Dog/Cat/Pig/Hedgehog, language vocabulary, etc.

One-hot encoding indicates an element out of all other elements. Examples are as follows:

**YES, NO** \
YES: [1, 0] \
NO: [0, 1] 

**Dog, Cat, Pig, Hedgehog** \
Dog: [1, 0, 0, 0] \
Cat: [0, 1, 0, 0] \
Pig: [0, 0, 1, 0] \
Hedgehog: [0, 0, 0, 1]

**Language Vocabulary** \
(The length of the vector is the number of vocabulary words/sub-words) \
Ant: [1, 0, 0, …, 0, 0] \
Apple:  [0, 1, 0, …, 0, 0] \
Art:  [0, 0, 1, …, 0, 0] \
… \
Zebra:  [0, 0, 0, …, 1, 0] \
Zoo:  [0, 0, 0, …, 0, 1]

Labels are used in supervised learning. They are paired with each element in training/test data.
Labels are represented using one-hot encoding most of the time. The illustration is given below.

<p align="center">
<img width="928" alt="Screenshot 2024-12-26 at 12 42 50" src="https://github.com/user-attachments/assets/1614794b-a982-4ea1-bf19-bce962b6de7e" /> 
</p>
<p align="center">
Figure 7. Label in Image Classification
</p>

<p align="center">
<img width="928" alt="Screenshot 2024-12-26 at 12 43 01" src="https://github.com/user-attachments/assets/88fe417e-ece5-4fa5-9856-53f2f6a72299" />
</p>
<p align="center">
Figure 8. Label in Next-word Prediction
</p>

<p align="center">
<img width="928" alt="Screenshot 2024-12-26 at 12 43 09" src="https://github.com/user-attachments/assets/7999aa16-4226-463c-987a-eef91ae1c940" />
</p>
<p align="center">
Figure 9. Label in Sentiment Classification
</p>


### Tokens
One token of a sequence is generated from a portion of the input sequence, representing the smallest language unit. (Eg: word, sub-word, punctuation) \
They are often represented in one-hot encoding or a representation generated from one-hot encoding or similar vectors.

<!--
### Loss
-->

### String distance
There are several ways to show how distant two strings are to each other. Some of them are explained here.
1. Levenshtein distance
   - Distance between two strings, calculated by the minimum number of single-character edits. The edits are: insert, delete, substitute
2. Dameran-Levenshtein distance
   - In addition to the above, swapping is allowed as one of the operations.
3. Hamming distance
   - This is the distance for the strings of the same length. It is the number of positions that the character is not the same.




