# Bangalore-House-Price-Prediction

# 🏠 Bangalore House Price Prediction

A machine learning web application that predicts house prices in Bangalore based on location, BHK, bathrooms, and square footage.

## 🌟 Features

- **Real-time Predictions**: Get instant house price estimates
- **Interactive Web Interface**: User-friendly Flask web application
- **Location-based Analysis**: Predictions based on actual Bangalore locations
- **Responsive Design**: Works on desktop and mobile devices

## 🛠️ Technology Stack

- **Backend**: Flask (Python)
- **Machine Learning**: Scikit-learn (Ridge Regression)
- **Data Processing**: Pandas, NumPy
- **Frontend**: HTML, CSS, Bootstrap
- **Model**: Ridge Regression with Column Transformer

## 📊 Dataset

The application uses a cleaned dataset of Bangalore house prices containing:
- Location information
- Number of bedrooms (BHK)
- Number of bathrooms
- Total square footage
- Price information

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8+
- pip package manager

### Local Setup

1. **Clone the repository**
```bash
git clone https://github.com/param2412/bangalore-house-prediction.git
cd bangalore-house-prediction
```

2. **Create virtual environment**
```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the application**
```bash
python main.py
```

5. **Open in browser**
```
http://localhost:5000
```

## 📁 Project Structure

```
Bangalore-House-Prediction/
├── main.py                 # Flask application
├── templates/
│   └── index.html          # Web interface
├── Cleaned_data.csv        # Dataset
├── RidgeModel.pkl         # Trained ML model
├── requirements.txt       # Dependencies
├── README.md             # Project documentation
└── .gitignore           # Git ignore rules
```

## 🎯 Usage

1. **Select Location**: Choose from available Bangalore locations
2. **Enter BHK**: Number of bedrooms (1-10)
3. **Enter Bathrooms**: Number of bathrooms (1-10)
4. **Enter Square Feet**: Total area (500-10000 sq ft)
5. **Click "Predict Price"**: Get instant price prediction


## 🔧 Model Information

- **Algorithm**: Ridge Regression
- **Features**: Location (encoded), BHK, Bathrooms, Square Feet
- **Preprocessing**: Column Transformer with One-Hot Encoding
- **Performance**: Optimized for Bangalore real estate market

## 📈 Future Enhancements

- [ ] Add more features (age of property, amenities)
- [ ] Implement advanced ML models
- [ ] Add price trend analysis
- [ ] Include property recommendation system
- [ ] Add map visualization

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/enhancement`)
3. Commit changes (`git commit -am 'Add enhancement'`)
4. Push to branch (`git push origin feature/enhancement`)
5. Create Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

- GitHub: [@param2412](https://github.com/param2412)

## 🙏 Acknowledgments

- Dataset source: Bangalore real estate data 
- Built with Flask and Scikit-learn
- Bootstrap for responsive design

---

⭐ **Star this repository if you found it helpful!**
