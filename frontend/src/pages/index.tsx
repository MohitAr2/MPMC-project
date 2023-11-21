import { useState } from 'react';
import "tailwindcss/tailwind.css";
import axios from 'axios';

const IndexPage = () => {
  const [inputValue, setInputValue] = useState('');
  const [response, setResponse] = useState('');

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setInputValue(e.target.value);
  };

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();

    try {
      const res = await axios.post('http://localhost:5000/answer', {
        prompt: inputValue,
      });
      setResponse(res.data);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100">
      <h1 className="text-3xl font-bold mb-4">Minemaw Chatbot</h1>
      <form onSubmit={handleSubmit} className="flex flex-col items-center">
        <input
          type="text"
          value={inputValue}
          onChange={handleInputChange}
          className="border border-gray-300 rounded-l px-4 py-2 focus:outline-none mb-2"
        />
        <button
          type="submit"
          className="bg-blue-500 hover:bg-blue-600 text-white px-4 py-2 rounded-r focus:outline-none"
        >
          Send
        </button>
      </form>
      {response && (
        <div className="mt-4 p-4 bg-gray-200 rounded">
          <p>{response}</p>
        </div>
      )}
    </div>
  );
};

export default IndexPage;
