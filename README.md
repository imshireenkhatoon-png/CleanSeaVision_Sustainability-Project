# 🌊 CleanSeaVision — Marine Waste Classification Project

---

## 🧠 Overview

*CleanSeaVision* is an AI-powered web application designed to classify marine environments into three categories:

1. **Marine Debris** 
2. **Clean Water**  
3. **Oil Spill**

The project supports ocean sustainability by detecting pollution through deep learning and image classification.

---

## 🎯 Objectives & Goals

- Develop a CNN-based image classifier for marine waste detection.  
- Convert the trained Keras model to a TensorFlow.js model for browser deployment.  
- Build an interactive front-end interface for users to upload and analyze ocean images.  
- Raise awareness of marine pollution through accessible AI technology.

---

## 🧰 Tools & Technologies Used

- **Python**, **TensorFlow**, **Keras**  
- **Teachable Machine** (Model Creation)  
- **TensorFlow.js** (Web Integration)  
- **HTML**, **CSS**, **JavaScript**  
- **VS Code**  
- **GitHub** (Version Control)  
- **Kaggle / Google Colab** (Model Testing)

---

## ⚙ Methodology

1. *Data Collection:*  
   Collected marine images representing debris, clean water, and oil spills.

2. *Model Training:*  
   Used CNN architecture via Teachable Machine and refined with Keras.

3. *Model Conversion:*  
   Exported .h5 model and converted it to TensorFlow.js format using tensorflowjs_converter.

4. *Web Integration:*  
   Built an HTML front end with JavaScript logic to load and run the model in-browser.

5. *Testing & Deployment:*  
   Model tested locally using Live Server and uploaded to GitHub for open access.

---

## 🧩 Folder Structure
```

CleanSeaVision_Sustainability-Project/
│
├── CleanSeaVision/               # Front-end (HTML, CSS, JS, model_web folder)
│   ├── index.html
│   ├── style.css
│   ├── script.js
│   └── model_web/
│       ├── model.json
│       ├── group1-shard1of1.bin
│
├── CleanSeaVision_Model/         # Keras / Teachable Machine model files
│   ├── model.h5
│   ├── labels.txt
│
├── Datasets_CleanSeaVision/      # Optional dataset reference
│
├── cleanseavision_test.ipynb     # Kaggle or Colab test notebook
└── README.md

```
---

## 📊 Sample Output

- Upload an ocean image through the interface.  
- The model predicts one of the three classes with a confidence score.  
- Displays eco-friendly insights based on prediction results.

---

## 🏁 Conclusion

*CleanSeaVision* demonstrates the potential of AI in environmental conservation.  
It bridges technology and sustainability by providing a simple yet impactful tool to classify marine waste and promote cleaner oceans.

---

## 👩‍💻 Author

*Shireen Khatoon*  
B.Tech (Computer Science) | Jabalpur Engineering College  
📧 imshireenkhatoon@gmail.com
