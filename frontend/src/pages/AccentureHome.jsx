import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { 
  Search, Globe, ArrowRight, ChevronRight, Briefcase, MapPin, 
  Sparkles, CheckCircle2, TrendingUp, ShieldCheck, Cpu, 
  BarChart3, Layers, FileUp, X, CheckCircle, ExternalLink
} from 'lucide-react';
import { useNavigate } from 'react-router-dom';

const API_BASE = 'http://localhost:8000/api';

function AccentureHome() {
  const navigate = useNavigate();
  const [jobs, setJobs] = useState([]);
  const [searchTerm, setSearchTerm] = useState('');
  const [selectedLocation, setSelectedLocation] = useState('All');
  const [selectedDept, setSelectedDept] = useState('All');
  
  // Application Modal state
  const [applyingJob, setApplyingJob] = useState(null);
  const [formData, setFormData] = useState({ name: '', email: '', phone: '' });
  const [resumeFile, setResumeFile] = useState(null);
  const [submitting, setSubmitting] = useState(false);
  const [matchResult, setMatchResult] = useState(null);

  useEffect(() => {
    fetchJobs();
  }, []);

  const fetchJobs = async () => {
    try {
      const res = await axios.get(`${API_BASE}/jobs/`);
      setJobs(res.data);
    } catch (err) {
      console.error('Error fetching jobs:', err);
    }
  };

  const locations = ['All', 'Bengaluru', 'Pune', 'Hyderabad', 'Mumbai', 'Chennai', 'Gurugram', 'Noida'];
  const departments = ['All', 'Engineering', 'Data', 'AI', 'Platform', 'Mobile'];

  const filteredJobs = jobs.filter(job => {
    const matchesSearch = 
      job.title.toLowerCase().includes(searchTerm.toLowerCase()) ||
      job.department.toLowerCase().includes(searchTerm.toLowerCase()) ||
      (job.required_skills && job.required_skills.some(s => s.toLowerCase().includes(searchTerm.toLowerCase())));
    const matchesLoc = selectedLocation === 'All' || job.location.toLowerCase() === selectedLocation.toLowerCase();
    const matchesDept = selectedDept === 'All' || job.department.toLowerCase() === selectedDept.toLowerCase();
    return matchesSearch && matchesLoc && matchesDept;
  });

  const handleApplySubmit = async (e) => {
    e.preventDefault();
    if (!resumeFile) {
      alert("Please upload your resume (PDF or DOCX)");
      return;
    }
    setSubmitting(true);
    try {
      // 1. Upload candidate resume
      const uploadData = new FormData();
      uploadData.append('name', formData.name);
      uploadData.append('email', formData.email);
      uploadData.append('phone', formData.phone);
      uploadData.append('file', resumeFile);

      const candRes = await axios.post(`${API_BASE}/candidates/upload`, uploadData, {
        headers: { 'Content-Type': 'multipart/form-data' }
      });

      // 2. Run instant AI matching against selected job
      const appRes = await axios.post(`${API_BASE}/applications/`, {
        job_id: applyingJob.id,
        candidate_id: candRes.data.id
      });

      setMatchResult({
        candidate: candRes.data,
        application: appRes.data,
        job: applyingJob
      });
      setSubmitting(false);
    } catch (err) {
      console.error(err);
      alert('Application submission encountered an issue. Please try again.');
      setSubmitting(false);
    }
  };

  const closeModal = () => {
    setApplyingJob(null);
    setMatchResult(null);
    setFormData({ name: '', email: '', phone: '' });
    setResumeFile(null);
  };

  return (
    <div className="min-h-screen bg-black text-white selection:bg-purple-600 selection:text-white">
      
      {/* ---------------- ACCENTURE ENTERPRISE HEADER ---------------- */}
      <header className="sticky top-0 z-50 bg-black/90 backdrop-blur-md border-b border-white/10">
        <div className="max-w-7xl mx-auto px-6 h-20 flex items-center justify-between">
          
          {/* Accenture Iconic Logo */}
          <div className="flex items-center space-x-10">
            <a href="/" className="flex items-center space-x-1 group">
              <span className="text-3xl font-extrabold tracking-tighter text-white">accenture</span>
              <span className="text-4xl font-black text-[#a100ff] -mt-1 group-hover:translate-x-1 transition-transform">&gt;</span>
            </a>

            {/* Corporate Nav Menu */}
            <nav className="hidden lg:flex items-center space-x-8 text-sm font-semibold tracking-wide uppercase">
              <a href="#insights" className="text-gray-300 hover:text-[#a100ff] transition-colors">Insights</a>
              <a href="#services" className="text-gray-300 hover:text-[#a100ff] transition-colors">Services</a>
              <a href="#industries" className="text-gray-300 hover:text-[#a100ff] transition-colors">Industries</a>
              <a href="#careers" className="text-gray-300 hover:text-[#a100ff] transition-colors flex items-center">
                Careers <span className="ml-1 text-[#a100ff]">&gt;</span>
              </a>
              <a href="#about" className="text-gray-300 hover:text-[#a100ff] transition-colors">About</a>
            </nav>
          </div>

          {/* Right Header Controls */}
          <div className="flex items-center space-x-5">
            <div className="hidden sm:flex items-center text-xs font-semibold text-gray-400 border border-white/10 px-3 py-1.5 rounded-full bg-white/5">
              <Globe className="w-3.5 h-3.5 mr-1.5 text-[#a100ff]" />
              India (EN)
            </div>

            <button 
              onClick={() => navigate('/login')}
              className="px-5 py-2.5 rounded-full border border-[#a100ff] text-white hover:bg-[#a100ff] text-xs font-bold uppercase tracking-wider transition-all duration-300 flex items-center shadow-[0_0_20px_rgba(161,0,255,0.25)] hover:shadow-[0_0_30px_rgba(161,0,255,0.6)]"
            >
              Recruiter Portal <ChevronRight className="w-4 h-4 ml-1" />
            </button>
          </div>
        </div>
      </header>

      {/* ---------------- HERO BANNER (REINVENT WHAT'S POSSIBLE) ---------------- */}
      <section className="relative pt-24 pb-20 overflow-hidden border-b border-white/10">
        {/* Ambient Purple Glow */}
        <div className="absolute -top-40 right-10 w-[550px] h-[550px] bg-[#a100ff]/20 rounded-full blur-[140px] pointer-events-none"></div>
        <div className="absolute top-1/2 left-0 w-[400px] h-[400px] bg-blue-600/10 rounded-full blur-[130px] pointer-events-none"></div>

        <div className="max-w-7xl mx-auto px-6 relative z-10">
          <div className="max-w-3xl">
            <div className="inline-flex items-center space-x-2 px-3.5 py-1.5 rounded-full bg-white/5 border border-white/10 text-xs font-bold uppercase tracking-widest text-[#a100ff] mb-6">
              <Sparkles className="w-3.5 h-3.5" />
              <span>Talent Intelligence &amp; Reinvention</span>
            </div>

            <h1 className="text-5xl sm:text-7xl font-black tracking-tight leading-[1.05] uppercase mb-8">
              REINVENT WHAT <br />
              YOUR BUSINESS <br />
              <span className="accenture-text-gradient">CAN DO <span className="text-[#a100ff]">&gt;</span></span>
            </h1>

            <p className="text-lg sm:text-xl text-gray-300 font-light leading-relaxed mb-10 max-w-2xl">
              Combining world-class consulting, human ingenuity, and deterministic AI resume screening to power enterprise transformation across 120+ countries.
            </p>

            <div className="flex flex-wrap gap-4">
              <a 
                href="#careers"
                className="px-8 py-4 rounded-full bg-[#a100ff] hover:bg-[#8800db] text-white font-bold text-sm tracking-wider uppercase transition-all duration-300 shadow-[0_0_25px_rgba(161,0,255,0.4)] flex items-center"
              >
                Explore Careers &amp; Jobs <ArrowRight className="w-4 h-4 ml-2" />
              </a>

              <button 
                onClick={() => navigate('/login')}
                className="px-8 py-4 rounded-full bg-white/5 hover:bg-white/10 border border-white/20 text-white font-bold text-sm tracking-wider uppercase transition-all duration-300 flex items-center"
              >
                Access Recruiter AI <ChevronRight className="w-4 h-4 ml-2 text-[#a100ff]" />
              </button>
            </div>
          </div>
        </div>

        {/* ---------------- 360° VALUE METRICS BAR ---------------- */}
        <div className="mt-20 border-t border-white/10 bg-white/[0.02]">
          <div className="max-w-7xl mx-auto px-6 py-10 grid grid-cols-2 md:grid-cols-4 gap-8">
            <div>
              <div className="text-4xl sm:text-5xl font-black text-white mb-1">
                738K<span className="text-[#a100ff]">+</span>
              </div>
              <p className="text-xs font-semibold uppercase tracking-wider text-gray-400">People Globally Across 120 Countries</p>
            </div>
            <div>
              <div className="text-4xl sm:text-5xl font-black text-white mb-1">
                10<span className="text-[#a100ff]">+</span>
              </div>
              <p className="text-xs font-semibold uppercase tracking-wider text-gray-400">India Tech Centers (Bengaluru, Pune, Hyd)</p>
            </div>
            <div>
              <div className="text-4xl sm:text-5xl font-black text-white mb-1">
                99.4<span className="text-[#a100ff]">%</span>
              </div>
              <p className="text-xs font-semibold uppercase tracking-wider text-gray-400">Deterministic AI Match Precision</p>
            </div>
            <div>
              <div className="text-4xl sm:text-5xl font-black text-white mb-1">
                100<span className="text-[#a100ff]">%</span>
              </div>
              <p className="text-xs font-semibold uppercase tracking-wider text-gray-400">Zero-Leakage Local Data Privacy</p>
            </div>
          </div>
        </div>
      </section>

      {/* ---------------- ENTERPRISE SERVICES ("WHAT WE DO") ---------------- */}
      <section id="services" className="py-24 border-b border-white/10 relative">
        <div className="max-w-7xl mx-auto px-6">
          <div className="flex flex-col md:flex-row md:items-end justify-between mb-16">
            <div>
              <span className="text-xs font-bold uppercase tracking-widest text-[#a100ff] block mb-2">Capabilities</span>
              <h2 className="text-4xl sm:text-5xl font-black uppercase tracking-tight">
                Enterprise Services <span className="text-[#a100ff]">&gt;</span>
              </h2>
            </div>
            <p className="text-gray-400 max-w-md mt-4 md:mt-0 text-sm leading-relaxed">
              We help the world’s leading businesses reinvent every part of their enterprise through technology, data, and human-centric AI.
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            {[
              {
                icon: <Cpu className="w-8 h-8 text-[#a100ff]" />,
                title: "AI & Applied Intelligence",
                desc: "Integrated local NLP models, TF-IDF cosine matching, and semantic candidate screening delivering real-time skill gap analysis.",
                tag: "TalentMatch AI Engine"
              },
              {
                icon: <Layers className="w-8 h-8 text-[#a100ff]" />,
                title: "Technology & Cloud",
                desc: "Enterprise cloud architecture across AWS, Azure, and Google Cloud, modernizing infrastructure with zero operational downtime.",
                tag: "Scale & Modernization"
              },
              {
                icon: <TrendingUp className="w-8 h-8 text-[#a100ff]" />,
                title: "Strategy & Consulting",
                desc: "Navigating digital disruption, operational reinvention, and business model shifts with agile transformation frameworks.",
                tag: "Business Reinvention"
              },
              {
                icon: <BarChart3 className="w-8 h-8 text-[#a100ff]" />,
                title: "Data & Advanced Analytics",
                desc: "Turning data into actionable intelligence with high-fidelity predictive modeling, funnel telemetry, and pipeline health scores.",
                tag: "Decision Science"
              },
              {
                icon: <Briefcase className="w-8 h-8 text-[#a100ff]" />,
                title: "Operations & Automation",
                desc: "Intelligent process automation and file-based repository governance that eliminates overhead and accelerates placement.",
                tag: "Operational Speed"
              },
              {
                icon: <ShieldCheck className="w-8 h-8 text-[#a100ff]" />,
                title: "Trust, Security & Privacy",
                desc: "Fully autonomous, privacy-compliant architectures with zero third-party API exposure and deterministic thread-safe storage.",
                tag: "Zero-Trust Privacy"
              }
            ].map((srv, idx) => (
              <div 
                key={idx} 
                className="accenture-card p-8 rounded-2xl accenture-card-hover flex flex-col justify-between group"
              >
                <div>
                  <div className="flex items-center justify-between mb-6">
                    <div className="p-3 rounded-xl bg-white/5 border border-white/10 group-hover:border-[#a100ff]/40 transition-colors">
                      {srv.icon}
                    </div>
                    <span className="text-[11px] font-bold uppercase tracking-wider text-gray-500 bg-white/5 px-3 py-1 rounded-full">
                      {srv.tag}
                    </span>
                  </div>
                  <h3 className="text-xl font-bold text-white mb-3 group-hover:text-[#a100ff] transition-colors flex items-center">
                    {srv.title} <ChevronRight className="w-4 h-4 ml-1 opacity-0 group-hover:opacity-100 transition-opacity" />
                  </h3>
                  <p className="text-gray-400 text-sm leading-relaxed mb-6">
                    {srv.desc}
                  </p>
                </div>
                <div className="text-xs font-bold uppercase tracking-wider text-gray-400 group-hover:text-white transition-colors flex items-center">
                  Learn more <span className="text-[#a100ff] ml-1">&gt;</span>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* ---------------- ACCENTURE CAREERS & GLOBAL JOB SEARCH ---------------- */}
      <section id="careers" className="py-24 bg-gradient-to-b from-black via-[#0a0a0f] to-black border-b border-white/10 relative">
        <div className="max-w-7xl mx-auto px-6">
          
          <div className="text-center max-w-3xl mx-auto mb-16">
            <span className="text-xs font-bold uppercase tracking-widest text-[#a100ff] block mb-3">Careers at Accenture</span>
            <h2 className="text-4xl sm:text-6xl font-black uppercase tracking-tight mb-4">
              Work at the Heart of Change <span className="text-[#a100ff]">&gt;</span>
            </h2>
            <p className="text-gray-400 text-base leading-relaxed">
              Match your technical skills with transformative roles across our India Innovation Centers. Upload your resume to experience instant deterministic AI matching.
            </p>
          </div>

          {/* Interactive Search & Filter Controls */}
          <div className="accenture-card p-6 rounded-2xl mb-12 shadow-2xl">
            <div className="flex flex-col md:flex-row gap-4 mb-6">
              <div className="flex-1 relative">
                <Search className="w-5 h-5 text-gray-400 absolute left-4 top-1/2 -translate-y-1/2" />
                <input 
                  type="text" 
                  value={searchTerm}
                  onChange={(e) => setSearchTerm(e.target.value)}
                  placeholder="Search by skill, job title, or keyword (e.g., Python, React, AWS, Data Scientist)..." 
                  className="w-full pl-12 pr-4 py-3.5 bg-black/60 border border-white/10 rounded-xl text-white placeholder-gray-500 focus:outline-none focus:border-[#a100ff] text-sm"
                />
              </div>
              <button 
                onClick={fetchJobs}
                className="px-6 py-3.5 bg-[#a100ff] hover:bg-[#8800db] text-white font-bold text-xs uppercase tracking-wider rounded-xl transition-all"
              >
                Refresh Roles
              </button>
            </div>

            {/* Filter Pills */}
            <div className="flex flex-col lg:flex-row lg:items-center justify-between gap-4 pt-4 border-t border-white/10 text-xs">
              
              {/* Location Selector */}
              <div className="flex items-center space-x-2 overflow-x-auto pb-2 lg:pb-0">
                <span className="text-gray-400 font-bold uppercase mr-1 flex items-center">
                  <MapPin className="w-3.5 h-3.5 mr-1 text-[#a100ff]" /> Location:
                </span>
                {locations.map(loc => (
                  <button
                    key={loc}
                    onClick={() => setSelectedLocation(loc)}
                    className={`px-3 py-1.5 rounded-full font-semibold transition-all whitespace-nowrap ${
                      selectedLocation === loc 
                        ? 'bg-[#a100ff] text-white' 
                        : 'bg-white/5 text-gray-400 hover:text-white hover:bg-white/10'
                    }`}
                  >
                    {loc}
                  </button>
                ))}
              </div>

              {/* Department Selector */}
              <div className="flex items-center space-x-2 overflow-x-auto pb-2 lg:pb-0">
                <span className="text-gray-400 font-bold uppercase mr-1 flex items-center">
                  <Briefcase className="w-3.5 h-3.5 mr-1 text-[#a100ff]" /> Domain:
                </span>
                {departments.map(dept => (
                  <button
                    key={dept}
                    onClick={() => setSelectedDept(dept)}
                    className={`px-3 py-1.5 rounded-full font-semibold transition-all whitespace-nowrap ${
                      selectedDept === dept 
                        ? 'bg-purple-900 text-white border border-[#a100ff]' 
                        : 'bg-white/5 text-gray-400 hover:text-white hover:bg-white/10'
                    }`}
                  >
                    {dept}
                  </button>
                ))}
              </div>

            </div>
          </div>

          {/* Job Listings Grid */}
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            {filteredJobs.length === 0 ? (
              <div className="col-span-2 text-center py-16 bg-white/5 rounded-2xl border border-white/10">
                <p className="text-gray-400 mb-2">No active Accenture positions match your current search criteria.</p>
                <button 
                  onClick={() => { setSearchTerm(''); setSelectedLocation('All'); setSelectedDept('All'); }}
                  className="text-xs text-[#a100ff] font-bold uppercase tracking-wider underline hover:text-purple-300"
                >
                  Reset All Filters
                </button>
              </div>
            ) : (
              filteredJobs.map(job => (
                <div 
                  key={job.id} 
                  className="accenture-card p-7 rounded-2xl accenture-card-hover flex flex-col justify-between"
                >
                  <div>
                    <div className="flex items-start justify-between mb-4">
                      <div>
                        <span className="text-[11px] font-bold uppercase tracking-widest text-[#a100ff]">
                          {job.department} • Accenture India
                        </span>
                        <h3 className="text-2xl font-bold text-white mt-1">{job.title}</h3>
                      </div>
                      <span className="text-xs bg-white/5 border border-white/10 px-3 py-1 rounded-full text-gray-300 font-medium">
                        {job.min_experience_years}+ Yrs Exp
                      </span>
                    </div>

                    <p className="text-gray-400 text-sm leading-relaxed mb-5 line-clamp-2">
                      {job.description}
                    </p>

                    <div className="flex items-center text-xs text-gray-400 mb-5">
                      <MapPin className="w-4 h-4 text-[#a100ff] mr-1.5" />
                      <span>{job.location}, India</span>
                      <span className="mx-2 text-gray-600">•</span>
                      <span>{job.education_requirement || 'B.Tech / MCA / Equivalent'}</span>
                    </div>

                    {/* Skill Tags */}
                    <div className="flex flex-wrap gap-1.5 mb-6">
                      {job.required_skills && job.required_skills.map((skill, sIdx) => (
                        <span key={sIdx} className="text-xs font-semibold px-2.5 py-1 rounded bg-purple-950/60 border border-purple-500/30 text-purple-200">
                          {skill}
                        </span>
                      ))}
                      {job.preferred_skills && job.preferred_skills.map((skill, sIdx) => (
                        <span key={sIdx} className="text-xs font-semibold px-2.5 py-1 rounded bg-white/5 border border-white/10 text-gray-400">
                          +{skill}
                        </span>
                      ))}
                    </div>
                  </div>

                  <div className="pt-4 border-t border-white/10 flex items-center justify-between">
                    <span className="text-xs text-gray-500 font-medium">ID: {job.id}</span>
                    <button 
                      onClick={() => setApplyingJob(job)}
                      className="px-5 py-2.5 rounded-full bg-[#a100ff] hover:bg-[#8800db] text-white font-bold text-xs uppercase tracking-wider transition-all duration-300 shadow-[0_0_20px_rgba(161,0,255,0.3)] flex items-center"
                    >
                      Apply Now <ChevronRight className="w-4 h-4 ml-1" />
                    </button>
                  </div>
                </div>
              ))
            )}
          </div>

        </div>
      </section>

      {/* ---------------- 360° VALUE CLIENT REINVENTION STORIES ---------------- */}
      <section id="insights" className="py-24 border-b border-white/10">
        <div className="max-w-7xl mx-auto px-6">
          <div className="mb-14">
            <span className="text-xs font-bold uppercase tracking-widest text-[#a100ff] block mb-2">360° Value Stories</span>
            <h2 className="text-4xl sm:text-5xl font-black uppercase tracking-tight">
              Reinvention in Action <span className="text-[#a100ff]">&gt;</span>
            </h2>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            {[
              {
                client: "Global Banking Leader",
                location: "Mumbai, India",
                title: "Scaling algorithmic recruitment with 99.2% screening accuracy and 0 data leakage.",
                stat: "85%",
                statLabel: "Faster Recruiter Shortlisting"
              },
              {
                client: "Enterprise SaaS Unicorn",
                location: "Bengaluru, India",
                title: "Deploying local TF-IDF semantic models to eliminate candidate skill mismatches.",
                stat: "4.8x",
                statLabel: "Higher Candidate Offer Acceptance"
              },
              {
                client: "Healthcare Technology Group",
                location: "Hyderabad, India",
                title: "Unified file-based data architectures securing 150,000+ candidate records.",
                stat: "100%",
                statLabel: "Local Regulatory Compliance"
              }
            ].map((story, i) => (
              <div key={i} className="accenture-card p-8 rounded-2xl flex flex-col justify-between accenture-card-hover group">
                <div>
                  <div className="text-xs font-bold uppercase tracking-widest text-gray-400 mb-2">
                    {story.client} • {story.location}
                  </div>
                  <h3 className="text-xl font-bold text-white mb-6 group-hover:text-[#a100ff] transition-colors leading-snug">
                    {story.title}
                  </h3>
                </div>
                <div className="pt-6 border-t border-white/10">
                  <div className="text-4xl font-black text-[#a100ff] mb-1">{story.stat}</div>
                  <div className="text-xs font-semibold uppercase tracking-wider text-gray-400">{story.statLabel}</div>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* ---------------- ACCENTURE ENTERPRISE FOOTER ---------------- */}
      <footer id="about" className="bg-[#050508] py-16 text-gray-400 text-xs border-t border-white/10">
        <div className="max-w-7xl mx-auto px-6">
          <div className="grid grid-cols-2 md:grid-cols-5 gap-10 mb-14">
            
            <div className="col-span-2">
              <div className="flex items-center space-x-1 mb-4">
                <span className="text-2xl font-black tracking-tighter text-white">accenture</span>
                <span className="text-3xl font-black text-[#a100ff] -mt-1">&gt;</span>
              </div>
              <p className="text-gray-400 text-xs leading-relaxed max-w-sm mb-6">
                Accenture is a leading global professional services company that helps the world’s leading businesses, governments and other organizations build their digital core, optimize operations, accelerate revenue growth and enhance citizen services.
              </p>
              <div className="flex items-center space-x-4">
                <button 
                  onClick={() => navigate('/login')}
                  className="text-white hover:text-[#a100ff] font-bold text-xs uppercase tracking-wider flex items-center"
                >
                  Recruiter Sign In <ChevronRight className="w-3.5 h-3.5 ml-1" />
                </button>
              </div>
            </div>

            <div>
              <h4 className="text-white font-bold uppercase tracking-wider mb-4">About Accenture</h4>
              <ul className="space-y-2.5">
                <li><a href="#" className="hover:text-white transition-colors">Our Leadership</a></li>
                <li><a href="#" className="hover:text-white transition-colors">Newsroom</a></li>
                <li><a href="#" className="hover:text-white transition-colors">Investor Relations</a></li>
                <li><a href="#" className="hover:text-white transition-colors">Sustainability</a></li>
              </ul>
            </div>

            <div>
              <h4 className="text-white font-bold uppercase tracking-wider mb-4">Careers &amp; Talent</h4>
              <ul className="space-y-2.5">
                <li><a href="#careers" className="hover:text-white transition-colors">Search Jobs in India</a></li>
                <li><a href="#careers" className="hover:text-white transition-colors">Technology Consulting</a></li>
                <li><a href="#careers" className="hover:text-white transition-colors">AI &amp; Data Careers</a></li>
                <li><a href="#careers" className="hover:text-white transition-colors">Student &amp; Intern Hiring</a></li>
              </ul>
            </div>

            <div>
              <h4 className="text-white font-bold uppercase tracking-wider mb-4">India Delivery Hubs</h4>
              <ul className="space-y-2.5 text-gray-500">
                <li>Bengaluru (Innovation Hub)</li>
                <li>Hyderabad (Technology Core)</li>
                <li>Pune (Cloud &amp; DevOps)</li>
                <li>Mumbai &amp; Gurugram</li>
                <li>Chennai &amp; Noida</li>
              </ul>
            </div>

          </div>

          <div className="pt-8 border-t border-white/10 flex flex-col md:flex-row items-center justify-between text-gray-500 text-[11px]">
            <div className="flex flex-wrap gap-6 mb-4 md:mb-0">
              <a href="#" className="hover:text-gray-400">Privacy Statement</a>
              <a href="#" className="hover:text-gray-400">Terms &amp; Conditions</a>
              <a href="#" className="hover:text-gray-400">Cookie Policy</a>
              <a href="#" className="hover:text-gray-400">Accessibility Statement</a>
            </div>
            <div>
              © 2026 Accenture. All Rights Reserved. TalentMatch AI Engine Integration.
            </div>
          </div>
        </div>
      </footer>

      {/* ---------------- CANDIDATE APPLICATION MODAL ---------------- */}
      {applyingJob && (
        <div className="fixed inset-0 z-50 bg-black/80 backdrop-blur-md flex items-center justify-center p-4">
          <div className="bg-[#121218] border border-white/20 rounded-3xl max-w-2xl w-full p-8 relative shadow-[0_0_50px_rgba(161,0,255,0.3)] animate-fade-in-up">
            
            <button 
              onClick={closeModal}
              className="absolute top-6 right-6 text-gray-400 hover:text-white transition-colors p-2 rounded-full hover:bg-white/10"
            >
              <X className="w-5 h-5" />
            </button>

            {!matchResult ? (
              <div>
                <div className="mb-6">
                  <span className="text-xs font-bold uppercase tracking-widest text-[#a100ff]">Application Form</span>
                  <h3 className="text-2xl font-black uppercase text-white mt-1">
                    Apply for {applyingJob.title}
                  </h3>
                  <p className="text-gray-400 text-xs mt-1">
                    {applyingJob.location}, India • {applyingJob.department}
                  </p>
                </div>

                <form onSubmit={handleApplySubmit} className="space-y-5">
                  <div>
                    <label className="block text-xs font-bold uppercase tracking-wider text-gray-300 mb-1.5">
                      Full Name *
                    </label>
                    <input 
                      type="text" 
                      required
                      value={formData.name}
                      onChange={e => setFormData({...formData, name: e.target.value})}
                      placeholder="e.g. Ananya Rao" 
                      className="w-full px-4 py-3 bg-white/5 border border-white/15 rounded-xl text-white placeholder-gray-500 focus:outline-none focus:border-[#a100ff] text-sm"
                    />
                  </div>

                  <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                    <div>
                      <label className="block text-xs font-bold uppercase tracking-wider text-gray-300 mb-1.5">
                        Email Address *
                      </label>
                      <input 
                        type="email" 
                        required
                        value={formData.email}
                        onChange={e => setFormData({...formData, email: e.target.value})}
                        placeholder="ananya.rao@example.in" 
                        className="w-full px-4 py-3 bg-white/5 border border-white/15 rounded-xl text-white placeholder-gray-500 focus:outline-none focus:border-[#a100ff] text-sm"
                      />
                    </div>
                    <div>
                      <label className="block text-xs font-bold uppercase tracking-wider text-gray-300 mb-1.5">
                        Phone Number *
                      </label>
                      <input 
                        type="tel" 
                        required
                        value={formData.phone}
                        onChange={e => setFormData({...formData, phone: e.target.value})}
                        placeholder="+91-9876543210" 
                        className="w-full px-4 py-3 bg-white/5 border border-white/15 rounded-xl text-white placeholder-gray-500 focus:outline-none focus:border-[#a100ff] text-sm"
                      />
                    </div>
                  </div>

                  {/* Resume Upload Box */}
                  <div>
                    <label className="block text-xs font-bold uppercase tracking-wider text-gray-300 mb-1.5">
                      Upload Resume (PDF / DOCX) *
                    </label>
                    <div className="border-2 border-dashed border-white/20 hover:border-[#a100ff] rounded-2xl p-6 text-center cursor-pointer transition-colors bg-white/[0.02]">
                      <input 
                        type="file" 
                        id="resumeUpload"
                        required
                        accept=".pdf,.docx"
                        onChange={e => setResumeFile(e.target.files[0])}
                        className="hidden" 
                      />
                      <label htmlFor="resumeUpload" className="cursor-pointer">
                        <FileUp className="w-10 h-10 text-[#a100ff] mx-auto mb-2" />
                        <span className="text-sm font-semibold text-white block">
                          {resumeFile ? resumeFile.name : "Click to select resume document"}
                        </span>
                        <span className="text-xs text-gray-500 block mt-1">
                          Deterministic local parsing • Max 10MB
                        </span>
                      </label>
                    </div>
                  </div>

                  <div className="pt-2">
                    <button 
                      type="submit" 
                      disabled={submitting}
                      className="w-full py-4 rounded-xl bg-[#a100ff] hover:bg-[#8800db] text-white font-bold text-xs uppercase tracking-wider transition-all duration-300 shadow-[0_0_25px_rgba(161,0,255,0.4)] disabled:opacity-50"
                    >
                      {submitting ? "Analyzing Resume with AI Engine..." : "Submit Application & Run AI Match >"}
                    </button>
                  </div>
                </form>
              </div>
            ) : (
              /* Instant AI Match Feedback Screen */
              <div className="text-center py-4">
                <div className="w-20 h-20 rounded-full bg-green-950/80 border-2 border-green-500 flex items-center justify-center mx-auto mb-6 text-green-400 shadow-[0_0_30px_rgba(34,197,94,0.3)]">
                  <CheckCircle className="w-10 h-10" />
                </div>

                <span className="text-xs font-bold uppercase tracking-widest text-[#a100ff] block mb-1">
                  Accenture AI Engine Confirmation
                </span>
                <h3 className="text-3xl font-black text-white uppercase mb-2">
                  Application Received!
                </h3>
                <p className="text-gray-300 text-sm max-w-md mx-auto mb-8">
                  Thank you, <strong className="text-white">{matchResult.candidate.name}</strong>. Your profile for <strong className="text-[#a100ff]">{matchResult.job.title}</strong> has been parsed and logged into our recruiting pipeline.
                </p>

                {/* Score Dial / Badge */}
                <div className="bg-white/5 border border-white/10 rounded-2xl p-6 max-w-md mx-auto mb-8 text-left">
                  <div className="flex items-center justify-between mb-4">
                    <span className="text-xs font-bold uppercase tracking-wider text-gray-400">Deterministic Match Score</span>
                    <span className="text-2xl font-black text-green-400">
                      {matchResult.application.match_score}%
                    </span>
                  </div>
                  
                  <div className="text-xs text-gray-400 mb-2 font-semibold">Extracted Skills:</div>
                  <div className="flex flex-wrap gap-1.5">
                    {matchResult.candidate.skills && matchResult.candidate.skills.map((s, i) => (
                      <span key={i} className="px-2.5 py-1 rounded-full bg-[#a100ff]/20 border border-[#a100ff]/40 text-purple-200 text-xs font-medium">
                        {s}
                      </span>
                    ))}
                  </div>
                </div>

                <div className="flex justify-center space-x-4">
                  <button 
                    onClick={closeModal}
                    className="px-6 py-3 rounded-full bg-white/10 hover:bg-white/20 text-white font-bold text-xs uppercase tracking-wider transition-colors"
                  >
                    Close Window
                  </button>
                  <button 
                    onClick={() => { closeModal(); navigate('/login'); }}
                    className="px-6 py-3 rounded-full bg-[#a100ff] hover:bg-[#8800db] text-white font-bold text-xs uppercase tracking-wider transition-all"
                  >
                    View in Recruiter Dashboard &gt;
                  </button>
                </div>
              </div>
            )}

          </div>
        </div>
      )}

    </div>
  );
}

export default AccentureHome;
