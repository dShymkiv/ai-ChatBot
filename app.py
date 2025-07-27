import os
os.environ["TOKENIZERS_PARALLELISM"] = "false"

from flask import Flask, request, jsonify, render_template
from sentence_transformers import SentenceTransformer, util
import numpy as np

app = Flask(__name__)

# Initialize the AI model for semantic search
model = SentenceTransformer('all-MiniLM-L6-v2')

# Enhanced FAQ with more detailed answers and categories
faq_data = [
    {
        "question": "recursion",
        "answer": "Recursion is a programming concept where a function calls itself to solve smaller instances of a problem. It consists of a base case (stopping condition) and a recursive case (function calling itself). Common examples include factorial calculation, Fibonacci sequence, and tree traversal algorithms.",
        "keywords": ["recursive", "function calls itself", "base case", "factorial", "fibonacci"]
    },
    {
        "question": "database",
        "answer": "A database is an organized collection of data, generally stored and accessed electronically from a computer system. It provides efficient storage, retrieval, and management of data. Types include relational (SQL), NoSQL, and graph databases. Key concepts include tables, relationships, indexing, and ACID properties.",
        "keywords": ["data storage", "SQL", "NoSQL", "tables", "relationships", "indexing"]
    },
    {
        "question": "data visualization",
        "answer": "Data visualization is the graphical representation of information and data using visual elements like charts, graphs, and maps. It helps identify patterns, trends, and insights in data. Popular tools include matplotlib, seaborn, plotly, and Tableau. Common chart types include bar charts, line graphs, scatter plots, and heatmaps.",
        "keywords": ["charts", "graphs", "matplotlib", "seaborn", "plotly", "visual representation"]
    },
    {
        "question": "algorithm",
        "answer": "An algorithm is a set of instructions designed to perform a specific task. It's like a recipe that tells a computer exactly what steps to follow. Algorithms can be analyzed for time complexity (Big O notation) and space complexity. Common algorithm types include sorting, searching, graph algorithms, and dynamic programming.",
        "keywords": ["instructions", "steps", "complexity", "sorting", "searching", "Big O"]
    },
    {
        "question": "oop",
        "answer": "OOP stands for Object-Oriented Programming. It's a programming paradigm based on the concept of 'objects' that contain data and code. Key principles include encapsulation, inheritance, polymorphism, and abstraction. Popular OOP languages include Java, C++, Python, and C#.",
        "keywords": ["objects", "encapsulation", "inheritance", "polymorphism", "abstraction", "classes"]
    },
    {
        "question": "ai",
        "answer": "Artificial Intelligence is the simulation of human intelligence in machines. It includes machine learning, natural language processing, computer vision, and robotics. AI can be narrow (specific tasks) or general (human-like intelligence). Applications include chatbots, recommendation systems, autonomous vehicles, and medical diagnosis.",
        "keywords": ["machine learning", "neural networks", "deep learning", "NLP", "computer vision"]
    },
    {
        "question": "machine learning",
        "answer": "Machine learning is a branch of AI focused on building systems that learn from data. Types include supervised learning (labeled data), unsupervised learning (unlabeled data), and reinforcement learning (trial and error). Popular algorithms include linear regression, decision trees, neural networks, and support vector machines.",
        "keywords": ["supervised", "unsupervised", "reinforcement", "neural networks", "training data"]
    },
    {
        "question": "python",
        "answer": "Python is a high-level, interpreted programming language known for its readability and simplicity. It's widely used in data science, web development, AI, and automation. Key features include dynamic typing, garbage collection, and extensive libraries like NumPy, Pandas, and Django.",
        "keywords": ["interpreted", "readable", "libraries", "data science", "web development"]
    },
    {
        "question": "javascript",
        "answer": "JavaScript is a scripting language used to create and control dynamic website content. It runs in web browsers and can also be used on servers (Node.js). Key features include event-driven programming, asynchronous operations, and extensive ecosystem with frameworks like React, Vue, and Angular.",
        "keywords": ["web", "browser", "Node.js", "frontend", "backend", "frameworks"]
    },
    {
        "question": "flask",
        "answer": "Flask is a micro web framework written in Python. It's lightweight and flexible, perfect for small to medium applications. Key features include routing, template engine (Jinja2), and easy integration with databases. It follows the WSGI standard and is often used for APIs and web services.",
        "keywords": ["web framework", "micro", "routing", "templates", "WSGI", "API"]
    },
    {
        "question": "api",
        "answer": "API stands for Application Programming Interface. It allows different software systems to communicate with each other. Types include REST APIs, GraphQL, and SOAP. APIs define endpoints, request/response formats, and authentication methods. They're essential for modern web and mobile applications.",
        "keywords": ["REST", "GraphQL", "endpoints", "authentication", "communication"]
    },
    {
        "question": "git",
        "answer": "Git is a distributed version-control system for tracking changes in source code. It allows multiple developers to collaborate on projects. Key concepts include commits, branches, merging, and remote repositories. Popular platforms include GitHub, GitLab, and Bitbucket.",
        "keywords": ["version control", "commits", "branches", "merging", "collaboration"]
    },
    {
        "question": "semaphores",
        "answer": "Semaphores are synchronization primitives used in concurrent programming to control access to shared resources. They maintain a count and can be used for signaling between threads or processes. Types include binary semaphores (mutex) and counting semaphores. They help prevent race conditions and deadlocks.",
        "keywords": ["synchronization", "threading", "concurrent", "race conditions", "mutex"]
    },
    {
        "question": "encryption",
        "answer": "Encryption is the method by which information is converted into secret code to protect data confidentiality. Types include symmetric encryption (same key) and asymmetric encryption (public/private keys). Common algorithms include AES, RSA, and SHA. It's essential for secure communication and data protection.",
        "keywords": ["security", "cryptography", "keys", "AES", "RSA", "confidentiality"]
    },
    {
        "question": "cloud computing",
        "answer": "Cloud computing is the delivery of different services through the Internet, including servers, storage, databases, and software. Types include IaaS (Infrastructure), PaaS (Platform), and SaaS (Software). Popular providers include AWS, Azure, and Google Cloud. Benefits include scalability, cost-effectiveness, and accessibility.",
        "keywords": ["AWS", "Azure", "IaaS", "PaaS", "SaaS", "scalability"]
    }
]

# Create embeddings for all FAQ questions and keywords
faq_embeddings = []
for item in faq_data:
    # Combine question and keywords for better matching
    text = f"{item['question']} {' '.join(item['keywords'])}"
    embedding = model.encode(text, convert_to_tensor=True)
    faq_embeddings.append({
        'embedding': embedding,
        'data': item
    })

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("message", "").strip().lower()

    if not user_input:
        return jsonify({"response": "Please type something!"})

    # Handle greetings and general questions
    greetings = ["hello", "hi", "hey", "good morning", "good afternoon", "good evening"]
    help_questions = ["what can you do", "what you can help with", "help", "what topics", "what subjects"]
    
    if any(greeting in user_input for greeting in greetings):
        return jsonify({
            "response": "Hello! 👋 I'm StudyBuddy, your AI-powered CS study assistant! I can help you learn about programming concepts, languages, algorithms, and computer science topics. Just ask me anything about CS!"
        })
    
    if any(help_q in user_input for help_q in help_questions):
        return jsonify({
            "response": "I can help you with many CS topics! Here's what I know about:\n\n• Programming Concepts: Recursion, OOP, Algorithms, Functions\n• Languages: Python, JavaScript, Java, HTML/CSS\n• Technologies: Flask, APIs, Git, Databases\n• AI & ML: Machine Learning, Artificial Intelligence, Data Visualization\n• Computer Science: Semaphores, Encryption, Cloud Computing\n\nJust ask me anything about these topics!"
        })

    # Encode user input
    user_embedding = model.encode(user_input, convert_to_tensor=True)
    
    # Find the best match using cosine similarity
    best_score = 0
    best_answer = None
    
    for faq_item in faq_embeddings:
        # Calculate cosine similarity
        similarity = util.pytorch_cos_sim(user_embedding, faq_item['embedding'])[0][0].item()
        
        if similarity > best_score:
            best_score = similarity
            best_answer = faq_item['data']['answer']
    
    # Set threshold for similarity (adjust as needed)
    if best_score > 0.3:  # 30% similarity threshold
        return jsonify({"response": best_answer})
    else:
        # Fallback to keyword matching for very specific queries
        for item in faq_data:
            if any(keyword in user_input for keyword in [item['question']] + item['keywords']):
                return jsonify({"response": item['answer']})
        
        return jsonify({
            "response": "I'm not sure about that specific topic, but I'd be happy to help you with CS topics! Try asking about:\n\n• Programming: recursion, algorithms, OOP, functions\n• Languages: Python, JavaScript, Java, HTML/CSS\n• Technologies: databases, APIs, Git, Flask\n• AI & ML: machine learning, artificial intelligence, data visualization\n• Computer Science: semaphores, encryption, cloud computing\n\nOr just say 'hello' to get started! 😊"
        })

if __name__ == '__main__':
    app.run(debug=False, host='127.0.0.1', port=8080)


