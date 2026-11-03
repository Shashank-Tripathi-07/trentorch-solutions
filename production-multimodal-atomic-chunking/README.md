# Chunk Multimodal Content Without Splitting Atomic Blocks

Intermediate | production-systems | multimodal | chunking

### The problem, from first principles

Fixed-size chunking (covered elsewhere in this curriculum) cuts text at a size boundary regardless of what's there. That's fine for plain prose, but an image's caption, a table, or a code block is a single indivisible unit -- cutting it in half produces two useless fragments instead of one usable one.

### The task

Write `chunk_with_atomic_blocks(blocks, max_chunk_size)`, where each block is `(content, size)` and is never split. Greedily pack blocks into chunks at or under `max_chunk_size`. A block whose own size already exceeds the limit still becomes its own chunk, since it genuinely can't be made smaller.
