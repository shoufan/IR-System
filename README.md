# Information Retrieval System

## Abstract
This project aims to develop an Information Retrieval (IR) system capable of crawling web documents, indexing them, and processing free text queries. The system utilizes Scrapy for web crawling, Scikit-Learn for indexing, and Flask for query processing. The objective is to create a robust and efficient system for retrieving relevant information from the web.

## Overview
The proposed system consists of three main components:
1. **Crawler**: Utilizes Scrapy to crawl web documents, allowing the system to download HTML content from specified seed URLs and domains. The crawler can be configured with parameters such as max pages and max depth.
2. **Indexer**: Implements a TF-IDF-based inverted index using Scikit-Learn, enabling the system to construct an index of crawled documents for efficient search retrieval.
3. **Processor**: Implements a Flask-based web server to handle free text queries in JSON format. The processor validates queries, retrieves relevant documents from the index, and returns top-ranked results.

## Design
### System Capabilities
- Web crawling: Scrapy-based crawler for downloading web documents in HTML format.
- Indexing: Scikit-Learn-based indexer for constructing an inverted index using TF-IDF representation.
- Query processing: Flask-based processor for handling free text queries and returning top-ranked results.

### Interactions
- Crawler interacts with web pages to download HTML content.
- Indexer interacts with crawled documents to construct an inverted index.
- Processor interacts with the index to retrieve relevant documents based on user queries.

### Integration
- Crawler output (HTML documents) is used as input for the indexer.
- Indexer output (inverted index) is used as input for the processor.

## Architecture
### Software Components
1. **Crawler**: Implemented using Scrapy.
2. **Indexer**: Implemented using Scikit-Learn's TfidfVectorizer.
3. **Processor**: Implemented using Flask.

### Interfaces
- Crawler exposes command-line interface for configuration.
- Indexer exposes Python API for indexing documents.
- Processor exposes HTTP API for query processing.

### Implementation
- Crawler and Indexer are standalone Python scripts.
- Processor is a Flask web application.

## Operation
### Software Commands
- **Crawler**: Execute `scrapy crawl my_spider -o output.json` to start crawling.
- **Indexer**: Execute `python indexer.py` to index crawled documents.
- **Processor**: Run `python processor.py` to start the Flask server.

### Inputs
- Seed URLs for crawling.
- Max pages and max depth for the crawler.
- Free text queries for the processor.

### Installation
1. Install required Python packages: `pip install scrapy scikit-learn flask`.
2. Clone the project repository: `git clone https://github.com/shoufan/IR-System`.
3. Navigate to the project directory: `cd IR-System`.

## Conclusion
The development of the Information Retrieval System has been successful, providing functionality for web crawling, indexing, and query processing. The system demonstrates the capability to retrieve relevant information from web documents based on user queries. Further enhancements could include additional features such as query spelling correction and query expansion.

## Data Sources
- Web documents: Crawled from specified seed URLs.
- Test data: Generated for evaluation purposes.

## Test Cases
- Framework: Implement unit tests using pytest.
- Test scenarios: Verify crawler functionality, indexer accuracy, and processor response.

## Bibliography
1. Scrapy Documentation: [https://docs.scrapy.org/en/latest/](https://docs.scrapy.org/en/latest/)
2. Scikit-Learn Documentation: [https://scikit-learn.org/stable/documentation.html](https://scikit-learn.org/stable/documentation.html)
3. Flask Documentation: [https://flask.palletsprojects.com/en/2.0.x/](https://flask.palletsprojects.com/en/2.0.x/)
4. Python Documentation: [https://docs.python.org/3/](https://docs.python.org/3/)
