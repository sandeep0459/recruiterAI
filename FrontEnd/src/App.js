import React, { useState, useEffect, useRef } from "react";
import "./App.css";

const suggestions = [
  "Who is Pranes Gopalan Venkatesh?",
  "Does Pranes code?",
  "What are Pranes's skills?",
  "How was this resume AI coded?",
  "Tell me about Pranes's automation experience",
  "How can I build my own Resume AI?",
];

function App() {
  const [question, setQuestion] = useState("");
  const [messages, setMessages] = useState([
    { sender: "bot", text: "👋 Hi, I'm Pranes's Resume AI. Ask me anything!" },
  ]);
  const [loading, setLoading] = useState(false);
  const chatRef = useRef(null);

  const sendMessage = async (q) => {
    if (!q.trim()) return;
    const userMsg = { sender: "user", text: q };
    setMessages((prev) => [...prev, userMsg]);
    setQuestion("");
    setLoading(true);

    try {
      const res = await fetch("https://resume-ai-v884.onrender.com/ask", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ question: q }),
      });

      const data = await res.json();
      setMessages((prev) => [...prev, { sender: "bot", text: data.answer }]);
    } catch (err) {
      setMessages((prev) => [
        ...prev,
        { sender: "bot", text: "⚠️ Error connecting to backend." },
      ]);
    }

    setLoading(false);
  };

  const handleSubmit = () => {
    if (loading || !question.trim()) return; // prevent sending while loading
    sendMessage(question.trim());
  };

  useEffect(() => {
    chatRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages, loading]);

  return (
    <div className="container">
      <aside className="sidebar">
        <img src="/profilepic.png" className="avatar" alt="AI Avatar" />
        <h2>Resume AI</h2>
        <p className="subtext">Ask about my experience, skills, and more.</p>
        <div className="suggestions">
          {suggestions.map((s, i) => (
            <button key={i} onClick={() => sendMessage(s)}>
              {s}
            </button>
          ))}
        </div>
      </aside>

      <main className="chat-section">
        <div className="chat-window">
          {messages.map((msg, idx) => (
            <div key={idx} className={`chat-row ${msg.sender}`}>
              {msg.sender === "bot" && (
                <img
                  src="/chat_bot.png"
                  className="bubble-avatar"
                  alt="bot avatar"
                />
              )}
              <div className={`bubble ${msg.sender}`}>{msg.text}</div>
            </div>
          ))}

          {loading && (
            <div className="chat-row bot">
              <img
                src="/chat_bot.png"
                className="bubble-avatar"
                alt="bot typing"
              />
              <div className="bubble bot">
                <div className="typing-indicator">
                  <div className="typing-dot"></div>
                  <div className="typing-dot"></div>
                  <div className="typing-dot"></div>
                </div>
              </div>
            </div>
          )}

          <div ref={chatRef} />
        </div>

        {/* Wrap input-bar inside a sticky wrapper */}
        <div className="input-wrapper">
          <div className="input-bar">
            <input
              placeholder="Type your question here..."
              value={question}
              onChange={(e) => setQuestion(e.target.value)}
              onKeyDown={(e) => {
                if (e.key === "Enter" && !loading) handleSubmit();
              }}
            />
            <button onClick={handleSubmit} disabled={loading}>
              Send
            </button>
          </div>
        </div>
      </main>
    </div>
  );
}

export default App;
