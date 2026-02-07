🐱 Cute Cat Password Checker (PowerShell)

A fun Python program where a fluffy cat checks your password in PowerShell (Windows) 🐾
The cat watches you type, shows * instead of characters, reacts with random phrases, and decides whether to grant access.

✨ Features

🐱 ASCII cat with emotions

🔐 Password input with * masking (visible typing, hidden password)

🎲 Random “cat phrases” while checking

⏳ Animated password verification

❌ Limited number of attempts

💻 Fully compatible with Windows PowerShell

🚫 No getpass() used

📦 Requirements

Windows

Python 3.8+

PowerShell or Windows Terminal

No external libraries needed — only standard Python modules.

🚀 How to Run

Save the file as:

cat_password.py


Open PowerShell in the folder with the file

Run:

python cat_password.py


(or)

py cat_password.py

🔐 How Password Input Works

While typing, you will see:

*****


The real password is hidden

Backspace works correctly

Press Enter to submit

This is implemented using msvcrt, which is why it works perfectly in PowerShell.

🧪 Default Settings
correct_password = "meow123"
attempts = 3


You can change:

the password

number of attempts

cat phrases

ASCII art

🐾 Example Output
🐱 A fluffy cat is guarding the system...

 /\_/\  
( o.o )   meow?
 > ^ <

🔐 Enter password: *****
🐾 sniff sniff...... 

😺 meow~! purr purr!
✅ Access granted!

⚠️ Notes

This project is for learning and fun, not real security

Password is stored in plain text (can be upgraded to hashing)

🌱 Possible Improvements

🔐 Password hashing (SHA-256)

⏳ Temporary lock after failures

👁️ Toggle show/hide password

🪟 GUI version (Tkinter)

🎮 Mini game version

❤️ Author

Made with love, cats, and Python 🐈‍⬛
Have fun hacking — responsibly 😉

Если хочешь, я могу:

сделать README на английском / русском / китайском

оформить под GitHub

добавить security disclaimer

или написать LICENSE

Скажи 👌

сделать README на английском

Конечно 😊
Вот чистый и аккуратный README на английском, готовый для GitHub или проекта.

🐱 Cute Cat Password Checker (PowerShell)

A fun Python program where a fluffy cat checks your password in Windows PowerShell 🐾
The cat watches you type, shows * instead of real characters, reacts with random cat phrases, and decides whether to grant access.

This project is designed for learning, demos, and fun.

✨ Features

🐱 Cute ASCII cat with emotions

🔐 Password input masked with * (you see typing, password stays hidden)

🎲 Random cat phrases while checking

⏳ Animated “checking password” effect

❌ Limited number of attempts

💻 Fully compatible with Windows PowerShell

🚫 No getpass() used (stable on Windows)

📦 Requirements

Windows

Python 3.8 or newer

PowerShell or Windows Terminal

✅ No external libraries required — only Python standard modules.

🚀 How to Run

Save the script as:

cat_password.py


Open PowerShell in the folder containing the file

Run the program:

python cat_password.py


or, if needed:

py cat_password.py

🔐 Password Input Behavior

While typing, characters are displayed as:

*****


The real password is never shown

Backspace works correctly

Press Enter to submit

This is implemented using the Windows-only msvcrt module, which ensures correct behavior in PowerShell.

⚙️ Default Settings
correct_password = "meow123"
attempts = 3


You can easily change:

the password

the number of attempts

cat phrases

ASCII art

🐾 Example Output
🐱 A fluffy cat is guarding the system...

 /\_/\  
( o.o )   meow?
 > ^ <

🔐 Enter password: *****
🐾 sniff sniff......

😺 meow~! purr purr!
✅ Access granted!

⚠️ Disclaimer

⚠️ This project is not intended for real security use.
The password is stored in plain text and is meant only for educational or fun purposes.
