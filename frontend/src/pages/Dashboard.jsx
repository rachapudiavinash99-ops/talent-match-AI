import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Briefcase, Users, FileText, TrendingUp, CheckCircle, Clock, Sparkles, ChevronRight, UserCheck, ArrowUpRight } from 'lucide-react';
import { Link } from 'react-router-dom';

const API_BASE = 'http://localhost:8000/api';

function Dashboard() {
  const [stats, setStats] = useState({ jobs: 0, candidates: 0, applications: 0, avgScore: 0 });
  const [pipeline, setPipeline] = useState({ Applied: 0, UnderReview: 0, Shortlisted: 0, Interview: 0, Offer: 0 });
  const [recentApps, setRecentApps] = useState([]);
  const [jobsList, setJobsList] = useState([]);
  const [candidatesList, setCandidatesList] = useState([]);

  useEffect(() => {
    async function fetchData() {
      try {
        const [jobsRes, candsRes, appsRes] = await Promise.all([
          axios.get(`${API_BASE}/jobs/`),
          axios.get(`${API_BASE}/candidates/`),
          axios.get(`${API_BASE}/applications/`)
        ]);
        
        const apps = appsRes.data;
        const avg = apps.length > 0 ? (apps.reduce((acc, curr) => acc + (curr.match_score || 0), 0) / apps.length).toFixed(1) : 0;
        
        const pipe = { Applied: 0, UnderReview: 0, Shortlisted: 0, Interview: 0, Offer: 0 };
        apps.forEach(a => {
          if (a.stage === 'Applied') pipe.Applied++;
          else if (a.stage === 'Under Review') pipe.UnderReview++;
          else if (a.stage === 'Shortlisted') pipe.Shortlisted++;
          else if (a.stage === 'Interview') pipe.Interview++;
          else if (a.stage === 'Offer') pipe.Offer++;
        });

        setStats({
          jobs: jobsRes.data.length,
          candidates: candsRes.data.length,
          applications: apps.length,
          avgScore: avg
        });
        setPipeline(pipe);
        setJobsList(jobsRes.data);
        setCandidatesList(candsRes.data);
        setRecentApps(apps.slice(-6).reverse());
      } catch (err) {
        console.error("Error fetching stats", err);
      }
    }
    fetchData();
  }, []);

  return (
    <div className="animate-fade-in-up text-white">
      
      {/* Header */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between pb-6 mb-8 border-b border-white/10">
        <div>
          <div className="inline-flex items-center space-x-1 text-xs font-bold uppercase tracking-widest text-[#ff8a3d] mb-1">
            <Sparkles className="w-3.5 h-3.5 mr-1" /> ElevateIQ Recruiter Intelligence
          </div>
          <h2 className="text-3xl font-black uppercase tracking-tight text-white">
            Talent Acquisition Command Center <span className="text-[#3fd0ff]">&gt;</span>
          </h2>
          <p className="text-gray-400 text-xs mt-1">
            Real-time candidate telemetry across {stats.jobs} positions with multi-percentage evaluations.
          </p>
        </div>
        <div className="mt-4 sm:mt-0 flex items-center space-x-3">
          <span className="text-xs font-bold uppercase tracking-wider text-green-400 bg-green-950/60 border border-green-500/30 px-3.5 py-1.5 rounded-full flex items-center shadow-[0_0_15px_rgba(16,185,129,0.2)]">
            <span className="w-2 h-2 rounded-full bg-green-400 mr-2 animate-ping"></span> AI Engine Live (Port 8000)
          </span>
        </div>
      </div>
      
      {/* Metric Cards */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
        <Link to="/jobs" className="elevate-card p-6 rounded-2xl border border-white/10 hover:border-[#ff8a3d]/50 transition-all flex items-center group">
          <div className="p-4 rounded-xl bg-orange-950/60 border border-[#ff8a3d]/30 text-[#ff8a3d] mr-4 group-hover:scale-105 transition-transform">
            <Briefcase className="w-6 h-6" />
          </div>
          <div>
            <h3 className="text-gray-400 text-xs font-bold uppercase tracking-wider">Active Requisitions</h3>
            <p className="text-3xl font-black text-white mt-1">{stats.jobs}</p>
            <span className="text-[10px] text-gray-500 font-semibold">Min. 5 candidates / job</span>
          </div>
        </Link>

        <Link to="/candidates" className="elevate-card p-6 rounded-2xl border border-white/10 hover:border-[#3fd0ff]/50 transition-all flex items-center group">
          <div className="p-4 rounded-xl bg-cyan-950/60 border border-[#3fd0ff]/30 text-[#3fd0ff] mr-4 group-hover:scale-105 transition-transform">
            <Users className="w-6 h-6" />
          </div>
          <div>
            <h3 className="text-gray-400 text-xs font-bold uppercase tracking-wider">Parsed Talent Pool</h3>
            <p className="text-3xl font-black text-white mt-1">{stats.candidates}</p>
            <span className="text-[10px] text-gray-500 font-semibold">Extracted skill profiles</span>
          </div>
        </Link>

        <Link to="/applications" className="elevate-card p-6 rounded-2xl border border-white/10 hover:border-indigo-500/50 transition-all flex items-center group">
          <div className="p-4 rounded-xl bg-indigo-950/60 border border-indigo-500/30 text-indigo-400 mr-4 group-hover:scale-105 transition-transform">
            <FileText className="w-6 h-6" />
          </div>
          <div>
            <h3 className="text-gray-400 text-xs font-bold uppercase tracking-wider">Total Evaluated Apps</h3>
            <p className="text-3xl font-black text-white mt-1">{stats.applications}</p>
            <span className="text-[10px] text-emerald-400 font-semibold">5+ apps per position</span>
          </div>
        </Link>

        <div className="elevate-card p-6 rounded-2xl border border-white/10 flex items-center">
          <div className="p-4 rounded-xl bg-emerald-950/60 border border-emerald-500/30 text-emerald-400 mr-4">
            <TrendingUp className="w-6 h-6" />
          </div>
          <div>
            <h3 className="text-gray-400 text-xs font-bold uppercase tracking-wider">Avg Neural Fit</h3>
            <p className="text-3xl font-black text-white mt-1">{stats.avgScore}%</p>
            <span className="text-[10px] text-gray-500 font-semibold">Deterministic TF-IDF</span>
          </div>
        </div>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        
        {/* Pipeline Breakdown */}
        <div className="elevate-card p-7 rounded-2xl border border-white/10 lg:col-span-2">
          <div className="flex items-center justify-between mb-6">
            <div>
              <span className="text-[10px] font-bold uppercase tracking-widest text-[#ff8a3d]">
                Candidate Funnel Velocity
              </span>
              <h3 className="text-lg font-bold text-white uppercase tracking-tight flex items-center mt-0.5">
                Conversion Pipeline <ChevronRight className="w-4 h-4 ml-1 text-[#3fd0ff]" />
              </h3>
            </div>
            <span className="text-xs text-gray-400 font-semibold bg-white/5 px-3 py-1 rounded-full border border-white/10">
              {stats.applications} Applications Distributed
            </span>
          </div>

          <div className="flex justify-between items-end h-44 space-x-3 pt-4">
            
            {/* Applied */}
            <div className="flex-1 flex flex-col justify-end items-center group">
              <span className="mb-2 font-bold text-white text-sm transition-transform group-hover:-translate-y-1">{pipeline.Applied}</span>
              <div 
                className="w-full bg-blue-900/60 border-t-2 border-blue-400 rounded-t-lg transition-all duration-500 group-hover:bg-blue-800/80" 
                style={{ height: `${Math.min(100, Math.max(pipeline.Applied * 8, 18))}%` }}
              ></div>
              <span className="mt-3 text-[10px] font-bold text-gray-400 uppercase tracking-wider">Applied</span>
            </div>

            {/* Under Review */}
            <div className="flex-1 flex flex-col justify-end items-center group">
              <span className="mb-2 font-bold text-white text-sm transition-transform group-hover:-translate-y-1">{pipeline.UnderReview}</span>
              <div 
                className="w-full bg-orange-900/60 border-t-2 border-[#ff8a3d] rounded-t-lg transition-all duration-500 group-hover:bg-orange-800/80" 
                style={{ height: `${Math.min(100, Math.max(pipeline.UnderReview * 8, 18))}%` }}
              ></div>
              <span className="mt-3 text-[10px] font-bold text-gray-400 uppercase tracking-wider">Review</span>
            </div>

            {/* Shortlisted */}
            <div className="flex-1 flex flex-col justify-end items-center group">
              <span className="mb-2 font-bold text-white text-sm transition-transform group-hover:-translate-y-1">{pipeline.Shortlisted}</span>
              <div 
                className="w-full bg-indigo-900/60 border-t-2 border-indigo-400 rounded-t-lg transition-all duration-500 group-hover:bg-indigo-800/80" 
                style={{ height: `${Math.min(100, Math.max(pipeline.Shortlisted * 8, 18))}%` }}
              ></div>
              <span className="mt-3 text-[10px] font-bold text-gray-400 uppercase tracking-wider">Shortlist</span>
            </div>

            {/* Interview */}
            <div className="flex-1 flex flex-col justify-end items-center group">
              <span className="mb-2 font-bold text-white text-sm transition-transform group-hover:-translate-y-1">{pipeline.Interview}</span>
              <div 
                className="w-full bg-cyan-900/60 border-t-2 border-[#3fd0ff] rounded-t-lg transition-all duration-500 group-hover:bg-cyan-800/80" 
                style={{ height: `${Math.min(100, Math.max(pipeline.Interview * 8, 18))}%` }}
              ></div>
              <span className="mt-3 text-[10px] font-bold text-gray-400 uppercase tracking-wider">Interview</span>
            </div>

            {/* Offer */}
            <div className="flex-1 flex flex-col justify-end items-center group">
              <span className="mb-2 font-bold text-white text-sm transition-transform group-hover:-translate-y-1">{pipeline.Offer}</span>
              <div 
                className="w-full bg-emerald-900/60 border-t-2 border-emerald-400 rounded-t-lg transition-all duration-500 group-hover:bg-emerald-800/80" 
                style={{ height: `${Math.min(100, Math.max(pipeline.Offer * 8, 18))}%` }}
              ></div>
              <span className="mt-3 text-[10px] font-bold text-gray-400 uppercase tracking-wider">Offer</span>
            </div>

          </div>
        </div>

        {/* Recent Matches */}
        <div className="elevate-card p-7 rounded-2xl border border-white/10 flex flex-col justify-between">
          <div>
            <div className="flex items-center justify-between mb-4">
              <h3 className="text-lg font-bold text-white uppercase tracking-tight flex items-center">
                Recent Evaluations <ChevronRight className="w-4 h-4 ml-1 text-[#ff8a3d]" />
              </h3>
              <Link to="/applications" className="text-xs text-[#3fd0ff] hover:underline font-bold flex items-center">
                View All <ArrowUpRight className="w-3 h-3 ml-0.5" />
              </Link>
            </div>
            
            <div className="space-y-2.5">
              {recentApps.length === 0 ? (
                <p className="text-xs text-gray-500">No applications recorded yet.</p>
              ) : (
                recentApps.map((app) => {
                  const cand = candidatesList.find(c => c.id === app.candidate_id);
                  const job = jobsList.find(j => j.id === app.job_id);
                  return (
                    <div key={app.id} className="p-3 bg-white/5 border border-white/5 hover:border-white/15 rounded-xl flex items-center justify-between transition-colors">
                      <div className="flex items-center space-x-3 overflow-hidden">
                        {app.match_score >= 80 ? (
                          <CheckCircle className="text-emerald-400 w-4 h-4 flex-shrink-0" />
                        ) : (
                          <Clock className="text-[#ff8a3d] w-4 h-4 flex-shrink-0" />
                        )}
                        <div className="truncate">
                          <p className="text-xs font-bold text-white truncate">{cand?.name || 'Candidate'}</p>
                          <p className="text-[10px] text-gray-400 truncate">{job?.title ? job.title.split('(')[0] : app.job_id}</p>
                        </div>
                      </div>
                      <div className="text-right flex-shrink-0 ml-2">
                        <span className={`text-xs font-black px-2 py-0.5 rounded-full border ${
                          app.match_score >= 80 
                            ? 'bg-emerald-950/80 text-emerald-300 border-emerald-500/40' 
                            : app.match_score >= 60 
                            ? 'bg-cyan-950/80 text-[#3fd0ff] border-[#3fd0ff]/40'
                            : 'bg-orange-950/80 text-[#ff8a3d] border-[#ff8a3d]/40'
                        }`}>
                          {app.match_score}%
                        </span>
                        <p className="text-[9px] text-gray-400 uppercase tracking-wider mt-0.5">{app.stage}</p>
                      </div>
                    </div>
                  );
                })
              )}
            </div>
          </div>

          <div className="pt-4 border-t border-white/10 mt-4 text-center">
            <Link 
              to="/applications" 
              className="text-xs text-[#ff8a3d] font-bold uppercase tracking-wider hover:text-white transition-colors flex items-center justify-center"
            >
              Open Full AI Screener Pipeline &gt;
            </Link>
          </div>
        </div>

      </div>
    </div>
  );
}

export default Dashboard;
