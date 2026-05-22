# CLI News Fetcher

A dynamic, interactive Python command-line application that interacts with the **News API v2 (`/everything` endpoint)** to fetch, filter, and read live news articles from across the web.

## 🚀 Features
- **Interactive Search:** Allows users to input any custom search term dynamically.
- **Custom Filtering Engine:** Optional configuration settings toggled directly through user inputs.
- **Advanced Sorting:** Sort results dynamically by `relevancy`, `popularity`, or `publishedAt` dates.
- **Pagination & Limits:** Set exact target page results and control the payload volume (total articles returned).
- **Graceful Error Handling:** Implements `try-except` blocks for network requests and input validation routines via `sys.exit`.

## 🛠️ Tech Stack & Requirements
- **Language:** Python 3.x
- **Libraries Used:** `requests` (HTTP client), `sys` (system exit handles)

## 📦 Installation & Setup

1. **Clone the repository:**
   
```bash
   git clone [https://github.com/Darsh/basic-news.git](https://github.com/Darsh/basic-news.git)
   cd basic-news
