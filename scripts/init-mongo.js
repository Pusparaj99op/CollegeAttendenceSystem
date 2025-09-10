db = db.getSiblingDB('atomic_attendance');

db.createUser({
  user: 'attendance_user',
  pwd: 'attendance_password',
  roles: [
    { role: 'readWrite', db: 'atomic_attendance' }
  ]
});

// Create collections
db.createCollection('users');
db.createCollection('students');
db.createCollection('faculty');
db.createCollection('attendance');
db.createCollection('sessions');
db.createCollection('courses');
db.createCollection('departments');

// Create admin user
db.users.insertOne({
  name: 'Admin User',
  email: 'admin@example.com',
  password: '$2a$10$gy5BWVfxCB.3WHaO9AX3qe4cO5EMFJLllZPUj01CNnXnrwkNBEZlm', // hashed 'adminpassword'
  role: 'admin',
  createdAt: new Date(),
  updatedAt: new Date()
});
