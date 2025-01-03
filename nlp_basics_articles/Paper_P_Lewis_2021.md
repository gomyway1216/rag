# Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks

Patrick Lewis, Ethan Perez, Aleksandra Piktus, Fabio Petroni, Vladimir Karpukhin, Naman Goyal, Heinrich Küttler, Mike Lewis, Wen-tau Yih, Tim Rocktäschel, Sebastian Riedel, Douwe Kiela

[Submitted on 22 May 2020 (v1), last revised 12 Apr 2021 (this version, v4)]

Issue #78
Link to the paper: https://arxiv.org/abs/2005.11401


## Abstract
> Large pre-trained language models have been shown to store factual knowledge in their parameters, and achieve state-of-the-art results when fine-tuned on downstream NLP tasks. However, their ability to access and precisely manipulate knowledge is still limited, and hence on knowledge-intensive tasks, their performance lags behind task-specific architectures. Additionally, providing provenance for their decisions and updating their world knowledge remain open research problems. Pre-trained models with a differentiable access mechanism to explicit non-parametric memory can overcome this issue, but have so far been only investigated for extractive downstream tasks. We explore a general-purpose fine-tuning recipe for retrieval-augmented generation (RAG) -- models that combine pre-trained parametric and non-parametric memory for language generation. We introduce RAG models where the parametric memory is a pre-trained seq2seq model and the non-parametric memory is a dense vector index of Wikipedia, accessed with a pre-trained neural retriever. We compare two RAG formulations, one which conditions on the same retrieved passages across the whole generated sequence, and the other can use different passages per token. We fine-tune and evaluate our models on a wide range of knowledge-intensive NLP tasks and set the state-of-the-art on three open domain QA tasks, outperforming parametric seq2seq models and task-specific retrieve-and-extract architectures. For language generation tasks, we find that RAG models generate more specific, diverse and factual language than a state-of-the-art parametric-only seq2seq baseline.

## Highlights of this research
- Proposed RAG models that use both parametric memory and non-parametric memory (RAG-Sequence model, RAG-Token model)
    - Parametric: Feed **specific dataset** for the model to learn
    - Non-parametric: Feed **general dataset** for the model to learn (Wikipedia dump in this paper)
    - The retriever of the model has non-parametric memory, and the generator of the model has parametric memory
- Experimented on several benchmarks
- Proposed models perform better than the SoTA methods

## RAG (Retrieval-Augmented Generation)
The RAG model used in this paper is illustrated in Figure 1.
<p align="center">
    <img width="600" alt="Screenshot 2024-12-02 at 01 06 08" src="https://github.com/user-attachments/assets/7fef3192-51dc-44b2-a2ed-11d0e2920aec">
</p>
<p align="center">
Figure 1. RAG
</p>

Components in the model architecture:
- Input (Query): Input to the model. (Question in QA task.)
- Retriever: Retrieves relevant information from the database based on the input.
- Database: Stores all given documents.
- Documents: Subset of documents. $k$ documents are retrieved to be fed to the generator. (Also known as chunks in other works)
- Previous tokens: Outputs from the model that was produced before this iteration. (Incomplete sentence)
- Generator: Generates a current token based on given Documents, Input, and Previous tokens.
- Current Token: Output from the generator. (A token following the incomplete sentence)

## Proposed models and their architecture
The authors propose two models: RAG-Sequence model and RAG-Token model. 
They both have basically the same structure. The only difference is in how they make current token candidates and how they marginalize them. 
**RAG-Sequence model** use the same document to predict each target token (current token).
**RAG-Token model** predict each target token based on a different document.

The difference between the two models is illustrated in Figure 2.

<p align="center">
    <img width="904" alt="Screenshot 2024-12-02 at 00 39 30" src="https://github.com/user-attachments/assets/9089bb04-9259-4768-a7a9-c89044b44cde">
</p>
<p align="center">
Figure 2. The difference between RAG-Sequence model and RAG-Token model
</p>

### Retriever: DPR (Dense Passage Retrieval)
- **Non-parametric model**
- BERT (Bidirectional Encoder Representations from Transformers) is used for encoding.
- It **retrieves relevant information** from the database based on the input. The relevance is how similar the input and a document in the database are, based on the inner product between encoded input and encoded documents (more similar when the inner product is larger).
    - $P_{\eta}(z|x) \propto \exp(\textbf{d}(z) ^\top \textbf{q}(x))$ 
    - $\textbf{d}(z) = BERT_{a}(z)$
    - $\textbf{q}(x) = BERT_{q}(x)$
    - $x$ is input, $z$ is document
- Retrieve $k$ most related documents ($k \in {5, 10}$) **using a neural model**.
    - The process of looking for $k$ most related documents is called the Maximum Inner Product Search (MIPS) problem.  
    - In this paper, an efficient method of solving the MIPS problem is used. (The method: https://arxiv.org/abs/1702.08734)
    - The retrieving model is trainable because it is based on a neural model. The pre-trained weights are used for initial weights.
    - This retrieving model refers to the non-parametric model in this paper.
    - The retrieving model is trained together with the generator. It is trained so that the performance of retrieval from the given specific information improves.

### Generator: BART (Bidirectional and Auto-Regressive Transformers)
- **Parametric model**
- Uses a variant of BART called **BART-large**
    - BART-large is a pre-trained seq2seq transformer model
- Produces $P_{\theta}(y_{i} | x, z, y_{1,...,i-1})$, which is used for getting current token.
    - $y_{i}$ is current token following previous tokens $y_{1,...,i-1}$
- Input $x$ and documents $z$ are simply concatenated when they are fed to the generator.

### Training
- Retriever and Generator are trained together.
- Objective function: $Minimize ( \sum_{j} -\log p(y_{j} | x_{j}))$
    - intuition: Increase the likelihood of one correct option 
- Stochastic Gradient Descent: get a gradient
- Adam (Adaptive Moment Estimation): move in the direction of the gradient with momentum
- By the way, fine-tuning the document encoder is very expensive, so fine-tune only the query encoder and the generator.

### Decoding
- For RAG-Token model, use standard beam decoder
- For RAG-Sequence model, beam search for each document
<!-- didn't clearly understand this section-->


##  Experiments and Results
Experiments are done on various knowledge-intensive tasks.

### Open-domain Question Answering (QA)
- QA benchmark datasets
    - Natural Questions (NQ)
    TriviaQA (TQA)
    WebQuestions (WQ)
    CuratedTrec (CT)
- Inputs and Outputs
    - Questions as input $x$
    - Answers as predicted output $y$
- Comparison Models
    - Closed book models (no document retrieval. rely only on the parametric dataset, the specific dataset) 
        - T5-11B
        - T5-11B + SSM
    - Open book models (rely only on the non-parametric dataset, the general dataset)
        - REALM
        - DPR
    - Proposed models
        - RAG-Token
        - RAG-Sequence
- Evaluation metrics
    - Exact Match (EM) scores

<p align="center">
    <img width="400" alt="Screenshot 2024-12-02 at 03 12 17" src="https://github.com/user-attachments/assets/c67b7775-2b36-40a9-8924-a3887578a821">
</p>

As shown in the table above, **proposed RAG models gave the best results** in all cases except for the TQA task. The proposed methods are better also because it does not require pre-training that is as expensive as other models.
Also, the proposed RAG models had some capacity to give correct answers even when the correct answer was not given in the documents.


### Abstractive Question Answering
- Benchmark Dataset
    - MSMARCO NLG task v2.1
- Inputs and Outputs
    - Questions as input $x$
    - Answers as predicted output $y$
    - (gold passage is provided in the dataset, but it is not used. Gold passage is specific information for one to answer the question.)
- Comparison Models
    - SoTA
    - BART
    - Proposed models
        - RAG-Token
        - RAG-Sequence
- Evaluation metrics
    - R-L: Rouge-L points
    - B-1: Bleu points

<p align="center">
    <img width="400" alt="Screenshot 2024-12-02 at 03 12 24" src="https://github.com/user-attachments/assets/959d7ce6-574e-4a2a-b892-c82dee40a3e5">
</p>

As shown in the middle columns in Table 2, the proposed RAG models are not as good as SoTA models but it is approaching. However, the proposed models are performing well considering that SoTA models have access to gold passages.
The authors also saw that **RAG models have fewer hallucinations**.

### Jeopardy Question Generation
The task is to generate a question for jeopardy given an answer. This is a new task.
- Benchmark dataset
    - SearchQA
- Inputs and Outputs
    - Answers as input $x$
    - Jeopardy questions as output $y$
- Comparison Models
    - BART
    - Proposed models
        - RAG-Token
        - RAG-Sequence
- Evaluation metrics
    - B-1: Bleu points
    - QB-1: SQuAD-tuned Q-BLEU-1 points
    - human evaluations
        - factuality: are there trusted sources behind the output?
        - specificity: high mutual difference between the input and output

As shown in the first two columns in Table 2, the proposed RAG-Token model is outperforming. Also, the human evaluations say that the RAG models had much more factuality and specificity compared to the BART model.
RAG models likely outperformed because Jeopardy questions require two different pieces of information about the answer and the structure of RAG where we retrieve documents matched the style.

### Fact Verification
The task is to classify a natural language claim into:
- Supported in Wikipedia
- Refuted in Wikipedia
- insufficient information to judge

Classifying into all three is called a 3-way classification task, and classifying into only supported or refuted is called a 2-way classification task.

- Benchmark dataset
    - FEVER3 (3-way classification)
    - FEVER2 (2-way classification)
- Inputs and Outputs
    - natural language claim as input $x$
    - classes as output $y$
- Comparison Models
    - SoTA
    - BART
    - Proposed models
        - RAG-Token
        - RAG-Sequence
- Evaluation metrics
    - label accuracy

As we can see in the last two columns in Table 2, RAG models are not greatly worse compared to the other models. However, RAG models do not require complex pipeline systems, domain-specific architectures, a lot of tuning, and heavy supervision, and yet it is not much worse off. RAG was able to retrieve the supporting Wikipedia documents with high probability. 

### Additional Experiments and Results
- Generation Diversity
    - Responses from RAG models had more diversity in writing. The ratio/number of tri-grams was higher than the BART model. 
- Retrieval Ablations
    - Froze the retrieval learning of the model; the weights of the retrieval model do not get updated throughout the training period. The results were worse than when it was not frozen. Learning in retrieval also helps the RAG models perform well.
- Index hot-swapping
    - Just by swapping the documents in the database (the non-parametric memory), RAG models were able to keep up with the updates.
- Effect of Retrieving more documents
    - There was no significant difference between when $k$ is $5$ or $10$. The peak or a good convergence point was at $10$, so keeping it around this value would be suggested.

## Mathematical Terms
### Mariginalize
#### Marginalizing is combining several probabilities into one probability.

P(α) being the probability of α, marginalizing is represented as:
<p align="center">
<img width="280" alt="Screenshot 2024-12-22 at 12 23 15" src="https://github.com/user-attachments/assets/5d4ebb82-580e-4073-b45b-deb873a2c66e" />


For example, 
There are 10 fruits. 
- 3 green apples
- 5 red apples
- 2 oranges
  
Here, we know that the probability of blindly picking a fruit of a kind is
- P(green apple) = 0.3
- P(red apple) = 0.5
- P(orange) = 0.2

Marginalizing is
- P(apple)
 = P(green apple) + P(red apple)
 = 0.3 + 0.5
 = 0.8

(reference: https://towardsdatascience.com/probability-concepts-explained-marginalisation-2296846344fc)

#### How marginalizing is used in the context of this paper is as follows.
Intuitively, one token is inferred by combining candidates of tokens. Marginalizing is possible because the tokens are represented in probability (like Softmax).
<!-- I don't have the deepest understanding.. :'( But I'm sure this is what they mean intuitively. -->

A paper nicely explains marginalization in the context of NLP: https://aclanthology.org/2020.emnlp-main.255/

<kbd>
<img width="427" alt="Screenshot 2024-12-22 at 12 40 43" src="https://github.com/user-attachments/assets/577fc02a-ad1f-493d-b548-a675c9f99afe" />
<img width="427" alt="Screenshot 2024-12-22 at 12 44 28" src="https://github.com/user-attachments/assets/46106fc5-307f-4c59-95a0-7e2c5e6a9241" />
</kbd>




