# A-ransomware-
# Project Description: Educational Ransomware Creation

# Introduction:

This project involves creating an educational ransomware to understand the workings of such malicious software and the security measures needed to protect against it. It's crucial to note that the use of this ransomware is strictly for educational and ethical purposes, and should never be used for malicious intent. The using language is python.

# Project Objectives:

• Understand how ransomware operates and the encryption techniques used.
• Implement security measures to protect against ransomware attacks, such as regular data backups, using antivirus and firewalls, and educating users on cybersecurity best practices.

# Important to kwo:

To install the cryptography package the command is:

- on linux: pip install cryptography
- on windows: py -m pip install cryptography

# How to run:
To test the script, you have to come up with files you don't need or have a copy of them somewhere on your computer (because if you forget the password during the encryption it will be impossible to decrypt them). For my case, I've made a folder named TestOfRansomware in the same directory where ransomware.py is located and brought some PDF documents, images, text files, and other files.
- To encrypt:
  - $ python ransomware.py -e . -s 32
  - I've specified the salt to be 32 in size and passed the '.' current folder to the script. You will be prompted for a password for encryption (you can choose the password you want).
- To decrypt:
  - $ python ransomware.py -d .
  - In the decryption process, do not pass -s as it will generate a new salt and override the previous salt that was used for encryption and so you won't be able to recover your files. You can edit the code to prevent this parameter in decryption.
  - Than you'll have to pass the password and the entire folder will be back to its original form!





# Conclusion:

This project aims to raise awareness of the threat of ransomware and promote good cybersecurity practices. It's essential to always act ethically and legally in the field of cybersecurity and never use this knowledge for malicious purposes.


