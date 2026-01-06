# Calculator Web - Full-Stack Web Calculator

A modern web-based calculator application built with Flask (Python) backend and interactive HTML/CSS/JavaScript frontend. Supports basic arithmetic operations with calculation history tracking.

## 🎯 Features

- **Basic Arithmetic Operations** - Addition, subtraction, multiplication, division
- **Calculation History** - Track and view all previous calculations
- **Clean User Interface** - Responsive and intuitive design
- **Real-time Computation** - Instant calculation results
- **History Management** - View, clear, or reference past calculations
- **Error Handling** - Proper handling of invalid inputs

## 🛠️ Technologies Used

- **Backend:**

  - Python 3.x
  - Flask - Lightweight web framework
  - Flask-CORS - Cross-origin resource sharing

- **Frontend:**
  - HTML5 - Structure
  - CSS3 - Styling and responsive design
  - JavaScript - Client-side logic and interactivity

## 📂 Project Structure

```
calculatorweb/
├── app.py              # Flask backend application
├── index.html          # Main calculator interface
├── history.html        # Calculation history page
├── static.css          # Stylesheet
├── requirements.txt    # Python dependencies
└── README.md           # Documentation
```

## 📋 Prerequisites

- Python 3.6 or higher
- pip (Python package manager)
- Modern web browser

## 🚀 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Prem-4545/calculatorweb.git
cd calculatorweb
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Application

```bash
python app.py
```

### 4. Access the Calculator

Open your browser and navigate to:

```
http://localhost:5000
```

## 📝 Usage Guide

### Basic Calculations

1. **Enter Numbers** - Click on number buttons or use keyboard
2. **Select Operation** - Choose +, -, \*, or /
3. **Get Result** - Press = to calculate
4. **View History** - Click "History" to see past calculations

### Keyboard Support

- **Numbers:** 0-9
- **Operations:** +, -, \*, /
- **Equals:** Enter key
- **Clear:** C or Delete key

### History Features

- View all previous calculations
- See operation details
- Timestamps for each calculation
- Clear history when needed

## 🔧 Configuration

### Customize Appearance

Edit `static.css` to change:

- Colors and themes
- Button sizes
- Layout dimensions
- Font styles

### Backend Configuration

Modify `app.py` to:

- Change port number
- Add new operations
- Implement database for persistent history
- Add user authentication

## 📊 API Endpoints

### Calculate

```
POST /calculate
Body: { "expression": "2+3" }
Response: { "result": 5 }
```

### Get History

```
GET /history
Response: [ { "expression": "2+3", "result": 5, "timestamp": "..." } ]
```

## 🎨 UI Components

- **Display Screen** - Shows current input and results
- **Number Buttons** - 0-9 with clear styling
- **Operation Buttons** - +, -, \*, /
- **Result Button** - = for calculation
- **History Panel** - Collapsible history view

## 🐛 Troubleshooting

### Port Already in Use

```bash
# Change port in app.py
if __name__ == '__main__':
    app.run(debug=True, port=5001)
```

### Dependencies Not Installing

```bash
# Upgrade pip first
pip install --upgrade pip
pip install -r requirements.txt
```

### Frontend Not Loading

- Ensure app.py is running
- Check browser console for errors
- Clear browser cache (Ctrl+Shift+Delete)

## 🚀 Future Enhancements

- ✅ Advanced mathematical operations (sin, cos, sqrt)
- ✅ Graphing calculator functionality
- ✅ User authentication and saved calculations
- ✅ Dark mode theme
- ✅ Mobile app version
- ✅ Scientific calculator mode
- ✅ Unit conversion tools

## 📖 Example Calculations

```
Operation: 25 + 17
Result: 42

Operation: 100 / 4
Result: 25

Operation: 12 * 5
Result: 60
```

## 🤝 Contributing

Contributions are welcome! Please:

- Fork the repository
- Create a feature branch (`git checkout -b feature/amazing-feature`)
- Commit changes (`git commit -m 'Add amazing feature'`)
- Push to branch (`git push origin feature/amazing-feature`)
- Open a Pull Request

## 📄 License

This project is open source and available under the MIT License.

## 👤 Author

**Prem-4545**

- GitHub: [@Prem-4545](https://github.com/Prem-4545)
- Email: jpremchand4939@gmail.com

## ⭐ Support

If you find this calculator helpful, please consider giving it a star! ⭐

---

**Last Updated:** January 6, 2026
**Version:** 1.0
