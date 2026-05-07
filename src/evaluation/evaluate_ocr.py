from jiwer import cer


def evaluate(reference, prediction):

    score = cer(
        reference,
        prediction
    )

    return {
        "cer": score
    }