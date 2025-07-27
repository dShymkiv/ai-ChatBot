# StudyBuddy - AI-Powered CS Study Assistant

A smart chatbot that helps students learn Computer Science concepts using AI-powered semantic search. Built with Flask and Sentence Transformers.

## 🚀 Features

- **AI-Powered Semantic Search**: Uses Sentence Transformers for intelligent question matching
- **Interactive Chat Interface**: Modern, responsive web interface
- **Comprehensive CS Knowledge Base**: Covers 15+ programming and CS topics
- **Smart Suggestions**: Clickable suggestion buttons for quick questions
- **Real-time Responses**: Instant answers with typing indicators

## 📚 Supported Topics

- **Programming Concepts**: Recursion, OOP, Algorithms, Functions
- **Languages**: Python, JavaScript, Java, HTML/CSS
- **Technologies**: Flask, APIs, Git, Databases
- **AI & ML**: Machine Learning, Artificial Intelligence, Data Visualization
- **Computer Science**: Semaphores, Encryption, Cloud Computing

## 🛠️ Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Modern web browser

## 📦 Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd master-ai-deployment
```

### 2. Create Virtual Environment

```bash
python3 -m venv venv
```

### 3. Activate Virtual Environment

**On macOS/Linux:**

```bash
source venv/bin/activate
```

**On Windows:**

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install flask sentence-transformers
```

## 🚀 Running the Application

### 1. Start the Server

```bash
source venv/bin/activate  # If not already activated
python app.py
```

### 2. Access the Application

Open your web browser and navigate to:

```
http://localhost:8080
```

### 3. Start Chatting!

- Type your questions in the chat input
- Click suggestion buttons for quick questions
- Ask about any CS topic in natural language

## 🧪 Testing the AI Features

Try these example questions to test the semantic search:

### Basic Questions:

- "What is recursion?"
- "Tell me about Python"
- "How do databases work?"

### Semantic Search (different wording):

- "What is a function that calls itself?" → Finds recursion
- "Explain artificial intelligence" → Finds AI
- "How do APIs function?" → Finds API information

### Advanced Topics:

- "What are semaphores in programming?"
- "Explain machine learning concepts"
- "How does cloud computing work?"

## 🏗️ Project Structure

```
master-ai-deployment/
├── app.py                 # Main Flask application
├── templates/
│   └── index.html        # Chat interface template
├── static/
│   ├── styles.css        # CSS styling
│   └── script.js         # Frontend JavaScript
├── venv/                 # Virtual environment
└── README.md            # This file
```

## 🔧 Technical Details

### AI Model

- **Model**: `all-MiniLM-L6-v2` (Sentence Transformers)
- **Purpose**: Semantic similarity matching
- **Features**: 384-dimensional embeddings, fast inference

### Search Algorithm

1. **Semantic Search**: Uses cosine similarity between user query and knowledge base
2. **Keyword Fallback**: Traditional keyword matching for specific terms
3. **Similarity Threshold**: 30% minimum similarity for AI responses

### Backend Technologies

- **Flask**: Web framework
- **Sentence Transformers**: AI model for semantic search
- **PyTorch**: Deep learning backend

## 🐛 Troubleshooting

### Port Already in Use

If you see "Address already in use" error:

```bash
# Kill processes on port 8080
lsof -ti:8080 | xargs kill -9

# Or change port in app.py
app.run(debug=False, host='127.0.0.1', port=8081)
```

### Model Download Issues

If the AI model fails to download:

```bash
# Clear cache and retry
rm -rf ~/.cache/huggingface/
python app.py
```

### Virtual Environment Issues

If you get import errors:

```bash
# Recreate virtual environment
rm -rf venv
python3 -m venv venv
source venv/bin/activate
pip install flask sentence-transformers
```

## 📝 Customization

### Adding New Topics

Edit `faq_data` in `app.py`:

```python
{
    "question": "your_topic",
    "answer": "Detailed explanation...",
    "keywords": ["keyword1", "keyword2", "keyword3"]
}
```

### Adjusting AI Sensitivity

Modify similarity threshold in `app.py`:

```python
if best_score > 0.3:  # Change 0.3 to desired threshold
```

### Changing Port

Edit the last line in `app.py`:

```python
app.run(debug=False, host='127.0.0.1', port=YOUR_PORT)
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Add your improvements
4. Submit a pull request

## 📄 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- **Sentence Transformers**: For semantic search capabilities
- **Flask**: For the web framework
- **Hugging Face**: For the AI model

---

**Happy Learning! 🎓**
