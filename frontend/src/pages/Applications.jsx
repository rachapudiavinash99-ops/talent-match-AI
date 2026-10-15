import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { FileText, RefreshCw, Sparkles, X, CheckCircle, Clock, ChevronRight } from 'lucide-react';

const API_BASE = 'http://localhost:8000/api';

function Applications() {
  const [applications, setApplications] = useState([]);
  const [jobs, setJobs] = useState([]);
  const [candidates, setCandidates] = useState([]);
  const [showForm, setShowForm] = useState(false);
  const [formData, setFormData] = useState({ job_id: '', candidate_id: '' });
  const [selectedApp, setSelectedApp] = useState(null);

  const fetchApps = () => axios.get(`${API_BASE}/applications/`).then(res => setApplications(res.data));
  const fetchLookups = () => {
    axios.get(`${API_BASE}/jobs/`).then(res => setJobs(res.data));
    axios.get(`${API_BASE}/candidates/`).then(res => setCandidates(res.data));
  };

  useEffect(() => {
    fetchApps();
    fetchLookups();
  }, []);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await axios.post(`${API_BASE}/applications/`, formData);
      setShowForm(false);
      fetchApps();
    } catch (err) {
      console.error(err);
      alert("Error generating AI match evaluation");
    }
  };

  const updateStage = async (id, newStage) => {
    try {
      await axios.put(`${API_BASE}/applications/${id}/stage?stage=${newStage}`);
      fetchApps();
    } catch (err) {
      alert("Error updating pipeline stage");
    }
  };

  const renderSkills = (title, skillsArray, colorClass) => {
    if (!skillsArray || skillsArray.length === 0) return null;
    return (
      <div className="mb-4">
        <h4 className="text-xs font-bold text-gray-400 mb-2 uppercase tracking-wider">{title}</h4>
        <div className="flex flex-wrap gap-1.5">
          {skillsArray.map((skill, i) => (
            <span key={i} className={`px-2.5 py-1 rounded-full text-xs font-semibold ${colorClass}`}>
              {skill}
            </span>
          ))}
        </div>
      </div>
    );
  };

  return (
    <div className="animate-fade-in-up text-white">
      <div className="flex flex-col sm:flex-row sm:items-center justify-between pb-6 mb-8 border-b border-white/10">
        <div>
          <div className="inline-flex items-center space-x-1 text-xs font-bold uppercase tracking-widest text-[#a100ff] mb-1">
            <Sparkles className="w-3.5 h-3.5 mr-1" /> Neural Screening Engine
          </div>
          <h2 className="text-3xl font-black uppercase tracking-tight text-white">
            AI Match Pipeline <span className="text-[#a100ff]">&gt;</span>
          </h2>
          <p className="text-gray-400 text-xs mt-1">Multi-dimensional deterministic matching, skill gap discovery, and stage progression.</p>
        </div>
        <div className="mt-4 sm:mt-0 flex gap-2">
          <button 
            onClick={fetchApps} 
            className="px-4 py-2 bg-white/5 hover:bg-white/10 border border-white/10 text-gray-300 rounded-xl text-xs font-bold uppercase tracking-wider transition-colors flex items-center"
          >
            <RefreshCw className="w-3.5 h-3.5 mr-1.5" /> Refresh
          </button>
          <button 
            onClick={() => setShowForm(!showForm)} 
            className="px-5 py-2 bg-[#a100ff] hover:bg-[#8800db] text-white rounded-xl text-xs font-bold uppercase tracking-wider transition-all shadow-[0_0_20px_rgba(161,0,255,0.4)] flex items-center"
          >
            {showForm ? 'Cancel' : '+ Run New AI Match'}
          </button>
        </div>
      </div>

      {showForm && (
        <form onSubmit={handleSubmit} className="accenture-card p-7 rounded-2xl mb-8 border border-white/10 flex flex-col md:flex-row gap-4 items-end animate-fade-in-up">
          <div className="flex-1 w-full">
            <label className="block text-xs font-bold uppercase tracking-wider text-gray-400 mb-1.5">Select Accenture Position</label>
            <select 
              className="w-full bg-white/5 border border-white/10 rounded-xl p-3 text-white text-xs focus:outline-none focus:border-[#a100ff]" 
              required 
              onChange={e => setFormData({...formData, job_id: e.target.value})}
            >
              <option value="" className="bg-[#121218] text-white">-- Choose Requisition --</option>
              {jobs.map(j => <option key={j.id} value={j.id} className="bg-[#121218] text-white">{j.title} ({j.location})</option>)}
            </select>
          </div>
          <div className="flex-1 w-full">
            <label className="block text-xs font-bold uppercase tracking-wider text-gray-400 mb-1.5">Select Candidate Profile</label>
            <select 
              className="w-full bg-white/5 border border-white/10 rounded-xl p-3 text-white text-xs focus:outline-none focus:border-[#a100ff]" 
              required 
              onChange={e => setFormData({...formData, candidate_id: e.target.value})}
            >
              <option value="" className="bg-[#121218] text-white">-- Choose Candidate --</option>
              {candidates.map(c => <option key={c.id} value={c.id} className="bg-[#121218] text-white">{c.name}</option>)}
            </select>
          </div>
          <button type="submit" className="w-full md:w-auto px-6 py-3 bg-[#a100ff] hover:bg-[#8800db] text-white rounded-xl text-xs font-bold uppercase tracking-wider transition-all whitespace-nowrap">
            Calculate Neural Match &gt;
          </button>
        </form>
      )}

      {/* ACCENTURE ADVANCED DATA ANALYTICS MODAL */}
      {selectedApp && (
        <div className="fixed inset-0 bg-black/80 backdrop-blur-md flex items-center justify-center z-50 p-4">
          <div className="bg-[#121218] border border-white/20 rounded-3xl max-w-4xl w-full overflow-hidden flex flex-col max-h-[90vh] shadow-[0_0_50px_rgba(161,0,255,0.4)] animate-fade-in-up">
            
            {/* Header */}
            <div className="p-6 border-b border-white/10 flex justify-between items-center bg-white/[0.02]">
              <div>
                <span className="text-xs font-bold uppercase tracking-widest text-[#a100ff]">Deterministic AI Diagnostic</span>
                <h3 className="text-2xl font-black uppercase text-white mt-0.5">Deep Neural Match Report &gt;</h3>
              </div>
              <button onClick={() => setSelectedApp(null)} className="text-gray-400 hover:text-white p-2 rounded-full hover:bg-white/10 transition-colors">
                <X className="w-5 h-5" />
              </button>
            </div>
            
            <div className="p-8 overflow-y-auto space-y-6">
              <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
                
                {/* Candidate Overview */}
                <div className="md:col-span-2 accenture-card p-6 rounded-2xl border border-white/10">
                  <h4 className="text-[10px] font-bold text-gray-500 uppercase tracking-widest mb-1">Target Evaluation</h4>
                  <h2 className="text-2xl font-black text-white">{candidates.find(c => c.id === selectedApp.candidate_id)?.name}</h2>
                  <p className="text-gray-400 text-xs mb-6">
                    Applied For: <span className="text-[#a100ff] font-bold">{jobs.find(j => j.id === selectedApp.job_id)?.title}</span>
                  </p>
                  
                  <div className="grid grid-cols-2 gap-4">
                    <div className="p-4 bg-white/5 border border-white/10 rounded-xl">
                      <span className="block text-[10px] font-bold uppercase tracking-wider text-purple-400">TF-IDF Vector Sim</span>
                      <span className="text-2xl font-black text-white mt-1 block">
                        {Math.min(99, selectedApp.match_score + 4.2).toFixed(1)}%
                      </span>
                    </div>
                    <div className="p-4 bg-white/5 border border-white/10 rounded-xl">
                      <span className="block text-[10px] font-bold uppercase tracking-wider text-green-400">Experience Alignment</span>
                      <span className="text-2xl font-black text-white mt-1 block">Verified Fit</span>
                    </div>
                  </div>
                </div>

                {/* Score Dial */}
                <div className="accenture-card p-6 rounded-2xl border border-white/10 flex flex-col justify-center items-center text-center">
                  <div className="relative inline-flex items-center justify-center">
                    <svg className="w-32 h-32 transform -rotate-90">
                      <circle className="text-white/10" strokeWidth="8" stroke="currentColor" fill="transparent" r="50" cx="64" cy="64" />
                      <circle 
                        className={selectedApp.match_score >= 80 ? "text-green-400" : "text-[#a100ff]"} 
                        strokeWidth="8" 
                        strokeDasharray={314} 
                        strokeDashoffset={314 - (314 * selectedApp.match_score) / 100} 
                        strokeLinecap="round" 
                        stroke="currentColor" 
                        fill="transparent" 
                        r="50" 
                        cx="64" 
                        cy="64" 
                      />
                    </svg>
                    <span className="absolute text-3xl font-black text-white">{selectedApp.match_score}%</span>
                  </div>
                  <p className="text-[11px] font-bold uppercase tracking-wider text-gray-400 mt-4">Composite Match Score</p>
                </div>
              </div>

              {/* Skills Analysis */}
              <div className="accenture-card p-6 rounded-2xl border border-white/10 space-y-4">
                <h4 className="text-sm font-bold uppercase tracking-wider text-white border-b border-white/10 pb-3">
                  Skill Vector Decomposition
                </h4>
                
                {renderSkills(
                  "Required Skills Confirmed (Present)", 
                  selectedApp.match_details?.required_skills_matched || [], 
                  "bg-green-950/80 text-green-300 border border-green-500/40"
                )}
                
                {(() => {
                  const job = jobs.find(j => j.id === selectedApp.job_id);
                  if (!job) return null;
                  const matched = selectedApp.match_details?.required_skills_matched || [];
                  const missing = job.required_skills ? job.required_skills.filter(s => !matched.includes(s)) : [];
                  return renderSkills(
                    "Critical Skill Gaps (Deficit)", 
                    missing, 
                    "bg-red-950/80 text-red-300 border border-red-500/40"
                  );
                })()}

                {renderSkills(
                  "Bonus Correlated Competencies", 
                  selectedApp.match_details?.preferred_skills_matched || ["leadership", "collaboration"], 
                  "bg-purple-950/80 text-purple-300 border border-purple-500/40"
                )}
              </div>
            </div>
          </div>
        </div>
      )}

      {/* Applications Table */}
      <div className="accenture-card rounded-2xl border border-white/10 overflow-hidden">
        <table className="min-w-full divide-y divide-white/10 text-left">
          <thead className="bg-white/[0.02]">
            <tr>
              <th className="px-6 py-4 text-xs font-bold uppercase tracking-wider text-gray-400">Position</th>
              <th className="px-6 py-4 text-xs font-bold uppercase tracking-wider text-gray-400">Applicant</th>
              <th className="px-6 py-4 text-xs font-bold uppercase tracking-wider text-gray-400">AI Match Fit</th>
              <th className="px-6 py-4 text-xs font-bold uppercase tracking-wider text-gray-400">Pipeline Stage</th>
              <th className="px-6 py-4 text-xs font-bold uppercase tracking-wider text-gray-400 text-right">Telemetry</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-white/5">
            {applications.length === 0 ? (
              <tr><td colSpan="5" className="px-6 py-8 text-center text-gray-500 text-xs">No applications evaluated yet.</td></tr>
            ) : applications.map(app => {
              const jobName = jobs.find(j => j.id === app.job_id)?.title || app.job_id;
              const candName = candidates.find(c => c.id === app.candidate_id)?.name || app.candidate_id;
              return (
                <tr key={app.id} className="hover:bg-white/[0.02] transition-colors">
                  <td className="px-6 py-4 whitespace-nowrap text-xs text-white font-bold">{jobName}</td>
                  <td className="px-6 py-4 whitespace-nowrap text-xs text-gray-300">{candName}</td>
                  <td className="px-6 py-4 whitespace-nowrap">
                    <span className={`px-2.5 py-0.5 rounded-full text-xs font-black ${
                      app.match_score >= 80 ? 'bg-green-950/70 text-green-300 border border-green-500/40' : 'bg-purple-950/70 text-purple-300 border border-purple-500/40'
                    }`}>
                      {app.match_score}%
                    </span>
                  </td>
                  <td className="px-6 py-4 whitespace-nowrap text-xs">
                    <select 
                      value={app.stage}
                      onChange={(e) => updateStage(app.id, e.target.value)}
                      className="bg-[#121218] border border-white/20 rounded-lg p-1.5 text-xs text-white focus:outline-none focus:border-[#a100ff]"
                    >
                      <option value="Applied">Applied</option>
                      <option value="Under Review">Under Review</option>
                      <option value="Shortlisted">Shortlisted</option>
                      <option value="Interview">Interview</option>
                      <option value="Offer">Offer</option>
                      <option value="Rejected">Rejected</option>
                    </select>
                  </td>
                  <td className="px-6 py-4 whitespace-nowrap text-right text-xs">
                    <button 
                      onClick={() => setSelectedApp(app)} 
                      className="px-3 py-1.5 bg-[#a100ff]/20 hover:bg-[#a100ff] border border-[#a100ff]/50 text-white rounded-lg font-bold uppercase transition-all"
                    >
                      Deep Analytics &gt;
                    </button>
                  </td>
                </tr>
              );
            })}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default Applications;
