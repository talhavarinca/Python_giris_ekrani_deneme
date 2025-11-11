# Python_giris_ekrani_deneme
# python giris ekrani deneme

Bu depo, Python dilinde yazılmış basit bir konsol tabanlı kullanıcı giriş ekranı denemesini içerir. Script (`deneme.py`), kullanıcıdan temel bilgileri alır ve bu bilgilere göre basit bir doğrulama yapar.

## 📜 Projenin Amacı

Bu script'in temel amacı, Python'da kullanıcıdan veri almayı (`input`), veri tipi dönüşümlerini (`int`), hata yakalamayı (`try-except`) ve koşullu ifadeleri (`if-elif-else`) kullanarak basit bir giriş kontrol mekanizması oluşturmaktır.

## ✨ Temel Özellikler

Script aşağıdaki işlevleri yerine getirir:

* Kullanıcıdan **Ad** ve **Soyad** bilgilerini alır.
* Kullanıcıdan **Yaş** bilgisini alır.
* **Gelişmiş Yaş Doğrulaması:**
    * Bir `while` döngüsü içinde kullanıcıdan geçerli bir yaş girmesini ister.
    * `try-except ValueError` bloğu sayesinde, yaş alanına sayı yerine harf veya özel karakter girilmesini engeller ve kullanıcıyı uyarır.
    * Girilen yaşın mantıklı bir aralıkta (0'dan büyük ve 100'den küçük) olmasını kontrol eder.
* **Giriş Kontrolü:**
    * Tüm bilgiler alındıktan sonra, girilen yaşı kontrol eder.
    * Yaş 18'den küçükse, girişin onaylanmadığını belirten bir mesaj gösterir.
    * Yaş 18 veya daha büyükse, kullanıcının ad ve soyadıyla birlikte hoş geldin mesajı gösterir.

## 🚀 Nasıl Çalıştırılır?

1.  Bu repoyu bilgisayarınıza klonlayın veya `deneme.py` dosyasını indirin.
2.  Terminalinizi (veya Komut İstemi'ni) açın.
3.  Dosyanın bulunduğu klasöre gidin.
4.  Dosya ingilizce bölümün altındadır.

# Simple Python Login Screen

This repository contains a simple console-based user login screen demo written in Python. The script (`deneme.py`) collects basic information from the user and performs a simple validation based on that input.

## 📜 Project Purpose

The main purpose of this script is to demonstrate how to create a simple login control mechanism in Python by using fundamental concepts like getting user input (`input`), data type conversions (`int`), error handling (`try-except`), and conditional statements (`if-elif-else`).

## ✨ Features

The script performs the following functions:

* Collects the user's **First Name** and **Last Name**.
* Asks for the user's **Age**.
* **Advanced Age Validation:**
    * Uses a `while` loop to prompt the user for a valid age until one is provided.
    * Prevents non-numeric input for the age field using a `try-except ValueError` block and alerts the user.
    * Checks if the entered age is within a logical range (greater than 0 and less than 100).
* **Login Control:**
    * After all information is collected, it checks the entered age.
    * If the age is less than 18, it displays a message that access is denied.
    * If the age is 18 or greater, it displays a welcome message with the user's full name, confirming successful login.

## 🚀 How to Run

1.  Clone this repository to your local machine or download the `deneme.py` file.
2.  Open your terminal (or Command Prompt).
3.  Navigate to the directory where the file is located.
4.  Run the script using the following command:

```bash
python deneme.py
