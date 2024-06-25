# Text Summarization API
This project provides a local API server for text summarization. Send text to the server, and it will return a concise summary.
## Getting Started
Follow these steps to set up and run the project on your local machine.

## Installation

  1. Clone the repository:
  
    git clone https://github.com/Qizix/test-task-junpy.git
  2. Navigate to the project directory:

    cd test-task-junpy

  3. Install the required Python libraries:

    pip install -r requirements.txt


## Usage

  1. Start the local server:

    python main.py

  2. The server will be running at http://127.0.0.1:8000.
  3. To use the summarization service, send a POST request to http://127.0.0.1:8000/summarize with your text in JSON format.
Example using curl:

    curl -X POST -H "Content-Type: application/json" -d '{"text": "Your long text here..."}' http://127.0.0.1:8000/summarize

  5. The server will respond with a JSON object containing the summarized text.

## Contact
  Yaroslav Dziubenko - yar.dziub2005@gmail.com
