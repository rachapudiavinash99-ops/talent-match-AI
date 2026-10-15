import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { 
  Users, RefreshCw, UploadCloud, Eye, FileText, Sparkles, Phone, Mail, 
  Search, MapPin, X, Target, Zap, Check, ArrowRight, Award, AlertCircle, CheckCircle
} from 'lucide-react';

const API_BASE = 'http://localhost:8000/api';

function Candidates() {
  const [candidates, setCandidates] = useState([]);
  const [jobs, setJobs] = useState([]);
  const [showForm, setShowForm] = useState(false);
  const [formData, setFormData] = useState({ name: '', email: '', phone: '' });
  const [file, setFile] = useState(null);
  const [uploading, setUploading] = useState(false);
  const [searchTerm, setSearchTerm] = useState('');
  const [selectedCandidate, setSelectedCandidate] = useState(null);

  // 🎯 Button 3 State: Best Job Matcher Modal
  const [bestMatchModal, setBestMatchModal] = useState(null);
  const [assignedJobId, setAssignedJobId] = useState(null);
  const [matchSuccessMsg, setMatchSuccessMsg] = useState('');

  const fetchCandidates = () => {
    axios.get(`${API_BASE}/candidates/`).then(res => setCandidates(res.data)).catch(err => console.error(err));
    axios.get(`${API_BASE}/jobs/`).then(res => setJobs(res.data)).catch(err => console.error(err));
  };

  useEffect(() => { 
    fetchCandidates(); 
  }, []);

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

  // ==============================================================
  // 🎯 BUTTON 3: FIND BEST JOB MATCH ALGORITHM
  // ==============================================================
  const handleFindBestMatch = (cand) => {
    const candSkills = (cand.skills || []).map(s => s.toLowerCase());

    const ranked = jobs.map(job => {
      const req = job.required_skills || [];
      const pref = job.preferred_skills || [];

      const matchedReq = req.filter(r => candSkills.includes(r.toLowerCase()));
      const missingReq = req.filter(r => !candSkills.includes(r.toLowerCase()));
      const matchedPref = pref.filter(p => candSkills.includes(p.toLowerCase()));

      // Calculate deterministic match score
      const reqRatio = req.length > 0 ? (matchedReq.length / req.length) : 0.5;
      const prefRatio = pref.length > 0 ? (matchedPref.length / pref.length) * 0.15 : 0;
      const overall = Math.min(98.5, Math.max(15.0, Math.round((reqRatio * 0.82 + prefRatio + 0.12) * 100 * 10) / 10));

      return {
        ...job,
        matchScore: overall,
        matchedReq,
        missingReq,
        matchedPref
      };
    }).sort((a, b) => b.matchScore - a.matchScore);

    setBestMatchModal({
      candidate: cand,
      rankedJobs: ranked
    });
    setAssignedJobId(null);
    setMatchSuccessMsg('');
  };

  const handleAssignCandidateToJob = async (jobId, candId, jobTitle) => {
    try {
      await axios.post(`${API_BASE}/applications/`, {
        job_id: jobId,
        candidate_id: candId
      });
      setAssignedJobId(jobId);
      setMatchSuccessMsg(`Candidate successfully assigned to "${jobTitle}"!`);
      setTimeout(() => setMatchSuccessMsg(''), 4000);
    } catch (err) {
      console.error(err);
      alert("Error assigning candidate to requisition");
    }
  };

  const filteredCandidates = candidates.filter(c => 
    c.name?.toLowerCase().includes(searchTerm.toLowerCase()) ||
    c.email?.toLowerCase().includes(searchTerm.toLowerCase()) ||
    c.skills?.some(s => s.toLowerCase().includes(searchTerm.toLowerCase()))
  );

  return (
    <div className="animate-fade-in-up text-white pb-16">
      
      {/* Header */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between pb-6 mb-8 border-b border-white/10">
        <div>
          <div className="inline-flex items-center space-x-1 text-xs font-bold uppercase tracking-widest text-[#ff8a3d] mb-1">
            <Sparkles className="w-3.5 h-3.5 mr-1" /> Enterprise Talent Repository
          </div>
          <h2 className="text-3xl font-black uppercase tracking-tight text-white">
            Talent Pool Intelligence <span className="text-[#3fd0ff]">&gt;</span>
          </h2>
          <p className="text-gray-400 text-xs mt-1">
            Browse parsed resumes, extracted skill vectors, and run reverse AI job matching across open requisitions.
          </p>
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
            className="px-5 py-2 bg-gradient-to-r from-[#ff8a3d] to-[#f2701c] hover:brightness-110 text-white rounded-xl text-xs font-bold uppercase tracking-wider transition-all shadow-[0_0_20px_rgba(255,138,61,0.35)] flex items-center"
          >
            {showForm ? 'Cancel' : '+ Ingest Resume'}
          </button>
        </div>
      </div>

      {showForm && (
        <form onSubmit={handleSubmit} className="elevate-card p-7 rounded-2xl mb-8 border border-white/10 animate-fade-in-up">
          <h3 className="text-lg font-bold uppercase text-white mb-4 flex items-center">
            Ingest &amp; Extract Resume <span className="text-[#3fd0ff] ml-1">&gt;</span>
          </h3>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mb-4">
            <input 
              placeholder="Candidate Full Name" 
              className="bg-white/5 border border-white/10 p-3 rounded-xl text-white placeholder-gray-500 focus:outline-none focus:border-[#3fd0ff] text-sm" 
              required 
              onChange={e => setFormData({...formData, name: e.target.value})} 
            />
            <input 
              type="email" 
              placeholder="Corporate / Personal Email" 
              className="bg-white/5 border border-white/10 p-3 rounded-xl text-white placeholder-gray-500 focus:outline-none focus:border-[#3fd0ff] text-sm" 
              required 
              onChange={e => setFormData({...formData, email: e.target.value})} 
            />
            <input 
              placeholder="Phone (+91-...)" 
              className="bg-white/5 border border-white/10 p-3 rounded-xl text-white placeholder-gray-500 focus:outline-none focus:border-[#3fd0ff] text-sm" 
              onChange={e => setFormData({...formData, phone: e.target.value})} 
            />
            <div className="border border-white/10 bg-white/5 p-2.5 rounded-xl flex items-center justify-between">
              <span className="text-xs text-gray-400">PDF / DOCX File</span>
              <input 
                type="file" 
                accept=".pdf,.docx" 
                required 
                onChange={e => setFile(e.target.files[0])} 
                className="text-xs text-gray-400 file:mr-3 file:py-1 file:px-3 file:rounded-full file:border-0 file:text-xs file:font-bold file:bg-[#ff8a3d] file:text-white hover:file:bg-[#f2701c]"
              />
            </div>
          </div>
          <button 
            type="submit" 
            disabled={uploading}
            className="px-6 py-3 bg-gradient-to-r from-[#ff8a3d] to-[#f2701c] hover:brightness-110 text-white rounded-xl text-xs font-bold uppercase tracking-wider transition-all disabled:opacity-50 shadow-[0_0_15px_rgba(255,138,61,0.3)]"
          >
            {uploading ? "Extracting Candidate Vectors..." : "Extract & Index Resume >"}
          </button>
        </form>
      )}

      {/* Search & Counter Bar */}
      <div className="elevate-card p-4 rounded-2xl border border-white/10 mb-6 flex flex-col sm:flex-row gap-4 items-center justify-between">
        <div className="relative w-full sm:w-80">
          <Search className="w-4 h-4 text-gray-400 absolute left-3 top-1/2 -translate-y-1/2" />
          <input 
            type="text" 
            placeholder="Search candidate name, email, skills..." 
            value={searchTerm}
            onChange={e => setSearchTerm(e.target.value)}
            className="w-full pl-9 pr-3 py-2 bg-black/40 border border-white/10 rounded-xl text-xs text-white placeholder-gray-500 focus:outline-none focus:border-[#3fd0ff]"
          />
        </div>
        <span className="text-xs text-gray-400 font-semibold">
          Showing <strong className="text-white">{filteredCandidates.length}</strong> of <strong className="text-[#3fd0ff]">{candidates.length}</strong> verified profiles
        </span>
      </div>

      {/* Candidates Table */}
      <div className="elevate-card rounded-2xl border border-white/10 overflow-hidden shadow-xl">
        <table className="min-w-full divide-y divide-white/10 text-left">
          <thead className="bg-white/[0.02]">
            <tr>
              <th className="px-6 py-4 text-xs font-bold uppercase tracking-wider text-gray-400">Candidate Name</th>
              <th className="px-6 py-4 text-xs font-bold uppercase tracking-wider text-gray-400">Contact Channels</th>
              <th className="px-6 py-4 text-xs font-bold uppercase tracking-wider text-gray-400">Extracted Skills Vector</th>
              <th className="px-6 py-4 text-xs font-bold uppercase tracking-wider text-gray-400 text-right">Actions</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-white/5">
            {filteredCandidates.length === 0 ? (
              <tr><td colSpan="4" className="px-6 py-8 text-center text-gray-500 text-xs">No candidate records match your search.</td></tr>
            ) : filteredCandidates.map(c => (
              <tr key={c.id} className="hover:bg-white/[0.02] transition-colors">
                
                {/* Name */}
                <td className="px-6 py-4 whitespace-nowrap">
                  <div className="font-bold text-white text-sm">{c.name}</div>
                  <div className="text-[11px] text-gray-500">{c.experience || 'Verified Professional Profile'}</div>
                </td>

                {/* Contact */}
                <td className="px-6 py-4 whitespace-nowrap text-xs text-gray-300">
                  <div className="flex items-center text-gray-300"><Mail className="w-3 h-3 text-[#3fd0ff] mr-1.5" /> {c.email}</div>
                  <div className="flex items-center text-gray-400 mt-1"><Phone className="w-3 h-3 text-gray-500 mr-1.5" /> {c.phone}</div>
                </td>

                {/* Skills Vector */}
                <td className="px-6 py-4">
                  <div className="flex flex-wrap gap-1 max-w-md">
                    {c.skills && c.skills.map((skill, sIdx) => (
                      <span key={sIdx} className="px-2 py-0.5 rounded-full bg-cyan-950/60 border border-[#3fd0ff]/30 text-[#3fd0ff] text-[10px] font-semibold">
                        {skill}
                      </span>
                    ))}
                  </div>
                </td>

                {/* Actions with Button 3: Find Best Job Match */}
                <td className="px-6 py-4 whitespace-nowrap text-right text-xs">
                  
                  {/* 🎯 BUTTON 3: BEST JOB MATCH */}
                  <button 
                    onClick={() => handleFindBestMatch(c)} 
                    className="px-3 py-1 bg-gradient-to-r from-cyan-600/30 to-blue-600/30 hover:from-[#3fd0ff] hover:to-cyan-400 border border-[#3fd0ff]/50 text-[#3fd0ff] hover:text-[#06091A] rounded-lg font-bold uppercase text-xs mr-2 transition-all shadow-[0_0_10px_rgba(63,208,255,0.2)] inline-flex items-center"
                    title="Run AI scan against all 10 open positions to rank best job fits"
                  >
                    <Target className="w-3.5 h-3.5 mr-1" />
                    Best Job Match
                  </button>

                  <button 
                    onClick={() => setSelectedCandidate(c)} 
                    className="px-3 py-1 bg-white/5 hover:bg-white/10 border border-white/10 text-white rounded-lg font-bold uppercase text-xs mr-2 transition-colors inline-flex items-center"
                  >
                    Profile
                  </button>

                  <button 
                    onClick={() => alert(`Downloading cached resume document for ${c.name}...`)} 
                    className="px-3 py-1 bg-[#ff8a3d]/15 hover:bg-[#ff8a3d]/30 border border-[#ff8a3d]/40 text-[#ff8a3d] rounded-lg font-bold uppercase text-xs transition-colors inline-flex items-center"
                  >
                    Resume
                  </button>
                </td>

              </tr>
            ))}
          </tbody>
        </table>
      </div>

      {/* ============================================================== */}
      {/* 🎯 MODAL: BUTTON 3 - AI BEST POSITION MATCHER */}
      {/* ============================================================== */}
      {bestMatchModal && (() => {
        const { candidate, rankedJobs } = bestMatchModal;
        const topJob = rankedJobs[0];

        return (
          <div className="fixed inset-0 bg-black/85 backdrop-blur-md flex items-center justify-center z-50 p-4">
            <div className="bg-[#0a0f24] border border-white/20 rounded-3xl max-w-4xl w-full overflow-hidden flex flex-col max-h-[92vh] shadow-[0_0_60px_rgba(63,208,255,0.35)] animate-fade-in-up">
              
              {/* Modal Header */}
              <div className="p-6 border-b border-white/10 flex justify-between items-center bg-white/[0.02]">
                <div>
                  <div className="inline-flex items-center space-x-1.5 text-xs font-bold uppercase tracking-widest text-[#3fd0ff]">
                    <Target className="w-3.5 h-3.5" /> AI Reverse Position Matcher
                  </div>
                  <h3 className="text-2xl font-black uppercase text-white mt-0.5">
                    Best Requisition Fits for {candidate.name} &gt;
                  </h3>
                </div>
                <button 
                  onClick={() => setBestMatchModal(null)} 
                  className="text-gray-400 hover:text-white p-2 rounded-full hover:bg-white/10 transition-colors"
                >
                  <X className="w-5 h-5" />
                </button>
              </div>

              {/* Success Notification */}
              {matchSuccessMsg && (
                <div className="mx-6 mt-4 p-3.5 rounded-xl bg-emerald-950/80 border border-emerald-500/50 text-emerald-300 text-xs font-bold flex items-center">
                  <CheckCircle className="w-4 h-4 mr-2 text-emerald-400 flex-shrink-0" />
                  <span>{matchSuccessMsg}</span>
                </div>
              )}

              {/* Scrollable Content */}
              <div className="p-6 md:p-8 overflow-y-auto space-y-6">
                
                {/* Candidate Summary Pill */}
                <div className="p-4 rounded-2xl bg-white/[0.03] border border-white/10 flex flex-col sm:flex-row justify-between items-start sm:items-center gap-3">
                  <div>
                    <span className="text-[10px] font-bold uppercase tracking-widest text-gray-400 block">Candidate Profile</span>
                    <h4 className="text-lg font-black text-white">{candidate.name}</h4>
                    <span className="text-xs text-gray-400">{candidate.email} • {candidate.phone}</span>
                  </div>
                  <div className="flex flex-wrap gap-1 max-w-sm">
                    {candidate.skills?.map((s, i) => (
                      <span key={i} className="px-2 py-0.5 rounded text-[10px] font-bold bg-[#3fd0ff]/15 text-[#3fd0ff] border border-[#3fd0ff]/30">
                        {s}
                      </span>
                    ))}
                  </div>
                </div>

                {/* Ranked Jobs List */}
                <div className="space-y-3">
                  <h4 className="text-xs font-bold uppercase tracking-wider text-gray-300">
                    Ranked Position Fits ({rankedJobs.length} Requisitions Evaluated)
                  </h4>

                  {rankedJobs.map((job, idx) => {
                    const isTop = idx === 0;
                    const isAssigned = assignedJobId === job.id;

                    return (
                      <div 
                        key={job.id} 
                        className={`p-4 rounded-2xl border transition-all flex flex-col md:flex-row justify-between items-start md:items-center gap-4 ${
                          isTop 
                            ? 'bg-gradient-to-r from-cyan-950/40 to-blue-950/30 border-[#3fd0ff]/60 shadow-[0_0_20px_rgba(63,208,255,0.2)]'
                            : 'bg-white/[0.02] border-white/10 hover:border-white/20'
                        }`}
                      >
                        <div className="flex-1">
                          <div className="flex items-center space-x-2">
                            <span className={`px-2 py-0.5 rounded-full text-[10px] font-black uppercase ${
                              isTop ? 'bg-[#3fd0ff] text-[#06091A]' : 'bg-white/10 text-gray-300'
                            }`}>
                              #{idx + 1} Fit
                            </span>
                            <span className="text-[10px] text-[#ff8a3d] font-bold uppercase">
                              {job.department}
                            </span>
                          </div>

                          <h5 className="text-base font-bold text-white mt-1">
                            {job.title}
                          </h5>

                          <div className="flex items-center text-xs text-gray-400 mt-1 space-x-3">
                            <span className="flex items-center">
                              <MapPin className="w-3 h-3 text-[#3fd0ff] mr-1" /> {job.location} Branch
                            </span>
                            <span>•</span>
                            <span>{job.min_experience_years}+ Yrs Exp</span>
                          </div>

                          {/* Skill Overlap Preview */}
                          <div className="flex flex-wrap gap-1 mt-2.5">
                            {job.matchedReq.map((s, i) => (
                              <span key={i} className="px-2 py-0.5 rounded text-[9px] font-bold bg-green-950 text-green-300 border border-green-500/30">
                                ✓ {s}
                              </span>
                            ))}
                            {job.missingReq.map((s, i) => (
                              <span key={i} className="px-2 py-0.5 rounded text-[9px] font-bold bg-red-950 text-red-300 border border-red-500/30">
                                ✕ {s}
                              </span>
                            ))}
                          </div>
                        </div>

                        {/* Match Score & Assign Button */}
                        <div className="flex md:flex-col items-center md:items-end justify-between w-full md:w-auto gap-3 flex-shrink-0">
                          <span className={`px-3 py-1 rounded-full text-base font-black border ${
                            job.matchScore >= 80 
                              ? 'bg-emerald-950/80 text-emerald-300 border-emerald-500/40' 
                              : job.matchScore >= 60 
                              ? 'bg-cyan-950/80 text-[#3fd0ff] border-[#3fd0ff]/40' 
                              : 'bg-orange-950/80 text-[#ff8a3d] border-[#ff8a3d]/40'
                          }`}>
                            {job.matchScore}%
                          </span>

                          <button
                            onClick={() => handleAssignCandidateToJob(job.id, candidate.id, job.title)}
                            disabled={isAssigned}
                            className={`px-4 py-2 rounded-xl text-xs font-bold uppercase tracking-wider transition-all flex items-center whitespace-nowrap ${
                              isAssigned 
                                ? 'bg-emerald-600 text-white cursor-default'
                                : 'bg-gradient-to-r from-[#ff8a3d] to-[#f2701c] hover:brightness-110 text-white shadow-[0_0_15px_rgba(255,138,61,0.3)]'
                            }`}
                          >
                            {isAssigned ? (
                              <><Check className="w-3.5 h-3.5 mr-1" /> Assigned</>
                            ) : (
                              <><Zap className="w-3.5 h-3.5 mr-1" /> Assign to Job</>
                            )}
                          </button>
                        </div>

                      </div>
                    );
                  })}
                </div>

              </div>

              {/* Modal Footer */}
              <div className="p-6 border-t border-white/10 bg-white/[0.02] flex justify-end">
                <button 
                  onClick={() => setBestMatchModal(null)} 
                  className="px-6 py-2.5 bg-white/10 hover:bg-white/20 text-white rounded-xl text-xs font-bold uppercase tracking-wider transition-colors"
                >
                  Close Matcher
                </button>
              </div>

            </div>
          </div>
        );
      })()}

      {/* Candidate Profile Modal */}
      {selectedCandidate && (
        <div className="fixed inset-0 bg-black/80 backdrop-blur-md flex items-center justify-center z-50 p-4">
          <div className="bg-[#0a0f24] border border-white/20 rounded-3xl max-w-2xl w-full overflow-hidden flex flex-col max-h-[90vh] shadow-2xl animate-fade-in-up">
            <div className="p-6 border-b border-white/10 flex justify-between items-center bg-white/[0.02]">
              <div>
                <span className="text-[10px] font-bold uppercase tracking-widest text-[#ff8a3d]">
                  Candidate Profile Dossier
                </span>
                <h3 className="text-2xl font-black text-white mt-0.5">{selectedCandidate.name}</h3>
              </div>
              <button onClick={() => setSelectedCandidate(null)} className="text-gray-400 hover:text-white p-2 rounded-full hover:bg-white/10">
                <X className="w-5 h-5" />
              </button>
            </div>
            
            <div className="p-6 space-y-4 overflow-y-auto">
              <div className="grid grid-cols-2 gap-4">
                <div className="p-4 rounded-xl bg-white/5 border border-white/10">
                  <span className="text-[10px] font-bold uppercase text-gray-400 block">Email</span>
                  <span className="text-sm font-bold text-white mt-1 block">{selectedCandidate.email}</span>
                </div>
                <div className="p-4 rounded-xl bg-white/5 border border-white/10">
                  <span className="text-[10px] font-bold uppercase text-gray-400 block">Phone</span>
                  <span className="text-sm font-bold text-white mt-1 block">{selectedCandidate.phone}</span>
                </div>
              </div>

              <div className="p-4 rounded-xl bg-white/5 border border-white/10">
                <span className="text-[10px] font-bold uppercase text-gray-400 block mb-1">Experience &amp; Delivery Hub</span>
                <p className="text-xs text-gray-200">{selectedCandidate.experience || 'Not specified'}</p>
              </div>

              <div className="p-4 rounded-xl bg-white/5 border border-white/10">
                <span className="text-[10px] font-bold uppercase text-gray-400 block mb-2">Skills Vector</span>
                <div className="flex flex-wrap gap-1.5">
                  {selectedCandidate.skills?.map((s, i) => (
                    <span key={i} className="px-2.5 py-1 rounded-full text-xs font-bold bg-[#3fd0ff]/15 border border-[#3fd0ff]/30 text-[#3fd0ff]">
                      {s}
                    </span>
                  ))}
                </div>
              </div>
            </div>
          </div>
        </div>
      )}

    </div>
  );
}

export default Candidates;
