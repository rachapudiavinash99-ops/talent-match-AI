import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Users, RefreshCw, UploadCloud, Eye, FileText, Sparkles, Phone, Mail } from 'lucide-react';

const API_BASE = 'http://localhost:8000/api';

function Candidates() {
  const [candidates, setCandidates] = useState([]);
  const [showForm, setShowForm] = useState(false);
  const [formData, setFormData] = useState({ name: '', email: '', phone: '' });
  const [file, setFile] = useState(null);
  const [uploading, setUploading] = useState(false);

  const fetchCandidates = () => axios.get(`${API_BASE}/candidates/`).then(res => setCandidates(res.data));

  useEffect(() => { fetchCandidates(); }, []);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!file) {
      alert("Please upload a resume file (PDF or DOCX)");
      return;
    }
    setUploading(true);
    const data = new FormData();
    data.append('name', formData.name);
    data.append('email', formData.email);
    data.append('phone', formData.phone);
    data.append('file', file);

    try {
      await axios.post(`${API_BASE}/candidates/upload`, data, {
        headers: { 'Content-Type': 'multipart/form-data' }
      });
      setShowForm(false);
      setFile(null);
      setUploading(false);
      fetchCandidates();
    } catch (err) {
      console.error(err);
      alert("Error parsing and storing candidate resume");
      setUploading(false);
    }
  };

  return (
    <div className="animate-fade-in-up text-white">
      <div className="flex flex-col sm:flex-row sm:items-center justify-between pb-6 mb-8 border-b border-white/10">
        <div>
          <div className="inline-flex items-center space-x-1 text-xs font-bold uppercase tracking-widest text-[#a100ff] mb-1">
            <Sparkles className="w-3.5 h-3.5 mr-1" /> Candidate Intelligence Database
          </div>
          <h2 className="text-3xl font-black uppercase tracking-tight text-white">
            Talent Pool <span className="text-[#a100ff]">&gt;</span>
          </h2>
          <p className="text-gray-400 text-xs mt-1">Directly view parsed resumes, technical skill vectors, and applicant records.</p>
        </div>
        <div className="mt-4 sm:mt-0 flex gap-2">
          <button 
            onClick={fetchCandidates} 
            className="px-4 py-2 bg-white/5 hover:bg-white/10 border border-white/10 text-gray-300 rounded-xl text-xs font-bold uppercase tracking-wider transition-colors flex items-center"
          >
            <RefreshCw className="w-3.5 h-3.5 mr-1.5" /> Refresh
          </button>
          <button 
            onClick={() => setShowForm(!showForm)} 
            className="px-5 py-2 bg-[#a100ff] hover:bg-[#8800db] text-white rounded-xl text-xs font-bold uppercase tracking-wider transition-all shadow-[0_0_20px_rgba(161,0,255,0.4)] flex items-center"
          >
            {showForm ? 'Cancel' : '+ Ingest Resume'}
          </button>
        </div>
      </div>

      {showForm && (
        <form onSubmit={handleSubmit} className="accenture-card p-7 rounded-2xl mb-8 border border-white/10 animate-fade-in-up">
          <h3 className="text-lg font-bold uppercase text-white mb-4">Ingest &amp; Extract Resume</h3>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mb-4">
            <input 
              placeholder="Candidate Full Name" 
              className="bg-white/5 border border-white/10 p-3 rounded-xl text-white placeholder-gray-500 focus:outline-none focus:border-[#a100ff] text-sm" 
              required 
              onChange={e => setFormData({...formData, name: e.target.value})} 
            />
            <input 
              type="email" 
              placeholder="Corporate / Personal Email" 
              className="bg-white/5 border border-white/10 p-3 rounded-xl text-white placeholder-gray-500 focus:outline-none focus:border-[#a100ff] text-sm" 
              required 
              onChange={e => setFormData({...formData, email: e.target.value})} 
            />
            <input 
              placeholder="Phone (+91-...)" 
              className="bg-white/5 border border-white/10 p-3 rounded-xl text-white placeholder-gray-500 focus:outline-none focus:border-[#a100ff] text-sm" 
              onChange={e => setFormData({...formData, phone: e.target.value})} 
            />
            <div className="border border-white/10 bg-white/5 p-2.5 rounded-xl flex items-center justify-between">
              <span className="text-xs text-gray-400">PDF / DOCX File</span>
              <input 
                type="file" 
                accept=".pdf,.docx" 
                required 
                onChange={e => setFile(e.target.files[0])} 
                className="text-xs text-gray-400 file:mr-3 file:py-1 file:px-3 file:rounded-full file:border-0 file:text-xs file:font-bold file:bg-[#a100ff] file:text-white hover:file:bg-[#8800db]"
              />
            </div>
          </div>
          <button 
            type="submit" 
            disabled={uploading}
            className="px-6 py-3 bg-[#a100ff] hover:bg-[#8800db] text-white rounded-xl text-xs font-bold uppercase tracking-wider transition-all disabled:opacity-50"
          >
            {uploading ? "Extracting Candidate Vectors..." : "Extract & Index Resume >"}
          </button>
        </form>
      )}

      {/* Candidates Table */}
      <div className="accenture-card rounded-2xl border border-white/10 overflow-hidden">
        <table className="min-w-full divide-y divide-white/10 text-left">
          <thead className="bg-white/[0.02]">
            <tr>
              <th className="px-6 py-4 text-xs font-bold uppercase tracking-wider text-gray-400">Candidate</th>
              <th className="px-6 py-4 text-xs font-bold uppercase tracking-wider text-gray-400">Contact</th>
              <th className="px-6 py-4 text-xs font-bold uppercase tracking-wider text-gray-400">Extracted Skills Vector</th>
              <th className="px-6 py-4 text-xs font-bold uppercase tracking-wider text-gray-400 text-right">Actions</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-white/5">
            {candidates.length === 0 ? (
              <tr><td colSpan="4" className="px-6 py-8 text-center text-gray-500 text-xs">No candidate records found in database.</td></tr>
            ) : candidates.map(c => (
              <tr key={c.id} className="hover:bg-white/[0.02] transition-colors">
                <td className="px-6 py-4 whitespace-nowrap">
                  <div className="font-bold text-white text-sm">{c.name}</div>
                  <div className="text-[11px] text-gray-500">ID: {c.id}</div>
                </td>
                <td className="px-6 py-4 whitespace-nowrap text-xs text-gray-300">
                  <div className="flex items-center"><Mail className="w-3 h-3 text-[#a100ff] mr-1.5" /> {c.email}</div>
                  <div className="flex items-center text-gray-400 mt-1"><Phone className="w-3 h-3 text-gray-500 mr-1.5" /> {c.phone}</div>
                </td>
                <td className="px-6 py-4">
                  <div className="flex flex-wrap gap-1 max-w-md">
                    {c.skills && c.skills.map((skill, sIdx) => (
                      <span key={sIdx} className="px-2 py-0.5 rounded bg-purple-950/60 border border-purple-500/30 text-purple-200 text-[10px] font-semibold">
                        {skill}
                      </span>
                    ))}
                  </div>
                </td>
                <td className="px-6 py-4 whitespace-nowrap text-right text-xs">
                  <button 
                    onClick={() => alert(`Candidate Profile:\n\nName: ${c.name}\nEmail: ${c.email}\nPhone: ${c.phone}\nSkills: ${c.skills?.join(', ')}`)} 
                    className="text-[#a100ff] hover:text-purple-300 font-bold uppercase mr-4"
                  >
                    Profile
                  </button>
                  <button 
                    onClick={() => alert(`Downloading cached resume document for ${c.name}...`)} 
                    className="text-gray-400 hover:text-white font-bold uppercase"
                  >
                    Resume
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default Candidates;
