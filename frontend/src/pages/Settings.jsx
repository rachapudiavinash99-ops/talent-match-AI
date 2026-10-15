import React, { useState } from 'react';
import { Settings as SettingsIcon, Sparkles, Shield, Cpu, Bell, Check } from 'lucide-react';

function Settings() {
  const [saved, setSaved] = useState(false);
  const [threshold, setThreshold] = useState(65);
  const [weight, setWeight] = useState('Balanced (50% weight)');

  const handleSave = () => {
    setSaved(true);
    setTimeout(() => setSaved(false), 3000);
  };

  return (
    <div className="animate-fade-in-up text-white">
      <div className="pb-6 mb-8 border-b border-white/10">
        <div className="inline-flex items-center space-x-1 text-xs font-bold uppercase tracking-widest text-[#ff8a3d] mb-1">
          <Sparkles className="w-3.5 h-3.5 mr-1" /> Platform Governance
        </div>
        <h2 className="text-3xl font-black uppercase tracking-tight text-white">
          ElevateIQ AI Configuration <span className="text-[#3fd0ff]">&gt;</span>
        </h2>
        <p className="text-gray-400 text-xs mt-1">Configure neural screening thresholds, skill vector strictness, and telemetry parameters.</p>
      </div>

      <div className="elevate-card p-8 rounded-2xl border border-white/10 max-w-3xl space-y-8">
        <div>
          <h3 className="text-lg font-bold uppercase text-white mb-4 flex items-center">
            <Cpu className="w-5 h-5 mr-2 text-[#ff8a3d]" /> Neural Matching Algorithm Sensitivity
          </h3>
          <div className="space-y-4">
            <div>
              <label className="block text-xs font-bold uppercase tracking-wider text-gray-300 mb-2">
                Minimum Match Score Acceptance Threshold ({threshold}%)
              </label>
              <input 
                type="range" 
                min="40" 
                max="90" 
                value={threshold} 
                onChange={e => setThreshold(e.target.value)}
                className="w-full accent-[#ff8a3d] bg-white/10 rounded-lg cursor-pointer h-2" 
              />
              <p className="text-[11px] text-gray-400 mt-1">Candidates below this score will be flagged for review or auto-archived.</p>
            </div>

            <div>
              <label className="block text-xs font-bold uppercase tracking-wider text-gray-300 mb-2">
                Skill Vector Strictness
              </label>
              <select 
                value={weight}
                onChange={e => setWeight(e.target.value)}
                className="w-full bg-[#0a0f24] border border-white/15 rounded-xl p-3 text-white text-xs focus:outline-none focus:border-[#3fd0ff]"
              >
                <option value="Strict (100% match required)" className="bg-[#0a0f24]">Strict (100% exact required skills match)</option>
                <option value="Balanced (50% weight)" className="bg-[#0a0f24]">Balanced (50% required skills + 50% semantic TF-IDF)</option>
                <option value="Loose (20% weight)" className="bg-[#0a0f24]">Broad (High weight on adjacent transferable skills)</option>
              </select>
            </div>
          </div>
        </div>

        <div className="pt-6 border-t border-white/10">
          <h3 className="text-lg font-bold uppercase text-white mb-4 flex items-center">
            <Shield className="w-5 h-5 mr-2 text-green-400" /> Data Privacy &amp; Thread-Safe Storage
          </h3>
          <div className="space-y-3">
            <label className="flex items-center space-x-3 cursor-pointer">
              <input type="checkbox" defaultChecked disabled className="form-checkbox h-4 w-4 text-[#ff8a3d] rounded bg-white/10 border-white/20" />
              <span className="text-xs text-gray-300 font-medium">Local JSON file-based repository active (No third-party database)</span>
            </label>
            <label className="flex items-center space-x-3 cursor-pointer">
              <input type="checkbox" defaultChecked className="form-checkbox h-4 w-4 text-[#ff8a3d] rounded bg-white/10 border-white/20" />
              <span className="text-xs text-gray-300 font-medium">Filelock concurrency protection enabled</span>
            </label>
            <label className="flex items-center space-x-3 cursor-pointer">
              <input type="checkbox" defaultChecked className="form-checkbox h-4 w-4 text-[#ff8a3d] rounded bg-white/10 border-white/20" />
              <span className="text-xs text-gray-300 font-medium">Zero-API external dependency mode enforced</span>
            </label>
          </div>
        </div>

        <div className="pt-6 border-t border-white/10 flex items-center justify-between">
          <button 
            onClick={handleSave}
            className="px-6 py-3.5 bg-gradient-to-r from-[#ff8a3d] to-[#f2701c] hover:brightness-110 text-white rounded-xl text-xs font-bold uppercase tracking-wider transition-all shadow-[0_0_20px_rgba(255,138,61,0.4)] flex items-center"
          >
            {saved ? <><Check className="w-4 h-4 mr-1.5" /> Configuration Saved</> : "Save Enterprise Settings >"}
          </button>
          {saved && (
            <span className="text-xs font-semibold text-green-400">Settings committed to repository.</span>
          )}
        </div>
      </div>
    </div>
  );
}

export default Settings;
