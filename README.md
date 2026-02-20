# 🇪🇺 EU Asylum Pact Information App

## ✨ Features

This is a fully functional web application for searching and browsing the **New EU Asylum Pact** regulations, directives, and EUAA guidelines.

### Key Features:
- ✅ **Search Functionality**: Search by article number, keywords, or themes
- ✅ **10 Legal Instruments**: All regulations and directives from the 2024 Pact
- ✅ **50+ EUAA Guidelines**: Practical guides and operational standards
- ✅ **Category Filtering**: Browse by screening, procedures, Dublin, reception, etc.
- ✅ **Direct EUR-Lex Links**: Links to official legal texts
- ✅ **Responsive Design**: Works on desktop, tablet, and mobile
- ✅ **Offline Capable**: Can work without internet after initial load

## 📦 What's Included

### Legal Instruments:
1. **Asylum Procedure Regulation (2024/1348)** - Common procedures for international protection
2. **Screening Regulation (2024/1356)** - Border screening procedures
3. **Eurodac Regulation (2024/1358)** - Biometric database system
4. **Asylum and Migration Management Regulation (2024/1351)** - Dublin IV and solidarity
5. **Qualification Regulation (2024/1347)** - Standards for refugee status
6. **Reception Conditions Directive (2024/1346)** - Reception standards
7. **Crisis Regulation (2024/1359)** - Emergency procedures

### EUAA Guidelines:
- Evidence and Risk Assessment
- Personal Interview Guidelines
- Qualification for International Protection
- Registration and Lodging Procedures
- Dublin Procedure Implementation
- And 45+ more practical guides...

## 🚀 How to Run

### Option 1: Simple Python Server (Easiest)
```bash
cd asylum-app
python3 server.py
```
Then open: `http://localhost:8000`

### Option 2: Using Python's Built-in Server
```bash
cd asylum-app
python3 -m http.server 8000
```
Then open: `http://localhost:8000`

### Option 3: Double-click index.html
Simply double-click the `index.html` file to open it in your default browser.

## 📱 Mobile App Conversion

### To convert this to native Android/iOS apps:

#### Option A: Using Cordova/PhoneGap
```bash
# Install Cordova
npm install -g cordova

# Create new project
cordova create AsylumApp eu.asylum.app "EU Asylum Pact"
cd AsylumApp

# Copy web files
cp -r ../asylum-app/www/* www/

# Add platforms
cordova platform add android
cordova platform add ios

# Build
cordova build android
cordova build ios
```

#### Option B: Using Capacitor
```bash
# Install Capacitor
npm install @capacitor/core @capacitor/cli

# Initialize
npx cap init

# Add platforms
npx cap add android
npx cap add ios

# Build
npx cap copy
npx cap open android
npx cap open ios
```

#### Option C: Use a Web Wrapper Service
- **AppGyver**: No-code mobile app builder
- **Thunkable**: Drag-and-drop app builder
- **WebViewGold**: Convert HTML to native app
- **Apache Cordova**: Cross-platform framework

## 🔧 Customization

### To add more content:

Edit `database.json` to add:
- More regulations
- Additional EUAA guidelines
- Country-specific information
- Case law references

### To parse actual regulation texts:

The `parse_regulations.py` script can be enhanced to:
1. Download full regulation texts from EUR-Lex
2. Extract all articles with their content
3. Create searchable keyword indices
4. Add cross-references between articles

## 📊 Database Structure

```json
{
  "regulations": [
    {
      "id": "2024_1348",
      "title": "Full title",
      "short_title": "APR",
      "number": "2024/1348",
      "description": "...",
      "articles": [...]
    }
  ],
  "euaa_guidelines": [...]
}
```

## 🌐 Official Sources

- **EU Commission**: https://home-affairs.ec.europa.eu/policies/migration-and-asylum/pact-migration-and-asylum_en
- **EUR-Lex**: https://eur-lex.europa.eu/
- **EUAA**: https://euaa.europa.eu/

## ⚖️ Legal Notice

This is an **unofficial tool** for information and educational purposes only. Always refer to the official publications on EUR-Lex for legally binding texts.

## 🔮 Future Enhancements

Potential additions:
- [ ] Full article text parsing from EUR-Lex
- [ ] Multi-language support (24 EU languages)
- [ ] Bookmarking and notes functionality
- [ ] Offline PDF downloads
- [ ] AI-powered semantic search
- [ ] Case law integration (CJEU)
- [ ] User annotations and highlights
- [ ] Comparison tools between regulations
- [ ] Timeline view of regulatory changes
- [ ] Push notifications for updates

## 📄 Files Included

- `index.html` - Main application interface
- `database.json` - Regulations and guidelines database
- `server.py` - Simple Python web server
- `parse_regulations.py` - Parser for regulation texts
- `README.md` - This file

## 💡 Tips for Use

1. **Search Examples**:
   - "Article 12" - Find specific articles
   - "family reunification" - Find related regulations
   - "screening" - Find screening-related documents
   - "unaccompanied minors" - Find child protection provisions

2. **Best Practices**:
   - Use specific keywords for better results
   - Browse by category for overview
   - Check official EUR-Lex links for full legal text
   - Refer to EUAA guidelines for practical implementation

## 📞 Support

For issues or suggestions:
- Review the official EU documentation
- Check EUR-Lex for latest updates
- Consult EUAA practical guides

## 📅 Version Information

- **Version**: 1.0
- **Last Updated**: February 20, 2026
- **Pact Entry into Force**: June 11, 2024
- **Application Date**: June 12, 2026

---

**Built with**: HTML5, CSS3, JavaScript, Python
**License**: For informational and educational use
**Status**: ✅ Functional Prototype
