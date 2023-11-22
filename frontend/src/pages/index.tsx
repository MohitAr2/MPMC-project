import { useState } from "react";
import "tailwindcss/tailwind.css";
import axios from "axios";

const IndexPage = () => {
  const [inputValue, setInputValue] = useState("");
  const [response, setResponse] = useState("");
  const [chatHistory, setChatHistory] = useState<string[]>([]);

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setInputValue(e.target.value);
  };

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();

    try {
      const res = await axios.get("http://localhost:5000/answer", {
        params: {
          prompt: inputValue,
        },
      });

      setResponse(res.data);
      setChatHistory((prevHistory) => [...prevHistory, inputValue, res.data]);
      setInputValue("");
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100">
      <h1 className="text-3xl font-bold mb-4">Minemaw Chatbot</h1>
      <h1 className="text-lg font-bold mb-4">
        AI based law chatbot to respond to queries related to the Indian mining
        industries
      </h1>
      <div className="flex flex-col items-start justify-start w-3/4 h-96 bg-white border border-gray-300 rounded-lg p-4 overflow-auto">
        <div className="flex flex-col space-y-2">
          {chatHistory.map((message, index) => (
            <div className="flex flex-row items-center" key={index}>
              {index % 2 === 0 ? (
                <div className="w-4 h-4 bg-blue-400 rounded-full"></div>
              ) : (
                <div className="w-4 h-4 bg-yellow-400 rounded-full"></div>
              )}
              <p
                className={`ml-2 text-lg ${
                  index % 2 === 1 ? "text-black" : "text-gray-600"
                }`}
              >
                {message}
              </p>
            </div>
          ))}
        </div>
      </div>
      <form onSubmit={handleSubmit} className="flex flex-row items-center mt-4">
        <input
          type="text"
          value={inputValue}
          onChange={handleInputChange}
          className="border border-gray-300 rounded-l px-4 py-2 focus:outline-none"
        />
        <button
          type="submit"
          className="bg-blue-500 hover:bg-blue-600 text-white px-4 py-2 rounded-r focus:outline-none"
        >
          Send
        </button>
      </form>
    </div>
  );
};

export default IndexPage;
