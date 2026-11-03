# Unified Retrieval Across Text and Image-Caption Chunks

Beginner | production-systems | multimodal | retrieval

### The problem, from first principles

A multimodal knowledge base doesn't store only paragraphs of text -- an image gets indexed by its caption or a generated description, a chart by a summary of what it shows. A query shouldn't need to know in advance whether the most relevant piece of content happens to be a paragraph or an image's caption; retrieval should treat both as equally eligible answers.

### The task

Write `retrieve_across_modalities(chunks, query_keywords)`, where each chunk is `(chunk_id, modality, text)`. Score every chunk by how many keywords match its text, case-insensitively, regardless of its modality, and return the ids of chunks with a positive score, ranked by score descending with ties broken by original order.
