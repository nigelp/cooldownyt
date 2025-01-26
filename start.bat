@echo off
start cmd /k "cd G:\downyt\frontend && npm run dev"
timeout /t 5
start cmd /k "cd G:\downyt && python server.py"