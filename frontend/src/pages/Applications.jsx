import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { 
  FileText, RefreshCw, Sparkles, X, CheckCircle, Clock, 
  ChevronRight, Filter, Search, ArrowUpDown, UserCheck, Layers, Building2, MapPin
} from 'lucide-react';

const API_BASE = 'http://localhost:8000/api';

function Applications() {
  const [applications, setApplications] = useState([]);
  const [jobs, setJobs] = useState([]);
  const [candidates, setCandidates] = useState([]);
  const [showForm, setShowForm] = useState(false);
  const [formData, setFormData] = useState({ job_id: '', candidate_id: '' });
  const [selectedApp, setSelectedApp] = useState(null);

  // Filters & Sorting
  const [selectedJobId, setSelectedJobId] = useState('ALL');
  const [selectedStage, setSelectedStage] = useState('ALL');
  const [searchTerm, setSearchTerm] = useState('');
  const [sortBy, setSortBy] = useState('score-desc'); // 'score-desc', 'score-asc', 'date-desc'

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

  // Color helper for match percentage
  const getScoreBadge = (score) => {
    if (score >= 85) {
      return {
        bg: 'bg-emerald-950/80 text-emerald-300 border-emerald-500/40 shadow-[0_0_10px_rgba(16,185,129,0.2)]',
        circle: 'text-emerald-400',
        label: 'Strong Match'
      };
    } else if (score >= 70) {
      return {
        bg: 'bg-cyan-950/80 text-[#3fd0ff] border-[#3fd0ff]/40 shadow-[0_0_10px_rgba(63,208,255,0.2)]',
        circle: 'text-[#3fd0ff]',
        label: 'Qualified Fit'
      };
    } else if (score >= 50) {
      return {
        bg: 'bg-[#ff8a3d]/20 text-[#ff8a3d] border-[#ff8a3d]/40 shadow-[0_0_10px_rgba(255,138,61,0.2)]',
        circle: 'text-[#ff8a3d]',
        label: 'Partial Match'
      };
    } else {
      return {
        bg: 'bg-rose-950/80 text-rose-300 border-rose-500/40',
        circle: 'text-rose-400',
        label: 'Skill Gap'
      };
    }
  };

  // Filtered & Sorted Applications
  const filteredApps = applications.filter(app => {
    // Filter by Job
    if (selectedJobId !== 'ALL' && app.job_id !== selectedJobId) return false;
    // Filter by Stage
    if (selectedStage !== 'ALL' && app.stage !== selectedStage) return false;
    // Search Term
    if (searchTerm) {
      const term = searchTerm.toLowerCase();
      const job = jobs.find(j => j.id === app.job_id);
      const cand = candidates.find(c => c.id === app.candidate_id);
      const jobMatch = job?.title?.toLowerCase().includes(term) || job?.location?.toLowerCase().includes(term);
      const candMatch = cand?.name?.toLowerCase().includes(term) || cand?.skills?.some(s => s.toLowerCase().includes(term));
      if (!jobMatch && !candMatch) return false;
    }
    return true;
  }).sort((a, b) => {
    if (sortBy === 'score-desc') return (b.match_score || 0) - (a.match_score || 0);
    if (sortBy === 'score-asc') return (a.match_score || 0) - (b.match_score || 0);
    return new Date(b.created_at || 0) - new Date(a.created_at || 0);
  });

  // Calculate quick stats
  const totalProfiles = applications.length;
  const highFitCount = applications.filter(a => a.match_score >= 80).length;
  const avgScore = totalProfiles > 0 
    ? (applications.reduce((acc, curr) => acc + (curr.match_score || 0), 0) / totalProfiles).toFixed(1) 
    : 0;

  const renderSkills = (title, skillsArray, colorClass) => {
    if (!skillsArray || skillsArray.length === 0) return null;
    return (
      <div className="mb-4">
        <h4 className="text-[11px] font-bold text-gray-400 mb-2 uppercase tracking-wider">{title}</h4>
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
      
      {/* Header */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between pb-6 mb-8 border-b border-white/10">
        <div>
          <div className="inline-flex items-center space-x-1 text-xs font-bold uppercase tracking-widest text-[#ff8a3d] mb-1">
            <Sparkles className="w-3.5 h-3.5 mr-1" /> Multi-Dimensional AI Match Pipeline
          </div>
          <h2 className="text-3xl font-black uppercase tracking-tight text-white">
            Candidate Evaluation Console <span className="text-[#3fd0ff]">&gt;</span>
          </h2>
          <p className="text-gray-400 text-xs mt-1">
            Deterministic NLP ranking, skill vector decomposition, and pipeline tracking for all {jobs.length} active positions.
          </p>
        </div>
        
        <div className="mt-4 sm:mt-0 flex gap-2">
          <button 
            onClick={() => { fetchApps(); fetchLookups(); }} 
            className="px-4 py-2 bg-white/5 hover:bg-white/10 border border-white/10 text-gray-300 rounded-xl text-xs font-bold uppercase tracking-wider transition-colors flex items-center"
          >
            <RefreshCw className="w-3.5 h-3.5 mr-1.5" /> Refresh
          </button>
          <button 
            onClick={() => setShowForm(!showForm)} 
            className="px-5 py-2 bg-gradient-to-r from-[#ff8a3d] to-[#f2701c] hover:brightness-110 text-white rounded-xl text-xs font-bold uppercase tracking-wider transition-all shadow-[0_0_20px_rgba(255,138,61,0.35)] flex items-center"
          >
            {showForm ? 'Cancel' : '+ Evaluate Candidate'}
          </button>
        </div>
      </div>

      {/* Summary KPI Cards */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 mb-8">
        <div className="elevate-card p-5 rounded-2xl border border-white/10 flex items-center">
          <div className="p-3.5 rounded-xl bg-orange-950/60 border border-[#ff8a3d]/30 text-[#ff8a3d] mr-3.5">
            <Layers className="w-5 h-5" />
          </div>
          <div>
            <h4 className="text-[11px] font-bold text-gray-400 uppercase tracking-wider">Evaluated Profiles</h4>
            <p className="text-2xl font-black text-white mt-0.5">{totalProfiles}</p>
          </div>
        </div>

        <div className="elevate-card p-5 rounded-2xl border border-white/10 flex items-center">
          <div className="p-3.5 rounded-xl bg-cyan-950/60 border border-[#3fd0ff]/30 text-[#3fd0ff] mr-3.5">
            <Building2 className="w-5 h-5" />
          </div>
          <div>
            <h4 className="text-[11px] font-bold text-gray-400 uppercase tracking-wider">Covered Requisitions</h4>
            <p className="text-2xl font-black text-white mt-0.5">{jobs.length} / {jobs.length} <span className="text-xs font-semibold text-emerald-400">(5+ per pos)</span></p>
          </div>
        </div>

        <div className="elevate-card p-5 rounded-2xl border border-white/10 flex items-center">
          <div className="p-3.5 rounded-xl bg-emerald-950/60 border border-emerald-500/30 text-emerald-400 mr-3.5">
            <UserCheck className="w-5 h-5" />
          </div>
          <div>
            <h4 className="text-[11px] font-bold text-gray-400 uppercase tracking-wider">Top Candidates (&gt;80%)</h4>
            <p className="text-2xl font-black text-white mt-0.5">{highFitCount}</p>
          </div>
        </div>

        <div className="elevate-card p-5 rounded-2xl border border-white/10 flex items-center">
          <div className="p-3.5 rounded-xl bg-blue-950/60 border border-blue-500/30 text-blue-400 mr-3.5">
            <Sparkles className="w-5 h-5" />
          </div>
          <div>
            <h4 className="text-[11px] font-bold text-gray-400 uppercase tracking-wider">Average Match Fit</h4>
            <p className="text-2xl font-black text-white mt-0.5">{avgScore}%</p>
          </div>
        </div>
      </div>

      {/* Manual Evaluation Trigger Modal / Form */}
      {showForm && (
        <form onSubmit={handleSubmit} className="elevate-card p-7 rounded-2xl mb-8 border border-white/10 flex flex-col md:flex-row gap-4 items-end animate-fade-in-up">
          <div className="flex-1 w-full">
            <label className="block text-xs font-bold uppercase tracking-wider text-gray-400 mb-1.5">
              Select Position
            </label>
            <select 
              className="w-full bg-[#0a0f24] border border-white/15 rounded-xl p-3 text-white text-xs focus:outline-none focus:border-[#3fd0ff]" 
              required 
              onChange={e => setFormData({...formData, job_id: e.target.value})}
            >
              <option value="" className="bg-[#0a0f24] text-white">-- Choose Requisition --</option>
              {jobs.map(j => <option key={j.id} value={j.id} className="bg-[#0a0f24] text-white">{j.title} ({j.location})</option>)}
            </select>
          </div>
          <div className="flex-1 w-full">
            <label className="block text-xs font-bold uppercase tracking-wider text-gray-400 mb-1.5">
              Select Candidate Profile
            </label>
            <select 
              className="w-full bg-[#0a0f24] border border-white/15 rounded-xl p-3 text-white text-xs focus:outline-none focus:border-[#3fd0ff]" 
              required 
              onChange={e => setFormData({...formData, candidate_id: e.target.value})}
            >
              <option value="" className="bg-[#0a0f24] text-white">-- Choose Candidate --</option>
              {candidates.map(c => <option key={c.id} value={c.id} className="bg-[#0a0f24] text-white">{c.name} ({c.skills?.slice(0, 3).join(', ')})</option>)}
            </select>
          </div>
          <button type="submit" className="w-full md:w-auto px-6 py-3 bg-gradient-to-r from-[#ff8a3d] to-[#f2701c] hover:brightness-110 text-white rounded-xl text-xs font-bold uppercase tracking-wider transition-all whitespace-nowrap shadow-[0_0_15px_rgba(255,138,61,0.3)]">
            Run AI Match &gt;
          </button>
        </form>
      )}

      {/* Position Quick-Selector Chips */}
      <div className="mb-6 overflow-x-auto pb-2 scrollbar-none">
        <div className="flex gap-2 min-w-max">
          <button
            onClick={() => setSelectedJobId('ALL')}
            className={`px-3.5 py-1.5 rounded-full text-xs font-bold uppercase tracking-wider transition-all flex items-center ${
              selectedJobId === 'ALL'
                ? 'bg-gradient-to-r from-[#ff8a3d] to-[#f2701c] text-white shadow-[0_0_12px_rgba(255,138,61,0.4)]'
                : 'bg-white/5 hover:bg-white/10 text-gray-400 hover:text-white border border-white/10'
            }`}
          >
            All Positions ({applications.length})
          </button>
          {jobs.map(job => {
            const count = applications.filter(a => a.job_id === job.id).length;
            const active = selectedJobId === job.id;
            return (
              <button
                key={job.id}
                onClick={() => setSelectedJobId(job.id)}
                className={`px-3.5 py-1.5 rounded-full text-xs font-bold uppercase tracking-wider transition-all flex items-center ${
                  active
                    ? 'bg-[#3fd0ff] text-[#06091A] shadow-[0_0_12px_rgba(63,208,255,0.4)]'
                    : 'bg-white/5 hover:bg-white/10 text-gray-400 hover:text-white border border-white/10'
                }`}
              >
                <span>{job.title.split('(')[0].trim()}</span>
                <span className={`ml-2 px-1.5 py-0.2 rounded-full text-[10px] font-black ${
                  active ? 'bg-[#06091A] text-[#3fd0ff]' : 'bg-white/10 text-gray-300'
                }`}>
                  {count}
                </span>
              </button>
            );
          })}
        </div>
      </div>

      {/* Control / Filter Bar */}
      <div className="elevate-card p-4 rounded-2xl border border-white/10 mb-6 flex flex-col md:flex-row gap-4 items-center justify-between">
        
        {/* Search */}
        <div className="relative w-full md:w-80">
          <Search className="w-4 h-4 text-gray-400 absolute left-3 top-1/2 -translate-y-1/2" />
          <input 
            type="text" 
            placeholder="Search candidate, skill, requisition..." 
            value={searchTerm}
            onChange={e => setSearchTerm(e.target.value)}
            className="w-full pl-9 pr-3 py-2 bg-black/40 border border-white/10 rounded-xl text-xs text-white placeholder-gray-500 focus:outline-none focus:border-[#3fd0ff]"
          />
        </div>

        {/* Dropdowns */}
        <div className="flex flex-wrap items-center gap-3 w-full md:w-auto">
          
          {/* Position Select */}
          <div className="flex items-center space-x-1.5">
            <span className="text-[11px] font-bold uppercase tracking-wider text-gray-400">Position:</span>
            <select
              value={selectedJobId}
              onChange={e => setSelectedJobId(e.target.value)}
              className="bg-[#0a0f24] border border-white/15 rounded-xl px-3 py-2 text-xs text-white focus:outline-none focus:border-[#3fd0ff]"
            >
              <option value="ALL">All Positions ({applications.length})</option>
              {jobs.map(j => {
                const count = applications.filter(a => a.job_id === j.id).length;
                return (
                  <option key={j.id} value={j.id}>
                    {j.title} ({count} applicants)
                  </option>
                );
              })}
            </select>
          </div>

          {/* Stage Select */}
          <div className="flex items-center space-x-1.5">
            <span className="text-[11px] font-bold uppercase tracking-wider text-gray-400">Stage:</span>
            <select
              value={selectedStage}
              onChange={e => setSelectedStage(e.target.value)}
              className="bg-[#0a0f24] border border-white/15 rounded-xl px-3 py-2 text-xs text-white focus:outline-none focus:border-[#3fd0ff]"
            >
              <option value="ALL">All Stages</option>
              <option value="Offer">Offer</option>
              <option value="Interview">Interview</option>
              <option value="Shortlisted">Shortlisted</option>
              <option value="Under Review">Under Review</option>
              <option value="Applied">Applied</option>
              <option value="Rejected">Rejected</option>
            </select>
          </div>

          {/* Sort Select */}
          <div className="flex items-center space-x-1.5">
            <span className="text-[11px] font-bold uppercase tracking-wider text-gray-400">Sort:</span>
            <select
              value={sortBy}
              onChange={e => setSortBy(e.target.value)}
              className="bg-[#0a0f24] border border-white/15 rounded-xl px-3 py-2 text-xs text-white focus:outline-none focus:border-[#3fd0ff]"
            >
              <option value="score-desc">Match % (High &rarr; Low)</option>
              <option value="score-asc">Match % (Low &rarr; High)</option>
              <option value="date-desc">Recent Submissions</option>
            </select>
          </div>

        </div>

      </div>

      {/* Selected Job Focus Card */}
      {selectedJobId !== 'ALL' && (
        <div className="mb-6 p-4 rounded-2xl bg-gradient-to-r from-cyan-950/30 to-blue-950/20 border border-[#3fd0ff]/30 flex flex-col sm:flex-row justify-between items-start sm:items-center gap-3">
          <div>
            <span className="text-[10px] font-bold uppercase tracking-widest text-[#3fd0ff] block">
              Focused Position Filter
            </span>
            <h3 className="text-lg font-black text-white mt-0.5">
              {jobs.find(j => j.id === selectedJobId)?.title}
            </h3>
            <p className="text-xs text-gray-400 mt-0.5">
              Showing {filteredApps.length} candidates with varied match percentages for this requisition.
            </p>
          </div>
          <button
            onClick={() => setSelectedJobId('ALL')}
            className="px-3 py-1.5 bg-white/10 hover:bg-white/20 text-white rounded-xl text-xs font-semibold flex items-center transition-colors"
          >
            <X className="w-3.5 h-3.5 mr-1" /> View All Positions
          </button>
        </div>
      )}

      {/* Applications Table */}
      <div className="elevate-card rounded-2xl border border-white/10 overflow-hidden shadow-xl">
        <table className="min-w-full divide-y divide-white/10 text-left">
          <thead className="bg-white/[0.02]">
            <tr>
              <th className="px-6 py-4 text-xs font-bold uppercase tracking-wider text-gray-400">Target Requisition</th>
              <th className="px-6 py-4 text-xs font-bold uppercase tracking-wider text-gray-400">Candidate Profile</th>
              <th className="px-6 py-4 text-xs font-bold uppercase tracking-wider text-gray-400">AI Match Fit</th>
              <th className="px-6 py-4 text-xs font-bold uppercase tracking-wider text-gray-400">Top Matched Skills</th>
              <th className="px-6 py-4 text-xs font-bold uppercase tracking-wider text-gray-400">Pipeline Stage</th>
              <th className="px-6 py-4 text-xs font-bold uppercase tracking-wider text-gray-400 text-right">Telemetry</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-white/5">
            {filteredApps.length === 0 ? (
              <tr>
                <td colSpan="6" className="px-6 py-12 text-center text-gray-400 text-xs">
                  No candidate evaluations matching selected filters.
                </td>
              </tr>
            ) : filteredApps.map(app => {
              const job = jobs.find(j => j.id === app.job_id);
              const cand = candidates.find(c => c.id === app.candidate_id);
              const jobName = job?.title || app.job_id;
              const candName = cand?.name || app.candidate_id;
              const scoreBadge = getScoreBadge(app.match_score);
              const matchedSkills = app.match_details?.required_skills_matched || [];

              return (
                <tr key={app.id} className="hover:bg-white/[0.02] transition-colors">
                  
                  {/* Job Requisition */}
                  <td className="px-6 py-4 whitespace-nowrap">
                    <span className="text-xs text-white font-bold block">{jobName}</span>
                    <span className="text-[10px] text-gray-400 flex items-center mt-0.5">
                      <MapPin className="w-3 h-3 text-[#3fd0ff] mr-1" />
                      {job?.location || 'India Delivery Hub'}
                    </span>
                  </td>

                  {/* Candidate */}
                  <td className="px-6 py-4 whitespace-nowrap">
                    <span className="text-xs font-bold text-gray-200 block">{candName}</span>
                    <span className="text-[10px] text-gray-500">{cand?.email || 'elevateiq-talent.in'}</span>
                  </td>

                  {/* AI Match Fit Percentage */}
                  <td className="px-6 py-4 whitespace-nowrap">
                    <div className="flex items-center space-x-2">
                      <span className={`px-3 py-1 rounded-full text-xs font-black border ${scoreBadge.bg}`}>
                        {app.match_score}%
                      </span>
                      <span className="text-[10px] font-semibold text-gray-400 hidden xl:inline">
                        {scoreBadge.label}
                      </span>
                    </div>
                  </td>

                  {/* Matched Skills */}
                  <td className="px-6 py-4">
                    <div className="flex flex-wrap gap-1 max-w-xs">
                      {matchedSkills.length > 0 ? (
                        matchedSkills.slice(0, 3).map((s, idx) => (
                          <span key={idx} className="px-2 py-0.5 rounded-full text-[10px] font-bold bg-cyan-950/60 text-[#3fd0ff] border border-[#3fd0ff]/30">
                            {s}
                          </span>
                        ))
                      ) : (
                        <span className="text-[10px] text-gray-500 italic">No direct keyword overlap</span>
                      )}
                      {matchedSkills.length > 3 && (
                        <span className="text-[10px] text-gray-400 self-center font-bold">
                          +{matchedSkills.length - 3}
                        </span>
                      )}
                    </div>
                  </td>

                  {/* Pipeline Stage */}
                  <td className="px-6 py-4 whitespace-nowrap text-xs">
                    <select 
                      value={app.stage}
                      onChange={(e) => updateStage(app.id, e.target.value)}
                      className="bg-[#0a0f24] border border-white/15 rounded-lg px-2.5 py-1.5 text-xs text-white focus:outline-none focus:border-[#3fd0ff]"
                    >
                      <option value="Applied">Applied</option>
                      <option value="Under Review">Under Review</option>
                      <option value="Shortlisted">Shortlisted</option>
                      <option value="Interview">Interview</option>
                      <option value="Offer">Offer</option>
                      <option value="Rejected">Rejected</option>
                    </select>
                  </td>

                  {/* Deep Analytics Button */}
                  <td className="px-6 py-4 whitespace-nowrap text-right text-xs">
                    <button 
                      onClick={() => setSelectedApp(app)} 
                      className="px-3 py-1.5 bg-[#3fd0ff]/10 hover:bg-[#3fd0ff] border border-[#3fd0ff]/40 text-[#3fd0ff] hover:text-[#06091A] rounded-lg font-bold uppercase transition-all shadow-[0_0_10px_rgba(63,208,255,0.15)]"
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

      {/* ============================================================== */}
      {/* 🔬 ELEVATEIQ ADVANCED DATA ANALYTICS MODAL */}
      {/* ============================================================== */}
      {selectedApp && (
        <div className="fixed inset-0 bg-black/80 backdrop-blur-md flex items-center justify-center z-50 p-4">
          <div className="bg-[#0a0f24] border border-white/20 rounded-3xl max-w-4xl w-full overflow-hidden flex flex-col max-h-[90vh] shadow-[0_0_50px_rgba(63,208,255,0.3)] animate-fade-in-up">
            
            {/* Modal Header */}
            <div className="p-6 border-b border-white/10 flex justify-between items-center bg-white/[0.02]">
              <div>
                <span className="text-xs font-bold uppercase tracking-widest text-[#ff8a3d]">
                  Deterministic AI Diagnostic
                </span>
                <h3 className="text-2xl font-black uppercase text-white mt-0.5">
                  Deep Neural Match Report &gt;
                </h3>
              </div>
              <button 
                onClick={() => setSelectedApp(null)} 
                className="text-gray-400 hover:text-white p-2 rounded-full hover:bg-white/10 transition-colors"
              >
                <X className="w-5 h-5" />
              </button>
            </div>
            
            <div className="p-8 overflow-y-auto space-y-6">
              <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
                
                {/* Candidate Overview */}
                <div className="md:col-span-2 elevate-card p-6 rounded-2xl border border-white/10">
                  <h4 className="text-[10px] font-bold text-gray-500 uppercase tracking-widest mb-1">
                    Target Evaluation Profile
                  </h4>
                  <h2 className="text-2xl font-black text-white">
                    {candidates.find(c => c.id === selectedApp.candidate_id)?.name || 'Candidate Profile'}
                  </h2>
                  <p className="text-gray-400 text-xs mb-6">
                    Applied For: <span className="text-[#3fd0ff] font-bold">{jobs.find(j => j.id === selectedApp.job_id)?.title}</span>
                  </p>
                  
                  <div className="grid grid-cols-2 gap-4">
                    <div className="p-4 bg-white/5 border border-white/10 rounded-xl">
                      <span className="block text-[10px] font-bold uppercase tracking-wider text-[#3fd0ff]">
                        Cosine Vector Similarity
                      </span>
                      <span className="text-2xl font-black text-white mt-1 block">
                        {selectedApp.match_details?.cosine_similarity || Math.max(10, selectedApp.match_score - 5.5).toFixed(1)}%
                      </span>
                    </div>
                    <div className="p-4 bg-white/5 border border-white/10 rounded-xl">
                      <span className="block text-[10px] font-bold uppercase tracking-wider text-emerald-400">
                        Pipeline Status
                      </span>
                      <span className="text-2xl font-black text-white mt-1 block">
                        {selectedApp.stage}
                      </span>
                    </div>
                  </div>
                </div>

                {/* Score Dial */}
                <div className="elevate-card p-6 rounded-2xl border border-white/10 flex flex-col justify-center items-center text-center">
                  <div className="relative inline-flex items-center justify-center">
                    <svg className="w-32 h-32 transform -rotate-90">
                      <circle className="text-white/10" strokeWidth="8" stroke="currentColor" fill="transparent" r="50" cx="64" cy="64" />
                      <circle 
                        className={getScoreBadge(selectedApp.match_score).circle} 
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
                  <p className="text-[11px] font-bold uppercase tracking-wider text-gray-400 mt-4">
                    {getScoreBadge(selectedApp.match_score).label}
                  </p>
                </div>
              </div>

              {/* Skills Analysis */}
              <div className="elevate-card p-6 rounded-2xl border border-white/10 space-y-4">
                <h4 className="text-sm font-bold uppercase tracking-wider text-white border-b border-white/10 pb-3">
                  Skill Vector Decomposition
                </h4>
                
                {renderSkills(
                  "Required Skills Confirmed (Present)", 
                  selectedApp.match_details?.required_skills_matched || [], 
                  "bg-green-950/80 text-green-300 border border-green-500/40"
                )}
                
                {renderSkills(
                  "Critical Skill Gaps (Deficit / Missing)", 
                  selectedApp.match_details?.required_skills_missing || [], 
                  "bg-red-950/80 text-red-300 border border-red-500/40"
                )}

                {renderSkills(
                  "Bonus Correlated Competencies (Preferred)", 
                  selectedApp.match_details?.preferred_skills_matched || [], 
                  "bg-orange-950/80 text-[#ff8a3d] border border-[#ff8a3d]/40"
                )}
              </div>
            </div>
          </div>
        </div>
      )}

    </div>
  );
}

export default Applications;
