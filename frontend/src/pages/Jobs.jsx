import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom';
import { 
  Briefcase, Plus, RefreshCw, Trash2, Eye, MapPin, Sparkles, 
  X, Check, Search, Tag, AlertCircle, Building2, Layers, Users, ArrowUpRight
} from 'lucide-react';

const API_BASE = 'http://localhost:8000/api';

function Jobs() {
  const [jobs, setJobs] = useState([]);
  const [applications, setApplications] = useState([]);
  const [candidates, setCandidates] = useState([]);
  const [showForm, setShowForm] = useState(false);
  const [searchTerm, setSearchTerm] = useState('');
  const [selectedJobView, setSelectedJobView] = useState(null);
  const [successMsg, setSuccessMsg] = useState('');

  // Form State
  const [title, setTitle] = useState('');
  const [department, setDepartment] = useState('IT Engineering');
  const [location, setLocation] = useState('Chennai');
  const [experience, setExperience] = useState(3);
  const [education, setEducation] = useState('B.Tech / MCA / Equivalent');
  const [description, setDescription] = useState('');
  
  // Interactive Manual Skills State
  const [requiredSkills, setRequiredSkills] = useState(['python', 'react']);
  const [preferredSkills, setPreferredSkills] = useState(['docker', 'aws']);
  const [newRequiredInput, setNewRequiredInput] = useState('');
  const [newPreferredInput, setNewPreferredInput] = useState('');

  // Suggested Skill Chips for Quick Add
  const suggestedITSkills = ['fastapi', 'next.js', 'typescript', 'kubernetes', 'sql', 'microservices', 'graphql', 'tailwind'];
  const suggestedDataSkills = ['machine learning', 'nlp', 'data scraping', 'selenium', 'pandas', 'ocr', 'tensorflow'];
  const suggestedBPOSkills = ['medical coding', 'icd-10', 'cpt coding', 'ar calling', 'rcm operations', 'hipaa', 'tess support'];

  const fetchJobs = () => {
    axios.get(`${API_BASE}/jobs/`).then(res => setJobs(res.data)).catch(err => console.error(err));
    axios.get(`${API_BASE}/applications/`).then(res => setApplications(res.data)).catch(err => console.error(err));
    axios.get(`${API_BASE}/candidates/`).then(res => setCandidates(res.data)).catch(err => console.error(err));
  };

  useEffect(() => { 
    fetchJobs(); 
  }, []);

  // Handlers for Required Skills
  const addRequiredSkill = (skillToAdd) => {
    const trimmed = (skillToAdd || newRequiredInput).trim().toLowerCase();
    if (trimmed && !requiredSkills.includes(trimmed)) {
      setRequiredSkills([...requiredSkills, trimmed]);
      setNewRequiredInput('');
    }
  };

  const removeRequiredSkill = (skillToRemove) => {
    setRequiredSkills(requiredSkills.filter(s => s !== skillToRemove));
  };

  // Handlers for Preferred Skills
  const addPreferredSkill = (skillToAdd) => {
    const trimmed = (skillToAdd || newPreferredInput).trim().toLowerCase();
    if (trimmed && !preferredSkills.includes(trimmed)) {
      setPreferredSkills([...preferredSkills, trimmed]);
      setNewPreferredInput('');
    }
  };

  const removePreferredSkill = (skillToRemove) => {
    setPreferredSkills(preferredSkills.filter(s => s !== skillToRemove));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (requiredSkills.length === 0) {
      alert("Please add at least one required skill manually.");
      return;
    }

    const payload = {
      title,
      department,
      location,
      min_experience_years: parseInt(experience),
      education_requirement: education,
      description,
      required_skills: requiredSkills,
      preferred_skills: preferredSkills
    };

    try {
      await axios.post(`${API_BASE}/jobs/`, payload);
      setSuccessMsg(`Job Opportunity "${title}" successfully created with ${requiredSkills.length} required and ${preferredSkills.length} preferred skills!`);
      setTimeout(() => setSuccessMsg(''), 5000);
      
      // Reset Form
      setTitle('');
      setDescription('');
      setRequiredSkills(['python', 'react']);
      setPreferredSkills(['docker']);
      setShowForm(false);
      fetchJobs();
    } catch (err) {
      console.error(err);
      alert("Error saving job requisition. Please verify all fields.");
    }
  };

  const handleDelete = async (id) => {
    if (window.confirm("Are you sure you want to permanently delete this job requisition?")) {
      try {
        await axios.delete(`${API_BASE}/jobs/${id}`);
        fetchJobs();
      } catch (err) {
        alert("Error deleting job.");
      }
    }
  };

  const filteredJobs = jobs.filter(job => 
    job.title?.toLowerCase().includes(searchTerm.toLowerCase()) ||
    job.department?.toLowerCase().includes(searchTerm.toLowerCase()) ||
    job.location?.toLowerCase().includes(searchTerm.toLowerCase()) ||
    job.required_skills?.some(s => s.toLowerCase().includes(searchTerm.toLowerCase()))
  );

  return (
    <div className="animate-fade-in-up text-white">
      
      {/* Page Header */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between pb-6 mb-8 border-b border-white/10">
        <div>
          <div className="inline-flex items-center space-x-1 text-xs font-bold uppercase tracking-widest text-[#ff8a3d] mb-1">
            <Sparkles className="w-3.5 h-3.5 mr-1" /> Requisition &amp; Skill Vector Builder
          </div>
          <h2 className="text-3xl font-black uppercase tracking-tight text-white">
            Job Opportunities &amp; Skills Console <span className="text-[#3fd0ff]">&gt;</span>
          </h2>
          <p className="text-gray-400 text-xs mt-1">
            Manually create enterprise job postings, define strict required skills, and configure bonus competency weights.
          </p>
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
            className="px-5 py-2.5 bg-gradient-to-r from-[#ff8a3d] to-[#f2701c] hover:brightness-110 text-white rounded-xl text-xs font-bold uppercase tracking-wider transition-all shadow-[0_0_20px_rgba(255,138,61,0.35)] flex items-center"
          >
            {showForm ? 'Close Builder' : '+ Add Job Opportunity & Skills'}
          </button>
        </div>
      </div>

      {/* Success Notification Banner */}
      {successMsg && (
        <div className="mb-6 p-4 rounded-xl bg-emerald-950/70 border border-emerald-500/40 text-emerald-300 text-xs font-semibold flex items-center shadow-lg animate-fade-in-up">
          <Check className="w-4 h-4 mr-2 text-emerald-400 flex-shrink-0" />
          <span>{successMsg}</span>
        </div>
      )}

      {/* ============================================================== */}
      {/* 🚀 MANUAL JOB OPPORTUNITY & SKILL BUILDER FORM */}
      {/* ============================================================== */}
      {showForm && (
        <div className="elevate-card p-8 rounded-3xl mb-10 border border-white/10 shadow-2xl animate-fade-in-up">
          <div className="flex items-center justify-between pb-4 mb-6 border-b border-white/10">
            <div>
              <span className="text-xs font-bold uppercase tracking-widest text-[#3fd0ff] block">Recruiter Studio</span>
              <h3 className="text-2xl font-black uppercase text-white mt-0.5">
                Manual Job Requisition &amp; Skill Configuration
              </h3>
            </div>
            <span className="text-xs text-gray-400 font-semibold bg-white/5 px-3 py-1 rounded-full border border-white/10">
              Live Synchronization Enabled
            </span>
          </div>

          <form onSubmit={handleSubmit} className="space-y-8">
            <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
              
              {/* Left Column: Job Details */}
              <div className="lg:col-span-2 space-y-5">
                <div>
                  <label className="block text-xs font-bold uppercase tracking-wider text-gray-300 mb-1.5">
                    Position Title *
                  </label>
                  <input 
                    type="text"
                    required
                    placeholder="e.g. Lead Full-Stack Software Engineer" 
                    value={title}
                    onChange={e => setTitle(e.target.value)}
                    className="w-full bg-white/5 border border-white/15 p-3 rounded-xl text-white placeholder-gray-500 focus:outline-none focus:border-[#3fd0ff] text-sm" 
                  />
                </div>

                <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                  <div>
                    <label className="block text-xs font-bold uppercase tracking-wider text-gray-300 mb-1.5">
                      Department / Domain *
                    </label>
                    <select 
                      value={department}
                      onChange={e => setDepartment(e.target.value)}
                      className="w-full bg-[#0a0f24] border border-white/15 p-3 rounded-xl text-white text-xs focus:outline-none focus:border-[#3fd0ff]"
                    >
                      <option value="IT Engineering">IT Engineering</option>
                      <option value="Data Solutions">Data Solutions &amp; Crawlers</option>
                      <option value="Cloud & Infra">Cloud, DevOps &amp; Infrastructure</option>
                      <option value="AI Solutions">AI &amp; Document Intelligence (IDP)</option>
                      <option value="Non-IT & Healthcare BPO">Non-IT &amp; Healthcare BPO (Medical Coding)</option>
                      <option value="BPO & Customer Operations">BPO &amp; Customer Operations (TESS/AR)</option>
                    </select>
                  </div>

                  <div>
                    <label className="block text-xs font-bold uppercase tracking-wider text-gray-300 mb-1.5">
                      Delivery Hub / Branch *
                    </label>
                    <select 
                      value={location}
                      onChange={e => setLocation(e.target.value)}
                      className="w-full bg-[#0a0f24] border border-white/15 p-3 rounded-xl text-white text-xs focus:outline-none focus:border-[#3fd0ff]"
                    >
                      <option value="Chennai">Chennai Branch (Guindy)</option>
                      <option value="Kochi">Kochi Branch (LR Towers)</option>
                      <option value="Narasaraopet">Narasaraopet Branch (Arundelpet)</option>
                      <option value="Hyderabad">Hyderabad Tech Center</option>
                      <option value="Bengaluru">Bengaluru Innovation Core</option>
                    </select>
                  </div>
                </div>

                <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                  <div>
                    <label className="block text-xs font-bold uppercase tracking-wider text-gray-300 mb-1.5">
                      Min Experience Required: <span className="text-[#ff8a3d] font-black">{experience} Years</span>
                    </label>
                    <input 
                      type="range"
                      min="0"
                      max="15"
                      value={experience}
                      onChange={e => setExperience(e.target.value)}
                      className="w-full accent-[#ff8a3d] bg-white/10 rounded-lg cursor-pointer h-2 mt-2" 
                    />
                  </div>

                  <div>
                    <label className="block text-xs font-bold uppercase tracking-wider text-gray-300 mb-1.5">
                      Education Requirement
                    </label>
                    <input 
                      type="text"
                      placeholder="e.g. B.Tech / MCA / B.Pharm" 
                      value={education}
                      onChange={e => setEducation(e.target.value)}
                      className="w-full bg-white/5 border border-white/15 p-3 rounded-xl text-white placeholder-gray-500 focus:outline-none focus:border-[#3fd0ff] text-sm" 
                    />
                  </div>
                </div>

                <div>
                  <label className="block text-xs font-bold uppercase tracking-wider text-gray-300 mb-1.5">
                    Position Description &amp; Responsibilities *
                  </label>
                  <textarea 
                    rows={4}
                    required
                    placeholder="Describe role responsibilities, key project deliverables, and team dynamics..." 
                    value={description}
                    onChange={e => setDescription(e.target.value)}
                    className="w-full bg-white/5 border border-white/15 p-3 rounded-xl text-white placeholder-gray-500 focus:outline-none focus:border-[#3fd0ff] text-sm" 
                  />
                </div>
              </div>

              {/* Right Column: Live Requisition Preview Card */}
              <div className="bg-[#040714] border border-white/10 p-6 rounded-2xl flex flex-col justify-between">
                <div>
                  <span className="text-[10px] font-bold uppercase tracking-widest text-gray-400 block mb-3">
                    Live Careers Portal Preview
                  </span>
                  
                  <div className="p-4 rounded-xl bg-white/5 border border-white/10 mb-4">
                    <span className="text-[10px] font-bold uppercase tracking-widest text-[#ff8a3d]">
                      {department} • ElevateIQ
                    </span>
                    <h4 className="text-lg font-black text-white mt-1">
                      {title || 'Untitled Opportunity'}
                    </h4>
                    
                    <div className="flex items-center text-xs text-gray-400 my-2">
                      <MapPin className="w-3.5 h-3.5 text-[#3fd0ff] mr-1" />
                      <span>{location} Branch, India</span>
                      <span className="mx-2 text-gray-600">•</span>
                      <span>{experience}+ Yrs Exp</span>
                    </div>

                    <p className="text-gray-400 text-xs line-clamp-2 my-2">
                      {description || 'Enter a description on the left to see the live candidate preview...'}
                    </p>

                    <div className="mt-3">
                      <div className="text-[10px] font-bold text-gray-400 uppercase tracking-wider mb-1">Configured Skills:</div>
                      <div className="flex flex-wrap gap-1">
                        {requiredSkills.map((s, idx) => (
                          <span key={idx} className="text-[10px] font-semibold px-2 py-0.5 rounded bg-[#3fd0ff]/20 border border-[#3fd0ff]/40 text-[#3fd0ff]">
                            {s}
                          </span>
                        ))}
                        {preferredSkills.map((s, idx) => (
                          <span key={idx} className="text-[10px] font-semibold px-2 py-0.5 rounded bg-[#ff8a3d]/20 border border-[#ff8a3d]/40 text-[#ff8a3d]">
                            +{s}
                          </span>
                        ))}
                      </div>
                    </div>
                  </div>
                </div>

                <div className="text-[11px] text-gray-400 border-t border-white/10 pt-3 flex items-center">
                  <Check className="w-3.5 h-3.5 mr-1 text-green-400" />
                  Synced with ElevateIQ Local Neural Matcher
                </div>
              </div>

            </div>

            {/* ======================================================= */}
            {/* 🛠️ MANUAL SKILLS BUILDER (REQUIRED & PREFERRED) */}
            {/* ======================================================= */}
            <div className="pt-6 border-t border-white/10 space-y-6">
              
              {/* 1. REQUIRED SKILLS BUCKET */}
              <div className="p-6 rounded-2xl bg-white/[0.02] border border-white/10">
                <div className="flex flex-col sm:flex-row sm:items-center justify-between mb-4">
                  <div>
                    <h4 className="text-sm font-bold uppercase tracking-wider text-white flex items-center">
                      <span className="w-2.5 h-2.5 rounded-full bg-[#3fd0ff] mr-2"></span>
                      1. Strict Required Skills ({requiredSkills.length} tagged)
                    </h4>
                    <p className="text-gray-400 text-xs mt-0.5">
                      Candidates must possess these skills to achieve a passing compatibility score.
                    </p>
                  </div>
                  
                  {/* Manual Skill Input */}
                  <div className="mt-3 sm:mt-0 flex gap-2">
                    <input 
                      type="text" 
                      placeholder="Type skill & press Enter..." 
                      value={newRequiredInput}
                      onChange={e => setNewRequiredInput(e.target.value)}
                      onKeyDown={e => { if (e.key === 'Enter') { e.preventDefault(); addRequiredSkill(); } }}
                      className="bg-black/60 border border-white/15 px-3 py-1.5 rounded-xl text-xs text-white placeholder-gray-500 focus:outline-none focus:border-[#3fd0ff]"
                    />
                    <button 
                      type="button"
                      onClick={() => addRequiredSkill()}
                      className="px-3 py-1.5 bg-[#3fd0ff] hover:bg-[#16a6e0] text-black font-bold text-xs uppercase tracking-wider rounded-xl transition-colors"
                    >
                      + Add
                    </button>
                  </div>
                </div>

                {/* Active Required Badges */}
                <div className="flex flex-wrap gap-2 min-h-[38px] p-3 rounded-xl bg-black/40 border border-white/10 mb-4">
                  {requiredSkills.length === 0 ? (
                    <span className="text-xs text-gray-500 italic">No required skills added yet. Type above or click suggestions below.</span>
                  ) : (
                    requiredSkills.map((skill, idx) => (
                      <span 
                        key={idx}
                        className="inline-flex items-center px-3 py-1 rounded-full text-xs font-bold bg-[#3fd0ff]/15 border border-[#3fd0ff]/40 text-[#3fd0ff]"
                      >
                        {skill}
                        <button 
                          type="button" 
                          onClick={() => removeRequiredSkill(skill)}
                          className="ml-2 hover:text-white"
                        >
                          <X className="w-3.5 h-3.5" />
                        </button>
                      </span>
                    ))
                  )}
                </div>

                {/* Quick Add Suggestions */}
                <div className="flex flex-wrap items-center gap-1.5 text-xs text-gray-400">
                  <span className="font-semibold text-gray-400 mr-1 flex items-center">
                    <Tag className="w-3 h-3 mr-1 text-[#3fd0ff]" /> Quick Add:
                  </span>
                  {[...suggestedITSkills, ...suggestedDataSkills.slice(0, 4), ...suggestedBPOSkills.slice(0, 3)].map((s, idx) => (
                    <button
                      key={idx}
                      type="button"
                      onClick={() => addRequiredSkill(s)}
                      disabled={requiredSkills.includes(s)}
                      className={`px-2 py-0.5 rounded text-[11px] font-semibold transition-colors ${
                        requiredSkills.includes(s) 
                          ? 'bg-white/5 text-gray-600 cursor-not-allowed' 
                          : 'bg-white/5 hover:bg-[#3fd0ff]/20 text-gray-300 hover:text-[#3fd0ff] border border-white/10'
                      }`}
                    >
                      +{s}
                    </button>
                  ))}
                </div>
              </div>

              {/* 2. PREFERRED / BONUS SKILLS BUCKET */}
              <div className="p-6 rounded-2xl bg-white/[0.02] border border-white/10">
                <div className="flex flex-col sm:flex-row sm:items-center justify-between mb-4">
                  <div>
                    <h4 className="text-sm font-bold uppercase tracking-wider text-white flex items-center">
                      <span className="w-2.5 h-2.5 rounded-full bg-[#ff8a3d] mr-2"></span>
                      2. Preferred / Bonus Skills ({preferredSkills.length} tagged)
                    </h4>
                    <p className="text-gray-400 text-xs mt-0.5">
                      Optional competencies that grant candidates extra match percentile points.
                    </p>
                  </div>
                  
                  {/* Manual Preferred Skill Input */}
                  <div className="mt-3 sm:mt-0 flex gap-2">
                    <input 
                      type="text" 
                      placeholder="Type bonus skill & press Enter..." 
                      value={newPreferredInput}
                      onChange={e => setNewPreferredInput(e.target.value)}
                      onKeyDown={e => { if (e.key === 'Enter') { e.preventDefault(); addPreferredSkill(); } }}
                      className="bg-black/60 border border-white/15 px-3 py-1.5 rounded-xl text-xs text-white placeholder-gray-500 focus:outline-none focus:border-[#ff8a3d]"
                    />
                    <button 
                      type="button"
                      onClick={() => addPreferredSkill()}
                      className="px-3 py-1.5 bg-[#ff8a3d] hover:bg-[#f2701c] text-white font-bold text-xs uppercase tracking-wider rounded-xl transition-colors"
                    >
                      + Add
                    </button>
                  </div>
                </div>

                {/* Active Preferred Badges */}
                <div className="flex flex-wrap gap-2 min-h-[38px] p-3 rounded-xl bg-black/40 border border-white/10 mb-4">
                  {preferredSkills.length === 0 ? (
                    <span className="text-xs text-gray-500 italic">No preferred skills added yet.</span>
                  ) : (
                    preferredSkills.map((skill, idx) => (
                      <span 
                        key={idx}
                        className="inline-flex items-center px-3 py-1 rounded-full text-xs font-bold bg-[#ff8a3d]/15 border border-[#ff8a3d]/40 text-[#ff8a3d]"
                      >
                        +{skill}
                        <button 
                          type="button" 
                          onClick={() => removePreferredSkill(skill)}
                          className="ml-2 hover:text-white"
                        >
                          <X className="w-3.5 h-3.5" />
                        </button>
                      </span>
                    ))
                  )}
                </div>

                {/* Quick Add Suggestions */}
                <div className="flex flex-wrap items-center gap-1.5 text-xs text-gray-400">
                  <span className="font-semibold text-gray-400 mr-1 flex items-center">
                    <Tag className="w-3 h-3 mr-1 text-[#ff8a3d]" /> Quick Add:
                  </span>
                  {[...suggestedBPOSkills, ...suggestedITSkills.slice(0, 4)].map((s, idx) => (
                    <button
                      key={idx}
                      type="button"
                      onClick={() => addPreferredSkill(s)}
                      disabled={preferredSkills.includes(s)}
                      className={`px-2 py-0.5 rounded text-[11px] font-semibold transition-colors ${
                        preferredSkills.includes(s) 
                          ? 'bg-white/5 text-gray-600 cursor-not-allowed' 
                          : 'bg-white/5 hover:bg-[#ff8a3d]/20 text-gray-300 hover:text-[#ff8a3d] border border-white/10'
                      }`}
                    >
                      +{s}
                    </button>
                  ))}
                </div>
              </div>

            </div>

            {/* Form Actions */}
            <div className="pt-4 border-t border-white/10 flex items-center justify-end space-x-3">
              <button 
                type="button"
                onClick={() => setShowForm(false)}
                className="px-5 py-3 rounded-xl border border-white/10 bg-white/5 hover:bg-white/10 text-gray-300 text-xs font-bold uppercase tracking-wider transition-colors"
              >
                Cancel
              </button>
              <button 
                type="submit" 
                className="px-7 py-3 rounded-xl bg-gradient-to-r from-[#ff8a3d] to-[#f2701c] hover:brightness-110 text-white font-bold text-xs uppercase tracking-wider transition-all shadow-[0_0_20px_rgba(255,138,61,0.4)] flex items-center"
              >
                Publish Opportunity &amp; Synchronize Skills &gt;
              </button>
            </div>
          </form>
        </div>
      )}

      {/* ============================================================== */}
      {/* 📋 JOB REQUISITIONS TABLE */}
      {/* ============================================================== */}
      <div className="elevate-card rounded-2xl border border-white/10 overflow-hidden shadow-xl">
        
        {/* Table Search & Filter Bar */}
        <div className="p-4 bg-white/[0.02] border-b border-white/10 flex flex-col sm:flex-row gap-4 items-center justify-between">
          <div className="relative w-full sm:w-80">
            <Search className="w-4 h-4 text-gray-400 absolute left-3 top-1/2 -translate-y-1/2" />
            <input 
              type="text" 
              placeholder="Search positions, locations, skills..." 
              value={searchTerm}
              onChange={e => setSearchTerm(e.target.value)}
              className="w-full pl-9 pr-3 py-2 bg-black/50 border border-white/10 rounded-xl text-xs text-white placeholder-gray-500 focus:outline-none focus:border-[#3fd0ff]"
            />
          </div>
          <span className="text-xs text-gray-400 font-semibold">
            Showing <strong className="text-white">{filteredJobs.length}</strong> active requisitions
          </span>
        </div>

        <table className="min-w-full divide-y divide-white/10 text-left">
          <thead className="bg-white/[0.01]">
            <tr>
              <th className="px-6 py-4 text-xs font-bold uppercase tracking-wider text-gray-400">Position Title</th>
              <th className="px-6 py-4 text-xs font-bold uppercase tracking-wider text-gray-400">Domain</th>
              <th className="px-6 py-4 text-xs font-bold uppercase tracking-wider text-gray-400">Delivery Hub</th>
              <th className="px-6 py-4 text-xs font-bold uppercase tracking-wider text-gray-400">Configured Skills</th>
              <th className="px-6 py-4 text-xs font-bold uppercase tracking-wider text-gray-400">Applicants</th>
              <th className="px-6 py-4 text-xs font-bold uppercase tracking-wider text-gray-400 text-right">Actions</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-white/5">
            {filteredJobs.length === 0 ? (
              <tr>
                <td colSpan="6" className="px-6 py-12 text-center text-gray-500 text-xs">
                  No job opportunities matching "{searchTerm}". Click "+ Add Job Opportunity &amp; Skills" above to create one.
                </td>
              </tr>
            ) : filteredJobs.map(job => {
              const jobApps = applications.filter(a => a.job_id === job.id);
              return (
              <tr key={job.id} className="hover:bg-white/[0.02] transition-colors">
                <td className="px-6 py-4">
                  <div className="font-bold text-white text-sm">{job.title}</div>
                  <div className="text-[11px] text-gray-400">{job.min_experience_years}+ Yrs Exp • {job.education_requirement}</div>
                </td>
                <td className="px-6 py-4 whitespace-nowrap text-xs text-gray-300 font-medium">
                  {job.department}
                </td>
                <td className="px-6 py-4 whitespace-nowrap text-xs text-gray-400">
                  <span className="flex items-center">
                    <MapPin className="w-3.5 h-3.5 text-[#3fd0ff] mr-1" /> {job.location}
                  </span>
                </td>
                <td className="px-6 py-4">
                  <div className="flex flex-wrap gap-1 max-w-sm">
                    {job.required_skills && job.required_skills.slice(0, 3).map((skill, sIdx) => (
                      <span key={sIdx} className="text-[10px] font-semibold px-2 py-0.5 rounded bg-[#3fd0ff]/15 border border-[#3fd0ff]/30 text-[#3fd0ff]">
                        {skill}
                      </span>
                    ))}
                    {job.required_skills && job.required_skills.length > 3 && (
                      <span className="text-[10px] text-gray-400 self-center">+{job.required_skills.length - 3} more</span>
                    )}
                  </div>
                </td>
                <td className="px-6 py-4 whitespace-nowrap">
                  <Link 
                    to="/applications"
                    className="inline-flex items-center px-2.5 py-1 rounded-full text-xs font-bold bg-[#3fd0ff]/15 hover:bg-[#3fd0ff]/25 border border-[#3fd0ff]/30 text-[#3fd0ff] transition-colors"
                  >
                    <Users className="w-3 h-3 mr-1" />
                    {jobApps.length} Applicants
                  </Link>
                </td>
                <td className="px-6 py-4 whitespace-nowrap text-right text-xs">
                  <button 
                    onClick={() => setSelectedJobView(job)} 
                    className="text-[#3fd0ff] hover:text-cyan-300 font-bold uppercase mr-4 transition-colors"
                  >
                    View Details
                  </button>
                  <button 
                    onClick={() => handleDelete(job.id)} 
                    className="text-red-400 hover:text-red-300 font-bold uppercase transition-colors"
                  >
                    Delete
                  </button>
                </td>
              </tr>
            );})}
          </tbody>
        </table>
      </div>

      {/* ============================================================== */}
      {/* 🔍 MODAL: VIEW DETAILED JOB REQUISITION */}
      {/* ============================================================== */}
      {selectedJobView && (
        <div className="fixed inset-0 z-50 bg-black/80 backdrop-blur-md flex items-center justify-center p-4">
          <div className="elevate-card border border-white/20 rounded-3xl max-w-2xl w-full p-8 relative shadow-2xl animate-fade-in-up">
            <button 
              onClick={() => setSelectedJobView(null)}
              className="absolute top-6 right-6 text-gray-400 hover:text-white p-2 rounded-full hover:bg-white/10"
            >
              <X className="w-5 h-5" />
            </button>

            <span className="text-xs font-bold uppercase tracking-widest text-[#ff8a3d]">Requisition Overview</span>
            <h3 className="text-2xl font-black text-white mt-1 mb-2">{selectedJobView.title}</h3>
            
            <div className="flex items-center text-xs text-gray-400 mb-6">
              <MapPin className="w-3.5 h-3.5 text-[#3fd0ff] mr-1" />
              <span>{selectedJobView.location} Branch</span>
              <span className="mx-2">•</span>
              <span>{selectedJobView.department}</span>
              <span className="mx-2">•</span>
              <span>{selectedJobView.min_experience_years}+ Years Experience</span>
            </div>

            <div className="space-y-4 text-xs text-gray-300 mb-6 bg-white/[0.02] p-4 rounded-xl border border-white/10">
              <div className="font-semibold text-gray-400 uppercase tracking-wider">Position Description:</div>
              <p className="leading-relaxed">{selectedJobView.description}</p>
              
              <div className="font-semibold text-gray-400 uppercase tracking-wider pt-2">Education:</div>
              <p>{selectedJobView.education_requirement || 'Any Graduate'}</p>
            </div>

            <div className="space-y-3 mb-6">
              <div>
                <span className="text-[10px] font-bold uppercase tracking-widest text-gray-400 block mb-1.5">Strict Required Skills:</span>
                <div className="flex flex-wrap gap-1.5">
                  {selectedJobView.required_skills?.map((s, idx) => (
                    <span key={idx} className="px-2.5 py-1 rounded-full text-xs font-bold bg-[#3fd0ff]/20 border border-[#3fd0ff]/40 text-[#3fd0ff]">
                      {s}
                    </span>
                  ))}
                </div>
              </div>

              {selectedJobView.preferred_skills?.length > 0 && (
                <div>
                  <span className="text-[10px] font-bold uppercase tracking-widest text-gray-400 block mb-1.5">Preferred / Bonus Skills:</span>
                  <div className="flex flex-wrap gap-1.5">
                    {selectedJobView.preferred_skills.map((s, idx) => (
                      <span key={idx} className="px-2.5 py-1 rounded-full text-xs font-bold bg-[#ff8a3d]/20 border border-[#ff8a3d]/40 text-[#ff8a3d]">
                        +{s}
                      </span>
                    ))}
                  </div>
                </div>
              )}
            </div>

            {/* Screened Applicants Section */}
            {(() => {
              const jobApps = applications.filter(a => a.job_id === selectedJobView.id);
              return (
                <div className="pt-4 border-t border-white/10 mb-6">
                  <div className="flex items-center justify-between mb-3">
                    <span className="text-xs font-bold uppercase tracking-wider text-gray-300 flex items-center">
                      <Users className="w-3.5 h-3.5 text-[#3fd0ff] mr-1.5" />
                      Screened Candidate Profiles ({jobApps.length} Applicants with Varied Percentages)
                    </span>
                    <Link
                      to="/applications"
                      className="text-xs font-bold text-[#ff8a3d] hover:underline flex items-center"
                    >
                      AI Screener Console <ArrowUpRight className="w-3.5 h-3.5 ml-0.5" />
                    </Link>
                  </div>

                  <div className="space-y-2 max-h-48 overflow-y-auto pr-1">
                    {jobApps.length === 0 ? (
                      <p className="text-xs text-gray-500 italic">No applications recorded for this requisition yet.</p>
                    ) : (
                      jobApps.map(app => {
                        const cand = candidates.find(c => c.id === app.candidate_id);
                        return (
                          <div key={app.id} className="p-2.5 rounded-xl bg-white/[0.03] border border-white/5 flex items-center justify-between text-xs">
                            <div>
                              <span className="font-bold text-white block">{cand?.name || 'Applicant'}</span>
                              <span className="text-[10px] text-gray-400">Stage: <strong className="text-gray-200">{app.stage}</strong></span>
                            </div>
                            <div className="flex items-center space-x-2">
                              <span className={`px-2.5 py-0.5 rounded-full text-xs font-black ${
                                app.match_score >= 85 
                                  ? 'bg-emerald-950/80 text-emerald-300 border border-emerald-500/40' 
                                  : app.match_score >= 70
                                  ? 'bg-cyan-950/80 text-[#3fd0ff] border border-[#3fd0ff]/40'
                                  : app.match_score >= 50
                                  ? 'bg-orange-950/80 text-[#ff8a3d] border border-[#ff8a3d]/40'
                                  : 'bg-rose-950/80 text-rose-300 border border-rose-500/40'
                              }`}>
                                {app.match_score}%
                              </span>
                            </div>
                          </div>
                        );
                      })
                    )}
                  </div>
                </div>
              );
            })()}

            <div className="flex justify-end pt-4 border-t border-white/10">
              <button 
                onClick={() => setSelectedJobView(null)}
                className="px-6 py-2.5 bg-white/10 hover:bg-white/20 text-white rounded-xl text-xs font-bold uppercase tracking-wider transition-colors"
              >
                Close Window
              </button>
            </div>
          </div>
        </div>
      )}

    </div>
  );
}

export default Jobs;
