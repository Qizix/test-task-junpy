Text Summarization API
This project provides a local API server for text summarization. Send text to the server, and it will return a concise summary.
Getting Started
Follow these steps to set up and run the project on your local machine.
Prerequisites

Python (version recommended for this project)
Git

Installation

Clone the repository:
Copygit clone https://github.com/Qizix/test-task-junpy.git

Navigate to the project directory:
Copycd test-task-junpy

Install the required Python libraries:
Copypip install -r requirements.txt


Usage

Start the local server:
Copypython main.py

The server will be running at http://127.0.0.1:8000.
To use the summarization service, send a POST request to http://127.0.0.1:8000/summarize with your text in JSON format.
Example using curl:
Copycurl -X POST -H "Content-Type: application/json" -d '{"text": "Your long text here..."}' http://127.0.0.1:8000/summarize

The server will respond with a JSON object containing the summarized text.
