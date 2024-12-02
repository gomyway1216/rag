# Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks

Patrick Lewis, Ethan Perez, Aleksandra Piktus, Fabio Petroni, Vladimir Karpukhin, Naman Goyal, Heinrich Küttler, Mike Lewis, Wen-tau Yih, Tim Rocktäschel, Sebastian Riedel, Douwe Kiela

[Submitted on 22 May 2020 (v1), last revised 12 Apr 2021 (this version, v4)]

Issue #78
Link to the paper: https://arxiv.org/abs/2005.11401


## Abstract
> Large pre-trained language models have been shown to store factual knowledge in their parameters, and achieve state-of-the-art results when fine-tuned on downstream NLP tasks. However, their ability to access and precisely manipulate knowledge is still limited, and hence on knowledge-intensive tasks, their performance lags behind task-specific architectures. Additionally, providing provenance for their decisions and updating their world knowledge remain open research problems. Pre-trained models with a differentiable access mechanism to explicit non-parametric memory can overcome this issue, but have so far been only investigated for extractive downstream tasks. We explore a general-purpose fine-tuning recipe for retrieval-augmented generation (RAG) -- models which combine pre-trained parametric and non-parametric memory for language generation. We introduce RAG models where the parametric memory is a pre-trained seq2seq model and the non-parametric memory is a dense vector index of Wikipedia, accessed with a pre-trained neural retriever. We compare two RAG formulations, one which conditions on the same retrieved passages across the whole generated sequence, the other can use different passages per token. We fine-tune and evaluate our models on a wide range of knowledge-intensive NLP tasks and set the state-of-the-art on three open domain QA tasks, outperforming parametric seq2seq models and task-specific retrieve-and-extract architectures. For language generation tasks, we find that RAG models generate more specific, diverse and factual language than a state-of-the-art parametric-only seq2seq baseline.

## Highlights of this research
- Proposed RAG models that uses both parametric memory and non-parametric memory (RAG-Sequence model, RAG-Token model)
    - Parametric: Feed **specific dataset** for the model to learn
    - Non-parametric: Feed **general dataset** for the model to learn (Wikipedia dump in this paper)
- Experimented on several benchmarks
- Proposed models perform better than the SoTA methods

## RAG (Retrieval-Augumented Generation)
The RAG model used in this paper is illustrated as Figure 1.
<p align="center">
    /insert a figure here
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
- Generator: Generates a current token based on given Documents, Input, and Previous tokens..
- Current Token: Output from generator. (A token following the incomplete sentence)

## Proposed models and their architecture
The authors propose two models: RAG-Sequence model and RAG-Token model. 
They both have basically the same structure. The only difference is in how they make current token candidates and how they marginalize them. 
**RAG-Sequence model** use the same document to predict each target token (current token).
**RAG-Token model** predict each target token based on a different document.

The difference between two models are illustrated in Figure 2.

<p align="center">
    /insert a figure here
</p>
<p align="center">
Figure 2. The difference between RAG-Sequence model and RAG-Token model
</p>

### Retriever: DPR (Dense Passage Retrieval)
- **Non-parametric model**
- BERT (Bidirectional Encoder Representations from Transformers) is used for encoding.
- It **retrieves relevant information** from the database based on the input. The relevance is how similar the input and a document in the database are, based on the inner-product between encoded input and encoded documents (more similar when inner-product is larger).
    - $P_{\eta}(z|x) \propto \exp(\textbf{d}(z) ^\top \textbf{q}(x))$ 
    - $\textbf{d}(z) = BERT_{a}(z)$
    - $\textbf{q}(x) = BERT_{q}(x)$
    - $x$ is input, $z$ is document
- Retrieve $k$ most related documents ($k \in {5, 10}$)

### Generator: BART (Bidirectional and Auto-Regressive Transformers)
- **Parametric model**
- Uses a variant of BART called **BART-large**
    - BART-large is a pretrained seq2seq transformer model
- Produces $P_{\theta}(y_{i} | x, z, y_{1,...,i-1})$, which is used for getting current token.
    - $y_{i}$ is current token following previous tokens $y_{1,...,i-1}$
- Input $x$ and documents $z$ are simply concatenated when they are fed to genetator.

### Training
- Retriever and Generator are trained together.
- Objective function: $Minimize ( \sum_{j} -\log p(y_{j} | x_{j}))$
    - intuition: Increase the likelihood of one correct option 
- Stochastic Gradient Descent: get gradient
- Adam (Adaptive Moment Estimation): move in the direction of gradient with momentum
- By the way, fine-tuning the document encoder is very expensive, so fine-tune only query encoder and generator.

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
    - Open book models (rely only on non-parametric dataset, the general dataset)
        - REALM
        - DPR
    - Proposed models
        - RAG-Token
        - RAG-Sequence
- Evaluation metrics
    - Exact Match (EM) scores

<p align="center">
    /insert Table 1 from the paper here
</p>

As shown on the table above, **proposed RAG models gave best results** in all cases except for TQA task. The proposed methods are better also because it does not require pre-training that is as expensive as other models.
Also, proposed RAG models had some capacity to respond correct answers even when the correct answer was not given in the documents.


### Abstractive Question Answering
- Benchmark Dataset
    - MSMARCO NLG task v2.1
- Inputs and Outputs
    - Questions as input $x$
    - Answers as predicted output $y$
    - (gold passage is provided in the dataset, but it is not used. gold passage is specific information for one to answer the question.)
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
    /insert Table 2 from the paper here
</p>

As shown in the middle columns in Table 2, proposed RAG models are not as good as SoTA models but it is approaching. However, the proposed models are performing well considering that SoTA models have access to gold passages.
The authors also saw that **RAG models has less hallucinations**.

### Jeopardy Question Generation
The task is to generate a question for jeopardy, given an answer. This is a new task.
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
        - factuality: is there trusted source behind the output?
        - specificity: high mutual difference between the input and output

As shown in the first two columns in Table 2, proposed RAG-Token model is outperformirng. Also, the human evaluations says that the RAG models had much more factuality and specificity comapred to BART model.
RAG models likely outperformed because Jeopardy questions require two different pieces of information about the answer and the structure of RAG where we retrieve documents matched the style.

### Fact Verification
The task is to classify a natural language claim into:
- Supported in Wikipedia
- Refuted in Wikipedia
- no enough information to judge

Classifying into all three is called 3-way classification task, and classifying into only supported or refuted is called 2-way classification task.

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

As we can see on the last two columns in Table 2, RAG models are not greatly worse compared to the other models. However, RAG models does not require complex pipeline systems, domain-specific architectures, a lot of tuning, and heavy supervision and yet it is not much worse off. RAG was able to retrieve the supporting wikipedia documents in high probability. 

### Additional Experiments and Results
- Generation Diversity
    - Responses from RAG models had more diversity in writing. The ratio/number of tri-grams were higher than BART model. 
- Retrieval Ablations
    - Froze the retrieval learning of the model. The results were worse than when it was not frozen. Learning in retrieval is also helping the RAG models to perform well.
- Index hot-swapping
    - Just by swapping the documents in database (the non-parametric memory), RAG models were able to keep up with the updates.
- Effect of Retrieving more documents
    - There was no significant difference between when $k$ is $5$ or $10$. The peak or a good convergence point was at $10$, so keeping it around this value would be suggested.
