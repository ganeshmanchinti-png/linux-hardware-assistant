import { useEffect, useState } from "react";
import "./App.css";

function App() {
  const [hardware, setHardware] = useState(null);
  const [question, setQuestion] = useState("");
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);

  const API_URL = "http://localhost:8000";

  // Get hardware information
  const getHardware = async () => {
    try {
      const response = await fetch(`${API_URL}/hardware`);
      const data = await response.json();
      setHardware(data);
    } catch (error) {
      console.log("Hardware API Error:", error);
    }
  };

  useEffect(() => {
    getHardware();
  }, []);

  // Send question to AI
  const sendMessage = async () => {
    if (question.trim() === "" || loading) return;

    const userQuestion = question;

    setMessages((prev) => [...prev, { role: "user", text: userQuestion }]);

    setQuestion("");
    setLoading(true);

    try {
      const response = await fetch(`${API_URL}/chat`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          question: userQuestion,
        }),
      });

      const data = await response.json();

      setMessages((prev) => [...prev, { role: "ai", text: data.answer }]);
    } catch (error) {
      setMessages((prev) => [
        ...prev,
        { role: "ai", text: "Unable to connect to AI server." },
      ]);
    } finally {
      setLoading(false);
    }
  };

  const totalRam = hardware?.memory?.total
    ? (hardware.memory.total / 1024 ** 3).toFixed(2)
    : "Loading...";

  return (
    <div className="app">
      <header className="header">
        <div className="logo">💻 Linux Hardware Assistant</div>
        <span className="status">● AI Assistant</span>
      </header>

      <main className="container">
        <section className="welcome">
          <h1>Welcome to Hardware Assistant</h1>
          <p>Ask questions about your Linux system hardware.</p>
        </section>

        <section className="hardware-section">
          <h2>System Information</h2>

          <div className="hardware-grid">
            <div className="hardware-card">
              <span>🖥️</span>
              <h3>Processor</h3>
              <p>{hardware?.cpu?.model_name || "Loading..."}</p>
              <small>{hardware?.cpu?.cpu_cores || "--"} Cores</small>
            </div>

            <div className="hardware-card">
              <span>🧠</span>
              <h3>Memory</h3>
              <p>{totalRam} GB</p>
              <small>Total RAM</small>
            </div>

            <div className="hardware-card">
              <span>🎮</span>
              <h3>Graphics</h3>
              <p>
                {hardware?.gpu?.length > 0
                  ? "GPU detected"
                  : hardware
                    ? "Not detected"
                    : "Loading..."}
              </p>
              <small>Graphics device</small>
            </div>

            <div className="hardware-card">
              <span>💾</span>
              <h3>Storage</h3>

              <p>{hardware?.storage?.length ?? "Loading..."} Devices</p>

              {hardware?.storage?.map((disk) => (
                <small key={disk.name}>
                  {disk.name} - {(disk.size / 1024 ** 3).toFixed(2)} GB
                  <br />
                </small>
              ))}
            </div>
          </div>
        </section>

        <section className="chat-section">
          <h2>AI Hardware Chat</h2>
          <p className="chat-description">
            Ask anything about your computer hardware.
          </p>

          <div className="chat-box">
            <div className="messages">
              {messages.length === 0 && (
                <div className="empty-message">
                  <span>🤖</span>
                  <h3>Hello! How can I help you?</h3>
                  <p>Try asking: What is my CPU?</p>
                </div>
              )}

              {messages.map((message, index) => (
                <div key={index} className={`message ${message.role}`}>
                  <strong>
                    {message.role === "user" ? "You" : "AI Assistant"}
                  </strong>
                  <p>{message.text}</p>
                </div>
              ))}

              {loading && <p className="loading">AI is thinking...</p>}
            </div>

            <div className="chat-input">
              <input
                type="text"
                placeholder="Ask about your hardware..."
                value={question}
                onChange={(event) => setQuestion(event.target.value)}
                onKeyDown={(event) => {
                  if (event.key === "Enter") sendMessage();
                }}
              />

              <button onClick={sendMessage} disabled={loading}>
                Send
              </button>
            </div>
          </div>
        </section>
      </main>
    </div>
  );
}

export default App;
