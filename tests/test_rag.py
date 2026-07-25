from rag.chunker import split_documents


def test_chunking():

    documents = [
        "Python is important for Data Engineering career"
    ]

    result = split_documents(documents)

    assert result is not None