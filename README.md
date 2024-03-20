# Ollama

Ollama is a tool for local execution of Mistral and LLama models. It provides a convenient way to serve these models locally for development and testing purposes.

## Installation

To download and install Ollama, please visit the official website or GitHub repository.

## Usage

After installation, follow these steps to use Ollama:

1. Open the command prompt or terminal.
2. Navigate to the directory where Ollama is installed.
3. Execute the following command to initiate the server:

```bash
ollama serve
```

4. This will start the Ollama server, enabling the local execution of Mistral and LLama models.

## Extension Setup

Make sure to load the Ollama extension on the Chrome browser and activate it. The extension provides additional functionality and integration with the browser.

## Troubleshooting

If an error occurs stating that port 11434 is occupied, you may need to terminate the process using that port and then rerun `ollama serve`.

To check for processes using port 11434, use the following command:

```bash
netstat -ano | findstr :11434
```

To terminate the process using that port, use the following command (replace `PID` with the actual process ID):

```bash
taskkill /PID PID /F
```
