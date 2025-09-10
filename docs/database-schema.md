# ============================================================================
# ATOMIC COLLEGE ATTENDANCE SYSTEM - DATABASE SCHEMA
# ============================================================================
# This file defines the complete database schema for MongoDB collections
# and MySQL tables (dual database support)
# ============================================================================

# ============================================================================
# MONGODB COLLECTIONS SCHEMA
# ============================================================================

# Users Collection (Faculty & Admin)
users:
  _id: ObjectId (Primary Key)
  employeeId: String (Unique, Required) # Employee ID
  name: String (Required)
  email: String (Unique, Required)
  password: String (Hashed, Required)
  role: String (Enum: ['faculty', 'admin', 'super_admin'])
  department: String (Required)
  phone: String
  profileImage: String (URL)
  biometricTemplates: Array
    - type: String (Enum: ['fingerprint', 'face', 'iris'])
    - template: String (Encrypted biometric template)
    - registeredAt: Date
  isActive: Boolean (Default: true)
  lastLogin: Date
  createdAt: Date (Default: Now)
  updatedAt: Date (Default: Now)
  permissions: Array[String]

# Students Collection
students:
  _id: ObjectId (Primary Key)
  rollNumber: String (Unique, Required)
  name: String (Required)
  email: String (Unique, Required)
  phone: String
  department: String (Required)
  year: Number (Required)
  section: String
  batch: String
  profileImage: String (URL)
  biometricTemplates: Array
    - type: String (Enum: ['fingerprint', 'face', 'iris'])
    - template: String (Encrypted biometric template)
    - registeredAt: Date
    - quality: Number (0-100)
  parentContact: Object
    - name: String
    - phone: String
    - email: String
    - relation: String
  address: Object
    - street: String
    - city: String
    - state: String
    - zipCode: String
    - country: String
  isActive: Boolean (Default: true)
  admissionDate: Date
  createdAt: Date (Default: Now)
  updatedAt: Date (Default: Now)

# Classes Collection
classes:
  _id: ObjectId (Primary Key)
  name: String (Required)
  code: String (Unique, Required)
  department: String (Required)
  semester: String (Required)
  academicYear: String (Required)
  facultyId: ObjectId (References: users._id)
  students: Array[ObjectId] (References: students._id)
  schedule: Array
    - dayOfWeek: Number (0-6, 0=Sunday)
    - startTime: String (HH:MM format)
    - endTime: String (HH:MM format)
    - classroomId: ObjectId (References: classrooms._id)
  credits: Number
  description: String
  isActive: Boolean (Default: true)
  createdAt: Date (Default: Now)
  updatedAt: Date (Default: Now)

# Classrooms Collection
classrooms:
  _id: ObjectId (Primary Key)
  name: String (Required)
  building: String (Required)
  floor: Number
  capacity: Number
  type: String (Enum: ['lecture', 'lab', 'seminar', 'auditorium'])
  location: Object
    - latitude: Number (Required)
    - longitude: Number (Required)
    - radius: Number (Default: 10) # Geofence radius in meters
  qrCode: String (Fixed QR code embedded in classroom)
  wifiSSID: String (Classroom-specific WiFi)
  beacons: Array
    - beaconId: String
    - uuid: String
    - major: Number
    - minor: Number
  facilities: Array[String]
  isActive: Boolean (Default: true)
  createdAt: Date (Default: Now)
  updatedAt: Date (Default: Now)

# Attendance Sessions Collection
attendance_sessions:
  _id: ObjectId (Primary Key)
  sessionId: String (Unique, Required)
  classId: ObjectId (References: classes._id, Required)
  facultyId: ObjectId (References: users._id, Required)
  classroomId: ObjectId (References: classrooms._id, Required)
  startTime: Date (Required)
  endTime: Date
  plannedDuration: Number # Duration in minutes
  status: String (Enum: ['active', 'ended', 'cancelled'], Default: 'active')
  attendanceMethod: Array[String] (Enum: ['qr_code', 'biometric', 'manual'])
  facultyLocation: Object
    - latitude: Number
    - longitude: Number
    - accuracy: Number
    - timestamp: Date
  sessionSettings: Object
    - qrRefreshInterval: Number (Default: 10) # seconds
    - geofenceRadius: Number (Default: 10) # meters
    - allowLateEntry: Boolean (Default: false)
    - lateEntryGracePeriod: Number # minutes
  totalStudents: Number
  studentsPresent: Number (Default: 0)
  blockchain: Object
    - transactionHash: String
    - blockNumber: Number
    - confirmed: Boolean (Default: false)
  createdAt: Date (Default: Now)
  updatedAt: Date (Default: Now)

# Attendance Records Collection
attendance_records:
  _id: ObjectId (Primary Key)
  sessionId: ObjectId (References: attendance_sessions._id, Required)
  studentId: ObjectId (References: students._id, Required)
  classId: ObjectId (References: classes._id, Required)
  facultyId: ObjectId (References: users._id, Required)
  status: String (Enum: ['present', 'absent', 'late', 'review'], Required)
  markingMethod: String (Enum: ['qr_code', 'biometric', 'manual'], Required)
  markingTime: Date (Required)
  verification: Object
    - qrCode: String
    - biometricMatch: Number # Confidence score 0-100
    - locationAccuracy: Number
    - deviceFingerprint: String
  location: Object
    - latitude: Number
    - longitude: Number
    - accuracy: Number
    - timestamp: Date
  deviceInfo: Object
    - userAgent: String
    - ipAddress: String
    - deviceId: String
    - platform: String
  blockchain: Object
    - transactionHash: String
    - blockNumber: Number
    - confirmed: Boolean (Default: false)
  review: Object
    - flagged: Boolean (Default: false)
    - reason: String
    - reviewedBy: ObjectId (References: users._id)
    - reviewedAt: Date
    - resolved: Boolean (Default: false)
  createdAt: Date (Default: Now)
  updatedAt: Date (Default: Now)

# Dynamic QR Codes Collection
qr_codes:
  _id: ObjectId (Primary Key)
  code: String (Unique, Required)
  sessionId: ObjectId (References: attendance_sessions._id, Required)
  classId: ObjectId (References: classes._id, Required)
  expiresAt: Date (Required)
  isUsed: Boolean (Default: false)
  usedBy: ObjectId (References: students._id)
  encryptionKey: String
  generatedAt: Date (Default: Now)
  metadata: Object
    - sequence: Number
    - location: Object
      - latitude: Number
      - longitude: Number
    - challenge: String # Anti-replay token

# Biometric Verification Logs Collection
biometric_logs:
  _id: ObjectId (Primary Key)
  userId: ObjectId (References: users._id OR students._id, Required)
  userType: String (Enum: ['faculty', 'student'], Required)
  sessionId: ObjectId (References: attendance_sessions._id)
  biometricType: String (Enum: ['fingerprint', 'face', 'iris'], Required)
  verificationResult: Object
    - matched: Boolean
    - confidence: Number (0-100)
    - quality: Number (0-100)
    - liveness: Boolean
  processingTime: Number # milliseconds
  deviceInfo: Object
    - deviceId: String
    - model: String
    - sdkVersion: String
  location: Object
    - latitude: Number
    - longitude: Number
    - accuracy: Number
  createdAt: Date (Default: Now)

# System Audit Logs Collection
audit_logs:
  _id: ObjectId (Primary Key)
  action: String (Required)
  entity: String (Required) # Table/Collection name
  entityId: String (Required)
  userId: ObjectId (References: users._id)
  userType: String (Enum: ['faculty', 'student', 'admin'])
  changes: Object # What was changed
  ipAddress: String
  userAgent: String
  location: Object
    - latitude: Number
    - longitude: Number
  severity: String (Enum: ['low', 'medium', 'high', 'critical'])
  category: String (Enum: ['auth', 'attendance', 'admin', 'security'])
  success: Boolean
  errorMessage: String
  createdAt: Date (Default: Now)

# Notifications Collection
notifications:
  _id: ObjectId (Primary Key)
  recipientId: ObjectId (Required) # Can reference users or students
  recipientType: String (Enum: ['faculty', 'student', 'parent'], Required)
  type: String (Enum: ['attendance_alert', 'session_start', 'system_alert'], Required)
  title: String (Required)
  message: String (Required)
  data: Object # Additional notification data
  channels: Array[String] (Enum: ['app', 'email', 'sms', 'push'])
  status: String (Enum: ['pending', 'sent', 'delivered', 'failed'], Default: 'pending')
  priority: String (Enum: ['low', 'normal', 'high', 'urgent'], Default: 'normal')
  readAt: Date
  sentAt: Date
  deliveredAt: Date
  expiresAt: Date
  createdAt: Date (Default: Now)

# System Configuration Collection
system_config:
  _id: ObjectId (Primary Key)
  key: String (Unique, Required)
  value: Mixed (Required)
  type: String (Enum: ['string', 'number', 'boolean', 'object', 'array'], Required)
  description: String
  category: String (Enum: ['security', 'biometric', 'qr_code', 'geolocation'])
  editable: Boolean (Default: true)
  lastModified: Object
    - userId: ObjectId (References: users._id)
    - timestamp: Date
  createdAt: Date (Default: Now)
  updatedAt: Date (Default: Now)

# ============================================================================
# INDEXES FOR PERFORMANCE OPTIMIZATION
# ============================================================================

# Users Collection Indexes
users_indexes:
  - { employeeId: 1 } # Unique
  - { email: 1 } # Unique
  - { role: 1, isActive: 1 }
  - { department: 1 }

# Students Collection Indexes
students_indexes:
  - { rollNumber: 1 } # Unique
  - { email: 1 } # Unique
  - { department: 1, year: 1, section: 1 }
  - { isActive: 1 }

# Classes Collection Indexes
classes_indexes:
  - { code: 1 } # Unique
  - { facultyId: 1 }
  - { department: 1, semester: 1, academicYear: 1 }
  - { students: 1 }

# Attendance Sessions Collection Indexes
attendance_sessions_indexes:
  - { sessionId: 1 } # Unique
  - { classId: 1, startTime: -1 }
  - { facultyId: 1, startTime: -1 }
  - { status: 1 }
  - { startTime: -1 }

# Attendance Records Collection Indexes
attendance_records_indexes:
  - { sessionId: 1, studentId: 1 } # Compound unique
  - { studentId: 1, markingTime: -1 }
  - { classId: 1, markingTime: -1 }
  - { status: 1 }
  - { "review.flagged": 1 }
  - { createdAt: -1 }

# QR Codes Collection Indexes
qr_codes_indexes:
  - { code: 1 } # Unique
  - { sessionId: 1 }
  - { expiresAt: 1 } # TTL index
  - { isUsed: 1 }

# Biometric Logs Collection Indexes
biometric_logs_indexes:
  - { userId: 1, userType: 1, createdAt: -1 }
  - { sessionId: 1 }
  - { createdAt: -1 } # TTL index (optional, for log retention)

# Audit Logs Collection Indexes
audit_logs_indexes:
  - { userId: 1, createdAt: -1 }
  - { entity: 1, entityId: 1, createdAt: -1 }
  - { action: 1, createdAt: -1 }
  - { severity: 1, createdAt: -1 }
  - { category: 1, createdAt: -1 }
  - { createdAt: -1 } # TTL index (for log retention)

# ============================================================================
# DATA VALIDATION RULES
# ============================================================================

validation_rules:
  users:
    - employeeId: /^[A-Z]{2}[0-9]{6}$/ # Format: AB123456
    - email: Valid email format
    - password: Minimum 8 characters, at least 1 uppercase, 1 lowercase, 1 number
    - phone: Valid phone number format

  students:
    - rollNumber: /^[0-9]{4}[A-Z]{2}[0-9]{4}$/ # Format: 2023CS1001
    - email: Valid email format
    - year: Range 1-4
    - phone: Valid phone number format

  classes:
    - code: /^[A-Z]{2}[0-9]{3}$/ # Format: CS101
    - semester: Enum ['Spring', 'Summer', 'Fall', 'Winter']
    - academicYear: /^[0-9]{4}-[0-9]{4}$/ # Format: 2023-2024

  attendance_records:
    - markingTime: Must be within session start and end time
    - location: Must be within classroom geofence
    - biometricMatch: Range 0-100

# ============================================================================
# BACKUP AND MAINTENANCE PROCEDURES
# ============================================================================

backup_strategy:
  frequency: Daily at 2:00 AM
  retention: 30 days
  compression: gzip
  encryption: AES-256
  storage: 
    - Local: /backups/mongodb/
    - Cloud: AWS S3 bucket
  verification: Automated restore testing weekly

maintenance_tasks:
  - Index optimization: Weekly
  - Log cleanup: Daily (logs older than 90 days)
  - QR code cleanup: Hourly (expired codes)
  - Session cleanup: Daily (ended sessions older than 30 days)
  - Notification cleanup: Weekly (delivered notifications older than 30 days)