const express = require('express');
const router = express.Router();
const { protect, authorize } = require('../middleware/auth');

router.get('/', protect, authorize('faculty', 'admin'), (req, res) => {
  res.json({ message: 'Students endpoint - to be implemented' });
});

module.exports = router;
