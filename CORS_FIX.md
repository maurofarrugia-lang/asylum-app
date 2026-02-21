# 🔧 FIX: "Error loading database" Issue

## Problem
When opening `index.html` directly (double-click), you see:
```
Error loading database
Please check console for details
```

## Why This Happens
Modern browsers block loading local JSON files for security (CORS policy).

---

## ✅ SOLUTION (Choose One)

### **Option 1: Use Python Server** ⭐ RECOMMENDED

This is the easiest and most reliable way:

**Mac/Linux:**
```bash
cd mauros-final-guide
python3 server.py
```

**Windows:**
```cmd
cd mauros-final-guide
python server.py
```

Then open: **http://localhost:8000**

✅ Works perfectly with all features  
✅ No CORS issues  
✅ Fast and reliable  

---

### **Option 2: Use Browser with Disabled Security** ⚠️ TEMPORARY FIX

**Chrome (Windows):**
```cmd
"C:\Program Files\Google\Chrome\Application\chrome.exe" --allow-file-access-from-files --disable-web-security --user-data-dir="C:\temp\chrome_dev"
```

**Chrome (Mac):**
```bash
open -na "Google Chrome" --args --allow-file-access-from-files --disable-web-security --user-data-dir="/tmp/chrome_dev"
```

**Firefox:**
1. Type `about:config` in address bar
2. Accept warning
3. Search for `privacy.file_unique_origin`
4. Set to `false`

⚠️ **WARNING**: Only use for testing! Don't browse other sites with these settings.

---

### **Option 3: Deploy Online** 🌐 BEST FOR SHARING

**Netlify (30 seconds):**
1. Go to https://app.netlify.com/drop
2. Drag the `mauros-final-guide` folder
3. Get URL like: `https://mauros-guide-xyz.netlify.app`
4. ✅ Works on any device!

**GitHub Pages (5 minutes):**
1. Create repo at https://github.com/new
2. Upload all files
3. Settings → Pages → Enable
4. Get URL: `https://your-username.github.io/repo-name`

---

### **Option 4: Use Live Server Extension** 💻 FOR DEVELOPERS

If you use VS Code:
1. Install "Live Server" extension
2. Right-click `index.html`
3. Select "Open with Live Server"
4. Opens at `http://127.0.0.1:5500`

---

## 🎯 Quick Test

After using any solution above, test the Caseworker Index:
1. Click "⚖️ Caseworker Index" tab
2. Search for: `credibility`
3. Should show results!

---

## 📊 Verify It's Working

Open browser console (F12) and you should see:
```
Database loaded: {regulations: Array(7), definitions: Array(132), ...}
```

Instead of:
```
Error loading database
```

---

## 💡 Why Python Server is Best

✅ **No security issues** - Proper HTTP server  
✅ **Works everywhere** - Mac, Windows, Linux  
✅ **No setup needed** - Python usually pre-installed  
✅ **Reliable** - Industry standard  
✅ **Fast** - Instant loading  

Just run:
```bash
python3 server.py
```

And you're done! 🎉

---

## 🆘 Still Not Working?

### Check Python is Installed:
```bash
python3 --version
# or
python --version
```

Should show: `Python 3.x.x`

If not installed:
- **Mac**: Already installed
- **Windows**: Download from https://python.org
- **Linux**: `sudo apt install python3`

### Alternative: Use Node.js Server

If you have Node.js:
```bash
npx http-server
```

Then open: http://localhost:8080

---

## 📱 For Mobile Use

**Best approach:**
1. Deploy to Netlify (drag folder to https://app.netlify.com/drop)
2. Get the URL
3. Open on phone
4. Add to Home Screen
5. ✅ Works like native app!

---

**TL;DR:**
- **Double-clicking HTML won't work** due to browser security
- **Use `python3 server.py`** → opens at localhost:8000
- **Or deploy online** → works everywhere

---

**Need help?** Let me know which option you'd like to use!
