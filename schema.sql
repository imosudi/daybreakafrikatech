-- ============================================
-- Daybreak Afrika Technologies
-- Database Schema
-- SQLite3
-- ============================================

PRAGMA foreign_keys = ON;

-- --------------------------------------------
-- Inquiries Table
-- Stores assessment-driven client requests
-- --------------------------------------------
CREATE TABLE IF NOT EXISTS inquiries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_name TEXT,
    contact_person TEXT,
    email TEXT,
    phone TEXT,
    business_need TEXT NOT NULL,
    recommended_solution TEXT NOT NULL,
    submitted_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- --------------------------------------------
-- Portfolio Table
-- Stores completed or reference projects
-- --------------------------------------------
CREATE TABLE IF NOT EXISTS portfolio (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_name TEXT NOT NULL,
    project_title TEXT NOT NULL,
    description TEXT,
    technologies TEXT,
    impact_summary TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
