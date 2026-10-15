import React, { useState } from 'react';
import { BrowserRouter as Router, Routes, Route, Link, useNavigate, useLocation } from 'react-router-dom';
import { LayoutDashboard, Briefcase, Users, FileText, BarChart, Settings, LogOut, Globe, ChevronRight } from 'lucide-react';
import ElevateIQHome from './pages/ElevateIQHome';
import Dashboard from './pages/Dashboard';
import Jobs from './pages/Jobs';
import Candidates from './pages/Candidates';
import Applications from './pages/Applications';
import ReportsPage from './pages/Reports';
import SettingsPage from './pages/Settings';

// ------------------------------------
// ElevateIQ Recruiter Portal Login
// ------------------------------------
function LoginScreen() {
  const navigate = useNavigate();
  const [creds, setCreds] = useState({ id: '', password: '' });

  const handleLogin = (e) => {
    e.preventDefault();
    if (creds.id && creds.password) {
      navigate('/dashboard');
    }
  };

  return (
    <div className="min-h-screen bg-[#06091A] flex flex-col justify-center py-12 sm:px-6 lg:px-8 relative overflow-hidden text-white">
      {/* Ambient Glow */}
      <div className="absolute top-0 right-1/4 w-96 h-96 bg-[#ff8a3d]/15 rounded-full blur-[140px] pointer-events-none"></div>
      <div className="absolute bottom-0 left-1/4 w-96 h-96 bg-[#3fd0ff]/15 rounded-full blur-[140px] pointer-events-none"></div>
      
      <div className="sm:mx-auto sm:w-full sm:max-w-md relative z-10 text-center animate-fade-in-up">
        <a href="/" className="inline-flex items-center justify-center mb-6 group">
          <img 
            src="https://elevateiq-softtech.com/images/logo.png" 
            alt="ElevateIQ" 
            className="h-12 w-auto object-contain filter drop-shadow-[0_0_12px_rgba(63,208,255,0.4)] hover:scale-105 transition-transform"
          />
        </a>
        <h2 className="text-2xl font-black uppercase tracking-tight text-white">
          Recruiter Command Center
        </h2>
        <p className="mt-2 text-xs font-semibold text-gray-400 uppercase tracking-wider">
          ElevateIQ AI Resume Screening &amp; Talent Platform
        </p>
      </div>

      <div className="mt-8 sm:mx-auto sm:w-full sm:max-w-md relative z-10 animate-fade-in-up-delay-1 px-4 sm:px-0">
        <div className="elevate-card py-8 px-6 sm:px-10 rounded-2xl shadow-2xl border border-white/10">
          <form className="space-y-6" onSubmit={handleLogin}>
            <div>
              <label className="block text-xs font-bold uppercase tracking-wider text-gray-300 mb-2">
                Recruiter Email / Enterprise ID
              </label>
              <input 
                required 
                type="text" 
                placeholder="recruiter@elevateiq-softtech.com" 
                className="block w-full px-4 py-3 bg-white/5 border border-white/10 rounded-xl text-white placeholder-gray-500 focus:outline-none focus:border-[#3fd0ff] text-sm" 
                value={creds.id} 
                onChange={e => setCreds({...creds, id: e.target.value})} 
              />
            </div>

            <div>
              <label className="block text-xs font-bold uppercase tracking-wider text-gray-300 mb-2">
                Password
              </label>
              <input 
                required 
                type="password" 
                placeholder="Enter password (demo mode)" 
                className="block w-full px-4 py-3 bg-white/5 border border-white/10 rounded-xl text-white placeholder-gray-500 focus:outline-none focus:border-[#3fd0ff] text-sm" 
                value={creds.password} 
                onChange={e => setCreds({...creds, password: e.target.value})} 
              />
            </div>

            <div className="flex items-center justify-between text-xs">
              <a href="/" className="font-semibold text-gray-400 hover:text-white transition-colors">
                &larr; Return to ElevateIQ Home
              </a>
              <span className="text-gray-500">SSO Protected</span>
            </div>

            <button 
              type="submit" 
              className="w-full flex justify-center items-center py-3.5 px-4 rounded-xl text-xs font-bold uppercase tracking-wider text-white bg-gradient-to-r from-[#ff8a3d] to-[#f2701c] hover:brightness-110 transition-all shadow-[0_0_20px_rgba(255,138,61,0.4)]"
            >
              Sign In to Recruiter Console &gt;
            </button>
          </form>
        </div>
      </div>
    </div>
  );
}

// ------------------------------------
// ElevateIQ Recruiter Layout
// ------------------------------------
function AdminLayout({ children }) {
  const location = useLocation();

  const navItems = [
    { name: 'Dashboard', path: '/dashboard', icon: <LayoutDashboard className="w-4 h-4 mr-3" /> },
    { name: 'Job Requisitions', path: '/jobs', icon: <Briefcase className="w-4 h-4 mr-3" /> },
    { name: 'Candidate Database', path: '/candidates', icon: <Users className="w-4 h-4 mr-3" /> },
    { name: 'AI Match Pipeline', path: '/applications', icon: <FileText className="w-4 h-4 mr-3" /> },
    { name: 'Recruitment Analytics', path: '/reports', icon: <BarChart className="w-4 h-4 mr-3" /> },
    { name: 'Platform Settings', path: '/settings', icon: <Settings className="w-4 h-4 mr-3" /> },
  ];

  return (
    <div className="flex h-screen bg-[#06091A] text-white overflow-hidden">
      
      {/* ElevateIQ Recruiter Sidebar */}
      <div className="w-64 bg-[#0a0f24] border-r border-white/10 flex flex-col justify-between">
        <div>
          {/* Logo */}
          <div className="p-6 border-b border-white/10">
            <Link to="/" className="flex items-center group">
              <img 
                src="https://elevateiq-softtech.com/images/logo.png" 
                alt="ElevateIQ" 
                className="h-9 w-auto object-contain hover:scale-105 transition-transform"
              />
            </Link>
            <p className="text-[10px] font-bold uppercase tracking-widest text-[#ff8a3d] mt-1">
              Recruiter Console
            </p>
          </div>
          
          {/* Nav List */}
          <nav className="mt-4 px-3 space-y-1">
            <div className="px-3 py-2 text-[10px] font-bold uppercase tracking-widest text-gray-400">
              Navigation
            </div>
            {navItems.map((item) => {
              const active = location.pathname === item.path;
              return (
                <Link 
                  key={item.path} 
                  to={item.path} 
                  className={`flex items-center px-3 py-2.5 rounded-xl text-xs font-semibold tracking-wide transition-all ${
                    active 
                      ? 'bg-gradient-to-r from-[#ff8a3d] to-[#f2701c] text-white shadow-[0_0_15px_rgba(255,138,61,0.4)]' 
                      : 'text-gray-400 hover:text-white hover:bg-white/5'
                  }`}
                >
                  {item.icon}
                  {item.name}
                </Link>
              );
            })}
          </nav>
        </div>
        
        {/* Sidebar Footer */}
        <div className="p-4 border-t border-white/10 space-y-2">
          <Link 
            to="/" 
            className="w-full flex items-center justify-center px-3 py-2 bg-white/5 hover:bg-white/10 border border-white/10 rounded-xl text-xs font-semibold text-gray-300 transition-colors"
          >
            <Globe className="w-3.5 h-3.5 mr-2 text-[#3fd0ff]" />
            ElevateIQ Global Site
          </Link>
          <Link 
            to="/" 
            className="w-full flex items-center justify-center px-3 py-2 text-red-400 hover:bg-red-950/30 rounded-xl text-xs font-semibold transition-colors"
          >
            <LogOut className="w-3.5 h-3.5 mr-2" />
            Sign Out
          </Link>
        </div>
      </div>

      {/* Main Workspace Area */}
      <div className="flex-1 overflow-auto bg-[#070b1e]">
        <main className="p-8">
          {children}
        </main>
      </div>
    </div>
  );
}

function App() {
  return (
    <Router>
      <Routes>
        {/* Main ElevateIQ Corporate Portal */}
        <Route path="/" element={<ElevateIQHome />} />
        <Route path="/careers" element={<ElevateIQHome />} />
        
        {/* ElevateIQ Recruiter Authentication */}
        <Route path="/login" element={<LoginScreen />} />
        
        {/* Recruiter Console Routes */}
        <Route path="/dashboard" element={<AdminLayout><Dashboard /></AdminLayout>} />
        <Route path="/jobs" element={<AdminLayout><Jobs /></AdminLayout>} />
        <Route path="/candidates" element={<AdminLayout><Candidates /></AdminLayout>} />
        <Route path="/applications" element={<AdminLayout><Applications /></AdminLayout>} />
        <Route path="/reports" element={<AdminLayout><ReportsPage /></AdminLayout>} />
        <Route path="/settings" element={<AdminLayout><SettingsPage /></AdminLayout>} />
      </Routes>
    </Router>
  );
}

export default App;
