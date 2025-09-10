const express = require('express');
const router = express.Router();
const { protect, authorize } = require('../middleware/auth');

router.post('/generate', protect, authorize('faculty', 'admin'), (req, res) => {
  res.json({ message: 'Generate QR code endpoint - to be implemented' });
});

router.post('/validate', protect, (req, res) => {
  res.json({ message: 'Validate QR code endpoint - to be implemented' });
});

module.exports = router;
