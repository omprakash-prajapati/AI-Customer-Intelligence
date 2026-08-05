from math import sqrt


def cosine_similarity(vector_a: list[float], vector_b: list[float]) -> float:
    if len(vector_a) != len(vector_b):
        raise ValueError("Vectors must have the same dimensions")

    dot_product = sum(a * b for a, b in zip(vector_a, vector_b, strict=True))
    magnitude_a = sqrt(sum(a * a for a in vector_a))
    magnitude_b = sqrt(sum(b * b for b in vector_b))
    print(dot_product, magnitude_a, magnitude_b)

    if magnitude_a == 0 or magnitude_b == 0:
        raise ValueError("Cosine similarity is undefined for zero vectors")

    return dot_product / (magnitude_a * magnitude_b)


print(cosine_similarity([1.0, 0.0, -1.0, 0.2], [0.3, 1.0, -0.2, 0.7]))

