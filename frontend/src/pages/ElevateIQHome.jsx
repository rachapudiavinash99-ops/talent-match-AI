import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { 
  Search, Globe, ArrowRight, ChevronRight, Briefcase, MapPin, 
  Sparkles, CheckCircle2, TrendingUp, ShieldCheck, Cpu, 
  BarChart3, Layers, FileUp, X, CheckCircle, Phone, Mail, 
  Code2, Database, FileText, Headphones, HeartPulse, Building2, ExternalLink
} from 'lucide-react';
import { useNavigate } from 'react-router-dom';

const API_BASE = 'http://localhost:8000/api';

function ElevateIQHome() {
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

  const locations = ['All', 'Chennai', 'Kochi', 'Narasaraopet', 'Hyderabad', 'Bengaluru'];
  const departments = ['All', 'IT Engineering', 'Data Solutions', 'Cloud & Infra', 'AI Solutions', 'Non-IT & Healthcare BPO'];

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
    <div className="min-h-screen bg-[#06091A] text-white selection:bg-[#ff8a3d] selection:text-white">
      
      {/* ---------------- ELEVATEIQ ENTERPRISE HEADER ---------------- */}
      <header className="sticky top-0 z-50 bg-[#06091A]/95 backdrop-blur-md border-b border-white/10">
        <div className="max-w-7xl mx-auto px-6 h-20 flex items-center justify-between">
          
          {/* ElevateIQ Brand Logo */}
          <div className="flex items-center space-x-10">
            <a href="/" className="flex items-center space-x-3 group">
              <img 
                src="https://elevateiq-softtech.com/images/logo.png" 
                alt="ElevateIQ Soft Tech" 
                className="h-10 w-auto object-contain filter drop-shadow-[0_0_12px_rgba(63,208,255,0.4)]"
                onError={(e) => { e.target.style.display = 'none'; }}
              />
              <div className="flex items-center">
                <span className="text-2xl font-black tracking-tight text-white flex items-center">
                  Elevate<span className="text-[#3fd0ff]">IQ</span>
                </span>
              </div>
            </a>

            {/* Corporate Nav Menu */}
            <nav className="hidden lg:flex items-center space-x-7 text-xs font-bold tracking-wider uppercase text-gray-300">
              <a 
                href="#about" 
                onClick={(e) => { e.preventDefault(); document.getElementById('about')?.scrollIntoView({ behavior: 'smooth' }); }}
                className="hover:text-[#3fd0ff] transition-colors cursor-pointer"
              >
                About Us
              </a>
              <a 
                href="#services" 
                onClick={(e) => { e.preventDefault(); document.getElementById('services')?.scrollIntoView({ behavior: 'smooth' }); }}
                className="hover:text-[#3fd0ff] transition-colors cursor-pointer"
              >
                Enterprise Services
              </a>
              <a 
                href="#careers" 
                onClick={(e) => { e.preventDefault(); document.getElementById('careers')?.scrollIntoView({ behavior: 'smooth' }); }}
                className="hover:text-[#ff8a3d] transition-colors flex items-center cursor-pointer"
              >
                Careers <span className="ml-1 px-1.5 py-0.5 rounded-full text-[9px] bg-[#ff8a3d]/20 text-[#ff8a3d] font-bold">Hiring</span>
              </a>
              <a 
                href="#branches" 
                onClick={(e) => { e.preventDefault(); document.getElementById('branches')?.scrollIntoView({ behavior: 'smooth' }); }}
                className="hover:text-[#3fd0ff] transition-colors cursor-pointer"
              >
                India Branches
              </a>
              <a 
                href="#contact" 
                onClick={(e) => { e.preventDefault(); document.getElementById('contact')?.scrollIntoView({ behavior: 'smooth' }); }}
                className="hover:text-[#3fd0ff] transition-colors cursor-pointer"
              >
                Contact
              </a>
            </nav>
          </div>

          {/* Right Header Controls */}
          <div className="flex items-center space-x-4">
            <a 
              href="tel:+916300855710"
              className="hidden sm:flex items-center text-xs font-semibold text-gray-400 hover:text-white transition-colors"
            >
              <Phone className="w-3.5 h-3.5 mr-1.5 text-[#3fd0ff]" />
              +91-6300855710
            </a>

            <button 
              onClick={() => navigate('/login')}
              className="px-5 py-2.5 rounded-full bg-gradient-to-r from-[#ff8a3d] to-[#f2701c] text-white hover:brightness-110 text-xs font-bold uppercase tracking-wider transition-all shadow-[0_0_20px_rgba(255,138,61,0.35)] flex items-center"
            >
              Recruiter AI Console <ChevronRight className="w-4 h-4 ml-1" />
            </button>
          </div>
        </div>
      </header>

      {/* ---------------- HERO HEADER SECTION ---------------- */}
      <section className="relative pt-20 pb-20 overflow-hidden border-b border-white/10">
        {/* Dynamic Backdrop Gradient Orbs (ElevateIQ Blue & Orange) */}
        <div className="absolute top-10 left-10 w-[500px] h-[500px] bg-[#3fd0ff]/15 rounded-full blur-[140px] pointer-events-none"></div>
        <div className="absolute top-20 right-10 w-[500px] h-[500px] bg-[#ff8a3d]/15 rounded-full blur-[140px] pointer-events-none"></div>

        <div className="max-w-7xl mx-auto px-6 relative z-10 text-center">
          
          {/* Hiring Notice Badge */}
          <div className="inline-flex items-center space-x-2 px-4 py-2 rounded-full bg-white/5 border border-white/10 backdrop-blur-md text-xs font-bold tracking-wider text-gray-300 uppercase mb-8 shadow-sm">
            <span className="w-2 h-2 rounded-full bg-[#ff8a3d] animate-pulse"></span>
            <span>We're Hiring • Chennai • Kochi • Narasaraopet • Hyderabad</span>
          </div>

          {/* Tagline & Main Headline */}
          <h1 className="text-4xl sm:text-6xl md:text-7xl font-black tracking-tight uppercase leading-[1.1] mb-6">
            Elevate Your Business. <br />
            <span className="elevate-text-gradient">Empower Your Future.</span>
          </h1>

          <p className="text-lg sm:text-xl text-gray-300 font-light leading-relaxed max-w-3xl mx-auto mb-10">
            Premier technology &amp; business solutions provider offering custom software engineering, cloud infrastructure, medical coding, AR calling, and deterministic AI talent screening.
          </p>

          <div className="flex flex-wrap items-center justify-center gap-4">
            <a 
              href="#careers"
              className="px-8 py-4 rounded-full bg-[#ff8a3d] hover:bg-[#f2701c] text-white font-bold text-xs uppercase tracking-wider transition-all duration-300 shadow-[0_0_25px_rgba(255,138,61,0.4)] flex items-center"
            >
              Browse Open Positions <ArrowRight className="w-4 h-4 ml-2" />
            </a>

            <a 
              href="#services"
              className="px-8 py-4 rounded-full bg-white/5 hover:bg-white/10 border border-white/20 text-white font-bold text-xs uppercase tracking-wider transition-all duration-300 flex items-center"
            >
              Our Enterprise Services <ChevronRight className="w-4 h-4 ml-1 text-[#3fd0ff]" />
            </a>

            <button 
              onClick={() => navigate('/login')}
              className="px-8 py-4 rounded-full bg-[#3fd0ff]/10 hover:bg-[#3fd0ff]/20 border border-[#3fd0ff]/40 text-[#3fd0ff] font-bold text-xs uppercase tracking-wider transition-all duration-300 flex items-center"
            >
              Recruiter AI Login <ChevronRight className="w-4 h-4 ml-1" />
            </button>
          </div>
        </div>

        {/* ---------------- QUANTITATIVE METRICS SECTION ---------------- */}
        <div className="mt-20 border-t border-white/10 bg-white/[0.01]">
          <div className="max-w-7xl mx-auto px-6 py-12 grid grid-cols-2 md:grid-cols-4 gap-8 text-center">
            <div className="elevate-card p-6 rounded-2xl border border-white/10">
              <h3 className="text-4xl sm:text-5xl font-black text-[#3fd0ff] mb-1">50<span className="text-[#ff8a3d]">+</span></h3>
              <p className="text-xs font-bold uppercase tracking-wider text-gray-400">Enterprise Clients</p>
            </div>
            <div className="elevate-card p-6 rounded-2xl border border-white/10">
              <h3 className="text-4xl sm:text-5xl font-black text-[#ff8a3d] mb-1">98<span className="text-[#3fd0ff]">%</span></h3>
              <p className="text-xs font-bold uppercase tracking-wider text-gray-400">Project Delivery Success</p>
            </div>
            <div className="elevate-card p-6 rounded-2xl border border-white/10">
              <h3 className="text-4xl sm:text-5xl font-black text-[#3fd0ff] mb-1">150<span className="text-[#ff8a3d]">+</span></h3>
              <p className="text-xs font-bold uppercase tracking-wider text-gray-400">Expert Engineers Placed</p>
            </div>
            <div className="elevate-card p-6 rounded-2xl border border-white/10">
              <h3 className="text-4xl sm:text-5xl font-black text-[#ff8a3d] mb-1">24/7</h3>
              <p className="text-xs font-bold uppercase tracking-wider text-gray-400">Consulting Support Desk</p>
            </div>
          </div>
        </div>
      </section>

      {/* ---------------- ABOUT US SECTION (WHO WE ARE & WHAT DRIVES US) ---------------- */}
      <section id="about" className="py-24 border-b border-white/10 relative scroll-mt-20">
        {/* Subtle Ambient Backing */}
        <div className="absolute top-1/2 left-1/3 w-96 h-96 bg-[#ff8a3d]/10 rounded-full blur-[140px] pointer-events-none"></div>

        <div className="max-w-7xl mx-auto px-6 relative z-10">
          
          <div className="text-center max-w-3xl mx-auto mb-16">
            <span className="text-xs font-bold uppercase tracking-widest text-[#ff8a3d] block mb-2">About ElevateIQ Soft Tech</span>
            <h2 className="text-3xl sm:text-5xl font-black uppercase tracking-tight text-white mb-4">
              Who We Are &amp; What Drives Us <span className="text-[#3fd0ff]">&gt;</span>
            </h2>
            <p className="text-[#3fd0ff] font-semibold text-base tracking-wide uppercase">
              "Elevate Your Business. Empower Your Future."
            </p>
          </div>

          {/* Main Story Box */}
          <div className="elevate-card p-8 sm:p-12 rounded-3xl border border-white/10 mb-12 shadow-2xl">
            <div className="max-w-4xl mx-auto space-y-6 text-gray-300 text-sm sm:text-base leading-relaxed">
              <p>
                <strong className="text-white font-bold">ElevateIQ Soft Tech Private Limited</strong> is a premier technology and business-solutions provider helping global organizations grow through reliable software engineering, highly skilled talent, and dependable operational support services.
              </p>
              <p>
                We combine strong engineering practices with a people-first approach — architecting everything from resilient backend systems, crawler pipelines, and cloud infrastructure to modern web platforms, while simultaneously empowering healthcare and corporate clients with Non-IT services including HIPAA-compliant medical coding, AR calling, and business process sourcing.
              </p>
              <div className="p-6 rounded-2xl bg-gradient-to-r from-[#ff8a3d]/15 to-[#3fd0ff]/15 border border-white/10 flex items-start space-x-4">
                <Sparkles className="w-6 h-6 text-[#ff8a3d] flex-shrink-0 mt-0.5" />
                <p className="text-white font-medium text-sm leading-relaxed m-0">
                  <strong className="text-[#ff8a3d]">Our Mission:</strong> Elevate your business, empower your future — with technology that works, high-integrity AI talent matching, and an agile team that genuinely cares about delivery excellence.
                </p>
              </div>
            </div>
          </div>

          {/* Three Core Corporate Pillars */}
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-12">
            
            <div className="elevate-card p-7 rounded-2xl border border-white/10 elevate-card-hover flex flex-col justify-between">
              <div>
                <div className="w-12 h-12 rounded-xl bg-[#ff8a3d]/15 border border-[#ff8a3d]/30 flex items-center justify-center text-[#ff8a3d] mb-5">
                  <Code2 className="w-6 h-6" />
                </div>
                <h3 className="text-xl font-bold text-white mb-2">Pillar 01: Engineering</h3>
                <p className="text-gray-400 text-xs leading-relaxed">
                  Full-stack software engineering, automated data harvesting, OCR document processing, and cloud-native DevOps built for scalability.
                </p>
              </div>
              <div className="mt-6 pt-4 border-t border-white/10 text-[11px] font-bold text-[#ff8a3d] uppercase tracking-wider">
                React • Python • AWS • Microservices
              </div>
            </div>

            <div className="elevate-card p-7 rounded-2xl border border-white/10 elevate-card-hover flex flex-col justify-between">
              <div>
                <div className="w-12 h-12 rounded-xl bg-[#3fd0ff]/15 border border-[#3fd0ff]/30 flex items-center justify-center text-[#3fd0ff] mb-5">
                  <HeartPulse className="w-6 h-6" />
                </div>
                <h3 className="text-xl font-bold text-white mb-2">Pillar 02: Healthcare BPO</h3>
                <p className="text-gray-400 text-xs leading-relaxed">
                  HIPAA-compliant medical coding, ICD-10 &amp; CPT charge entry, proactive AR insurance follow-ups, and QA-driven denial prevention.
                </p>
              </div>
              <div className="mt-6 pt-4 border-t border-white/10 text-[11px] font-bold text-[#3fd0ff] uppercase tracking-wider">
                RCM Operations • AR Calling • TESS
              </div>
            </div>

            <div className="elevate-card p-7 rounded-2xl border border-white/10 elevate-card-hover flex flex-col justify-between">
              <div>
                <div className="w-12 h-12 rounded-xl bg-purple-500/15 border border-purple-500/30 flex items-center justify-center text-purple-400 mb-5">
                  <Cpu className="w-6 h-6" />
                </div>
                <h3 className="text-xl font-bold text-white mb-2">Pillar 03: AI Talent Engine</h3>
                <p className="text-gray-400 text-xs leading-relaxed">
                  Deterministic local AI resume screening with skill-gap extraction, TF-IDF cosine matching, and zero cloud data leakage.
                </p>
              </div>
              <div className="mt-6 pt-4 border-t border-white/10 text-[11px] font-bold text-purple-400 uppercase tracking-wider">
                TalentMatch AI • Deterministic NLP
              </div>
            </div>

          </div>

          {/* Quick Action */}
          <div className="text-center">
            <button 
              onClick={() => document.getElementById('careers')?.scrollIntoView({ behavior: 'smooth' })}
              className="px-8 py-3.5 rounded-full bg-gradient-to-r from-[#ff8a3d] to-[#f2701c] hover:brightness-110 text-white font-bold text-xs uppercase tracking-wider transition-all shadow-[0_0_20px_rgba(255,138,61,0.35)]"
            >
              See Open Positions at ElevateIQ &gt;
            </button>
          </div>

        </div>
      </section>

      {/* ---------------- ENTERPRISE SERVICES SECTION (IT & NON-IT) ---------------- */}
      <section id="services" className="py-24 border-b border-white/10 relative scroll-mt-20">
        <div className="max-w-7xl mx-auto px-6">
          
          <div className="text-center max-w-3xl mx-auto mb-16">
            <span className="text-xs font-bold uppercase tracking-widest text-[#ff8a3d] block mb-2">Our Enterprise Capabilities</span>
            <h2 className="text-3xl sm:text-5xl font-black uppercase tracking-tight text-white mb-4">
              Comprehensive IT &amp; Non-IT Solutions
            </h2>
            <p className="text-gray-400 text-sm leading-relaxed">
              We deliver end-to-end tech engineering and high-performance BPO operations with dedicated expertise for global enterprise scaling.
            </p>
          </div>

          {/* ================= CATEGORY 01: IT SERVICES & DATA SOLUTIONS ================= */}
          <div className="mb-16">
            <div className="flex items-center justify-between p-6 rounded-2xl bg-gradient-to-r from-[#ff8a3d]/15 to-[#f2701c]/5 border border-[#ff8a3d]/30 mb-8 backdrop-blur-md">
              <div>
                <span className="text-xs font-bold uppercase tracking-wider text-[#ff8a3d] block mb-1">Category 01 • Engineering &amp; Technology</span>
                <h3 className="text-2xl font-black text-white flex items-center">
                  <Code2 className="w-6 h-6 mr-2 text-[#ff8a3d]" /> IT Services &amp; Data Solutions
                </h3>
              </div>
              <span className="hidden sm:inline-block text-xs font-semibold text-gray-300 bg-white/10 px-4 py-1.5 rounded-full border border-white/10">
                6 Specialized Domains
              </span>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
              {[
                {
                  title: "Software & Web Engineering",
                  desc: "Full-stack web applications, microservices, and enterprise software designed for high availability using React, Next.js, Python, Java, and Go.",
                  tags: ["React / Next.js", "Python & Go", "Microservices"]
                },
                {
                  title: "Data Collection & Harvesting",
                  desc: "Large-scale web scraping, automated crawler pipelines, structured data extraction, and market intelligence with enterprise anti-bot bypass.",
                  tags: ["Web Scraping", "Selenium / Scrapy", "Structured Data"]
                },
                {
                  title: "PDF Data Collection & IDP",
                  desc: "Intelligent Document Processing (IDP) utilizing OCR, layout models, and NLP for table extraction, financial parsing, and schema normalization.",
                  tags: ["OCR & LayoutLM", "Invoice Parsing", "Schema Normalization"]
                },
                {
                  title: "Data Annotation & ML Labeling",
                  desc: "High-precision ground-truth labeling for AI models: computer vision bounding boxes, polygon segmentation, and NLP sentiment tagging.",
                  tags: ["Computer Vision", "Bounding Boxes", "NLP Tagging"]
                },
                {
                  title: "Cloud, DevOps & Databases",
                  desc: "Cloud-native infrastructure on AWS, GCP, and Azure with automated CI/CD pipelines, Docker, Kubernetes, and high-performance databases.",
                  tags: ["AWS / GCP / Azure", "Docker & K8s", "CI/CD Pipelines"]
                },
                {
                  title: "EduTech & Technical Training",
                  desc: "Enterprise developer bootcamps, technical certifications, and live cohort workshops preparing talent for modern cloud and AI roles.",
                  tags: ["Corporate Bootcamps", "Developer Upskilling", "Certifications"]
                }
              ].map((srv, idx) => (
                <div key={idx} className="elevate-card p-7 rounded-2xl border border-white/10 elevate-card-hover flex flex-col justify-between group">
                  <div>
                    <h4 className="text-xl font-bold text-white mb-3 group-hover:text-[#3fd0ff] transition-colors">{srv.title}</h4>
                    <p className="text-gray-400 text-xs leading-relaxed mb-5">{srv.desc}</p>
                  </div>
                  <div className="flex flex-wrap gap-1.5 pt-4 border-t border-white/10">
                    {srv.tags.map((t, tIdx) => (
                      <span key={tIdx} className="text-[10px] font-bold px-2 py-0.5 rounded bg-white/5 border border-white/10 text-gray-300">
                        {t}
                      </span>
                    ))}
                  </div>
                </div>
              ))}
            </div>
          </div>

          {/* ================= CATEGORY 02: NON-IT SERVICES & BPO ================= */}
          <div>
            <div className="flex items-center justify-between p-6 rounded-2xl bg-gradient-to-r from-[#3fd0ff]/15 to-[#16a6e0]/5 border border-[#3fd0ff]/30 mb-8 backdrop-blur-md">
              <div>
                <span className="text-xs font-bold uppercase tracking-wider text-[#3fd0ff] block mb-1">Category 02 • Healthcare &amp; Operations</span>
                <h3 className="text-2xl font-black text-white flex items-center">
                  <Headphones className="w-6 h-6 mr-2 text-[#3fd0ff]" /> Non-IT Services &amp; Healthcare BPO
                </h3>
              </div>
              <span className="hidden sm:inline-block text-xs font-semibold text-gray-300 bg-white/10 px-4 py-1.5 rounded-full border border-white/10">
                5 Specialized Domains
              </span>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
              {[
                {
                  title: "Medical Coding & Billing",
                  desc: "Comprehensive HIPAA-compliant Revenue Cycle Management (RCM), certified ICD-10-CM and CPT coding, and denial prevention.",
                  tags: ["HIPAA Compliant", "ICD-10 & CPT", "RCM Operations"]
                },
                {
                  title: "Call Recording & AR Calling",
                  desc: "Proactive Accounts Receivable (AR) insurance follow-up calls, patient billing resolution, and compliant call recording with QA scoring.",
                  tags: ["AR Follow-Up", "Denial Management", "QA Scoring"]
                },
                {
                  title: "TESS (Tele-Evaluation & Support)",
                  desc: "Specialized Tele-Evaluation & Support Services providing remote quality audits, customer satisfaction evaluation, and 24/7 helpdesk.",
                  tags: ["Remote Audits", "Customer Support", "Performance Telemetry"]
                }
              ].map((srv, idx) => (
                <div key={idx} className="elevate-card p-7 rounded-2xl border border-white/10 elevate-card-hover flex flex-col justify-between group">
                  <div>
                    <h4 className="text-xl font-bold text-white mb-3 group-hover:text-[#ff8a3d] transition-colors">{srv.title}</h4>
                    <p className="text-gray-400 text-xs leading-relaxed mb-5">{srv.desc}</p>
                  </div>
                  <div className="flex flex-wrap gap-1.5 pt-4 border-t border-white/10">
                    {srv.tags.map((t, tIdx) => (
                      <span key={tIdx} className="text-[10px] font-bold px-2 py-0.5 rounded bg-white/5 border border-white/10 text-gray-300">
                        {t}
                      </span>
                    ))}
                  </div>
                </div>
              ))}
            </div>
          </div>

        </div>
      </section>

      {/* ---------------- ELEVATEIQ CAREERS & AI JOB SEARCH ENGINE ---------------- */}
      <section id="careers" className="py-24 bg-gradient-to-b from-[#06091A] via-[#090e24] to-[#06091A] border-b border-white/10 relative">
        <div className="max-w-7xl mx-auto px-6">
          
          <div className="text-center max-w-3xl mx-auto mb-16">
            <span className="text-xs font-bold uppercase tracking-widest text-[#ff8a3d] block mb-2">ElevateIQ Careers</span>
            <h2 className="text-3xl sm:text-5xl font-black uppercase tracking-tight text-white mb-4">
              Explore Open Positions Across India <span className="text-[#ff8a3d]">&gt;</span>
            </h2>
            <p className="text-gray-400 text-sm leading-relaxed">
              Find your next career leap at ElevateIQ Soft Tech. Upload your resume to experience instant deterministic AI matching against our active requisitions.
            </p>
          </div>

          {/* Search and Filters */}
          <div className="elevate-card p-6 rounded-2xl mb-12 shadow-2xl border border-white/10">
            <div className="flex flex-col md:flex-row gap-4 mb-6">
              <div className="flex-1 relative">
                <Search className="w-5 h-5 text-gray-400 absolute left-4 top-1/2 -translate-y-1/2" />
                <input 
                  type="text" 
                  value={searchTerm}
                  onChange={(e) => setSearchTerm(e.target.value)}
                  placeholder="Search by skill, job title, or domain (e.g., Python, React, Medical Coding, AWS)..." 
                  className="w-full pl-12 pr-4 py-3.5 bg-black/50 border border-white/10 rounded-xl text-white placeholder-gray-500 focus:outline-none focus:border-[#3fd0ff] text-sm"
                />
              </div>
              <button 
                onClick={fetchJobs}
                className="px-6 py-3.5 bg-gradient-to-r from-[#ff8a3d] to-[#f2701c] text-white font-bold text-xs uppercase tracking-wider rounded-xl transition-all shadow-md"
              >
                Refresh Roles
              </button>
            </div>

            {/* Filter Pills */}
            <div className="flex flex-col lg:flex-row lg:items-center justify-between gap-4 pt-4 border-t border-white/10 text-xs">
              
              {/* Branch Locations */}
              <div className="flex items-center space-x-2 overflow-x-auto pb-2 lg:pb-0">
                <span className="text-gray-400 font-bold uppercase mr-1 flex items-center">
                  <MapPin className="w-3.5 h-3.5 mr-1 text-[#ff8a3d]" /> Hub:
                </span>
                {locations.map(loc => (
                  <button
                    key={loc}
                    onClick={() => setSelectedLocation(loc)}
                    className={`px-3 py-1.5 rounded-full font-semibold transition-all whitespace-nowrap ${
                      selectedLocation === loc 
                        ? 'bg-[#3fd0ff] text-black font-bold' 
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
                  <Briefcase className="w-3.5 h-3.5 mr-1 text-[#3fd0ff]" /> Domain:
                </span>
                {departments.map(dept => (
                  <button
                    key={dept}
                    onClick={() => setSelectedDept(dept)}
                    className={`px-3 py-1.5 rounded-full font-semibold transition-all whitespace-nowrap ${
                      selectedDept === dept 
                        ? 'bg-[#ff8a3d] text-white font-bold' 
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
                <p className="text-gray-400 mb-2">No active ElevateIQ positions match your filter criteria.</p>
                <button 
                  onClick={() => { setSearchTerm(''); setSelectedLocation('All'); setSelectedDept('All'); }}
                  className="text-xs text-[#3fd0ff] font-bold uppercase tracking-wider underline hover:text-cyan-300"
                >
                  Reset Filters
                </button>
              </div>
            ) : (
              filteredJobs.map(job => (
                <div 
                  key={job.id} 
                  className="elevate-card p-7 rounded-2xl border border-white/10 elevate-card-hover flex flex-col justify-between"
                >
                  <div>
                    <div className="flex items-start justify-between mb-4">
                      <div>
                        <span className="text-[11px] font-bold uppercase tracking-widest text-[#ff8a3d]">
                          {job.department} • ElevateIQ Soft Tech
                        </span>
                        <h3 className="text-xl font-bold text-white mt-1">{job.title}</h3>
                      </div>
                      <span className="text-xs bg-white/5 border border-white/10 px-3 py-1 rounded-full text-gray-300 font-medium">
                        {job.min_experience_years}+ Yrs
                      </span>
                    </div>

                    <p className="text-gray-400 text-xs leading-relaxed mb-5 line-clamp-2">
                      {job.description}
                    </p>

                    <div className="flex items-center text-xs text-gray-400 mb-5">
                      <MapPin className="w-3.5 h-3.5 text-[#3fd0ff] mr-1.5" />
                      <span>{job.location} Branch, India</span>
                      <span className="mx-2 text-gray-600">•</span>
                      <span>{job.education_requirement}</span>
                    </div>

                    {/* Skill Tags */}
                    <div className="flex flex-wrap gap-1.5 mb-6">
                      {job.required_skills && job.required_skills.map((skill, sIdx) => (
                        <span key={sIdx} className="text-[11px] font-semibold px-2.5 py-1 rounded bg-[#3fd0ff]/10 border border-[#3fd0ff]/30 text-[#3fd0ff]">
                          {skill}
                        </span>
                      ))}
                      {job.preferred_skills && job.preferred_skills.map((skill, sIdx) => (
                        <span key={sIdx} className="text-[11px] font-semibold px-2.5 py-1 rounded bg-white/5 border border-white/10 text-gray-400">
                          +{skill}
                        </span>
                      ))}
                    </div>
                  </div>

                  <div className="pt-4 border-t border-white/10 flex items-center justify-between">
                    <span className="text-xs text-gray-500 font-medium">{job.id}</span>
                    <button 
                      onClick={() => setApplyingJob(job)}
                      className="px-5 py-2.5 rounded-full bg-gradient-to-r from-[#ff8a3d] to-[#f2701c] hover:brightness-110 text-white font-bold text-xs uppercase tracking-wider transition-all shadow-[0_0_20px_rgba(255,138,61,0.3)] flex items-center"
                    >
                      Apply with AI Match <ChevronRight className="w-4 h-4 ml-1" />
                    </button>
                  </div>
                </div>
              ))
            )}
          </div>

        </div>
      </section>

      {/* ---------------- ELEVATEIQ BRANCHES & DELIVERY HUBS ---------------- */}
      <section id="branches" className="py-24 border-b border-white/10">
        <div className="max-w-7xl mx-auto px-6">
          <div className="text-center max-w-3xl mx-auto mb-16">
            <span className="text-xs font-bold uppercase tracking-widest text-[#3fd0ff] block mb-2">Our Locations</span>
            <h2 className="text-3xl sm:text-5xl font-black uppercase tracking-tight text-white mb-4">
              India Delivery Hubs &amp; Offices
            </h2>
            <p className="text-gray-400 text-sm leading-relaxed">
              Operating state-of-the-art facilities across South India to deliver continuous engineering and BPO excellence.
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            <div className="elevate-card p-8 rounded-2xl border border-white/10 elevate-card-hover">
              <div className="flex items-center space-x-3 mb-4">
                <div className="p-3 bg-[#ff8a3d]/15 border border-[#ff8a3d]/30 rounded-xl text-[#ff8a3d]">
                  <Building2 className="w-6 h-6" />
                </div>
                <div>
                  <h3 className="text-xl font-bold text-white">Chennai Branch</h3>
                  <span className="text-xs text-gray-400">Tamil Nadu</span>
                </div>
              </div>
              <p className="text-gray-300 text-xs leading-relaxed mb-4">
                Guindy / Little Mount, Chennai, Tamil Nadu - 600032, India.
              </p>
              <div className="text-[11px] font-semibold text-[#3fd0ff] flex items-center">
                <MapPin className="w-3.5 h-3.5 mr-1" /> Software Engineering &amp; Healthcare RCM Core
              </div>
            </div>

            <div className="elevate-card p-8 rounded-2xl border border-white/10 elevate-card-hover">
              <div className="flex items-center space-x-3 mb-4">
                <div className="p-3 bg-[#3fd0ff]/15 border border-[#3fd0ff]/30 rounded-xl text-[#3fd0ff]">
                  <Building2 className="w-6 h-6" />
                </div>
                <div>
                  <h3 className="text-xl font-bold text-white">Kochi Branch</h3>
                  <span className="text-xs text-gray-400">Kerala</span>
                </div>
              </div>
              <p className="text-gray-300 text-xs leading-relaxed mb-4">
                LR Towers, SJRRA 104, S Janatha Rd, Palarivattom, Kochi, Ernakulam, Kerala - 682025, India.
              </p>
              <div className="text-[11px] font-semibold text-[#ff8a3d] flex items-center">
                <MapPin className="w-3.5 h-3.5 mr-1" /> Cloud &amp; DevOps Center, AR Calling Operations
              </div>
            </div>

            <div className="elevate-card p-8 rounded-2xl border border-white/10 elevate-card-hover">
              <div className="flex items-center space-x-3 mb-4">
                <div className="p-3 bg-purple-500/15 border border-purple-500/30 rounded-xl text-purple-400">
                  <Building2 className="w-6 h-6" />
                </div>
                <div>
                  <h3 className="text-xl font-bold text-white">Narasaraopet Branch</h3>
                  <span className="text-xs text-gray-400">Andhra Pradesh</span>
                </div>
              </div>
              <p className="text-gray-300 text-xs leading-relaxed mb-4">
                Arundelpet, Narasaraopet, Andhra Pradesh - 522601, India.
              </p>
              <div className="text-[11px] font-semibold text-purple-300 flex items-center">
                <MapPin className="w-3.5 h-3.5 mr-1" /> Data Annotation, TESS Operations &amp; Training
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* ---------------- ELEVATEIQ CORPORATE FOOTER ---------------- */}
      <footer id="contact" className="bg-[#040612] py-16 text-gray-400 text-xs border-t border-white/10">
        <div className="max-w-7xl mx-auto px-6">
          <div className="grid grid-cols-1 md:grid-cols-4 gap-10 mb-14">
            
            <div className="md:col-span-2">
              <div className="flex items-center space-x-2 mb-3">
                <span className="text-2xl font-black text-white">Elevate<span className="text-[#3fd0ff]">IQ</span></span>
              </div>
              <p className="text-xs text-gray-400 leading-relaxed max-w-sm mb-6">
                ElevateIQ Soft Tech Private Limited is a premier technology &amp; business solutions provider delivering custom enterprise software, cloud infrastructure, medical billing, and AI talent intelligence.
              </p>
              <div className="space-y-2 text-xs">
                <div className="flex items-center text-gray-300">
                  <Mail className="w-3.5 h-3.5 mr-2 text-[#ff8a3d]" />
                  <a href="mailto:hr.support@elevateiq-softtech.com" className="hover:text-white transition-colors">
                    hr.support@elevateiq-softtech.com
                  </a>
                </div>
                <div className="flex items-center text-gray-300">
                  <Phone className="w-3.5 h-3.5 mr-2 text-[#3fd0ff]" />
                  <a href="tel:+916300855710" className="hover:text-white transition-colors">
                    +91-6300855710
                  </a>
                </div>
                <div className="flex items-center text-gray-400 pt-2">
                  <Globe className="w-3.5 h-3.5 mr-2 text-gray-500" />
                  <a href="https://elevateiq-softtech.com/" target="_blank" rel="noreferrer" className="hover:text-white transition-colors">
                    https://elevateiq-softtech.com/
                  </a>
                </div>
              </div>
            </div>

            <div>
              <h4 className="text-white font-bold uppercase tracking-wider mb-4">Enterprise Services</h4>
              <ul className="space-y-2 text-xs text-gray-400">
                <li><a href="#services" className="hover:text-white transition-colors">Software &amp; Web Engineering</a></li>
                <li><a href="#services" className="hover:text-white transition-colors">Data Harvesting &amp; Crawlers</a></li>
                <li><a href="#services" className="hover:text-white transition-colors">PDF Data Extraction &amp; IDP</a></li>
                <li><a href="#services" className="hover:text-white transition-colors">Cloud &amp; DevOps (AWS/K8s)</a></li>
                <li><a href="#services" className="hover:text-white transition-colors">Medical Coding &amp; AR Calling</a></li>
                <li><a href="#services" className="hover:text-white transition-colors">TESS Support Operations</a></li>
              </ul>
            </div>

            <div>
              <h4 className="text-white font-bold uppercase tracking-wider mb-4">Quick Links</h4>
              <ul className="space-y-2 text-xs text-gray-400">
                <li>
                  <a 
                    href="#about" 
                    onClick={(e) => { e.preventDefault(); document.getElementById('about')?.scrollIntoView({ behavior: 'smooth' }); }}
                    className="hover:text-white transition-colors cursor-pointer"
                  >
                    About ElevateIQ
                  </a>
                </li>
                <li>
                  <a 
                    href="#careers" 
                    onClick={(e) => { e.preventDefault(); document.getElementById('careers')?.scrollIntoView({ behavior: 'smooth' }); }}
                    className="hover:text-white transition-colors cursor-pointer"
                  >
                    Current Openings
                  </a>
                </li>
                <li>
                  <a 
                    href="#branches" 
                    onClick={(e) => { e.preventDefault(); document.getElementById('branches')?.scrollIntoView({ behavior: 'smooth' }); }}
                    className="hover:text-white transition-colors cursor-pointer"
                  >
                    Our Delivery Hubs
                  </a>
                </li>
                <li><a href="/login" className="hover:text-white transition-colors text-[#ff8a3d] font-bold">Recruiter AI Console</a></li>
              </ul>
            </div>

          </div>

          <div className="pt-8 border-t border-white/10 flex flex-col md:flex-row items-center justify-between text-gray-500 text-[11px]">
            <div>
              © 2026 ElevateIQ Soft Tech Pvt. Ltd. All Rights Reserved.
            </div>
            <div className="mt-4 md:mt-0 flex gap-6">
              <a href="https://elevateiq-softtech.com/" target="_blank" rel="noreferrer" className="hover:text-gray-400">elevateiq-softtech.com</a>
              <span>•</span>
              <span>Chennai • Kochi • Narasaraopet</span>
            </div>
          </div>
        </div>
      </footer>

      {/* ---------------- CANDIDATE APPLICATION MODAL ---------------- */}
      {applyingJob && (
        <div className="fixed inset-0 z-50 bg-black/80 backdrop-blur-md flex items-center justify-center p-4">
          <div className="bg-[#0e1426] border border-white/20 rounded-3xl max-w-2xl w-full p-8 relative shadow-[0_0_50px_rgba(63,208,255,0.25)] animate-fade-in-up">
            
            <button 
              onClick={closeModal}
              className="absolute top-6 right-6 text-gray-400 hover:text-white transition-colors p-2 rounded-full hover:bg-white/10"
            >
              <X className="w-5 h-5" />
            </button>

            {!matchResult ? (
              <div>
                <div className="mb-6">
                  <span className="text-xs font-bold uppercase tracking-widest text-[#ff8a3d]">ElevateIQ Talent Application</span>
                  <h3 className="text-2xl font-black uppercase text-white mt-1">
                    Apply for {applyingJob.title}
                  </h3>
                  <p className="text-gray-400 text-xs mt-1">
                    {applyingJob.location} Branch • {applyingJob.department}
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
                      placeholder="e.g. Divya Balaji" 
                      className="w-full px-4 py-3 bg-white/5 border border-white/15 rounded-xl text-white placeholder-gray-500 focus:outline-none focus:border-[#3fd0ff] text-sm"
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
                        placeholder="divya.balaji@example.in" 
                        className="w-full px-4 py-3 bg-white/5 border border-white/15 rounded-xl text-white placeholder-gray-500 focus:outline-none focus:border-[#3fd0ff] text-sm"
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
                        className="w-full px-4 py-3 bg-white/5 border border-white/15 rounded-xl text-white placeholder-gray-500 focus:outline-none focus:border-[#3fd0ff] text-sm"
                      />
                    </div>
                  </div>

                  {/* Resume Upload Box */}
                  <div>
                    <label className="block text-xs font-bold uppercase tracking-wider text-gray-300 mb-1.5">
                      Upload Resume (PDF / DOCX) *
                    </label>
                    <div className="border-2 border-dashed border-white/20 hover:border-[#3fd0ff] rounded-2xl p-6 text-center cursor-pointer transition-colors bg-white/[0.02]">
                      <input 
                        type="file" 
                        id="resumeUpload"
                        required
                        accept=".pdf,.docx"
                        onChange={e => setResumeFile(e.target.files[0])}
                        className="hidden" 
                      />
                      <label htmlFor="resumeUpload" className="cursor-pointer">
                        <FileUp className="w-10 h-10 text-[#3fd0ff] mx-auto mb-2" />
                        <span className="text-sm font-semibold text-white block">
                          {resumeFile ? resumeFile.name : "Click to select your resume file"}
                        </span>
                        <span className="text-xs text-gray-400 block mt-1">
                          Processed locally by ElevateIQ Neural Engine • Max 10MB
                        </span>
                      </label>
                    </div>
                  </div>

                  <div className="pt-2">
                    <button 
                      type="submit" 
                      disabled={submitting}
                      className="w-full py-4 rounded-xl bg-gradient-to-r from-[#ff8a3d] to-[#f2701c] hover:brightness-110 text-white font-bold text-xs uppercase tracking-wider transition-all duration-300 shadow-[0_0_25px_rgba(255,138,61,0.4)] disabled:opacity-50"
                    >
                      {submitting ? "Analyzing Resume with AI Engine..." : "Submit Application & Check Match Score >"}
                    </button>
                  </div>
                </form>
              </div>
            ) : (
              /* Instant AI Match Feedback Screen */
              <div className="text-center py-4">
                <div className="w-20 h-20 rounded-full bg-emerald-950/80 border-2 border-emerald-400 flex items-center justify-center mx-auto mb-6 text-emerald-400 shadow-[0_0_30px_rgba(52,211,153,0.3)]">
                  <CheckCircle className="w-10 h-10" />
                </div>

                <span className="text-xs font-bold uppercase tracking-widest text-[#3fd0ff] block mb-1">
                  ElevateIQ Talent Screening Result
                </span>
                <h3 className="text-3xl font-black text-white uppercase mb-2">
                  Application Logged!
                </h3>
                <p className="text-gray-300 text-sm max-w-md mx-auto mb-8">
                  Welcome, <strong className="text-white">{matchResult.candidate.name}</strong>. Your profile for <strong className="text-[#ff8a3d]">{matchResult.job.title}</strong> has been vectorized and stored in our candidate pipeline.
                </p>

                {/* Score Dial / Badge */}
                <div className="bg-white/5 border border-white/10 rounded-2xl p-6 max-w-md mx-auto mb-8 text-left">
                  <div className="flex items-center justify-between mb-4">
                    <span className="text-xs font-bold uppercase tracking-wider text-gray-400">Deterministic Match Score</span>
                    <span className="text-2xl font-black text-[#3fd0ff]">
                      {matchResult.application.match_score}%
                    </span>
                  </div>
                  
                  <div className="text-xs text-gray-400 mb-2 font-semibold">Matched Skills:</div>
                  <div className="flex flex-wrap gap-1.5">
                    {matchResult.candidate.skills && matchResult.candidate.skills.map((s, i) => (
                      <span key={i} className="px-2.5 py-1 rounded-full bg-[#ff8a3d]/20 border border-[#ff8a3d]/40 text-orange-200 text-xs font-medium">
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
                    Close
                  </button>
                  <button 
                    onClick={() => { closeModal(); navigate('/login'); }}
                    className="px-6 py-3 rounded-full bg-gradient-to-r from-[#ff8a3d] to-[#f2701c] text-white font-bold text-xs uppercase tracking-wider transition-all"
                  >
                    Open Recruiter Console &gt;
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

export default ElevateIQHome;
