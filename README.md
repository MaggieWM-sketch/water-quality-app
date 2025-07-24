 water-quality-app
 AI Water Quality Predictor for Clean Water Access (SDG 6)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://streamlit.io)

🌍 Project Overview

Smart Water Quality Assessment Tool for Rural Communities

This project addresses UN Sustainable Development Goal 6 (Clean Water and Sanitation) by providing rural communities with an accessible AI-powered tool to quickly assess water quality and identify safe drinking water sources.

- Duration: 1 Week
- Impact: Help communities prevent waterborne diseases through early water quality detection

🎯 Problem Statement

Rural communities worldwide lack affordable, quick methods to assess water quality, leading to:
- Increased waterborne diseases
- Limited access to safe drinking water
- Health risks for vulnerable populations
- Economic burden from water treatment

Our solution provides a simple ML model that predicts water potability based on easily measurable parameters.

🚀 Features

- Binary Classification: Determines if water is Safe/Unsafe for consumption
- Real-time Predictions: Instant results with confidence intervals
- User-friendly Interface: Simple web app accessible to non-technical users
- Mobile-optimized: Lightweight design suitable for mobile devices
- Offline Capability: Can be deployed without internet connectivity

🛠️ Technical Stack

| Component | Technology |
|-----------|------------|
| Machine Learning | Scikit-learn, Pandas, NumPy |
| Web Framework | Streamlit |
| Visualization| Matplotlib, Seaborn |
| Testing | pytest |
| Version Control | Git |
| Data Source | Water Quality Dataset (Kaggle) |

📊 Model Features

The model analyzes 9 key water quality parameters:

1. pH Level - Acidity/alkalinity measure
2. Hardness - Calcium and magnesium concentration
3. Solids (TDS) - Total dissolved solids
4. Chloramines - Disinfectant levels
5. Sulfate - Sulfate ion concentration
6. Conductivity - Electrical conductivity
7. Organic Carbon - Organic matter content
8. Trihalomethanes - Disinfection byproducts
9. Turbidity - Water clarity measure


⚡ Quick Start

Prerequisites

- Python 3.8 or higher
- pip package manager
- Git (optional)

Installation

1. Clone the repository
```bash
git clone https://github.com/yourusername/water-quality-predictor.git
cd water-quality-predictor
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Run the web application
```bash
streamlit run water_quality_app.py
```

4. Access the app
   - Open your browser and navigate to `http://localhost:8501`

Alternative: Direct Installation

```bash
# Install required packages directly
pip install streamlit pandas scikit-learn matplotlib seaborn pytest numpy

# Download the project files and run
streamlit run water_quality_app.py
```


 🌟 Usage Examples
 Web Application
1. Open the Streamlit app
2. Input water quality parameters
3. Click "Predict Water Quality"
4. View results with confidence score

 Python API
```python
from src.prediction import predict_water_quality

# Sample water data
water_data = {
    'ph': 7.2,
    'Hardness': 158.3,
    'Solids': 15000.2,
    'Chloramines': 7.8,
    'Sulfate': 320.1,
    'Conductivity': 420.5,
    'Organic_carbon': 18.2,
    'Trihalomethanes': 72.1,
    'Turbidity': 3.8
}

result = predict_water_quality(water_data)
print(f"Water Quality: {result['prediction']}")
print(f"Confidence: {result['confidence']:.2%}")
```

🎯 SDG 6 Impact

This project directly contributes to Sustainable Development Goal 6 by:

- Ensuring Access: Helping communities identify safe water sources
- Preventing Disease: Early detection of contaminated water
- Reducing Costs: Avoiding expensive water treatment when unnecessary
- Empowering Communities: Providing tools for local water management
- Supporting Decision-Making: Data-driven water safety decisions

Target Beneficiaries
- Rural communities without access to water testing labs
- NGOs working in water and sanitation
- Community health workers
- Local government water management departments

🔧 Development Roadmap

 Week 1 Implementation
- [x] Days 1-2: Data analysis and preprocessing
- [x] Days 3-4: Model development and validation
- [x] Days 5-6: Web application deployment
- [x] Day 7: Testing and documentation

Future Enhancements
- [ ] Mobile app version (Android/iOS)
- [ ] IoT sensor integration
- [ ] Multi-language support
- [ ] Offline-first functionality
- [ ] GPS location tagging
- [ ] Historical data tracking
- [ ] Community reporting features

🔒 Ethical Considerations

- Bias Mitigation: Model tested across diverse water sources and geographic regions
- Transparency: Clear confidence intervals and model limitations provided
- Accessibility: Simple interface designed for users with varying technical skills
- Privacy: No personal data collection or storage
- Reliability: Clear disclaimers about model limitations and when to seek professional testing



 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

 🙏 Acknowledgments

- Dataset: Water Quality Dataset from Kaggle contributors
- UN SDG Framework: United Nations Sustainable Development Goals
- Open Source Community: Libraries and tools that made this project possible
 📞 Contact & Support



📊 Project Stats

![GitHub stars](https://img.shields.io/github/stars/MaggieWM-sketch/water-quality-predictor)
![GitHub forks](https://img.shields.io/github/forks/MaggieWM-sketch/water-quality-predictor)
![GitHub issues](https://img.shields.io/github/issues/MaggieWM-sketch/water-quality-predictor)


"Clean water is not a privilege, it's a human right. This tool helps make that right accessible to everyone."

*Made with ❤️ for global water security*
