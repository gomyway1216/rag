# Chunk Size

Here, we discuss how we **determine a right chunk size** for our project.

## What is chunk size?
Chunk size is the **length of the string sequence that we divide the source documents into**. It varies depending on the purpose, application, language, the size of the source documents, and other factors. Chunk sizes are often in **letters, words, sentences, paragraphs, and documents**.

**The unit of the piece of data that is stored into the database** is the chunk size. 
- **Larger chunks** allow the embedding mechanism to capture a **bigger picture** of the text and **saves memory** space in the database because we get less number of chunks from the source documents given that the embedded chunk size is constant. However, it is prone to **missing small details**, leading to a vague response to a query.
- **Smaller chunks** allow the embedding mechanism to **capture the text more granulary**. However, it uses a lot of memory space in the database because we have more number of chunks from the source documents, given that the embedded chunk size is constant. This also makes the **search harder**.


## Resources
- Free diary text from Helen Keller:
Helen Keller's journal: https://www.gutenberg.org/files/2397/2397-h/2397-h.htm
This book is now public domain because the author died in 1968 and it's been more than 55 years since then. It is more like storytelling in the beginning, but it gets more like a diary towards the end of the book. We can make good use of the latter part of the book because she has many life issues and complaints, as well as solutions sometimes.
- Sentence/Paragraph splitter Python library:

## Our method
We use Chapter XX from Helen Keller's journal. We feed one chapter to the database. The chapter is divided into different sizes of chunks:
- 1 sentence
- 2 sentences
- 5 sentences
- 10 sentences
- 1 paragraph

Then, we ask 15 text-related questions that is handcrafted by Carolina. (Carolina is writing this document, btw!)

Lastly, we read the response to the questions from our RAG model and determine which chunk size gives the best reponse. The best is decided by our intuition.

Here is a part of her text:
>  I remember my first day at Radcliffe. It was a day full of interest for me. I had looked forward to it for years. A potent force within me, stronger than the persuasion of my friends, stronger even than the pleadings of my heart, had impelled me to try my strength by the standards of those who see and hear. I knew that there were obstacles in the way; but I was eager to overcome them. I had taken to heart the words of the wise Roman who said, "To be banished from Rome is but to live outside of Rome." Debarred from the great highways of knowledge, I was compelled to make the journey across country by unfrequented roads—that was all; and I knew that in college there were many bypaths where I could touch hands with girls who were thinking, loving and struggling like me.

Here are the questions:
> - On what year did the author start college?
> - How did the author feel when she joined the college?
> - Was the author disappointed when she faced the reality of college?
> - Why did the author think that there is no enough time when she joined college?
> - What did the author study in her first year?
> - How much was the author able to concentrate to the lecture compared to her peers?
> - In one word, what does the author use to write down? Was this important to her?
> - What makes her jealous about other girls?
> - What did the author like about the composition class in her second year?
> - How does the author like to enjoy literature works?
> - What does the author mean when she says "overtaxed mind cannot enjoy the treasure it has secured at the greatest cost"?
> - What is Huss an example of?
> - How did the author feel when she took an exam?
> - What is one lesson that the author learned through attending college?
> - What should the author do to improve her life?