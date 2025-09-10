const express = require('express');
const router = express.Router();
const { protect } = require('../middleware/auth');

router.post('/verify', protect, (req, res) => {
  res.json({ message: 'Biometric verification endpoint - to be implemented' });
});

router.post('/register', protect, (req, res) => {
  res.json({ message: 'Biometric registration endpoint - to be implemented' });
});

module.exports = router;
