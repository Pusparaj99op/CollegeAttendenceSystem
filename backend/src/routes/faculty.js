const express = require('express');
const router = express.Router();
const { protect, authorize } = require('../middleware/auth');

/**
 * @swagger
 * /api/v1/faculty/profile:
 *   get:
 *     summary: Get faculty profile
 *     tags: [Faculty]
 *     security:
 *       - BearerAuth: []
 *     responses:
 *       200:
 *         description: Faculty profile retrieved successfully
 */
router.get('/profile', protect, authorize('faculty', 'admin'), (req, res) => {
  res.json({ 
    message: 'Faculty profile endpoint - to be implemented',
    user: req.user
  });
});

/**
 * @swagger
 * /api/v1/faculty/classes:
 *   get:
 *     summary: Get faculty classes
 *     tags: [Faculty]
 *     security:
 *       - BearerAuth: []
 *     responses:
 *       200:
 *         description: Faculty classes retrieved successfully
 */
router.get('/classes', protect, authorize('faculty', 'admin'), (req, res) => {
  res.json({ message: 'Faculty classes endpoint - to be implemented' });
});

module.exports = router;
