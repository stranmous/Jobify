import React, { useState, useEffect } from 'react';
import axios from 'axios';
import Header from './components/Header';
import Footer from './components/Footer';
import JobCard from './components/JobCard';
import './App.css'; // For styling

function App() {
    const [jobs, setJobs] = useState([]); // State to hold the list of jobs

    // useEffect hook to fetch data when the component mounts
    useEffect(() => {
        const fetchJobs = async () => {
            try {
                // Fetch data from the Django backend
                const response = await axios.get('http://127.0.0.1:8000/api/jobs/');
                setJobs(response.data); // Update state with the fetched jobs
            } catch (error) {
                console.error("Error fetching jobs:", error);
            }
        };

        fetchJobs();
    }, []); // Empty array ensures this runs only once

    return (
        <>
            <div className="sidebar">
                <Header />
            </div>
            <div className="container">
                <main>
                    <h2>Available Jobs</h2>
                    <div className="job-grid">
                        {/* Loop through the jobs state and render a JobCard for each one */}
                        {jobs.map(job => (
                            <JobCard key={job.id} job={job} />
                        ))}
                    </div>
                </main>
            </div>
        </>
    );
}

export default App;
