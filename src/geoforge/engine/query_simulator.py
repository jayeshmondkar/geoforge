import random

DEFAULT_QUERIES = [
    "what is {topic}",
    "best {topic}",
    "how to use {topic}",
    "top platforms for {topic}",
    "examples of {topic}",
    "benefits of {topic}",
    "compare {topic} services",
    "how does {topic} work"
]


def generate_queries(topic: str, n=10):
    queries = []
    for _ in range(n):
        template = random.choice(DEFAULT_QUERIES)
        queries.append(template.format(topic=topic))
    return queries