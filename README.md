# NLP and SpaCy Exploration

This Python script explores natural language processing (NLP) using the SpaCy library. It demonstrates various operations such as word similarity comparisons and sentence similarity calculations.

## Requirements

To run this script, you need to have Python installed on your system. Additionally, you need to install the SpaCy library by running the following command:

```
pip install spacy
```

You also need to download the SpaCy English models by running the following command:

```
python -m spacy download en_core_web_md
python -m spacy download en_core_web_sm
```

## Usage

1. Make sure you have installed the required dependencies.
2. Open the script in a Python editor or IDE.
3. Run the script.
4. The script will perform various NLP operations and display the results.

## Functionality

1. **Word Similarity:** The script compares the similarity between different words using the SpaCy library's word vectors.

2. **Word Similarity Comparison:** The script compares the similarity between multiple words using nested loops.

3. **Sentence Similarity:** The script calculates the similarity between a given sentence and a list of sentences using SpaCy.

## Notes

- The script demonstrates the use of two different SpaCy models: `en_core_web_md` and `en_core_web_sm`. The former has word vectors included, while the latter does not.

- When using `en_core_web_md`, the word similarity calculations are based on the word vectors and provide meaningful results. However, if you use `en_core_web_sm`, which lacks word vectors, the similarity calculations are based on taggers and may not be accurate.

## License

This script is released under the [MIT License](https://opensource.org/licenses/MIT). Please refer to the `LICENSE` file for more information.
