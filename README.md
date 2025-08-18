# Pipeline Canvas

Pipeline Canvas is a visual workflow builder for connecting and experimenting with different data processing nodes. It lets you drag, drop, and link together components like APIs, databases, LLMs, and text processors to create custom pipelines—all in your browser.

## Features

- Drag-and-drop interface for building pipelines
- Modular nodes: API, database, LLM, text, and more
- Real-time editing and configuration of each node
- Visual feedback for connections and data flow
- Easy to extend with new node types

## Getting Started

### Prerequisites
- Node.js (for the frontend)
- Python 3 (for the backend)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/kayjayy22/pipeline-canvas.git
   cd pipeline-canvas
   ```

2. **Frontend setup:**
   ```bash
   cd frontend
   npm install
   npm start
   ```
   This will start the React app on [http://localhost:3000](http://localhost:3000).

3. **Backend setup:**
   ```bash
   cd ../backend
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt  # If requirements.txt exists
   python main.py
   ```
   The backend will run on [http://localhost:8000](http://localhost:8000) by default.

## Project Structure

```
frontend/   # React app for the UI
backend/    # Python backend for processing
```

## Screenshots

![Pipeline Canvas Screenshot](./frontend/public/logo192.png)

## Contributing

Pull requests are welcome! If you have ideas for new node types or features, open an issue or fork the repo.

## License

MIT License. See LICENSE file for details.

---

This project was started as a personal experiment to make building and testing data workflows more visual and fun. Suggestions and feedback are always appreciated.