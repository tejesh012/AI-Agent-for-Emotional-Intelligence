# Sentio - AI Vision & Emotion Analysis Platform

## 1. Project Overview
Sentio is an advanced emotional AI companion web application that integrates real-time computer vision, machine learning, and generative AI to detect, analyze, and respond to user emotions. It features a modern, responsive frontend and a robust Python backend, providing users with insights into their emotional state and an empathetic chatbot companion.

## 2. Architecture High-Level
The project follows a decoupled client-server architecture:
- **Frontend**: Next.js 16 (React 19) application using the App Router. Handles UI, client-side webcam processing, and 3D visualizations.
- **Backend**: Flask 3.0 API. Handles authentication, database management, server-side image processing, and LLM integration.
- **Database**: PostgreSQL. Stores user data, sessions, and detection logs.
- **AI/ML Layer**: Hybrid approach using both client-side (MediaPipe/TensorFlow.js) for real-time mesh rendering and server-side (OpenCV) for validation, plus Mistral AI for natural language generation.

---

## 3. Tech Stack & Dependencies

### Frontend
- **Framework**: Next.js 16.1.6 (App Router), React 19.2.3
- **Language**: TypeScript
- **Styling**: Tailwind CSS 4, CSS Variables, `clsx`, `tailwind-merge`
- **UI Components**: Radix UI primitives (`@radix-ui/react-slot`)
- **Animations**: Framer Motion (`framer-motion`)
- **3D Graphics**: Spline (`@splinetool/react-spline`)
- **Machine Learning (Client)**:
  - `@tensorflow/tfjs`
  - `@mediapipe/face_mesh`
- **Icons**: Lucide React
- **Particles**: `tsparticles`

### Backend
- **Framework**: Flask 3.0.0
- **Language**: Python 3.9+
- **Database ORM**: Flask-SQLAlchemy (SQLAlchemy 2.0)
- **Migrations**: Flask-Migrate (Alembic)
- **Authentication**: Flask-JWT-Extended
- **Security**: Flask-Bcrypt (Password hashing), Flask-CORS
- **Computer Vision**: OpenCV (`opencv-python-headless`), NumPy, Pillow
- **Generative AI**: Mistral AI SDK (`mistralai`)
- **Database Driver**: `psycopg` (PostgreSQL adapter)

---

## 4. Key Components & Implementation Details

### A. Real-Time Emotion Detection (Hybrid System)
Sentio uses a unique dual-layer detection strategy:

1.  **Client-Side (Primary Visuals)**:
    -   **File**: `frontend/src/components/CameraEmotionTFJS.tsx`
    -   **Tech**: MediaPipe FaceMesh & TensorFlow.js.
    -   **Function**: Captures webcam stream, runs inference in the browser to detect 468 facial landmarks.
    -   **Output**: Draws the face mesh overlay on an HTML5 Canvas aligned with the video feed. Calculates emotion probabilities locally using a lightweight model loaded from `/public/models/tfjs_landmark_model/`.
    -   **Smoothing**: Implements Exponential Moving Average (EMA) to prevent jitter in detection results.

2.  **Server-Side (Validation & Logging)**:
    -   **File**: `backend/app/ml/face_detection.py`
    -   **Tech**: OpenCV (Haar Cascades).
    -   **Function**: Processes base64 image frames sent to `/api/detection/analyze`.
    -   **Logic**:
        -   Detects faces (`haarcascade_frontalface_default.xml`).
        -   Detects eyes and smiles (`haarcascade_eye.xml`, `haarcascade_smile.xml`).
        -   Infers emotion based on heuristic combinations (e.g., Smile + Open Eyes = Happy).
    -   **Purpose**: Provides a second opinion and logs verifiable detection data to the database.

### B. Intelligent Chat System
The chatbot is context-aware and adapts to the user's detected emotion.

-   **File**: `backend/app/routes/chat.py`
-   **Integration**: Uses `mistralai` to communicate with the Mistral Small model.
-   **Workflow**:
    1.  **Context Injection**: The system prompt is dynamically updated with the user's current emotion (detected via camera or self-reported).
    2.  **History**: Maintains conversation history for context.
    3.  **Emotion Extraction**: The backend parses the LLM response for hidden tags like `[EMOTION:SAD]` to update the application state if the user expresses a mood change in text (e.g., "I'm actually feeling happy now").
    4.  **Fallback**: If the LLM API fails, it falls back to a deterministic keyword-matching system (`KNOWLEDGE_BASE`) to ensure high availability.

### C. Database Schema
Defined in `backend/app/models/user.py`:

1.  **User**:
    -   Core identity (`id`, `email`, `username`, `password_hash`).
    -   Profile (`first_name`, `last_name`, `avatar_url`).
    -   Metadata (`created_at`, `last_login`).

2.  **UserSession**:
    -   Manages JWT refresh tokens (`refresh_token`).
    -   Tracks device info (`ip_address`, `device_info`) for security.

3.  **DetectionLog**:
    -   Stores analysis history (`user_id`, `detection_type`).
    -   Saves raw results (`result_data` JSON) and confidence scores for analytics dashboard.

### D. Authentication
-   **Flow**: JWT (JSON Web Token) based.
-   **Access Token**: Short-lived, used for API requests.
-   **Refresh Token**: Long-lived, stored in DB, used to generate new access tokens.
-   **Endpoints**: `/api/auth/register`, `/api/auth/login`, `/api/auth/refresh`.

---

## 5. Application Structure

### Frontend Structure (`/frontend`)
-   `src/app`: App Router pages (Dashboard, Auth, Landing).
-   `src/components/blocks`: Complex UI blocks (3D Robot, Features).
-   `src/components/ui`: Reusable UI components (Buttons, Cards, Chat Panel).
-   `src/services`: API client definitions (`api.ts`).
-   `src/contexts`: React Context for global state (AuthContext).

### Backend Structure (`/backend`)
-   `app/routes`: API endpoints grouped by feature (Auth, User, Detection, Chat).
-   `app/models`: SQLAlchemy database models.
-   `app/ml`: Machine learning logic and service classes.
-   `migrations`: Database migration scripts.
-   `run.py`: Application entry point.

---

## 6. Running Locally

### Prerequisites
-   Node.js v18+
-   Python 3.9+
-   PostgreSQL

### Steps
1.  **Database**: Create a Postgres database named `ai_demo_db`.
2.  **Backend**:
    ```bash
    cd backend
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    # Configure .env with DATABASE_URL and MISTRAL_API_KEY
    python run.py
    ```
3.  **Frontend**:
    ```bash
    cd frontend
    npm install
    npm run dev
    ```
4.  **Access**: Open `http://localhost:3000`.
