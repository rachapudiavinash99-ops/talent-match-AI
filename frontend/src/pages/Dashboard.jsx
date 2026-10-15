import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Briefcase, Users, FileText, TrendingUp, CheckCircle, Clock, Sparkles, ChevronRight } from 'lucide-react';

const API_BASE = 'http://localhost:8000/api';

function Dashboard() {
  const [stats, setStats] = useState({ jobs: 0, candidates: 0, applications: 0, avgScore: 0 });
  const [pipeline, setPipeline] = useState({ Applied: 0, Shortlisted: 0, Interview: 0, Offer: 0 });
  const [recentApps, setRecentApps] = useState([]);

  useEffect(() => {
    async function fetchData() {
      try {
        const [jobsRes, candsRes, appsRes] = await Promise.all([
          axios.get(`${API_BASE}/jobs/`),
          axios.get(`${API_BASE}/candidates/`),
          axios.get(`${API_BASE}/applications/`)
        ]);
        
        const apps = appsRes.data;
        const avg = apps.length > 0 ? (apps.reduce((acc, curr) => acc + curr.match_score, 0) / apps.length).toFixed(1) : 0;
        
        const pipe = { Applied: 0, Shortlisted: 0, Interview: 0, Offer: 0 };
        apps.forEach(a => {
          if (pipe[a.stage] !== undefined) pipe[a.stage]++;
        });

        setStats({
          jobs: jobsRes.data.length,
          candidates: candsRes.data.length,
          applications: apps.length,
          avgScore: avg
        });
        setPipeline(pipe);
        setRecentApps(apps.slice(-4).reverse());
      } catch (err) {
        console.error("Error fetching stats", err);
      }
    }
    fetchData();
  }, []);

  return (
    <div className="animate-fade-in-up text-white">
      <div className="flex flex-col sm:flex-row sm:items-center justify-between pb-6 mb-8 border-b border-white/10">
        <div>
          <div className="inline-flex items-center space-x-1 text-xs font-bold uppercase tracking-widest text-[#a100ff] mb-1">
            <Sparkles className="w-3.5 h-3.5 mr-1" /> Accenture Recruiter Telemetry
          </div>
          <h2 className="text-3xl font-black uppercase tracking-tight text-white">
            Talent Acquisition Overview <span className="text-[#a100ff]">&gt;</span>
          </h2>
          <p className="text-gray-400 text-xs mt-1">Real-time candidate metrics, funnel conversion, and deterministic AI scoring.</p>
        </div>
        <div className="mt-4 sm:mt-0 flex items-center space-x-3">
          <span className="text-xs font-bold uppercase tracking-wider text-green-400 bg-green-950/60 border border-green-500/30 px-3 py-1.5 rounded-full flex items-center">
            <span className="w-2 h-2 rounded-full bg-green-400 mr-2 animate-ping"></span> AI Engine Live
          </span>
        </div>
      </div>
      
      {/* Metric Cards */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
        <div className="accenture-card p-6 rounded-2xl border border-white/10 accenture-card-hover flex items-center">
          <div className="p-4 rounded-xl bg-purple-950/60 border border-purple-500/30 text-[#a100ff] mr-4">
            <Briefcase className="w-6 h-6" />
          </div>
          <div>
            <h3 className="text-gray-400 text-xs font-bold uppercase tracking-wider">Active Requisitions</h3>
            <p className="text-3xl font-black text-white mt-1">{stats.jobs}</p>
          </div>
        </div>

        <div className="accenture-card p-6 rounded-2xl border border-white/10 accenture-card-hover flex items-center">
          <div className="p-4 rounded-xl bg-blue-950/60 border border-blue-500/30 text-blue-400 mr-4">
            <Users className="w-6 h-6" />
          </div>
          <div>
            <h3 className="text-gray-400 text-xs font-bold uppercase tracking-wider">Parsed Candidates</h3>
            <p className="text-3xl font-black text-white mt-1">{stats.candidates}</p>
          </div>
        </div>

        <div className="accenture-card p-6 rounded-2xl border border-white/10 accenture-card-hover flex items-center">
          <div className="p-4 rounded-xl bg-indigo-950/60 border border-indigo-500/30 text-indigo-400 mr-4">
            <FileText className="w-6 h-6" />
          </div>
          <div>
            <h3 className="text-gray-400 text-xs font-bold uppercase tracking-wider">Total Applications</h3>
            <p className="text-3xl font-black text-white mt-1">{stats.applications}</p>
          </div>
        </div>

        <div className="accenture-card p-6 rounded-2xl border border-white/10 accenture-card-hover flex items-center">
          <div className="p-4 rounded-xl bg-emerald-950/60 border border-emerald-500/30 text-emerald-400 mr-4">
            <TrendingUp className="w-6 h-6" />
          </div>
          <div>
            <h3 className="text-gray-400 text-xs font-bold uppercase tracking-wider">Avg Neural Fit</h3>
            <p className="text-3xl font-black text-white mt-1">{stats.avgScore}%</p>
          </div>
        </div>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* Pipeline Breakdown */}
        <div className="accenture-card p-7 rounded-2xl border border-white/10 lg:col-span-2">
          <div className="flex items-center justify-between mb-6">
            <h3 className="text-lg font-bold text-white uppercase tracking-tight flex items-center">
              Recruitment Funnel Velocity <ChevronRight className="w-4 h-4 ml-1 text-[#a100ff]" />
            </h3>
            <span className="text-xs text-gray-400">Total: {stats.applications} in pipeline</span>
          </div>

          <div className="flex justify-between items-end h-44 space-x-4 pt-4">
            <div className="w-1/4 flex flex-col justify-end items-center group">
              <span className="mb-2 font-bold text-white text-sm transition-transform group-hover:-translate-y-1">{pipeline.Applied}</span>
              <div className="w-full bg-blue-900/60 border-t-2 border-blue-400 rounded-t-lg transition-all duration-500 group-hover:bg-blue-800/80" style={{ height: `${Math.max(pipeline.Applied * 10, 15)}%` }}></div>
              <span className="mt-3 text-[11px] font-bold text-gray-400 uppercase tracking-wider">Applied</span>
            </div>

            <div className="w-1/4 flex flex-col justify-end items-center group">
              <span className="mb-2 font-bold text-white text-sm transition-transform group-hover:-translate-y-1">{pipeline.Shortlisted}</span>
              <div className="w-full bg-indigo-900/60 border-t-2 border-indigo-400 rounded-t-lg transition-all duration-500 group-hover:bg-indigo-800/80" style={{ height: `${Math.max(pipeline.Shortlisted * 10, 15)}%` }}></div>
              <span className="mt-3 text-[11px] font-bold text-gray-400 uppercase tracking-wider">Shortlisted</span>
            </div>

            <div className="w-1/4 flex flex-col justify-end items-center group">
              <span className="mb-2 font-bold text-white text-sm transition-transform group-hover:-translate-y-1">{pipeline.Interview}</span>
              <div className="w-full bg-purple-900/60 border-t-2 border-purple-400 rounded-t-lg transition-all duration-500 group-hover:bg-purple-800/80" style={{ height: `${Math.max(pipeline.Interview * 10, 15)}%` }}></div>
              <span className="mt-3 text-[11px] font-bold text-gray-400 uppercase tracking-wider">Interview</span>
            </div>

            <div className="w-1/4 flex flex-col justify-end items-center group">
              <span className="mb-2 font-bold text-white text-sm transition-transform group-hover:-translate-y-1">{pipeline.Offer}</span>
              <div className="w-full bg-emerald-900/60 border-t-2 border-emerald-400 rounded-t-lg transition-all duration-500 group-hover:bg-emerald-800/80" style={{ height: `${Math.max(pipeline.Offer * 10, 15)}%` }}></div>
              <span className="mt-3 text-[11px] font-bold text-gray-400 uppercase tracking-wider">Offer</span>
            </div>
          </div>
        </div>

        {/* Recent Matches */}
        <div className="accenture-card p-7 rounded-2xl border border-white/10">
          <h3 className="text-lg font-bold text-white uppercase tracking-tight mb-4 flex items-center">
            Recent AI Matches <ChevronRight className="w-4 h-4 ml-1 text-[#a100ff]" />
          </h3>
          <div className="space-y-3">
            {recentApps.length === 0 ? (
              <p className="text-xs text-gray-500">No applications recorded yet.</p>
            ) : (
              recentApps.map((app) => (
                <div key={app.id} className="p-3.5 bg-white/5 border border-white/5 hover:border-white/10 rounded-xl flex items-center justify-between transition-colors">
                  <div className="flex items-center space-x-3">
                    {app.match_score >= 80 ? (
                      <CheckCircle className="text-green-400 w-5 h-5 flex-shrink-0" />
                    ) : (
                      <Clock className="text-yellow-400 w-5 h-5 flex-shrink-0" />
                    )}
                    <div>
                      <p className="text-xs font-bold text-white">Score: {app.match_score}%</p>
                      <p className="text-[10px] text-gray-400 font-semibold uppercase tracking-wider">Stage: {app.stage}</p>
                    </div>
                  </div>
                  <span className={`text-[10px] font-bold px-2 py-0.5 rounded-full ${
                    app.match_score >= 80 ? 'bg-green-950 text-green-300 border border-green-800' : 'bg-yellow-950 text-yellow-300 border border-yellow-800'
                  }`}>
                    {app.match_score >= 80 ? 'Strong Fit' : 'Moderate'}
                  </span>
                </div>
              ))
            )}
          </div>
        </div>
      </div>
    </div>
  );
}

export default Dashboard;
