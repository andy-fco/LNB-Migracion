from transformers import pipeline

_summarizer = None

def resumir_texto(texto: str):
    global _summarizer

    if not texto or len(texto) < 50:
        return texto

    if _summarizer is None:
        _summarizer = pipeline(
            "summarization",
            model="philschmid/bart-large-cnn-samsum"
        )

    res = _summarizer(texto, max_length=60, min_length=20)
    return res[0]["summary_text"]
