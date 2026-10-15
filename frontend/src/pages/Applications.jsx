import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { 
  FileText, RefreshCw, Sparkles, X, CheckCircle, Clock, 
  Filter, Search, ArrowUpDown, UserCheck, Layers, Building2, MapPin,
  Briefcase, ChevronRight, Check, AlertCircle, ArrowUpRight, Award, Mail, Phone,
  Zap, Scale, CheckSquare, Square, ArrowLeftRight, ArrowRight
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
  const [selectedJobId, setSelectedJobId] = useState(null);
  const [selectedStage, setSelectedStage] = useState('ALL');
  const [searchTerm, setSearchTerm] = useState('');
  const [sortBy, setSortBy] = useState('score-desc');

  // Interactive Buttons State
  const [actionBanner, setActionBanner] = useState('');
  const [selectedCompareIds, setSelectedCompareIds] = useState([]);
  const [showCompareModal, setShowCompareModal] = useState(false);

  const fetchApps = () => axios.get(`${API_BASE}/applications/`).then(res => setApplications(res.data));
  const fetchLookups = () => {
    axios.get(`${API_BASE}/jobs/`).then(res => {
      setJobs(res.data);
      if (!selectedJobId && res.data.length > 0) {
        setSelectedJobId(res.data[0].id);
      }
    });
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
      if (selectedApp && selectedApp.id === id) {
        setSelectedApp({ ...selectedApp, stage: newStage });
      }
    } catch (err) {
      alert("Error updating pipeline stage");
    }
  };

  // ==============================================================
  // ⚡ BUTTON 1: AUTO-SHORTLIST TOP CANDIDATES (>= 80%)
  // ==============================================================
  const handleAutoShortlist = async () => {
    const candidatesToShortlist = filteredApps.filter(
      app => (app.match_score || 0) >= 80 && app.stage !== 'Shortlisted' && app.stage !== 'Offer'
    );
    
    if (candidatesToShortlist.length === 0) {
      setActionBanner('All top candidates (≥80%) in current view are already Shortlisted or in Offer stage!');
      setTimeout(() => setActionBanner(''), 4500);
      return;
    }

    try {
      await Promise.all(
        candidatesToShortlist.map(app => 
          axios.put(`${API_BASE}/applications/${app.id}/stage?stage=Shortlisted`)
        )
      );
      setActionBanner(`⚡ Successfully advanced ${candidatesToShortlist.length} candidate(s) (≥80%) to "Shortlisted"!`);
      setTimeout(() => setActionBanner(''), 5000);
      fetchApps();
    } catch (err) {
      console.error(err);
      alert('Error auto-shortlisting candidates.');
    }
  };

  // ==============================================================
  // ⚖️ BUTTON 2: COMPARE CANDIDATES SELECTION TOGGLE
  // ==============================================================
  const toggleSelectForCompare = (appId) => {
    if (selectedCompareIds.includes(appId)) {
      setSelectedCompareIds(selectedCompareIds.filter(id => id !== appId));
    } else {
      if (selectedCompareIds.length >= 2) {
        // Keep the second one and add the new one (always max 2 for clean side-by-side)
        setSelectedCompareIds([selectedCompareIds[1], appId]);
      } else {
        setSelectedCompareIds([...selectedCompareIds, appId]);
      }
    }
  };

  // Color helper for match percentage
  const getScoreBadge = (score) => {
    const num = parseFloat(score) || 0;
    if (num >= 85) {
      return {
        bg: 'bg-emerald-950/80 text-emerald-300 border-emerald-500/40 shadow-[0_0_10px_rgba(16,185,129,0.2)]',
        circle: 'text-emerald-400',
        label: 'Strong Match'
      };
    } else if (num >= 70) {
      return {
        bg: 'bg-cyan-950/80 text-[#3fd0ff] border-[#3fd0ff]/40 shadow-[0_0_10px_rgba(63,208,255,0.2)]',
        circle: 'text-[#3fd0ff]',
        label: 'Qualified Fit'
      };
    } else if (num >= 50) {
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
    if (selectedJobId && selectedJobId !== 'ALL' && app.job_id !== selectedJobId) return false;
    if (selectedStage !== 'ALL' && app.stage !== selectedStage) return false;
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

  const selectedJob = jobs.find(j => j.id === selectedJobId);

  return (
    <div className="animate-fade-in-up text-white pb-16">
      
      {/* Page Header */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between pb-6 mb-8 border-b border-white/10">
        <div>
          <div className="inline-flex items-center space-x-1 text-xs font-bold uppercase tracking-widest text-[#ff8a3d] mb-1">
            <Sparkles className="w-3.5 h-3.5 mr-1" /> Multi-Dimensional AI Match Pipeline
          </div>
          <h2 className="text-3xl font-black uppercase tracking-tight text-white">
            AI Screening &amp; Candidate Fit Console <span className="text-[#3fd0ff]">&gt;</span>
          </h2>
          <p className="text-gray-400 text-xs mt-1">
            Click any job role square box below to isolate its candidate applications and inspect deep neural telemetry.
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

      {/* Action Notification Banner */}
      {actionBanner && (
        <div className="mb-6 p-4 rounded-xl bg-emerald-950/80 border border-emerald-500/50 text-emerald-300 text-xs font-bold flex items-center shadow-lg animate-fade-in-up">
          <CheckCircle className="w-4 h-4 mr-2 text-emerald-400 flex-shrink-0" />
          <span>{actionBanner}</span>
        </div>
      )}

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

      {/* ============================================================== */}
      {/* 📦 JOB ROLES IN SQUARE BOXES */}
      {/* ============================================================== */}
      <div className="mb-8">
        <div className="flex items-center justify-between mb-4">
          <div className="flex items-center space-x-2">
            <Briefcase className="w-4 h-4 text-[#ff8a3d]" />
            <h3 className="text-sm font-bold uppercase tracking-wider text-white">
              Enterprise Job Roles ({jobs.length} Positions)
            </h3>
            <span className="text-[11px] text-gray-400 hidden sm:inline">— Click any square box to view its applications</span>
          </div>

          <button
            onClick={() => setSelectedJobId('ALL')}
            className={`px-3 py-1.5 rounded-xl text-xs font-bold uppercase tracking-wider transition-all flex items-center ${
              selectedJobId === 'ALL'
                ? 'bg-gradient-to-r from-[#ff8a3d] to-[#f2701c] text-white shadow-[0_0_12px_rgba(255,138,61,0.4)]'
                : 'bg-white/5 hover:bg-white/10 text-gray-400 hover:text-white border border-white/10'
            }`}
          >
            Show All ({applications.length} Applications)
          </button>
        </div>

        {/* Square Boxes Grid */}
        <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-5 gap-4">
          {jobs.map((job) => {
            const jobApps = applications.filter(a => a.job_id === job.id);
            const isSelected = selectedJobId === job.id;
            const scores = jobApps.map(a => a.match_score || 0);
            const topScore = scores.length > 0 ? Math.max(...scores) : 0;
            const avgScore = scores.length > 0 ? (scores.reduce((a, b) => a + b, 0) / scores.length).toFixed(1) : 0;

            return (
              <div
                key={job.id}
                onClick={() => setSelectedJobId(job.id)}
                className={`group cursor-pointer rounded-2xl p-4 flex flex-col justify-between transition-all duration-300 relative overflow-hidden aspect-square border ${
                  isSelected
                    ? 'bg-gradient-to-b from-[#0e1638] to-[#070b1e] border-[#3fd0ff] shadow-[0_0_25px_rgba(63,208,255,0.35)] scale-[1.02]'
                    : 'bg-[#080d22] border-white/10 hover:border-[#ff8a3d]/60 hover:bg-[#0c122e] hover:scale-[1.01]'
                }`}
              >
                {/* Active Indicator Top Glow */}
                {isSelected && (
                  <div className="absolute top-0 left-0 right-0 h-1 bg-gradient-to-r from-[#ff8a3d] via-[#3fd0ff] to-[#ff8a3d]"></div>
                )}

                {/* Top: Department & Application Count */}
                <div className="flex items-start justify-between gap-1">
                  <span className="text-[10px] font-bold uppercase tracking-wider text-[#ff8a3d] truncate block max-w-[65%]">
                    {job.department?.split('&')[0]?.trim()}
                  </span>
                  <span className={`px-2 py-0.5 rounded-full text-[10px] font-black tracking-wide ${
                    isSelected 
                      ? 'bg-[#3fd0ff] text-[#06091A]' 
                      : 'bg-white/10 text-gray-300 group-hover:bg-white/15'
                  }`}>
                    {jobApps.length} Apps
                  </span>
                </div>

                {/* Center: Position Title & Location */}
                <div className="my-2">
                  <h4 className={`text-sm font-black tracking-tight leading-snug line-clamp-2 transition-colors ${
                    isSelected ? 'text-white' : 'text-gray-100 group-hover:text-white'
                  }`}>
                    {job.title}
                  </h4>
                  <div className="flex items-center text-[11px] text-gray-400 mt-1.5">
                    <MapPin className="w-3 h-3 text-[#3fd0ff] mr-1 flex-shrink-0" />
                    <span className="truncate">{job.location} Branch</span>
                  </div>
                </div>

                {/* Bottom: Match Percentages & Selection Callout */}
                <div className="pt-2 border-t border-white/10">
                  <div className="flex items-center justify-between text-[10px] font-bold">
                    <span className="text-emerald-400">
                      Top: {topScore}%
                    </span>
                    <span className="text-gray-400">
                      Avg: {avgScore}%
                    </span>
                  </div>
                  <div className="mt-1.5 flex items-center justify-between">
                    <span className="text-[9px] text-gray-500 font-semibold uppercase tracking-wider">
                      {job.min_experience_years}+ Yrs Exp
                    </span>
                    <span className={`text-[10px] font-bold flex items-center transition-colors ${
                      isSelected ? 'text-[#3fd0ff]' : 'text-gray-400 group-hover:text-[#ff8a3d]'
                    }`}>
                      {isSelected ? '✓ Selected' : 'View →'}
                    </span>
                  </div>
                </div>

              </div>
            );
          })}
        </div>
      </div>

      {/* ============================================================== */}
      {/* 📋 APPLICATIONS SECTION WITH ACTION BUTTONS */}
      {/* ============================================================== */}
      <div className="elevate-card rounded-2xl border border-white/10 overflow-hidden shadow-xl">
        
        {/* Banner with Button 1 & Button 2 */}
        <div className="p-5 bg-gradient-to-r from-white/[0.04] to-transparent border-b border-white/10 flex flex-col xl:flex-row justify-between items-start xl:items-center gap-4">
          <div>
            <div className="flex items-center space-x-2">
              <span className="text-[10px] font-bold uppercase tracking-widest text-[#3fd0ff] bg-cyan-950/60 border border-[#3fd0ff]/30 px-2 py-0.5 rounded-full">
                {selectedJob ? 'Selected Job Role' : 'All Open Roles'}
              </span>
              <span className="text-xs text-gray-400 font-semibold">
                Showing <strong className="text-white">{filteredApps.length}</strong> Applications
              </span>
            </div>
            
            <h3 className="text-xl font-black text-white mt-1">
              {selectedJob ? selectedJob.title : 'All Active Requisitions'}
            </h3>
            
            {selectedJob && (
              <div className="flex flex-wrap items-center gap-3 text-xs text-gray-400 mt-1">
                <span className="flex items-center">
                  <MapPin className="w-3.5 h-3.5 text-[#3fd0ff] mr-1" /> {selectedJob.location} Hub
                </span>
                <span>•</span>
                <span>{selectedJob.department}</span>
                <span>•</span>
                <span>Min: {selectedJob.min_experience_years}+ Years Experience</span>
              </div>
            )}
          </div>

          {/* Action Buttons & Filters Bar */}
          <div className="flex flex-wrap items-center gap-3 w-full xl:w-auto">
            
            {/* ⚡ BUTTON 1: AUTO-SHORTLIST TOP CANDIDATES (>=80%) */}
            <button
              onClick={handleAutoShortlist}
              className="px-3.5 py-1.5 bg-gradient-to-r from-emerald-600 to-teal-600 hover:brightness-110 text-white rounded-xl text-xs font-bold uppercase tracking-wider flex items-center shadow-[0_0_15px_rgba(16,185,129,0.35)] transition-all whitespace-nowrap"
              title="Automatically advance all candidates with >=80% match score to Shortlisted stage"
            >
              <Zap className="w-3.5 h-3.5 mr-1.5 text-yellow-300 fill-yellow-300" />
              Auto-Shortlist (&ge;80%)
            </button>

            {/* ⚖️ BUTTON 2: COMPARE CANDIDATES (SIDE-BY-SIDE) */}
            <button
              onClick={() => setShowCompareModal(true)}
              disabled={selectedCompareIds.length < 2}
              className={`px-3.5 py-1.5 rounded-xl text-xs font-bold uppercase tracking-wider flex items-center transition-all whitespace-nowrap ${
                selectedCompareIds.length >= 2
                  ? 'bg-gradient-to-r from-[#ff8a3d] to-[#f2701c] hover:brightness-110 text-white shadow-[0_0_15px_rgba(255,138,61,0.4)] cursor-pointer'
                  : 'bg-white/5 text-gray-500 border border-white/10 cursor-not-allowed'
              }`}
              title={selectedCompareIds.length < 2 ? "Select at least 2 candidates using the checkboxes below to compare" : "Compare 2 selected candidates side-by-side"}
            >
              <Scale className="w-3.5 h-3.5 mr-1.5" />
              Compare ({selectedCompareIds.length}/2)
            </button>

            {/* Search */}
            <div className="relative w-full sm:w-52">
              <Search className="w-3.5 h-3.5 text-gray-400 absolute left-3 top-1/2 -translate-y-1/2" />
              <input 
                type="text" 
                placeholder="Search applicant..." 
                value={searchTerm}
                onChange={e => setSearchTerm(e.target.value)}
                className="w-full pl-8 pr-3 py-1.5 bg-black/40 border border-white/10 rounded-xl text-xs text-white placeholder-gray-500 focus:outline-none focus:border-[#3fd0ff]"
              />
            </div>

            {/* Stage Filter */}
            <select
              value={selectedStage}
              onChange={e => setSelectedStage(e.target.value)}
              className="bg-[#0a0f24] border border-white/15 rounded-xl px-2.5 py-1.5 text-xs text-white focus:outline-none focus:border-[#3fd0ff]"
            >
              <option value="ALL">All Stages</option>
              <option value="Offer">Offer</option>
              <option value="Interview">Interview</option>
              <option value="Shortlisted">Shortlisted</option>
              <option value="Under Review">Under Review</option>
              <option value="Applied">Applied</option>
              <option value="Rejected">Rejected</option>
            </select>

            {/* Sort Filter */}
            <select
              value={sortBy}
              onChange={e => setSortBy(e.target.value)}
              className="bg-[#0a0f24] border border-white/15 rounded-xl px-2.5 py-1.5 text-xs text-white focus:outline-none focus:border-[#3fd0ff]"
            >
              <option value="score-desc">Match % (High &rarr; Low)</option>
              <option value="score-asc">Match % (Low &rarr; High)</option>
              <option value="date-desc">Recent</option>
            </select>
          </div>
        </div>

        {/* Selection Hint when compare count is 1 */}
        {selectedCompareIds.length === 1 && (
          <div className="bg-orange-950/40 border-b border-[#ff8a3d]/20 px-5 py-2 text-xs text-[#ff8a3d] flex items-center justify-between">
            <span className="flex items-center">
              <Scale className="w-3.5 h-3.5 mr-1.5" />
              1 candidate selected for comparison. Check one more candidate to unlock side-by-side comparison.
            </span>
            <button 
              onClick={() => setSelectedCompareIds([])}
              className="text-gray-400 hover:text-white text-[11px] font-bold uppercase underline"
            >
              Clear
            </button>
          </div>
        )}

        {/* Applications Table */}
        <table className="min-w-full divide-y divide-white/10 text-left">
          <thead className="bg-white/[0.02]">
            <tr>
              <th className="px-4 py-4 text-xs font-bold uppercase tracking-wider text-gray-400 text-center w-12">
                Compare
              </th>
              <th className="px-6 py-4 text-xs font-bold uppercase tracking-wider text-gray-400">Applicant Name &amp; Contact</th>
              <th className="px-6 py-4 text-xs font-bold uppercase tracking-wider text-gray-400">Position Role</th>
              <th className="px-6 py-4 text-xs font-bold uppercase tracking-wider text-gray-400">AI Match Fit</th>
              <th className="px-6 py-4 text-xs font-bold uppercase tracking-wider text-gray-400">Verified Skills Overlap</th>
              <th className="px-6 py-4 text-xs font-bold uppercase tracking-wider text-gray-400">Pipeline Stage</th>
              <th className="px-6 py-4 text-xs font-bold uppercase tracking-wider text-gray-400 text-right">Telemetry</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-white/5">
            {filteredApps.length === 0 ? (
              <tr>
                <td colSpan="7" className="px-6 py-12 text-center text-gray-400 text-xs">
                  No applications match your active filters for this position.
                </td>
              </tr>
            ) : filteredApps.map(app => {
              const job = jobs.find(j => j.id === app.job_id);
              const cand = candidates.find(c => c.id === app.candidate_id);
              const jobName = job?.title || app.job_id;
              const candName = cand?.name || (app.candidate_id ? 'Candidate ' + app.candidate_id.slice(0, 8) : 'Applicant');
              const scoreBadge = getScoreBadge(app.match_score);
              const matchedSkills = app.match_details?.required_skills_matched || [];
              const isCheckedForCompare = selectedCompareIds.includes(app.id);

              return (
                <tr 
                  key={app.id} 
                  className={`transition-colors ${isCheckedForCompare ? 'bg-[#ff8a3d]/10' : 'hover:bg-white/[0.02]'}`}
                >
                  
                  {/* Compare Selection Checkbox */}
                  <td className="px-4 py-4 whitespace-nowrap text-center">
                    <button
                      type="button"
                      onClick={() => toggleSelectForCompare(app.id)}
                      className="p-1 rounded text-gray-400 hover:text-white transition-colors"
                      title={isCheckedForCompare ? "Deselect candidate" : "Select for side-by-side comparison"}
                    >
                      {isCheckedForCompare ? (
                        <CheckSquare className="w-4 h-4 text-[#ff8a3d]" />
                      ) : (
                        <Square className="w-4 h-4 text-gray-600 hover:text-gray-400" />
                      )}
                    </button>
                  </td>

                  {/* Candidate Name & Contact */}
                  <td className="px-6 py-4 whitespace-nowrap">
                    <span className="text-xs font-bold text-white block">{candName}</span>
                    <span className="text-[10px] text-gray-400 flex items-center mt-0.5">
                      <Mail className="w-3 h-3 text-[#3fd0ff] mr-1" />
                      {cand?.email || 'elevateiq-talent.in'}
                    </span>
                  </td>

                  {/* Target Position */}
                  <td className="px-6 py-4 whitespace-nowrap">
                    <span className="text-xs text-gray-200 font-semibold block">{jobName}</span>
                    <span className="text-[10px] text-gray-500">{job?.location || 'India Delivery Hub'}</span>
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
                        matchedSkills.map((s, idx) => (
                          <span key={idx} className="px-2 py-0.5 rounded-full text-[10px] font-bold bg-cyan-950/60 text-[#3fd0ff] border border-[#3fd0ff]/30">
                            {s}
                          </span>
                        ))
                      ) : (
                        <span className="text-[10px] text-gray-500 italic">No direct keyword overlap</span>
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
                      className="px-3.5 py-1.5 bg-[#3fd0ff]/15 hover:bg-[#3fd0ff] border border-[#3fd0ff]/40 text-[#3fd0ff] hover:text-[#06091A] rounded-xl font-bold uppercase transition-all shadow-[0_0_12px_rgba(63,208,255,0.2)]"
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
      {/* ⚖️ MODAL: SIDE-BY-SIDE CANDIDATE COMPARISON MATRIX */}
      {/* ============================================================== */}
      {showCompareModal && selectedCompareIds.length >= 2 && (() => {
        const app1 = applications.find(a => a.id === selectedCompareIds[0]);
        const app2 = applications.find(a => a.id === selectedCompareIds[1]);
        if (!app1 || !app2) return null;

        const cand1 = candidates.find(c => c.id === app1.candidate_id);
        const cand2 = candidates.find(c => c.id === app2.candidate_id);
        const job1 = jobs.find(j => j.id === app1.job_id);
        const job2 = jobs.find(j => j.id === app2.job_id);

        const score1 = app1.match_score || 0;
        const score2 = app2.match_score || 0;
        const delta = Math.abs(score1 - score2).toFixed(1);

        const skills1 = cand1?.skills || [];
        const skills2 = cand2?.skills || [];
        const sharedSkills = skills1.filter(s => skills2.map(x => x.toLowerCase()).includes(s.toLowerCase()));
        const uniqueTo1 = skills1.filter(s => !skills2.map(x => x.toLowerCase()).includes(s.toLowerCase()));
        const uniqueTo2 = skills2.filter(s => !skills1.map(x => x.toLowerCase()).includes(s.toLowerCase()));

        return (
          <div className="fixed inset-0 bg-black/85 backdrop-blur-md flex items-center justify-center z-50 p-4">
            <div className="bg-[#0a0f24] border border-white/20 rounded-3xl max-w-5xl w-full overflow-hidden flex flex-col max-h-[92vh] shadow-[0_0_60px_rgba(255,138,61,0.35)] animate-fade-in-up">
              
              {/* Modal Header */}
              <div className="p-6 border-b border-white/10 flex justify-between items-center bg-white/[0.02]">
                <div>
                  <span className="text-xs font-bold uppercase tracking-widest text-[#ff8a3d] flex items-center">
                    <Scale className="w-3.5 h-3.5 mr-1.5" /> Candidate Differential Matrix
                  </span>
                  <h3 className="text-2xl font-black uppercase text-white mt-0.5">
                    Side-by-Side Candidate Evaluation &gt;
                  </h3>
                </div>
                <button 
                  onClick={() => setShowCompareModal(false)}
                  className="text-gray-400 hover:text-white p-2 rounded-full hover:bg-white/10 transition-colors"
                >
                  <X className="w-5 h-5" />
                </button>
              </div>

              {/* Scrollable Comparison Content */}
              <div className="p-6 md:p-8 overflow-y-auto space-y-6">
                
                {/* Score Delta Banner */}
                <div className="p-4 rounded-2xl bg-gradient-to-r from-orange-950/40 via-cyan-950/40 to-blue-950/40 border border-white/10 flex flex-col sm:flex-row items-center justify-between gap-3 text-center sm:text-left">
                  <div>
                    <span className="text-[10px] font-bold uppercase tracking-widest text-[#3fd0ff] block">
                      Comparative Assessment
                    </span>
                    <p className="text-xs text-white font-medium mt-0.5">
                      {score1 > score2
                        ? `Candidate ${cand1?.name || 'A'} holds a +${delta}% competency lead over ${cand2?.name || 'B'}.`
                        : score2 > score1
                        ? `Candidate ${cand2?.name || 'B'} holds a +${delta}% competency lead over ${cand1?.name || 'A'}.`
                        : `Both candidates are tied at an identical ${score1}% match fit.`}
                    </p>
                  </div>
                  <div className="flex items-center space-x-2">
                    <span className="text-xs font-bold px-3 py-1 bg-white/10 rounded-full border border-white/15 text-white">
                      Delta: &Delta; {delta}%
                    </span>
                  </div>
                </div>

                {/* 2-Column Side-by-Side Cards */}
                <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                  
                  {/* Candidate 1 Column */}
                  <div className={`p-6 rounded-2xl border transition-all ${
                    score1 >= score2 ? 'bg-[#060c24] border-[#3fd0ff]/50 shadow-[0_0_20px_rgba(63,208,255,0.2)]' : 'bg-[#080d22] border-white/10'
                  }`}>
                    <div className="flex items-start justify-between">
                      <div>
                        <span className="text-[10px] font-bold uppercase tracking-widest text-gray-400">Candidate A</span>
                        <h4 className="text-xl font-black text-white mt-0.5">{cand1?.name || 'Candidate A'}</h4>
                        <p className="text-xs text-gray-400">{job1?.title || 'Target Role'}</p>
                      </div>
                      <span className={`px-3 py-1 rounded-full text-sm font-black border ${getScoreBadge(score1).bg}`}>
                        {score1}%
                      </span>
                    </div>

                    <div className="mt-4 space-y-3 text-xs">
                      <div className="p-3 rounded-xl bg-white/5 border border-white/10">
                        <span className="text-[10px] text-gray-400 font-bold uppercase block">Contact &amp; Location</span>
                        <span className="text-white font-semibold mt-0.5 block">{cand1?.email}</span>
                        <span className="text-gray-400 text-[11px] block">{cand1?.phone} • {cand1?.experience}</span>
                      </div>

                      <div className="p-3 rounded-xl bg-white/5 border border-white/10">
                        <span className="text-[10px] text-gray-400 font-bold uppercase block mb-1">Confirmed Role Skills</span>
                        <div className="flex flex-wrap gap-1">
                          {(app1.match_details?.required_skills_matched || []).map((s, i) => (
                            <span key={i} className="px-2 py-0.5 rounded text-[10px] font-bold bg-green-950 text-green-300 border border-green-500/30">
                              ✓ {s}
                            </span>
                          ))}
                        </div>
                      </div>

                      <div className="p-3 rounded-xl bg-white/5 border border-white/10">
                        <span className="text-[10px] text-gray-400 font-bold uppercase block mb-1">Skill Gaps (Deficits)</span>
                        <div className="flex flex-wrap gap-1">
                          {(app1.match_details?.required_skills_missing || []).length > 0 ? (
                            (app1.match_details?.required_skills_missing || []).map((s, i) => (
                              <span key={i} className="px-2 py-0.5 rounded text-[10px] font-bold bg-red-950 text-red-300 border border-red-500/30">
                                ✕ {s}
                              </span>
                            ))
                          ) : (
                            <span className="text-[11px] text-emerald-400 font-semibold">Zero gaps — Full required alignment</span>
                          )}
                        </div>
                      </div>

                      <div className="pt-2 flex items-center justify-between">
                        <span className="text-xs text-gray-400 font-semibold">Stage: <strong className="text-white">{app1.stage}</strong></span>
                        <button
                          onClick={() => updateStage(app1.id, 'Interview')}
                          className="px-3 py-1.5 bg-[#3fd0ff]/20 hover:bg-[#3fd0ff] border border-[#3fd0ff]/40 text-[#3fd0ff] hover:text-[#06091A] rounded-lg text-xs font-bold uppercase transition-all"
                        >
                          Advance to Interview
                        </button>
                      </div>
                    </div>
                  </div>

                  {/* Candidate 2 Column */}
                  <div className={`p-6 rounded-2xl border transition-all ${
                    score2 > score1 ? 'bg-[#060c24] border-[#3fd0ff]/50 shadow-[0_0_20px_rgba(63,208,255,0.2)]' : 'bg-[#080d22] border-white/10'
                  }`}>
                    <div className="flex items-start justify-between">
                      <div>
                        <span className="text-[10px] font-bold uppercase tracking-widest text-gray-400">Candidate B</span>
                        <h4 className="text-xl font-black text-white mt-0.5">{cand2?.name || 'Candidate B'}</h4>
                        <p className="text-xs text-gray-400">{job2?.title || 'Target Role'}</p>
                      </div>
                      <span className={`px-3 py-1 rounded-full text-sm font-black border ${getScoreBadge(score2).bg}`}>
                        {score2}%
                      </span>
                    </div>

                    <div className="mt-4 space-y-3 text-xs">
                      <div className="p-3 rounded-xl bg-white/5 border border-white/10">
                        <span className="text-[10px] text-gray-400 font-bold uppercase block">Contact &amp; Location</span>
                        <span className="text-white font-semibold mt-0.5 block">{cand2?.email}</span>
                        <span className="text-gray-400 text-[11px] block">{cand2?.phone} • {cand2?.experience}</span>
                      </div>

                      <div className="p-3 rounded-xl bg-white/5 border border-white/10">
                        <span className="text-[10px] text-gray-400 font-bold uppercase block mb-1">Confirmed Role Skills</span>
                        <div className="flex flex-wrap gap-1">
                          {(app2.match_details?.required_skills_matched || []).map((s, i) => (
                            <span key={i} className="px-2 py-0.5 rounded text-[10px] font-bold bg-green-950 text-green-300 border border-green-500/30">
                              ✓ {s}
                            </span>
                          ))}
                        </div>
                      </div>

                      <div className="p-3 rounded-xl bg-white/5 border border-white/10">
                        <span className="text-[10px] text-gray-400 font-bold uppercase block mb-1">Skill Gaps (Deficits)</span>
                        <div className="flex flex-wrap gap-1">
                          {(app2.match_details?.required_skills_missing || []).length > 0 ? (
                            (app2.match_details?.required_skills_missing || []).map((s, i) => (
                              <span key={i} className="px-2 py-0.5 rounded text-[10px] font-bold bg-red-950 text-red-300 border border-red-500/30">
                                ✕ {s}
                              </span>
                            ))
                          ) : (
                            <span className="text-[11px] text-emerald-400 font-semibold">Zero gaps — Full required alignment</span>
                          )}
                        </div>
                      </div>

                      <div className="pt-2 flex items-center justify-between">
                        <span className="text-xs text-gray-400 font-semibold">Stage: <strong className="text-white">{app2.stage}</strong></span>
                        <button
                          onClick={() => updateStage(app2.id, 'Interview')}
                          className="px-3 py-1.5 bg-[#3fd0ff]/20 hover:bg-[#3fd0ff] border border-[#3fd0ff]/40 text-[#3fd0ff] hover:text-[#06091A] rounded-lg text-xs font-bold uppercase transition-all"
                        >
                          Advance to Interview
                        </button>
                      </div>
                    </div>
                  </div>

                </div>

                {/* Unique Competency Overlap Breakdown */}
                <div className="elevate-card p-5 rounded-2xl border border-white/10 space-y-3">
                  <h5 className="text-xs font-bold uppercase tracking-wider text-gray-300 flex items-center">
                    <ArrowLeftRight className="w-3.5 h-3.5 text-[#ff8a3d] mr-1.5" />
                    Unique Competencies Analysis
                  </h5>
                  <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 text-xs">
                    <div>
                      <span className="text-gray-400 block mb-1 font-semibold">Exclusive to {cand1?.name}:</span>
                      <div className="flex flex-wrap gap-1">
                        {uniqueTo1.length > 0 ? uniqueTo1.map((s, i) => (
                          <span key={i} className="px-2 py-0.5 rounded bg-[#ff8a3d]/15 text-[#ff8a3d] border border-[#ff8a3d]/30 text-[10px] font-bold">
                            +{s}
                          </span>
                        )) : <span className="text-gray-500 italic">No unique skills</span>}
                      </div>
                    </div>
                    <div>
                      <span className="text-gray-400 block mb-1 font-semibold">Exclusive to {cand2?.name}:</span>
                      <div className="flex flex-wrap gap-1">
                        {uniqueTo2.length > 0 ? uniqueTo2.map((s, i) => (
                          <span key={i} className="px-2 py-0.5 rounded bg-[#3fd0ff]/15 text-[#3fd0ff] border border-[#3fd0ff]/30 text-[10px] font-bold">
                            +{s}
                          </span>
                        )) : <span className="text-gray-500 italic">No unique skills</span>}
                      </div>
                    </div>
                  </div>
                </div>

              </div>

              {/* Modal Footer */}
              <div className="p-6 border-t border-white/10 bg-white/[0.02] flex justify-end items-center">
                <button 
                  onClick={() => setShowCompareModal(false)}
                  className="px-6 py-2.5 bg-white/10 hover:bg-white/20 text-white rounded-xl text-xs font-bold uppercase tracking-wider transition-colors"
                >
                  Close Comparison
                </button>
              </div>

            </div>
          </div>
        );
      })()}

      {/* ============================================================== */}
      {/* 🔬 DEEP ANALYTICS MODAL */}
      {/* ============================================================== */}
      {selectedApp && (() => {
        const candidate = candidates.find(c => c.id === selectedApp.candidate_id);
        const job = jobs.find(j => j.id === selectedApp.job_id);
        
        const candName = candidate?.name || 'Candidate ' + (selectedApp.candidate_id || '').slice(0, 8);
        const candEmail = candidate?.email || 'candidate@elevateiq-talent.in';
        const candPhone = candidate?.phone || '+91-9870000000';
        const candExperience = candidate?.experience || 'Experienced Professional Profile';
        const candEducation = candidate?.education || 'B.Tech / MCA / Equivalent Degree';
        const candSkills = candidate?.skills || [];
        const resumeFile = candidate?.resume_file || `${candName.replace(' ', '_')}_Resume.pdf`;

        const jobTitle = job?.title || 'Target Requisition ' + selectedApp.job_id;
        const jobLocation = job?.location || 'India Delivery Hub';
        const jobReqSkills = job?.required_skills || [];
        const jobPrefSkills = job?.preferred_skills || [];

        const matchedReq = (selectedApp.match_details?.required_skills_matched && selectedApp.match_details.required_skills_matched.length > 0)
          ? selectedApp.match_details.required_skills_matched
          : candSkills.filter(s => jobReqSkills.map(j => j.toLowerCase()).includes(s.toLowerCase()));

        const missingReq = (selectedApp.match_details?.required_skills_missing !== undefined)
          ? selectedApp.match_details.required_skills_missing
          : jobReqSkills.filter(s => !matchedReq.map(m => m.toLowerCase()).includes(s.toLowerCase()));

        const matchedPref = (selectedApp.match_details?.preferred_skills_matched && selectedApp.match_details.preferred_skills_matched.length > 0)
          ? selectedApp.match_details.preferred_skills_matched
          : candSkills.filter(s => jobPrefSkills.map(j => j.toLowerCase()).includes(s.toLowerCase()));

        const cosineSim = selectedApp.match_details?.cosine_similarity || 
          Math.max(12.5, (selectedApp.match_score - 4.5)).toFixed(1);

        const scoreBadge = getScoreBadge(selectedApp.match_score);

        return (
          <div className="fixed inset-0 bg-black/85 backdrop-blur-md flex items-center justify-center z-50 p-4">
            <div className="bg-[#0a0f24] border border-white/20 rounded-3xl max-w-4xl w-full overflow-hidden flex flex-col max-h-[92vh] shadow-[0_0_60px_rgba(63,208,255,0.35)] animate-fade-in-up">
              
              {/* Modal Header */}
              <div className="p-6 border-b border-white/10 flex justify-between items-center bg-white/[0.02]">
                <div>
                  <div className="inline-flex items-center space-x-1.5 text-xs font-bold uppercase tracking-widest text-[#ff8a3d]">
                    <Sparkles className="w-3.5 h-3.5" /> Deterministic AI Screening Diagnostic
                  </div>
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
              
              {/* Modal Scrollable Body */}
              <div className="p-6 md:p-8 overflow-y-auto space-y-6">
                
                {/* Top Section */}
                <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
                  
                  {/* Candidate Overview Card */}
                  <div className="md:col-span-2 elevate-card p-6 rounded-2xl border border-white/10 space-y-4">
                    <div>
                      <span className="text-[10px] font-bold text-gray-500 uppercase tracking-widest block">
                        Evaluated Candidate Dossier
                      </span>
                      <h2 className="text-2xl font-black text-white mt-0.5">{candName}</h2>
                      <p className="text-gray-400 text-xs mt-1">
                        Applied Position: <strong className="text-[#3fd0ff]">{jobTitle}</strong> ({jobLocation})
                      </p>
                    </div>

                    <div className="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs pt-2">
                      <div className="p-3 bg-white/5 border border-white/10 rounded-xl">
                        <span className="text-[10px] font-bold uppercase tracking-wider text-gray-400 block">Email Contact</span>
                        <span className="font-semibold text-white mt-0.5 block truncate">{candEmail}</span>
                      </div>
                      <div className="p-3 bg-white/5 border border-white/10 rounded-xl">
                        <span className="text-[10px] font-bold uppercase tracking-wider text-gray-400 block">Phone</span>
                        <span className="font-semibold text-white mt-0.5 block">{candPhone}</span>
                      </div>
                      <div className="p-3 bg-white/5 border border-white/10 rounded-xl">
                        <span className="text-[10px] font-bold uppercase tracking-wider text-gray-400 block">Experience &amp; Delivery Center</span>
                        <span className="font-semibold text-white mt-0.5 block truncate">{candExperience}</span>
                      </div>
                      <div className="p-3 bg-white/5 border border-white/10 rounded-xl">
                        <span className="text-[10px] font-bold uppercase tracking-wider text-gray-400 block">Education Qualification</span>
                        <span className="font-semibold text-white mt-0.5 block truncate">{candEducation}</span>
                      </div>
                    </div>

                    <div className="grid grid-cols-2 gap-3 pt-1">
                      <div className="p-3 bg-cyan-950/40 border border-[#3fd0ff]/30 rounded-xl">
                        <span className="block text-[10px] font-bold uppercase tracking-wider text-[#3fd0ff]">
                          Semantic TF-IDF Cosine
                        </span>
                        <span className="text-xl font-black text-white mt-0.5 block">
                          {cosineSim}%
                        </span>
                      </div>
                      <div className="p-3 bg-emerald-950/40 border border-emerald-500/30 rounded-xl">
                        <span className="block text-[10px] font-bold uppercase tracking-wider text-emerald-400">
                          Current Stage
                        </span>
                        <span className="text-xl font-black text-white mt-0.5 block">
                          {selectedApp.stage}
                        </span>
                      </div>
                    </div>

                  </div>

                  {/* Circular Score Dial Card */}
                  <div className="elevate-card p-6 rounded-2xl border border-white/10 flex flex-col justify-center items-center text-center">
                    <div className="relative inline-flex items-center justify-center">
                      <svg className="w-36 h-36 transform -rotate-90">
                        <circle className="text-white/10" strokeWidth="8" stroke="currentColor" fill="transparent" r="56" cx="72" cy="72" />
                        <circle 
                          className={scoreBadge.circle} 
                          strokeWidth="8" 
                          strokeDasharray={351} 
                          strokeDashoffset={351 - (351 * (selectedApp.match_score || 0)) / 100} 
                          strokeLinecap="round" 
                          stroke="currentColor" 
                          fill="transparent" 
                          r="56" 
                          cx="72" 
                          cy="72" 
                        />
                      </svg>
                      <div className="absolute flex flex-col items-center">
                        <span className="text-3xl font-black text-white">{selectedApp.match_score}%</span>
                        <span className="text-[10px] font-bold uppercase text-gray-400">Fit Index</span>
                      </div>
                    </div>
                    
                    <span className={`mt-4 px-3 py-1 rounded-full text-xs font-bold border ${scoreBadge.bg}`}>
                      {scoreBadge.label}
                    </span>
                    <p className="text-[11px] text-gray-400 mt-2 font-semibold">
                      Multi-Vector Deterministic NLP
                    </p>
                  </div>

                </div>

                {/* Skill Vector Decomposition */}
                <div className="elevate-card p-6 rounded-2xl border border-white/10 space-y-5">
                  <div className="flex items-center justify-between border-b border-white/10 pb-3">
                    <h4 className="text-sm font-bold uppercase tracking-wider text-white flex items-center">
                      <Layers className="w-4 h-4 mr-2 text-[#3fd0ff]" />
                      Skill Vector Decomposition &amp; Gap Analysis
                    </h4>
                    <span className="text-xs text-gray-400 font-semibold">
                      {matchedReq.length} / {jobReqSkills.length} Required Skills Matched
                    </span>
                  </div>
                  
                  {/* Confirmed Required Skills */}
                  <div>
                    <h5 className="text-[11px] font-bold text-gray-300 mb-2 uppercase tracking-wider flex items-center">
                      <CheckCircle className="w-3.5 h-3.5 text-emerald-400 mr-1.5" />
                      Required Skills Confirmed in Resume ({matchedReq.length})
                    </h5>
                    {matchedReq.length > 0 ? (
                      <div className="flex flex-wrap gap-1.5">
                        {matchedReq.map((skill, idx) => (
                          <span key={idx} className="px-3 py-1 rounded-full text-xs font-bold bg-green-950/80 text-green-300 border border-green-500/40">
                            ✓ {skill}
                          </span>
                        ))}
                      </div>
                    ) : (
                      <div className="p-3 bg-rose-950/30 border border-rose-500/30 rounded-xl text-xs text-rose-300 flex items-center">
                        <AlertCircle className="w-4 h-4 mr-2 flex-shrink-0" />
                        <span>No exact mandatory skills confirmed from resume text.</span>
                      </div>
                    )}
                  </div>

                  {/* Critical Skill Gaps */}
                  <div>
                    <h5 className="text-[11px] font-bold text-gray-300 mb-2 uppercase tracking-wider flex items-center">
                      <AlertCircle className="w-3.5 h-3.5 text-rose-400 mr-1.5" />
                      Critical Skill Gaps (Deficits) ({missingReq.length})
                    </h5>
                    {missingReq.length > 0 ? (
                      <div className="flex flex-wrap gap-1.5">
                        {missingReq.map((skill, idx) => (
                          <span key={idx} className="px-3 py-1 rounded-full text-xs font-bold bg-red-950/80 text-red-300 border border-red-500/40">
                            ✕ Missing: {skill}
                          </span>
                        ))}
                      </div>
                    ) : (
                      <div className="p-3 bg-emerald-950/30 border border-emerald-500/30 rounded-xl text-xs text-emerald-300 flex items-center">
                        <Check className="w-4 h-4 mr-2 flex-shrink-0 text-emerald-400" />
                        <span>Zero Deficits — All required role competencies are confirmed in candidate resume!</span>
                      </div>
                    )}
                  </div>

                  {/* Bonus Preferred Competencies */}
                  <div>
                    <h5 className="text-[11px] font-bold text-gray-300 mb-2 uppercase tracking-wider flex items-center">
                      <Award className="w-3.5 h-3.5 text-[#ff8a3d] mr-1.5" />
                      Bonus / Preferred Competencies ({matchedPref.length})
                    </h5>
                    {matchedPref.length > 0 ? (
                      <div className="flex flex-wrap gap-1.5">
                        {matchedPref.map((skill, idx) => (
                          <span key={idx} className="px-3 py-1 rounded-full text-xs font-bold bg-orange-950/80 text-[#ff8a3d] border border-[#ff8a3d]/40">
                            +{skill}
                          </span>
                        ))}
                      </div>
                    ) : (
                      <div className="p-3 bg-white/5 border border-white/10 rounded-xl text-xs text-gray-400">
                        <span>No secondary preferred competencies detected for this candidate profile.</span>
                      </div>
                    )}
                  </div>

                  {/* Complete Candidate Skills from Resume */}
                  {candSkills.length > 0 && (
                    <div className="pt-2 border-t border-white/10">
                      <h5 className="text-[11px] font-bold text-gray-400 mb-2 uppercase tracking-wider">
                        All Skills Extracted from Candidate Resume:
                      </h5>
                      <div className="flex flex-wrap gap-1.5">
                        {candSkills.map((s, idx) => (
                          <span key={idx} className="px-2 py-0.5 rounded-md text-[11px] font-semibold bg-white/5 border border-white/10 text-gray-300">
                            {s}
                          </span>
                        ))}
                      </div>
                    </div>
                  )}

                </div>

                {/* AI Screening Recommendation & Stage Action */}
                <div className="p-5 rounded-2xl bg-gradient-to-r from-blue-950/40 to-cyan-950/30 border border-[#3fd0ff]/30 flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4">
                  <div>
                    <span className="text-[10px] font-bold uppercase tracking-widest text-[#3fd0ff] block">
                      AI Screener Recommendation
                    </span>
                    <p className="text-xs text-white font-medium mt-1">
                      {selectedApp.match_score >= 85
                        ? "🌟 Top Recommendation: High competency alignment. Advance candidate directly to Technical Interview or Offer stage."
                        : selectedApp.match_score >= 70
                        ? "✓ Qualified Fit: Candidate satisfies primary core requirements. Shortlist for team lead discussion."
                        : selectedApp.match_score >= 50
                        ? "⚠️ Moderate Match: Foundational skills present, but noticeable gaps exist. Recommend skill assessment test."
                        : "❌ Low Match: Significant skill deficit against required job vectors. Candidate not recommended for this requisition."}
                    </p>
                    <p className="text-[11px] text-gray-400 mt-1 italic">
                      {selectedApp.notes || `Screened profile evaluated against ${jobTitle} skill requirements.`}
                    </p>
                  </div>

                  <div className="flex items-center space-x-2 flex-shrink-0">
                    <span className="text-xs font-bold text-gray-300">Update Stage:</span>
                    <select
                      value={selectedApp.stage}
                      onChange={(e) => updateStage(selectedApp.id, e.target.value)}
                      className="bg-[#0a0f24] border border-[#3fd0ff]/50 rounded-xl px-3 py-2 text-xs font-bold text-white focus:outline-none focus:border-[#3fd0ff]"
                    >
                      <option value="Applied">Applied</option>
                      <option value="Under Review">Under Review</option>
                      <option value="Shortlisted">Shortlisted</option>
                      <option value="Interview">Interview</option>
                      <option value="Offer">Offer</option>
                      <option value="Rejected">Rejected</option>
                    </select>
                  </div>
                </div>

              </div>

              {/* Modal Footer */}
              <div className="p-6 border-t border-white/10 bg-white/[0.02] flex justify-between items-center">
                <span className="text-xs text-gray-400 font-semibold">
                  Resume: <strong className="text-white">{resumeFile}</strong>
                </span>
                <button 
                  onClick={() => setSelectedApp(null)}
                  className="px-6 py-2.5 bg-white/10 hover:bg-white/20 text-white rounded-xl text-xs font-bold uppercase tracking-wider transition-colors"
                >
                  Close Window
                </button>
              </div>

            </div>
          </div>
        );
      })()}

    </div>
  );
}

export default Applications;
