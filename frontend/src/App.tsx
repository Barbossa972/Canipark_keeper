import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

interface LoginCredentials {
  username: string;
  password: string;
}

interface LoginFormProps {
  onLogin: (credentials: LoginCredentials) => Promise<void>;
  onError?: (message: string) => void;
}

const LoginForm: React.FC<LoginFormProps> = ({ onLogin, onError }) => {
  const [username, setUsername] = useState<string>('');
  const [password, setPassword] = useState<string>('');
  const [errors, setErrors] = useState<{ username?: string; password?: string }>({});

  const validateForm = (): boolean => {
    const newErrors: { username?: string; password?: string } = {};
    
    if (!username.trim()) {
      newErrors.username = 'Username is required';
    }
    
    if (!password) {
      newErrors.password = 'Password is required';
    } else if (password.length < 6) {
      newErrors.password = 'Password must be at least 6 characters';
    }
    
    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const handleSubmit = async (): Promise<void> => {
    if (validateForm()) {
      await onLogin({ username, password });
      setUsername('');
      setPassword('');
      setErrors({});
    } else {
      onError?.('Please fix the form errors');
    }
  };

  return (
    <>
      <div>
        <input
          id="Username"
          type='Text'
          placeholder='Enter your username'
          value={username}
          onChange={e => setUsername(e.target.value)}
        />
      </div>
      <div>
        <input
          id="Password"
          type='password'
          placeholder='Enter your password'
          value={password}
          onChange={e => setPassword(e.target.value)}
        />
      </div>
      <button onClick={handleSubmit}>Login</button>
    </>
  );
}

const App: React.FC = () => {
  const [user, setUser] = useState<string | null>(null);
  const [message, setMessage] = useState<string>('');
  const [isLoading, setIsLoading] = useState<boolean>(false);

 
  const handleLogin = async (credentials: LoginCredentials): Promise<void> => {
    setIsLoading(true);
    setMessage('');
    
    try {
      // Type the Promise explicitly
      await new Promise<void>(resolve => setTimeout(resolve, 1000));
      
      if (credentials.username === 'admin' && credentials.password === 'password123') {
        setUser(credentials.username);
        setMessage(`Welcome back, ${credentials.username}!`);
      } else {
        setMessage('Invalid credentials. Try username: "admin", password: "password123"');
      }
    } catch (error: unknown) {
      // Proper error handling with type guards
      if (error instanceof Error) {
        setMessage(`Login failed: ${error.message}`);
      } else {
        setMessage('An unexpected error occurred.');
      }
    } finally {
      setIsLoading(false);
    }
  };

  const handleLoginError = (errorMessage: string): void => {
    setMessage(errorMessage);
  };

  const handleLogout = (): void => {
    setUser(null);
    setMessage('');
  };

  
  return (
    <>
    {!user ? (
      <div>
        <h1>Welcome to the canipark</h1>
        <LoginForm 
          onLogin={handleLogin} 
          onError={handleLoginError}
        />
        <div>
        {isLoading && (
              <div className="text-center mt-4">
                <p className="text-blue-600">Logging in...</p>
              </div>
            )}
            
            {message && (
              <div className={`text-center mt-4 p-3 rounded ${
                message.includes('Welcome') 
                  ? 'bg-green-100 text-green-800' 
                  : 'bg-red-100 text-red-800'
              }`}>
                {message}
              </div>
            )}
            
            <div className="text-center mt-6 p-4 bg-blue-50 rounded-lg">
              <p className="text-sm text-gray-600">
                Demo credentials:<br />
                Username: <strong>admin</strong><br />
                Password: <strong>password123</strong>
              </p>
            </div>
          </div>
      </div>
    ):(<div className="max-w-md mx-auto text-center">
            <div className="bg-white p-6 rounded-lg shadow-md">
              <h2 className="text-2xl font-bold text-green-600 mb-4">
                Login Successful! 🎉
              </h2>
              <p className="text-gray-700 mb-4">
                Logged in as: <strong>{user}</strong>
              </p>
              <button
                onClick={handleLogout}
                className="bg-red-600 text-white py-2 px-4 rounded-md hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-red-500 focus:ring-offset-2 transition duration-200"
              >
                Logout
              </button>
            </div>
          </div>
        )}
    </>
  );
}

export default App
