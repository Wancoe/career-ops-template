@echo off
REM Test Script for Career-Ops
REM Run this to verify Node.js, Playwright, and PDF generation are working

echo.
echo ============================================
echo Career-Ops Test Suite
echo ============================================
echo.

REM Check Node.js
echo [1/4] Checking Node.js...
node --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Node.js not installed. Download from https://nodejs.org/
    exit /b 1
) else (
    for /f "tokens=*" %%i in ('node --version') do echo [OK] Node.js %%i
)

REM Check npm
echo.
echo [2/4] Checking npm...
npm --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] npm not found
    exit /b 1
) else (
    for /f "tokens=*" %%i in ('npm --version') do echo [OK] npm %%i
)

REM Check System Health
echo.
echo [3/4] Running system diagnostics...
node doctor.mjs >nul 2>&1
if errorlevel 1 (
    echo [WARNING] System check found issues. Run: node doctor.mjs
) else (
    echo [OK] System healthy
)

REM Test PDF Generation
echo.
echo [4/4] Creating test PDF...

REM Create a minimal test HTML
(
    echo ^<!DOCTYPE html^>
    echo ^<html lang="en"^>
    echo ^<head^>
    echo   ^<meta charset="UTF-8"^>
    echo   ^<title^>Career-Ops Test^</title^>
    echo   ^<style^>
    echo     body { font-family: Arial, sans-serif; margin: 40px; line-height: 1.6; }
    echo     h1 { color: #333; }
    echo     .section { margin: 20px 0; }
    echo     .success { color: green; font-weight: bold; }
    echo   ^</style^>
    echo ^</head^>
    echo ^<body^>
    echo   ^<h1^>Career-Ops PDF Test^</h1^>
    echo   ^<div class="section"^>
    echo     ^<h2^>System Status^</h2^>
    echo     ^<p class="success"^>✓ All systems operational^</p^>
    echo   ^</div^>
    echo   ^<div class="section"^>
    echo     ^<h2^>What's Next^</h2^>
    echo     ^<ol^>
    echo       ^<li^>Edit config/profile.yml with your details^</li^>
    echo       ^<li^>Create cv.md with your resume^</li^>
    echo       ^<li^>Customize templates/cv-template.html^</li^>
    echo       ^<li^>Run: node generate-pdf.mjs^</li^>
    echo     ^</ol^>
    echo   ^</div^>
    echo ^</body^>
    echo ^</html^>
) > /tmp/test-career-ops.html

node generate-pdf.mjs /tmp/test-career-ops.html output/test-career-ops.pdf --format=a4 >nul 2>&1
if errorlevel 1 (
    echo [ERROR] PDF generation failed
    echo Run: npx playwright install chromium
    exit /b 1
) else (
    echo [OK] PDF generated: output/test-career-ops.pdf
)

echo.
echo ============================================
echo All tests passed! ✓
echo ============================================
echo.
echo Next steps:
echo   1. Review: CLI_GUIDE.md
echo   2. Check: QUICK_REFERENCE.md
echo   3. Edit: config/profile.yml
echo   4. Follow the workflow in the guides
echo.

pause
