import React from 'react';

// Destructuring props for clean access to job data
const JobCard = ({ job }) => {
    // Function to handle the apply button click
    const handleApply = () => {
        alert(`Application initiated for ${job.title} at ${job.company_name}`);
    };

    return (
        <div style={{ border: '1px solid #ddd', padding: '15px', margin: '10px', borderRadius: '8px' }}>
            <h3>{job.title}</h3>
            <h4>{job.company_name}</h4>
            <p>{job.description.substring(0, 100)}...</p> {/* Show a brief summary */}
            <button onClick={handleApply}>Apply</button>
        </div>
    );
};

export default JobCard; 