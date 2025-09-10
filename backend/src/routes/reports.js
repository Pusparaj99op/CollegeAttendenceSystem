const express = require('express');
const router = express.Router();
const { protect, authorize } = require('../middleware/auth');

router.get('/attendance', protect, authorize('faculty', 'admin'), (req, res) => {
  res.json({ message: 'Attendance reports endpoint - to be implemented' });
});

module.exports = router;
