# 🌐 Auto-Portfolio Generator

Welcome to **Auto-Portfolio Generator** – an open-source Python project that empowers developers, students, freelancers, and professionals to instantly create a beautiful personal portfolio website using just a JSON file. 🧠💻✨

## 🚀 What is This?

This project reads your personal and professional data (like name, skills, projects, and contact info) from a `user.json` file and generates a complete, ready-to-use `index.html` portfolio webpage using a clean HTML + CSS template.

You **don’t need to write any frontend code**. Just update the JSON, run the Python script, and your portfolio is ready! Perfect for those who want to showcase their work fast and professionally.

---

## 📂 Folder Structure

```
Auto-Portfolio-Generator/
│
├── generator.py           # Main Python script
├── index.html             # Auto-generated portfolio webpage
│
├── data/
│   └── user.json          # Your personal data in JSON format
│
├── templates/
│   └── simple.html        # HTML template with placeholders
│
├── assets/
│   └── style.css          # CSS styling for the generated page
│
├── README.md              # This file
├── .gitignore             # To ignore unnecessary files
└── LICENSE                # Optional open-source license
```

---

## 🛠️ Features

- ✅ No frontend coding required  
- ✅ Easy-to-edit JSON for portfolio data  
- ✅ Clean, minimal responsive layout  
- ✅ Fully customizable HTML/CSS  
- ✅ Ready for GitHub Pages or any static hosting  
- ✅ Add unlimited projects, skills, and links  
- ✅ Beginner-friendly & open-source  

---

## 👩‍💻 How to Use

### 1. Clone the Repository

```bash
git clone https://github.com/YourUsername/Auto-Portfolio-Generator.git
cd Auto-Portfolio-Generator
```

### 2. Customize Your Data

Open `data/user.json` and update with your personal information:

```json
{
  "name": "Ayesha",
  "bio": "I am a passionate Data Scientist...",
  "skills": ["Python", "ML", "Web Dev"],
  "projects": [
    {
      "title": "AI Tool",
      "description": "An intelligent resume scanner.",
      "link": "https://github.com/AyeshaTechX/AI-Resume-Analyzer"
    }
  ],
  "contact": {
    "email": "youremail@example.com",
    "github": "https://github.com/YourProfile"
  }
}
```

### 3. Run the Generator

Make sure Python is installed, then:

```bash
python generator.py
```

This will generate `index.html` — open it in any browser to view your portfolio!

---

## 🖼️ Screenshots (Optional)

You can add screenshots here:

| Preview | Portfolio Page |
|--------|----------------|
| ![demo](https://via.placeholder.com/300x180?text=Preview) | ![portfolio](https://via.placeholder.com/300x180?text=Portfolio) |

---

## 🌍 Hosting Your Portfolio

### 🧷 Option 1: GitHub Pages (Recommended)

1. Create a `docs/` folder.
2. Move `index.html`, `assets/`, etc., into `docs/`.
3. Go to your repo → Settings → Pages → Source: `docs/` → Save.
4. Your site will be live at:
   ```
   https://yourusername.github.io/Auto-Portfolio-Generator/
   ```

### 🌐 Option 2: Netlify / Vercel / Firebase

Upload `index.html` and the `assets/` folder as a static website.

---

## 🎯 Why Use This?

- 🚀 Save time creating portfolios manually  
- 👩‍🎓 Great for students building resumes  
- 🧑‍💼 Perfect for freelancers to show projects  
- 📂 Version-controlled and reproducible  
- 🌈 Easy to customize and extend  

---

## 💡 Future Ideas (You Can Add Later)

- Multiple templates to choose from  
- Dark mode switch  
- PDF export of portfolio  
- Add a blog section  
- GitHub activity stats integration  
- Deployment automation script  

---

## 🤝 Contributing

Contributions are welcome! If you want to add templates, improve the generator, or suggest features:

1. Fork the repo  
2. Create a branch  
3. Commit changes  
4. Push and make a pull request  

---

## 📜 License

This project is licensed under the **MIT License** – feel free to use, copy, and modify it freely.

---

## ✨ Made with Passion by [Ayesha](https://github.com/AyeshaTechX)

> “Your portfolio is the mirror of your journey. Let it shine through automation.”
