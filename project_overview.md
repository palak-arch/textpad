# HealthBot - AI-Powered Health Assistant

HealthBot is a comprehensive health platform designed to provide reliable, AI-driven guidance on symptoms, disease prevention, and vaccinations.

## 🚀 Key Features

### 1. AI Health Chat 🤖
*   **Intelligent Responses**: Powered by Google's **Gemini Pro** model.
*   **Specialized Knowledge**: Trained to focus on disease prevention, hygiene, lifestyle, and vaccinations.
*   **Voice Input** 🎤: Speak your queries directly using the microphone button.
*   **Offline Mode**: Robust error handling that provides helpful fallback responses when internet or API availability is limited.

### 2. Health Center Locator 🏥
*   Find nearby health centers and clinics.
*   (Coming Soon: Interactive Map Integration).

### 3. Vaccination Tracker 💉 (In Progress)
*   Track vaccination history and upcoming schedules.
*   Age-based recommendations (Infant, Child, Adult).

### 4. Health Dashboard 📊 (Planned)
*   Personalized user profile.
*   Health metrics tracking.

---

## 🛠 Technology Stack

*   **Frontend**: [React](https://react.dev/) (v18) with [Vite](https://vitejs.dev/)
*   **Language**: [TypeScript](https://www.typescriptlang.org/)
*   **Styling**: [Tailwind CSS](https://tailwindcss.com/) & [Shadcn UI](https://ui.shadcn.com/)
*   **Backend**: [Supabase](https://supabase.com/) (PostgreSQL Database, Authentication)
*   **AI**: [Google Generative AI SDK](https://www.npmjs.com/package/@google/generative-ai)

---

## 📂 Project Structure

```
health/
├── src/
│   ├── components/         # Reusable UI components
│   │   ├── chat/           # Chat-specific components (ChatWindow, ChatInput)
│   │   ├── landing/        # Landing page sections
│   │   └── ui/             # Shadcn UI primitives (Button, Card, etc.)
│   ├── hooks/              # Custom React hooks
│   │   └── useHealthChat.ts # Main chat logic (AI & Supabase integration)
│   ├── pages/              # Page components
│   │   ├── Index.tsx       # Home/Landing Page
│   │   └── Chat.tsx        # Dedicated Chat Page
│   ├── integrations/       # Backend connections (Supabase client)
│   └── App.tsx             # Main router configuration
├── supabase/               # SQL migrations and config
└── public/                 # Static assets
```

---

## ⚡ Setup & Installation

1.  **Install Dependencies**:
    ```bash
    npm install
    ```

2.  **Environment Setup**:
    Create a `.env` file in the root directory with:
    ```env
    VITE_SUPABASE_URL="your_supabase_url"
    VITE_SUPABASE_PUBLISHABLE_KEY="your_supabase_key"
    VITE_GEMINI_API_KEY="your_gemini_api_key"
    ```

3.  **Run Development Server**:
    ```bash
    npm run dev
    ```
    Access the app at `http://localhost:8080`.

---

## 📝 Recent Changes

*   **v1.1 (Voice Input)**: Added Web Speech API support for microphone input in chat.
*   **v1.0 (Chat Page)**: Created dedicated `/chat` route and page.
*   **Fixes**: Resolved "Offline Mode" 404 error by switching to `gemini-pro`.
