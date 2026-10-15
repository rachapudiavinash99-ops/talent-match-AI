import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { BarChart, Download, Sparkles, FileSpreadsheet } from 'lucide-react';

const API_BASE = 'http://localhost:8000/api';

function Reports() {
  const [stats, setStats] = useState({ applications: 0, candidates: 0, jobs: 0 });

  useEffect(() => {
    async function fetchData() {
      try {
        const [candsRes, appsRes, jobsRes] = await Promise.all([
          axios.get(`${API_BASE}/candidates/`),
          axios.get(`${API_BASE}/applications/`),
          axios.get(`${API_BASE}/jobs/`)
        ]);
        setStats({
          candidates: candsRes.data.length,
          applications: appsRes.data.length,
          jobs: jobsRes.data.length
        });
      } catch (err) {
        console.error("Error fetching stats", err);
      }
    }
    fetchData();
  }, []);

  const downloadCSV = async () => {
    try {
      const [candsRes, appsRes, jobsRes] = await Promise.all([
        axios.get(`${API_BASE}/candidates/`),
        axios.get(`${API_BASE}/applications/`),
        axios.get(`${API_BASE}/jobs/`)
      ]);

      const jobsMap = Object.fromEntries(jobsRes.data.map(j => [j.id, j.title]));
      const candsMap = Object.fromEntries(candsRes.data.map(c => [c.id, c.name]));

      let csv = "Application ID,Job Title,Candidate Name,AI Match Score,Stage\n";
      appsRes.data.forEach(app => {
        const jTitle = jobsMap[app.job_id] || app.job_id;
        const cName = candsMap[app.candidate_id] || app.candidate_id;
        csv += `"${app.id}","${jTitle}","${cName}","${app.match_score}%","${app.stage}"\n`;
      });

      const encodedUri = encodeURI("data:text/csv;charset=utf-8," + csv);
      const link = document.createElement("a");
      link.setAttribute("href", encodedUri);
      link.setAttribute("download", `ElevateIQ_TalentMatch_Report_${new Date().toISOString().split('T')[0]}.csv`);
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
    } catch (err) {
      alert("Error generating CSV export");
    }
  };

  return (
    <div className="animate-fade-in-up text-white">
      <div className="pb-6 mb-8 border-b border-white/10">
        <div className="inline-flex items-center space-x-1 text-xs font-bold uppercase tracking-widest text-[#ff8a3d] mb-1">
          <Sparkles className="w-3.5 h-3.5 mr-1" /> Enterprise Telemetry &amp; Auditing
        </div>
        <h2 className="text-3xl font-black uppercase tracking-tight text-white">
          Recruitment Intelligence Reports <span className="text-[#3fd0ff]">&gt;</span>
        </h2>
        <p className="text-gray-400 text-xs mt-1">Export structured tabular data, compliance records, and applicant tracking summaries.</p>
      </div>
      
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
        <div className="elevate-card p-6 rounded-2xl border border-white/10 flex flex-col items-center justify-center text-center">
          <h3 className="text-gray-400 text-xs font-bold uppercase tracking-wider mb-2">Ingested Resumes</h3>
          <p className="text-5xl font-black text-[#ff8a3d]">{stats.candidates}</p>
          <span className="text-[10px] text-gray-500 mt-2 font-semibold uppercase">Parsed &amp; Vectorized</span>
        </div>
        <div className="elevate-card p-6 rounded-2xl border border-white/10 flex flex-col items-center justify-center text-center">
          <h3 className="text-gray-400 text-xs font-bold uppercase tracking-wider mb-2">Active Pipeline Matches</h3>
          <p className="text-5xl font-black text-emerald-400">{stats.applications}</p>
          <span className="text-[10px] text-gray-500 mt-2 font-semibold uppercase">Evaluated by Local NLP</span>
        </div>
        <div className="elevate-card p-6 rounded-2xl border border-white/10 flex flex-col items-center justify-center text-center">
          <h3 className="text-gray-400 text-xs font-bold uppercase tracking-wider mb-2">Active Requisitions</h3>
          <p className="text-5xl font-black text-[#3fd0ff]">{stats.jobs}</p>
          <span className="text-[10px] text-gray-500 mt-2 font-semibold uppercase">Live on Portal (5+ apps each)</span>
        </div>
      </div>

      <div className="elevate-card p-8 rounded-2xl border border-white/10">
        <div className="flex items-center space-x-3 mb-4">
          <div className="p-3 bg-orange-950/60 border border-[#ff8a3d]/30 rounded-xl text-[#ff8a3d]">
            <FileSpreadsheet className="w-6 h-6" />
          </div>
          <div>
            <h3 className="text-xl font-bold uppercase text-white">Export Audit CSV Report</h3>
            <p className="text-gray-400 text-xs mt-0.5">Generate a complete tabular snapshot of all candidate match scores, skills, and current pipeline stages.</p>
          </div>
        </div>
        
        <p className="text-gray-400 text-sm mb-6 leading-relaxed">
          The export adheres to zero-database local JSON persistence guidelines, extracting live structured telemetry directly from the thread-safe repository layer for your team's analytics.
        </p>
        
        <button 
          onClick={downloadCSV} 
          className="px-6 py-3.5 bg-gradient-to-r from-[#ff8a3d] to-[#f2701c] hover:brightness-110 text-white rounded-xl text-xs font-bold uppercase tracking-wider transition-all shadow-[0_0_20px_rgba(255,138,61,0.4)] flex items-center"
        >
          <Download className="w-4 h-4 mr-2" /> Export Master CSV Report &gt;
        </button>
      </div>
    </div>
  );
}

export default Reports;
