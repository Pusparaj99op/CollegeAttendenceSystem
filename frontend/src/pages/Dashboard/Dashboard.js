import React from 'react';
import { Box, Typography } from '@mui/material';

const Dashboard = () => {
  return (
    <Box>
      <Typography variant="h4" component="h1" gutterBottom>
        Dashboard
      </Typography>
      <Typography variant="body1">
        Welcome to the Atomic College Attendance System Dashboard.
      </Typography>
    </Box>
  );
};

export default Dashboard;
