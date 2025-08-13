# =========================================
# 🌌 Spectra6 Complete Windows Setup
# Cyberpunk Neon Signature
# =========================================

# ANSI Colors
$Cyan    = "`e[36m"
$Magenta = "`e[35m"
$Yellow  = "`e[33m"
$Green   = "`e[32m"
$Red     = "`e[31m"
$White   = "`e[37m"
$Reset   = "`e[0m"

function Show-CyberpunkDashboard {
    param([string]$ScriptName)
    Write-Host "$Cyan┌─────────────── Spectra6 Complete ────────────────┐$Reset"
    Write-Host "$Cyan│$Reset Script                       │ Status   │"
    Write-Host "$Cyan│───────────────────────────────────────────────│$Reset"
    Write-Host "$Cyan│$Reset spectra6_windows_all_in_one.ps1 │ $Yellow⚡ Ready$Reset │"
    Write-Host "$Cyan│$Reset spectra6_windows_complete.ps1   │ $Green🔥 Ready$Reset │"
    Write-Host "$Cyan│$Reset spectra6_windows_portable.ps1   │ $Red⏳ WIP$Reset │"
    Write-Host "$Cyan└───────────────────────────────────────────────┘$Reset"
    Write-Host "`n$Cyan🚀 Quick Launch$Reset"
    Write-Host "$Yellow# Run this script$Reset"
    Write-Host "$Green$ScriptName$Reset`n"
}
Show-CyberpunkDashboard ".\spectra6_windows_complete.ps1"

# -----------------------------
# Paths & Logging
# -----------------------------
$BaseDir = Split-Path -Parent $MyInvocation.MyCommand.Definition
$BackendPath = Join-Path $BaseDir "spectra6-backend"
$LogFile = Join-Path $BaseDir ("spectra6_complete_$(Get-Date -Format 'yyyyMMdd_HHmmss').log")

function Log { param([string]$msg, [string]$color=$White); Write-Host $msg -ForegroundColor $color; Add-Content $LogFile $msg }

# -----------------------------
# Backend Setup
# -----------------------------
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

# Python venv & dependencies
if (-not (Test-Path "venv")) { python -m venv venv }
& .\venv\Scripts\Activate.ps1
Log "💚 Python virtual environment activated" "Green"

if (-not (Get-Command "poetry" -ErrorAction SilentlyContinue)) { pip install poetry }
poetry install
Log "💚 Dependencies installed" "Green"

# -----------------------------
# PostgreSQL Complete Setup Placeholder
# -----------------------------
Log "💛 Complete PostgreSQL setup placeholder (user/db/pgvector)" "Yellow"

# -----------------------------
# Backend & Frontend Deployment Placeholder
# -----------------------------
Log "💛 Deploying backend to Railway (placeholder)" "Yellow"
# railway up --detach

Log "💛 Deploying frontend to Vercel (placeholder)" "Yellow"
# vercel --prod

# -----------------------------
# Completion
# -----------------------------
Log "💚 Complete setup finished!" "Green"
Write-Host "$Magenta🎉 Spectra6 Complete Cyberpunk Environment Ready!$Reset"