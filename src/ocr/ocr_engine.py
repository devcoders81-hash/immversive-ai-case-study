import easyocr

reader = easyocr.Reader(
    ['hi', 'en'],
    gpu=False
)

def extract_text(image_path):

    results = reader.readtext(image_path)

    lines = []

    for result in results:
        lines.append(result[1])

    return "\n".join(lines)