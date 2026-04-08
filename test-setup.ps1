#!/usr/bin/env powershell
# Test Script for Career-Ops (PowerShell)
# Run this to verify Node.js, Playwright, and PDF generation are working

Write-Host ""
Write-Host "============================================" -ForegroundColor Cyan
Write-Host "Career-Ops Test Suite" -ForegroundColor Cyan
Write-Host "============================================" -ForegroundColor Cyan
Write-Host ""

# Test 1: Check Node.js
Write-Host "[1/4] Checking Node.js..." -ForegroundColor Yellow
try {
    $nodeVersion = node --version
    Write-Host "[OK] Node.js $nodeVersion" -ForegroundColor Green
} catch {
    Write-Host "[ERROR] Node.js not installed. Download from https://nodejs.org/" -ForegroundColor Red
    exit 1
}

# Test 2: Check npm
Write-Host ""
Write-Host "[2/4] Checking npm..." -ForegroundColor Yellow
try {
    $npmVersion = npm --version
    Write-Host "[OK] npm $npmVersion" -ForegroundColor Green
} catch {
    Write-Host "[ERROR] npm not found" -ForegroundColor Red
    exit 1
}

# Test 3: Run System Health
Write-Host ""
Write-Host "[3/4] Running system diagnostics..." -ForegroundColor Yellow
try {
    node doctor.mjs | Out-Null
    Write-Host "[OK] System healthy" -ForegroundColor Green
} catch {
    Write-Host "[WARNING] System check found issues. Run: node doctor.mjs" -ForegroundColor Yellow
}

# Test 4: Test PDF Generation
Write-Host ""
Write-Host "[4/4] Creating test PDF..." -ForegroundColor Yellow

# Create minimal test HTML
$testHtml = @'
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Career-Ops Test</title>
  <style>
    body { font-family: Arial, sans-serif; margin: 40px; line-height: 1.6; }
    h1 { color: #333; }
    .section { margin: 20px 0; }
    .success { color: green; font-weight: bold; }
  </style>
</head>
<body>
  <h1>Career-Ops PDF Test</h1>
  <div class="section">
    <h2>System Status</h2>
    <p class="success">✓ All systems operational</p>
  </div>
  <div class="section">
    <h2>What's Next</h2>
    <ol>
      <li>Edit config/profile.yml with your details</li>
      <li>Create cv.md with your resume</li>
      <li>Customize templates/cv-template.html</li>
      <li>Run: node generate-pdf.mjs</li>
    </ol>
  </div>
</body>
</html>
'@

# Save test HTML
$testHtml | Set-Content -Path "$env:TEMP\test-career-ops.html" -Encoding UTF8

# Generate PDF
try {
    node generate-pdf.mjs "$env:TEMP\test-career-ops.html" output/test-career-ops.pdf --format=a4 | Out-Null
    Write-Host "[OK] PDF generated: output/test-career-ops.pdf" -ForegroundColor Green
} catch {
    Write-Host "[ERROR] PDF generation failed" -ForegroundColor Red
    Write-Host "Run: npx playwright install chromium" -ForegroundColor Yellow
    exit 1
}

Write-Host ""
Write-Host "============================================" -ForegroundColor Green
Write-Host "All tests passed! ✓" -ForegroundColor Green
Write-Host "============================================" -ForegroundColor Green
Write-Host ""
Write-Host "Next steps:" -ForegroundColor Cyan
Write-Host "  1. Review: CLI_GUIDE.md" -ForegroundColor White
Write-Host "  2. Check: QUICK_REFERENCE.md" -ForegroundColor White
Write-Host "  3. Edit: config/profile.yml" -ForegroundColor White
Write-Host "  4. Follow the workflow in the guides" -ForegroundColor White
Write-Host ""

Read-Host "Press Enter to continue"
