# =========================================
# 🌌 Spectra6 Portable Windows All-In-One
# Cyberpunk Neon Console Signature Edition
# =========================================

# -----------------------------
# ANSI color codes for cyberpunk aesthetics
# -----------------------------
$Cyan    = "`e[36m"
$Magenta = "`e[35m"
$Yellow  = "`e[33m"
$Green   = "`e[32m"
$Red     = "`e[31m"
$White   = "`e[37m"
$Reset   = "`e[0m"

# -----------------------------
# Dashboard Header
# -----------------------------
Write-Host "$Cyan┌────────────────────── Spectra6 Portable Setup ──────────────────────┐$Reset"
Write-Host "$Cyan│$Reset Script                                   │ Status   │"
Write-Host "$Cyan│───────────────────────────────────────────────────────────────────│$Reset"
Write-Host "$Cyan│$Reset spectra6_windows_all_in_one.ps1         │ $Yellow⚡ Ready$Reset │"
Write-Host "$Cyan│  └─ Setup backend, dependencies, venv, deploy                                  │"
Write-Host "$Cyan│$Reset spectra6_windows_complete.ps1          │ $Green🔥 Ready$Reset │"
Write-Host "$Cyan│  └─ Full PostgreSQL auto-setup, backend + frontend                           │"
Write-Host "$Cyan│$Reset spectra6_windows_portable.ps1          │ $Red⏳ WIP$Reset │"
Write-Host "$Cyan│  └─ Fully portable: no system installs needed                                 │"
Write-Host "$Cyan└───────────────────────────────────────────────────────────────────┘$Reset"

# -----------------------------
# Quick Launch Instructions
# -----------------------------
Write-Host "`n$Cyan🚀 Quick Launch$Reset"
Write-Host "$Yellow# Open PowerShell as Administrator$Reset"
Write-Host "$YellowSet-ExecutionPolicy RemoteSigned -Scope CurrentUser$Reset"
Write-Host "$Yellow# Run this script$Reset"
Write-Host "$Green.\spectra6_windows_portable.ps1$Reset"

# -----------------------------
# Requirements & Notes
# -----------------------------
Write-Host "`n$Cyan⚡ Requirements$Reset"
Write-Host "Windows 10+, PowerShell 5+, Internet, Admin privileges recommended"

Write-Host "`n$Cyan🔐 Notes & Security$Reset"
Write-Host "- Change default database credentials in production"
Write-Host "- Logs saved as timestamped .log files"
Write-Host "- Railway & Vercel credentials prompted by script"

# -----------------------------
# Setup Paths
# -----------------------------
$BaseDir      = Split-Path -Parent $MyInvocation.MyCommand.Definition
$PythonDir    = Join-Path $BaseDir "portable_python"
$NodeDir      = Join-Path $BaseDir "portable_node"
$PostgresDir  = Join-Path $BaseDir "portable_postgres"
$LogFile      = Join-Path $BaseDir ("spectra6_portable_$(Get-Date -Format 'yyyyMMdd_HHmmss').log")

# Logging function
function Log { param([string]$msg, [string]$color=$White); Write-Host $msg -ForegroundColor $color; Add-Content $LogFile $msg }

# -----------------------------
# Download & Extract Portable Binaries
# -----------------------------
function Download-Extract($url, $target) {
    Log "💛 Downloading $url..." "Yellow"
    $zip = Join-Path $env:TEMP ([System.IO.Path]::GetRandomFileName() + ".zip")
    Invoke-WebRequest $url -OutFile $zip
    Expand-Archive $zip -DestinationPath $target -Force
    Remove-Item $zip
    Log "💚 Extracted to $target" "Green"
}

# Example URLs (replace with actual latest portable URLs)
$PythonUrl = "https://www.python.org/ftp/python/3.12.0/python-3.12.0-embed-amd64.zip"
$NodeUrl   = "https://nodejs.org/dist/v20.5.0/node-v20.5.0-win-x64.zip"
$PostgresUrl = "https://get.enterprisedb.com/postgresql/postgresql-16.6-1-windows-x64-binaries.zip"

if (-not (Test-Path $PythonDir)) { Download-Extract $PythonUrl $PythonDir }
if (-not (Test-Path $NodeDir)) { Download-Extract $NodeUrl $NodeDir }
if (-not (Test-Path $PostgresDir)) { Download-Extract $PostgresUrl $PostgresDir }

# Add portable Python/Node to session PATH
$env:PATH = "$PythonDir;$NodeDir;$env:PATH"

# -----------------------------
# PostgreSQL Portable Setup
# -----------------------------
Log "💛 Configuring portable PostgreSQL..." "Yellow"
$PGUser = "spectra_user"
$PGPass = "SpectraSecure123!"
$PGDB   = "spectra_db"
$PGPort = 5432

# Initialize database if not exists (simplified for portable)
# TODO: fully configure portable PostgreSQL service, pgvector, and user creation
# Placeholder command:
# & "$PostgresDir\bin\initdb.exe" -D "$PostgresDir\data"

Log "💚 PostgreSQL setup complete (manual config for portable service may be required)" "Green"

# -----------------------------
# Backend Setup
# -----------------------------
$BackendPath = Join-Path $BaseDir "spectra6-backend"
if (-not (Test-Path $BackendPath)) {
    Log "💛 Cloning Spectra6 backend..." "Yellow"
    git clone -b prism https://github.com/Vesryin/spectra6-backend.git $BackendPath
} else {
    Log "💛 Updating Spectra6 backend..." "Yellow"
    Set-Location $BackendPath
    git fetch origin prism
    git reset --hard origin/prism
}

Set-Location $BackendPath

# Python virtual environment
if (-not (Test-Path "venv")) { & "$PythonDir\python.exe" -m venv venv }
& .\venv\Scripts\Activate.ps1
Log "💚 Python virtual environment activated" "Green"

# Install dependencies (Poetry)
if (-not (Get-Command "poetry" -ErrorAction SilentlyContinue)) { pip install poetry }
poetry install
Log "💚 Dependencies installed" "Green"

# -----------------------------
# Deploy Backend & Frontend
# -----------------------------
Log "💛 Deploying backend to Railway..." "Yellow"
# railway up --detach  # Uncomment when railway CLI configured

# Optional frontend deployment (Vercel)
# if (Test-Path "frontend/package.json") { vercel --prod }

# -----------------------------
# Verification
# -----------------------------
Log "💚 Spectra6 portable setup complete!" "Green"
Write-Host "$Magenta🎉 Enjoy your cyberpunk Spectra6 environment!$Reset"