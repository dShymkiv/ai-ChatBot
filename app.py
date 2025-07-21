from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Keyword-based question and answer mapping
faq = {
    "recursion": "Recursion is a programming concept where a function calls itself to solve smaller instances of a problem.",
    "database": "A database is an organized collection of data, generally stored and accessed electronically from a computer system.",
    "data visualization": "Data visualization is the graphical representation of information and data.",
    "algorithm": "An algorithm is a set of instructions designed to perform a specific task.",
    "oop": "OOP stands for Object-Oriented Programming. It's a programming paradigm based on the concept of 'objects'.",
    "ai": "Artificial Intelligence is the simulation of human intelligence in machines.",
    "machine learning": "Machine learning is a branch of AI focused on building systems that learn from data.",
    "function": "A function is a block of code which only runs when it is called.",
    "variable": "A variable is a storage location paired with an associated symbolic name.",
    "loop": "Loops are used to repeat a block of code as long as a specified condition is met.",
    "python": "Python is a high-level, interpreted programming language known for its readability.",
    "java": "Java is a class-based, object-oriented programming language designed to have as few implementation dependencies as possible.",
    "html": "HTML stands for HyperText Markup Language. It's used to structure web pages.",
    "css": "CSS stands for Cascading Style Sheets and is used to style HTML content.",
    "javascript": "JavaScript is a scripting language used to create and control dynamic website content.",
    "flask": "Flask is a micro web framework written in Python.",
    "api": "API stands for Application Programming Interface. It allows different software systems to communicate.",
    "json": "JSON stands for JavaScript Object Notation. It's a lightweight format for storing and transporting data.",
    "binary": "Binary is a base-2 numeral system used by computers.",
    "compiler": "A compiler translates source code written in a programming language into machine code.",
    "interpreter": "An interpreter directly executes instructions written in a programming or scripting language.",
    "debugging": "Debugging is the process of identifying and removing errors from computer programs.",
    "stack": "A stack is a linear data structure which follows the LIFO (Last In First Out) principle.",
    "queue": "A queue is a linear data structure that follows the FIFO (First In First Out) principle.",
    "linked list": "A linked list is a linear data structure where elements are stored in nodes and connected via pointers.",
    "array": "An array is a collection of items stored at contiguous memory locations.",
    "database normalization": "Normalization is the process of organizing data in a database to reduce redundancy.",
    "encryption": "Encryption is the method by which information is converted into secret code.",
    "hashing": "Hashing is the transformation of a string of characters into a usually shorter fixed-length value.",
    "firewall": "A firewall is a network security device that monitors incoming and outgoing network traffic.",
    "cloud computing": "Cloud computing is the delivery of different services through the Internet.",
    "virtualization": "Virtualization is the creation of a virtual version of something, such as a server or operating system.",
    "operating system": "An operating system manages computer hardware and software resources.",
    "linux": "Linux is an open-source Unix-like operating system kernel.",
    "windows": "Windows is a series of operating systems developed by Microsoft.",
    "compiler vs interpreter": "A compiler translates the entire code before execution, while an interpreter executes line-by-line.",
    "http": "HTTP stands for HyperText Transfer Protocol. It's used for transmitting web pages.",
    "https": "HTTPS is the secure version of HTTP. It uses SSL/TLS to encrypt communication.",
    "ip address": "An IP address is a unique address that identifies a device on the internet or a local network.",
    "dns": "DNS stands for Domain Name System. It translates domain names into IP addresses.",
    "software development lifecycle": "SDLC is a process followed for a software project, within a software organization.",
    "agile": "Agile is a methodology based on iterative development.",
    "scrum": "Scrum is an Agile framework that helps teams work together.",
    "compiler error": "A compiler error occurs when a program fails to compile due to syntax or semantic issues.",
    "syntax": "Syntax is the set of rules that defines the combinations of symbols considered correctly structured in that language.",
    "runtime error": "A runtime error is an error that occurs during the execution of a program.",
    "exception": "An exception is an event that disrupts the normal flow of the program's instructions.",
    "try except": "Try-except is used in Python to handle exceptions.",
    "unit test": "Unit testing is a software testing method where individual units are tested.",
    "version control": "Version control is a system that records changes to a file or set of files over time.",
    "git": "Git is a distributed version-control system for tracking changes in source code.",
    "github": "GitHub is a platform for version control and collaboration."
}

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("message", "").strip().lower()

    if not user_input:
        return jsonify({"response": "Please type something!"})

    for keyword, answer in faq.items():
        if keyword in user_input:
            return jsonify({"response": answer})

    return jsonify({
        "response": "Hmm, I'm not sure about that. Try asking about recursion, data structures, or machine learning!"
    })

if __name__ == '__main__':
    app.run(debug=True)


