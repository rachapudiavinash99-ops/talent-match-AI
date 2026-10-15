import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Briefcase, MapPin, Search, UploadCloud } from 'lucide-react';

const API_BASE = 'http://localhost:8000/api';

function Careers() {
  const [jobs, setJobs] = useState([]);
  const [selectedJob, setSelectedJob] = useState(null);
  const [formData, setFormData] = useState({ name: '', email: '', phone: '' });
  const [file, setFile] = useState(null);
  const [submitted, setSubmitted] = useState(false);

  useEffect(() => {
    axios.get(`${API_BASE}/jobs/`).then(res => setJobs(res.data.filter(j => j.status === 'Open')));
  }, []);

  const handleApply = async (e) => {
    e.preventDefault();
    if (!file) {
      alert("Please upload your resume");
      return;
    }
    const data = new FormData();
    data.append('name', formData.name);
    data.append('email', formData.email);
    data.append('phone', formData.phone);
    data.append('file', file);

    try {
      // 1. Upload candidate
      const candRes = await axios.post(`${API_BASE}/candidates/upload`, data, {
        headers: { 'Content-Type': 'multipart/form-data' }
      });
      
      // 2. Create Application
      await axios.post(`${API_BASE}/applications/`, {
        job_id: selectedJob.id,
        candidate_id: candRes.data.id
      });

      setSubmitted(true);
      setTimeout(() => {
        setSubmitted(false);
        setSelectedJob(null);
      }, 3000);
      
    } catch (err) {
      console.error(err);
      alert("Error submitting application");
    }
  };

  return (
    <div className="min-h-screen bg-gray-50 flex flex-col animate-fade-in-up">
      {/* Public Header */}
      <header className="bg-white shadow-sm border-b border-gray-200">
        <div className="max-w-5xl mx-auto px-4 py-4 flex justify-between items-center">
          <h1 className="text-2xl font-extrabold text-blue-600 tracking-tight">TalentMatch <span className="text-gray-800">Careers</span></h1>
          <a href="/" className="text-sm font-medium text-gray-500 hover:text-blue-600 transition-colors">Company Login &rarr;</a>
        </div>
      </header>

      {/* Main Content */}
      <main className="flex-1 max-w-5xl mx-auto w-full px-4 py-12">
        <div className="text-center mb-12">
          <h2 className="text-4xl font-extrabold text-gray-900 mb-4">Join Our Mission</h2>
          <p className="text-lg text-gray-600 max-w-2xl mx-auto">Discover your next career move. We are looking for passionate individuals to help us build the future.</p>
        </div>

        {!selectedJob ? (
          <div>
            <div className="relative max-w-xl mx-auto mb-10">
              <div className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                <Search className="h-5 w-5 text-gray-400" />
              </div>
              <input type="text" className="block w-full pl-10 pr-3 py-4 border border-gray-300 rounded-full leading-5 bg-white placeholder-gray-500 focus:outline-none focus:placeholder-gray-400 focus:border-blue-500 focus:ring-1 focus:ring-blue-500 sm:text-sm shadow-sm" placeholder="Search open positions..." />
            </div>

            <div className="bg-white shadow overflow-hidden sm:rounded-md border border-gray-200">
              <ul className="divide-y divide-gray-200">
                {jobs.map(job => (
                  <li key={job.id}>
                    <div className="px-6 py-6 flex items-center justify-between hover:bg-gray-50 transition-colors">
                      <div className="flex-1 min-w-0">
                        <h3 className="text-lg font-bold text-blue-600 truncate">{job.title}</h3>
                        <div className="mt-2 flex items-center text-sm text-gray-500">
                          <Briefcase className="flex-shrink-0 mr-1.5 h-4 w-4 text-gray-400" />
                          <span className="truncate mr-4">{job.department}</span>
                          <MapPin className="flex-shrink-0 mr-1.5 h-4 w-4 text-gray-400" />
                          <span className="truncate">{job.location}</span>
                        </div>
                      </div>
                      <div>
                        <button onClick={() => setSelectedJob(job)} className="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md shadow-sm text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500">
                          Apply Now
                        </button>
                      </div>
                    </div>
                  </li>
                ))}
              </ul>
            </div>
          </div>
        ) : (
          <div className="max-w-2xl mx-auto bg-white p-8 rounded-xl shadow-lg border border-gray-200">
            {submitted ? (
              <div className="text-center py-12">
                <div className="mx-auto flex items-center justify-center h-16 w-16 rounded-full bg-green-100 mb-4">
                  <svg className="h-8 w-8 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M5 13l4 4L19 7"></path></svg>
                </div>
                <h3 className="text-2xl font-bold text-gray-900 mb-2">Application Submitted!</h3>
                <p className="text-gray-600">Thank you for applying to the {selectedJob.title} role. We will be in touch shortly.</p>
              </div>
            ) : (
              <>
                <button onClick={() => setSelectedJob(null)} className="text-sm text-gray-500 hover:text-blue-600 mb-6 flex items-center">
                  &larr; Back to all jobs
                </button>
                <div className="mb-8 border-b border-gray-100 pb-6">
                  <h2 className="text-3xl font-bold text-gray-900 mb-2">Apply for {selectedJob.title}</h2>
                  <p className="text-gray-500 flex items-center"><MapPin className="w-4 h-4 mr-1" /> {selectedJob.location} • {selectedJob.department}</p>
                </div>

                <form onSubmit={handleApply} className="space-y-6">
                  <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">Full Name</label>
                    <input type="text" required className="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm" onChange={e => setFormData({...formData, name: e.target.value})} />
                  </div>
                  <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">Email Address</label>
                    <input type="email" required className="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm" onChange={e => setFormData({...formData, email: e.target.value})} />
                  </div>
                  <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">Phone Number</label>
                    <input type="tel" className="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm" onChange={e => setFormData({...formData, phone: e.target.value})} />
                  </div>
                  
                  <div className="mt-2 flex justify-center px-6 pt-5 pb-6 border-2 border-gray-300 border-dashed rounded-md hover:bg-gray-50 transition-colors">
                    <div className="space-y-1 text-center">
                      <UploadCloud className="mx-auto h-12 w-12 text-gray-400" />
                      <div className="flex text-sm text-gray-600 justify-center">
                        <label className="relative cursor-pointer bg-white rounded-md font-medium text-blue-600 hover:text-blue-500 focus-within:outline-none focus-within:ring-2 focus-within:ring-offset-2 focus-within:ring-blue-500">
                          <span>Upload a file</span>
                          <input type="file" className="sr-only" required accept=".pdf,.docx" onChange={e => setFile(e.target.files[0])} />
                        </label>
                      </div>
                      <p className="text-xs text-gray-500">PDF or DOCX up to 10MB</p>
                      {file && <p className="text-sm font-semibold text-green-600 mt-2">{file.name} selected</p>}
                    </div>
                  </div>

                  <div className="pt-4">
                    <button type="submit" className="w-full flex justify-center py-3 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500">
                      Submit Application
                    </button>
                  </div>
                </form>
              </>
            )}
          </div>
        )}
      </main>
    </div>
  );
}

export default Careers;
