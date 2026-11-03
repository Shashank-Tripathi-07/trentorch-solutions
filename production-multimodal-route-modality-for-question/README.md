# Route a Question to the Right Modality

Beginner | production-systems | multimodal | routing

### The problem, from first principles

A question about a document can be about its text, an embedded image, or a table -- and answering it well usually means retrieving from the specific modality it's actually asking about, rather than searching everything indiscriminately every time.

### The task

Write `route_modality_for_question(question, modality_keywords, default_modality)`, where `modality_keywords` maps a modality name to a list of keywords. Return the first modality (in dict order) with a case-insensitive keyword match in the question, or `default_modality` if none match.
