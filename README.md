# My Locality! 🗺️

[![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)](https://djangoproject.com/)
[![Google Maps](https://img.shields.io/badge/Google%20Maps-4285F4?style=for-the-badge&logo=google-maps&logoColor=white)](https://developers.google.com/maps)
[![Firebase](https://img.shields.io/badge/Firebase-039BE5?style=for-the-badge&logo=Firebase&logoColor=white)](https://firebase.google.com/)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)

**🏆 First Prize Winner - PALS Event 2022 (Analyze Case Study)**  
*Awarded among 100+ teams for innovative application design and functionality*

A location-based web application that discovers nearby attractions and events based on user preferences, complete with navigation routes and smart filtering options.

## 🎯 Overview

My Locality! is a Django-powered web application that leverages Google APIs to help users discover what's happening around them. Whether you're looking for events, attractions, or activities, this app provides personalized recommendations with turn-by-turn navigation.

## ✨ Features

### 🌍 Location Services
- **Auto-Detection**: Automatically detects user's current location
- **Manual Input**: Option to search for specific locations
- **Real-time Updates**: Live location tracking for dynamic results

### 🎪 Smart Discovery
- **Nearby Attractions**: Discover popular places and landmarks
- **Local Events**: Find ongoing and upcoming events
- **Personalized Results**: Tailored recommendations based on user preferences

### 🔍 Advanced Filtering
- **Time-based Filters**: Filter events by start time and duration
- **Category Selection**: Choose from various event/attraction categories
- **Distance Range**: Set preferred search radius
- **Date Selection**: Find events for specific dates

### 🗺️ Navigation Integration
- **Route Planning**: Get directions to selected destinations
- **Multiple Transport Modes**: Walking, driving, public transport options
- **Real-time Traffic**: Live traffic updates for optimal routing

## 🛠️ Tech Stack

- **Backend**: Django (Python)
- **Database**: Firebase Firestore
- **APIs**: 
  - Google Maps JavaScript API
  - Google Places API
  - Google Events API
  - Google Directions API
- **Frontend**: HTML, CSS, JavaScript
- **Deployment**: Firebase Hosting

## 🚀 Quick Start

### Prerequisites
- Python 3.6+
- Django 4.0+
- Google Cloud Platform account
- Firebase project

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/vaarunx/mylocality.git
cd mylocality
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Configure API Keys**
Create a `config/settings.py` file:
```python
# Google APIs Configuration
GOOGLE_MAPS_API_KEY = 'your-google-maps-api-key'
GOOGLE_PLACES_API_KEY = 'your-google-places-api-key'
GOOGLE_EVENTS_API_KEY = 'your-google-events-api-key'

# Firebase Configuration
FIREBASE_CONFIG = {
    'apiKey': 'your-firebase-api-key',
    'authDomain': 'your-project.firebaseapp.com',
    'projectId': 'your-project-id',
    # ... other config
}
```

5. **Run migrations**
```bash
python manage.py migrate
```

6. **Start development server**
```bash
python manage.py runserver
```

Visit `http://localhost:8000` to see the application in action!

## 📱 Usage

1. **Enable Location**: Allow the app to access your location
2. **Set Preferences**: Choose categories and filters
3. **Discover**: Browse nearby attractions and events
4. **Navigate**: Get directions to your chosen destination
5. **Explore**: Enjoy your local discoveries!

## 🗂️ Project Structure

```
mylocality/
├── config/              # Django settings and configuration
├── mylocality/          # Main application directory
│   ├── models.py        # Database models
│   ├── views.py         # Application views
│   ├── urls.py          # URL routing
│   └── templates/       # HTML templates
├── templates/           # Global templates
├── static/              # CSS, JS, images
├── requirements.txt     # Python dependencies
├── manage.py           # Django management script
└── db.sqlite3          # Local database file
```

## 🔧 Configuration

### Google APIs Setup
1. Enable Google Maps, Places, and Events APIs in Google Cloud Console
2. Create API credentials and restrict them appropriately
3. Add your domain to authorized domains

### Firebase Setup
1. Create a Firebase project
2. Enable Firestore database
3. Configure authentication (optional)
4. Download configuration file

## 🏆 Recognition

**PALS Event 2022 - Analyze Case Study Competition**
- 🥇 **First Prize** among 100+ participating teams
- Recognized for innovative application design and functionality
- Demonstrated practical solution for location-based discovery

## 🚀 Future Enhancements

### Google Chrome Extension
- Browser plugin for quick local discovery
- Integration with Google Calendar for event planning
- Offline mode for saved locations

### Enhanced Features
- **Social Integration**: Share discoveries with friends
- **Review System**: User ratings and reviews for places
- **AI Recommendations**: Machine learning-based suggestions
- **Augmented Reality**: AR navigation and information overlay
- **Multi-language Support**: Localization for different regions

### Mobile Application
- Native iOS and Android apps
- Push notifications for nearby events
- Location-based reminders

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
- GitHub: [@vaarunx](https://github.com/vaarunx)
- Project Link: [https://github.com/vaarunx/mylocality](https://github.com/vaarunx/mylocality)

---

**Made with ❤️ for local exploration and discovery**
