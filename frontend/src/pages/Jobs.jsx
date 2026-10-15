import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Briefcase, Plus, RefreshCw, Trash2, Eye, MapPin, Sparkles } from 'lucide-react';

const API_BASE = 'http://localhost:8000/api';

function Jobs() {
  const [jobs, setJobs] = useState([]);
  const [showForm, setShowForm] = useState(false);
  const [formData, setFormData] = useState({
    title: '', department: '', location: '', description: '',
    required_skills: '', preferred_skills: '', min_experience_years: 0, education_requirement: ''
  });

  const fetchJobs = () => axios.get(`${API_BASE}/jobs/`).then(res => setJobs(res.data));

  useEffect(() => { fetchJobs(); }, []);

  const handleSubmit = async (e) => {
    e.preventDefault();
    const payload = {
      ...formData,
      required_skills: formData.required_skills.split(',').map(s => s.trim()),
      preferred_skills: formData.preferred_skills.split(',').map(s => s.trim())
    };
    await axios.post(`${API_BASE}/jobs/`, payload);
    setShowForm(false);
    fetchJobs();
  };

  const handleDelete = async (id) => {
    if (window.confirm("Delete this job requisition?")) {
      await axios.delete(`${API_BASE}/jobs/${id}`);
      fetchJobs();
    }
  };

  return (
    <div className="animate-fade-in-up text-white">
      <div className="flex flex-col sm:flex-row sm:items-center justify-between pb-6 mb-8 border-b border-white/10">
        <div>
          <div className="inline-flex items-center space-x-1 text-xs font-bold uppercase tracking-widest text-[#a100ff] mb-1">
            <Sparkles className="w-3.5 h-3.5 mr-1" /> Accenture Requisition Engine
          </div>
          <h2 className="text-3xl font-black uppercase tracking-tight text-white">
            Job Requisitions <span className="text-[#a100ff]">&gt;</span>
          </h2>
          <p className="text-gray-400 text-xs mt-1">Manage corporate job postings synced directly with the Accenture India Careers portal.</p>
        </div>
        <div className="mt-4 sm:mt-0 flex gap-2">
          <button 
            onClick={fetchJobs} 
            className="px-4 py-2 bg-white/5 hover:bg-white/10 border border-white/10 text-gray-300 rounded-xl text-xs font-bold uppercase tracking-wider transition-colors flex items-center"
          >
            <RefreshCw className="w-3.5 h-3.5 mr-1.5" /> Refresh
          </button>
          <button 
            onClick={() => setShowForm(!showForm)} 
            className="px-5 py-2 bg-[#a100ff] hover:bg-[#8800db] text-white rounded-xl text-xs font-bold uppercase tracking-wider transition-all shadow-[0_0_20px_rgba(161,0,255,0.4)] flex items-center"
          >
            {showForm ? 'Cancel Requisition' : '+ Post New Requisition'}
          </button>
        </div>
      </div>

      {showForm && (
        <form onSubmit={handleSubmit} className="accenture-card p-7 rounded-2xl mb-8 border border-white/10 animate-fade-in-up">
          <h3 className="text-lg font-bold uppercase text-white mb-4">Create Enterprise Position</h3>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            <input 
              placeholder="Job Title (e.g. Senior Cloud Architect)" 
              className="bg-white/5 border border-white/10 p-3 rounded-xl text-white placeholder-gray-500 focus:outline-none focus:border-[#a100ff] text-sm" 
              required 
              onChange={e => setFormData({...formData, title: e.target.value})} 
            />
            <input 
              placeholder="Department (Engineering, AI, Consulting, Data)" 
              className="bg-white/5 border border-white/10 p-3 rounded-xl text-white placeholder-gray-500 focus:outline-none focus:border-[#a100ff] text-sm" 
              required 
              onChange={e => setFormData({...formData, department: e.target.value})} 
            />
            <input 
              placeholder="Location (Bengaluru, Hyderabad, Pune, Mumbai, etc.)" 
              className="bg-white/5 border border-white/10 p-3 rounded-xl text-white placeholder-gray-500 focus:outline-none focus:border-[#a100ff] text-sm" 
              required 
              onChange={e => setFormData({...formData, location: e.target.value})} 
            />
            <input 
              type="number" 
              placeholder="Min Experience (years)" 
              className="bg-white/5 border border-white/10 p-3 rounded-xl text-white placeholder-gray-500 focus:outline-none focus:border-[#a100ff] text-sm" 
              required 
              onChange={e => setFormData({...formData, min_experience_years: parseInt(e.target.value)})} 
            />
            <input 
              placeholder="Required Skills (comma separated: python, aws, docker)" 
              className="bg-white/5 border border-white/10 p-3 rounded-xl text-white placeholder-gray-500 focus:outline-none focus:border-[#a100ff] text-sm md:col-span-2" 
              required 
              onChange={e => setFormData({...formData, required_skills: e.target.value})} 
            />
            <input 
              placeholder="Preferred Skills (comma separated: kubernetes, kafka)" 
              className="bg-white/5 border border-white/10 p-3 rounded-xl text-white placeholder-gray-500 focus:outline-none focus:border-[#a100ff] text-sm md:col-span-2" 
              onChange={e => setFormData({...formData, preferred_skills: e.target.value})} 
            />
            <textarea 
              placeholder="Detailed Position Description..." 
              rows={3}
              className="bg-white/5 border border-white/10 p-3 rounded-xl text-white placeholder-gray-500 focus:outline-none focus:border-[#a100ff] text-sm md:col-span-2" 
              required 
              onChange={e => setFormData({...formData, description: e.target.value})}
            ></textarea>
            <input 
              placeholder="Education Requirement (e.g. B.Tech / M.Tech / MCA)" 
              className="bg-white/5 border border-white/10 p-3 rounded-xl text-white placeholder-gray-500 focus:outline-none focus:border-[#a100ff] text-sm md:col-span-2" 
              required 
              onChange={e => setFormData({...formData, education_requirement: e.target.value})} 
            />
          </div>
          <button 
            type="submit" 
            className="mt-5 px-6 py-3 bg-[#a100ff] hover:bg-[#8800db] text-white rounded-xl text-xs font-bold uppercase tracking-wider transition-all"
          >
            Publish Requisition to Accenture Portal &gt;
          </button>
        </form>
      )}

      {/* Jobs Table */}
      <div className="accenture-card rounded-2xl border border-white/10 overflow-hidden">
        <table className="min-w-full divide-y divide-white/10 text-left">
          <thead className="bg-white/[0.02]">
            <tr>
              <th className="px-6 py-4 text-xs font-bold uppercase tracking-wider text-gray-400">Position Title</th>
              <th className="px-6 py-4 text-xs font-bold uppercase tracking-wider text-gray-400">Domain</th>
              <th className="px-6 py-4 text-xs font-bold uppercase tracking-wider text-gray-400">India Hub</th>
              <th className="px-6 py-4 text-xs font-bold uppercase tracking-wider text-gray-400">Status</th>
              <th className="px-6 py-4 text-xs font-bold uppercase tracking-wider text-gray-400 text-right">Actions</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-white/5">
            {jobs.length === 0 ? (
              <tr><td colSpan="5" className="px-6 py-8 text-center text-gray-500 text-xs">No active positions found in database.</td></tr>
            ) : jobs.map(job => (
              <tr key={job.id} className="hover:bg-white/[0.02] transition-colors">
                <td className="px-6 py-4 whitespace-nowrap">
                  <div className="font-bold text-white text-sm">{job.title}</div>
                  <div className="text-[11px] text-gray-400">{job.min_experience_years}+ Yrs • {job.required_skills?.slice(0, 3).join(', ')}</div>
                </td>
                <td className="px-6 py-4 whitespace-nowrap text-xs text-gray-300 font-medium">{job.department}</td>
                <td className="px-6 py-4 whitespace-nowrap text-xs text-gray-400 flex items-center pt-5">
                  <MapPin className="w-3.5 h-3.5 text-[#a100ff] mr-1" /> {job.location}
                </td>
                <td className="px-6 py-4 whitespace-nowrap">
                  <span className="px-2.5 py-0.5 rounded-full text-[10px] font-bold uppercase bg-green-950/60 border border-green-500/40 text-green-300">
                    {job.status || 'Active'}
                  </span>
                </td>
                <td className="px-6 py-4 whitespace-nowrap text-right text-xs">
                  <button 
                    onClick={() => alert(`Requisition Details:\n\n${job.description}\n\nRequired Skills: ${job.required_skills?.join(', ')}`)} 
                    className="text-[#a100ff] hover:text-purple-300 font-bold uppercase mr-4"
                  >
                    View
                  </button>
                  <button 
                    onClick={() => handleDelete(job.id)} 
                    className="text-red-400 hover:text-red-300 font-bold uppercase"
                  >
                    Delete
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

export default Jobs;
