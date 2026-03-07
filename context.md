# Project Overview
LADES is a high-performance web application engineered to provide a seamless, watermark-free video downloading experience across multiple social media platforms. The project focuses on speed, server-side efficiency, and a minimalist user interface that ensures high-quality output with minimal resource consumption.

## Tech Stack
Frontend: HTML5, Modern CSS (Blue Palette), Vanilla JavaScript

Backend: Python (Flask Framework)

Core Library: yt-dlp for advanced video extraction and processing

Middleware: Flask-CORS for cross-origin resource sharing management

Deployment: Gunicorn WSGI server (Optimized for Render/Production environments)

## Coding Rules
Visual Identity: Maintain a compact, modern design using strictly blue tones as the primary color palette.

Numerical Formatting: Always use a comma (,) as the decimal separator (e.g., 3,5 instead of 3.5).

Decimal Precision: If there are four zeros after the decimal comma, they must be omitted (e.g., write 5 instead of 5,0000).

Resource Optimization: Strict enforcement of a 720p quality limit and a 50,0 MB file size ceiling to preserve server RAM.

Language Policy: Non-coding explanations and step-by-step guides should be written in simple, clear Turkish.

## Memory (Project Status & Decisions)
CORS/Load Failed Solution: Frontend is now served via Flask's render_template to eliminate domain mismatches.

Mobile UX Update: Platform selection buttons are converted to a horizontal scrollable container for better mobile readability.

Localization: Dynamic TR/EN language switching via flag icons is integrated into the core JS logic.

Security: Automatic file deletion (after_this_request) is implemented to prevent server disk congestion.