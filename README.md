```txt
  ___  _____    ___                   _      __
 / _ \|_   _|  / _ \                 | |    / _|
/ /_\ \ | |   / /_\ \ __ _  ___ _ __ | |_  | |_ ___  _ __
|  _  | | |   |  _  |/ _` |/ _ \ '_ \| __| |  _/ _ \| '__|
| | | |_| |_  | | | | (_| |  __/ | | | |_  | || (_) | |
\_| |_/\___/  \_| |_/\__, |\___|_| |_|\__| |_| \___/|_|
                      __/ |
                     |___/
 _____                _   _                   _
|  ___|              | | (_)                 | |
| |__ _ __ ___   ___ | |_ _  ___  _ __   __ _| |
|  __| '_ ` _ \ / _ \| __| |/ _ \| '_ \ / _` | |
| |__| | | | | | (_) | |_| | (_) | | | | (_| | |
\____/_| |_| |_|\___/ \__|_|\___/|_| |_|\__,_|_|


 _____      _       _ _ _
|_   _|    | |     | | (_)
  | | _ __ | |_ ___| | |_  __ _  ___ _ __   ___ ___
  | || '_ \| __/ _ \ | | |/ _` |/ _ \ '_ \ / __/ _ \
 _| || | | | ||  __/ | | | (_| |  __/ | | | (_|  __/
 \___/_| |_|\__\___|_|_|_|\__, |\___|_| |_|\___\___|
                           __/ |
                          |___/
 ```

# Sentio - AI Agent for Emotional Intelligence 🤖

A sophisticated emotional AI companion platform that combines real-time computer vision, machine learning, and generative AI to detect, analyze, and respond to user emotions. Built with **Next.js**, **Flask**, **TensorFlow.js**, and **Mistral AI**.

---

## ✨ Features

- **👀 Real-time Emotion Detection**: Hybrid detection system using MediaPipe FaceMesh (Client-side) and OpenCV (Server-side) to detect 7 core emotions.
- **🤖 Context-Aware AI Chat**: Integrated Mistral AI chatbot that adapts its personality and responses based on your current emotional state.
- **📊 Interactive Dashboard**: Track your emotional trends with beautiful visualizations and real-time confidence metrics.
- **🔒 Privacy First**: Local-first processing where possible, with secure session management and data handling.
- **🎨 Modern UI/UX**: Stunning 3D visualizations (Spline), particle effects, and smooth Framer Motion animations.
- **🔄 Multimodal Interaction**: Combines visual input (face) with textual input (chat) for a holistic understanding of user state.

---

## 🛠️ Tech Stack

### Frontend
- **Framework**: Next.js 16 (App Router)
- **Language**: TypeScript
- **Styling**: Tailwind CSS 4, shadcn-ui components
- **ML/Vision**: TensorFlow.js, MediaPipe FaceMesh
- **3D & Animation**: Spline, Framer Motion

### Backend
- **Framework**: Flask 3.0 API
- **Language**: Python 3.9+
- **Database**: PostgreSQL (SQLAlchemy ORM)
- **AI/LLM**: Mistral AI SDK
- **Vision**: OpenCV (Haar Cascades)
- **Auth**: JWT (Flask-JWT-Extended)

---

## 📁 Project Structure

```txt
/
├─ backend/
│  ├─ app/
│  │  ├─ ml/              # Machine Learning logic (OpenCV)
│  │  ├─ models/          # Database models (User, DetectionLog)
│  │  └─ routes/          # API endpoints (Auth, Chat, Detection)
│  ├─ migrations/         # Database migrations
│  ├─ run.py              # App entry point
│  └─ requirements.txt    # Python dependencies
│
├─ frontend/
│  ├─ public/             # Static assets & 3D models
│  ├─ src/
│  │  ├─ app/             # Next.js Pages (Dashboard, Auth)
│  │  ├─ components/      # UI Components (ChatPanel, CameraEmotion)
│  │  ├─ contexts/        # React Context (Auth)
│  │  └─ services/        # API Client integration
│  └─ package.json        # Frontend dependencies
│
├─ models/                # ML Models (TFJS & FaceMesh files)
└─ README.md              # Documentation
```

---

## 🚀 Quick Start

### Prerequisites
- Node.js v18+
- Python 3.9+
- PostgreSQL database

### 1. Backend Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

# Create .env file with your credentials
# DATABASE_URL=postgresql://user:pass@localhost:5432/ai_demo_db
# MISTRAL_API_KEY=your_key_here

python run.py
```

### 2. Frontend Setup
```bash
cd frontend
npm install
npm run dev
```

Visit `http://localhost:3000` to start the application.

---

## 📸 Screenshots

*(Add your screenshots here)*
- **Landing Page**: Immersive 3D robot interaction.
- **Dashboard**: Real-time camera feed with mesh overlay and emotion metrics.
- **Chat Interface**: Context-aware conversation log.

---

## 🧩 Key Components

- **CameraEmotionTFJS**: Handles webcam stream and runs FaceMesh inference in-browser.
- **ChatPanel**: Manages chat state and communicates with the emotion-aware backend agent.
- **InteractiveRobotSpline**: Renders the 3D mascot that greets users.

---

## 💡 Development Tips

- **Emotion State**: The chat system can update the application's emotion state if the user explicitly states their feelings (e.g., "I am sad"), overriding the camera momentarily.
- **Hybrid Detection**: The client does the heavy lifting for visualization, while the server validates detection frames for data logging.

---

## 🤝 Contributing

Feel free to create issues or pull requests. Keep commits small and clear.

---

## 📝 License

This project is open source and available under the [MIT License](LICENSE).
