# 🛡️ Python-Based Web Security Scanner

<p align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-black?style=for-the-badge&logo=flask)
![Security](https://img.shields.io/badge/Cybersecurity-Web%20Scanner-red?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

</p>

> A lightweight **Web Application Security Scanner** built with **Python** and **Flask** to identify common web security issues such as **SQL Injection**, **Cross-Site Scripting (XSS)**, **Missing Security Headers**, and **SSL Certificate Validation**.

Designed as a learning-oriented cybersecurity project, this tool demonstrates how automated vulnerability assessment can help identify basic security misconfigurations and common web application weaknesses.

---

# 🌟 Features

- 🔍 SQL Injection Detection
- 🚨 Reflected XSS Detection
- 🔐 SSL Certificate Validation
- 🛡️ HTTP Security Header Analysis
- 🌐 Website Availability & Status Code Check
- 💻 Simple Web-Based User Interface
- ⚡ Fast Vulnerability Assessment
- 📋 Human-Readable Security Report

---

# 💡 Why This Project?

Web applications are frequently targeted by attackers exploiting common vulnerabilities such as SQL Injection and Cross-Site Scripting (XSS).

This project provides an easy-to-use interface for performing basic security checks against web applications, making it useful for cybersecurity learners, developers, and penetration testing practice.

---

# 🔍 Security Checks

## SQL Injection Detection

The scanner sends predefined SQL Injection payloads to application parameters and inspects server responses for common database error messages that may indicate vulnerable input handling.

Example payloads:

```text
' OR 1=1 --
' OR 'a'='a
" OR "a"="a
```

---

## Cross-Site Scripting (XSS)

The scanner injects common XSS payloads into request parameters and checks whether the payload is reflected back in the response.

Example payloads:

```html
<script>alert('XSS')</script>

<img src="x" onerror="alert(1)">
```

---

## Security Headers Analysis

The application checks whether important HTTP security headers are present.

Headers inspected:

- Strict-Transport-Security
- Content-Security-Policy
- X-Frame-Options
- X-Content-Type-Options

Missing headers are highlighted in the generated report.

---

## SSL Certificate Validation

The scanner establishes a secure TLS connection with the target website and verifies that a valid SSL certificate is available.

---

## Website Status Check

Displays the HTTP response status code to verify website accessibility.

Example:

```
200 OK
301 Redirect
403 Forbidden
404 Not Found
500 Internal Server Error
```

---

# 🏗️ System Architecture

```text
             User Input (Target URL)
                      │
                      ▼
               Flask Web Server
                      │
        ┌─────────────┼──────────────┐
        ▼             ▼              ▼
 SQL Injection     XSS Test     Security Headers
        │             │              │
        └─────────────┼──────────────┘
                      ▼
             SSL Certificate Check
                      │
                      ▼
             HTTP Status Code Check
                      │
                      ▼
            Vulnerability Report
```

---

# 📂 Project Structure

```text
Python-Based-security-tools/

├── webscanner.py
│
├── templates/
│   └── index.html
│
├── static/
│   └── styles.css
│
└── .vscode/
```

---

# ⚙️ Technology Stack

## Programming Language

- Python

## Backend

- Flask
- Requests
- urllib3
- SSL
- Socket

## Frontend

- HTML5
- CSS3

---

# 🧠 Concepts Demonstrated

- Web Application Security
- SQL Injection Testing
- Cross-Site Scripting (XSS)
- HTTP Security Headers
- SSL/TLS Validation
- Flask Web Development
- HTTP Requests
- Socket Programming
- Client-Server Communication

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/palak00027/Python-Based-security-tools.git

cd Python-Based-security-tools
```

---

## Install Dependencies

```bash
pip install flask requests urllib3
```

---

## Run the Application

```bash
python webscanner.py
```

The application will start on:

```
http://127.0.0.1:5000
```

---

# 📋 Usage

1. Launch the Flask application.
2. Open the web interface.
3. Enter the target website URL.
4. Click **Scan**.
5. Review the generated security report.

The scanner checks:

- SQL Injection
- XSS
- Security Headers
- SSL Certificate
- HTTP Status Code

---

# 📸 Screenshots

## 🏠 Home Page

<img width="939" height="370" alt="image" src="https://github.com/user-attachments/assets/9fbf564c-1c10-4264-a7ca-0b69462b1edd" />


---

## 🔍 Scan Results

<img width="601" height="808" alt="image" src="https://github.com/user-attachments/assets/6c23ea21-a1fe-4adc-8d25-fd7809298d50" />

---

<img width="640" height="746" alt="image" src="https://github.com/user-attachments/assets/171dbac4-6223-4593-9675-fbf240d017c0" />

<img width="960" height="1344" alt="image" src="https://github.com/user-attachments/assets/c8324d22-c097-4fd3-8e3d-6206271cd4b4" />



---

# 📈 Current Capabilities

| Feature | Status |
|----------|--------|
| SQL Injection Detection | ✅ |
| XSS Detection | ✅ |
| SSL Certificate Validation | ✅ |
| Security Header Analysis | ✅ |
| HTTP Status Check | ✅ |
| Web Dashboard | ✅ |
| Open Port Scanning | 🚧 Planned |

---

# 🚀 Future Enhancements

- Network Port Scanner
- Directory & File Enumeration
- CSRF Detection
- Clickjacking Detection
- Cookie Security Analysis
- Server Fingerprinting
- Technology Stack Detection
- OWASP Top 10 Checks
- PDF Report Generation
- Export Scan Results
- Multi-threaded Scanning
- REST API Support

---

# ⚠️ Disclaimer

This tool is intended **solely for educational purposes and authorized security testing**.

Do **not** use it against systems or applications without explicit permission from the owner. Unauthorized scanning may violate laws or organizational policies.

---

# 📚 Learning Outcomes

This project demonstrates practical knowledge of:

- Python Programming
- Flask Development
- HTTP Protocol
- Web Application Security
- Vulnerability Assessment
- Secure Communication (SSL/TLS)
- Cybersecurity Fundamentals

---

# 👩‍💻 Author

**Palak Upadhyay** ,  **Sakshi Singh**  , **Rhitika vishwakarma**

🎓 B.E. Computer Science & Engineering (Cyber Security)

💡 Passionate about Cybersecurity, Cloud Security, Secure Software Development, Full Stack Development, and Artificial Intelligence.

**GitHub:**  
https://github.com/palak00027

---

# ⭐ Show Your Support

If you found this project useful, consider giving it a **⭐ Star** on GitHub. Your support encourages future improvements and new cybersecurity projects.
