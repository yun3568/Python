@echo off
:: 切换到当前脚本所在的目录（确保在 D 盘正确位置运行）
cd /d "%~dp0"

echo 正在检测文件变化...

:: 1. 添加所有新文件和修改
git add .

:: 2. 提交修改，备注里自动加上当前的日期和时间
git commit -m "Auto update: %date% %time%"

:: 3. 推送到 GitHub
echo 正在上传到 GitHub...
git push -u origin main

echo.
echo ================================================
echo  上传成功！(如果没有看到红色报错信息)
echo ================================================
pause