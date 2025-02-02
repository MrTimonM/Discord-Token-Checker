# Discord Token Checker ⭐

🔍 **A Python script to validate and analyze Discord tokens with ease!** 🚀  
✨ Check token validity, extract user details, and categorize them automatically.  

![Checker](https://i.ibb.co.com/b5sd9LHd/discord-tok.png)  

---

## 🌟 Features  

✅ **Token Validation:** Instantly check if Discord tokens are **valid or invalid**.  
🔎 **Token Info:** Get detailed data on valid tokens, including:  
   - 👤 **Username**  
   - 📧 **Email** (if linked)  
   - ✅ **Email Verification Status**  
   - 📞 **Phone Verification Status**  
   - 📅 **Account Creation Date**  
   - ⏳ **Account Age (in days)**  

📂 **Automatic Sorting:**  
   - ✅ **Valid tokens** are saved in `valid_tokens.txt`  
   - ❌ **Invalid tokens** are saved in `invalid_tokens.txt`  

---

## ⚙️ Requirements  

📌 **Python 3.x** is required. Install dependencies with:  

```bash
pip install requests colorama pyfiglet
```

## 🚀 How to Use
* 1️⃣ Clone the Repository:
```bash
git clone https://github.com/MrTimonM/Discord-Token-Checker
cd Discord-Token-Checker
```
2️⃣ Prepare Your Tokens:
- Create a **.txt** file (e.g., tokens.txt) and paste your tokens inside.
3️⃣ Run the Checker:
```bash
python main.py
```
4️⃣ Enjoy the Results! 🎉

## 📌 Example Usage
```bash
Enter the token file name (e.g., tokens.txt): my_tokens.txt
Total tokens found: 15
Do you want to start processing? (yes/no): yes
2023-10-27 12:00:00 | Username: username | Email_verified: True | Phone_verified: True | Days_old: 365
[INVALID] Token: abcdefghij...klmno
...
Validation complete.
Valid tokens: 10
Invalid tokens: 5
```
## ⚠️ Disclaimer  

🚨 For educational purposes only! 🚨  
❗ Using this script to access Discord accounts without authorization is strictly prohibited and may be illegal.  
💀 Respect Discord's Terms of Service. The author is not responsible for any misuse. Use it responsibly and ethically.  

## ⭐ Support  
If you find this project useful, make sure to **star this repo** ⭐ 
