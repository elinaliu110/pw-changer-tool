import tkinter as tk
from tkinter import messagebox
import requests

# Create the main window
root = tk.Tk()
root.title("修改密碼工具")
root.geometry("400x400")

# API URL template
API_URL_TEMPLATE = "https://portal-sso-ensaas.sa.wise-paas.com/v4.0/users/{}/password"

# Function to call the API
def change_password():
    emails = email_textbox.get("1.0", "end-1c").strip()  # Get email input
    new_password = password_entry.get().strip()  # Get new password
    token = token_entry.get().strip()  # Get the Bearer token

    if not emails or not new_password or not token:
        messagebox.showerror("錯誤", "請輸入 email、新密碼和 Token")
        return

    email_list = emails.split(",")  # Split emails by comma
    success_list = []
    failure_list = []

    for email in email_list:
        email = email.strip()  # Clean up spaces
        if email:
            url = API_URL_TEMPLATE.format(email)

            payload = {
                "new_password": new_password
            }

            headers = {
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json"
            }

            try:
                response = requests.put(url, json=payload, headers=headers)
                response.raise_for_status()

                if response.status_code == 200:
                    success_list.append(email)
                else:
                    failure_list.append(f"{email} - {response.text}")
            except requests.exceptions.RequestException as e:
                failure_list.append(f"{email} - {str(e)}")

    # Combine the success and failure results into one message
    result_message = ""

    if success_list:
        result_message += "密碼修改成功的 Email:\n" + "\n".join(success_list) + "\n\n"
    if failure_list:
        result_message += "密碼修改失敗的 Email 和錯誤訊息:\n" + "\n".join(failure_list)

    if result_message:
        messagebox.showinfo("結果", result_message)
    else:
        messagebox.showinfo("結果", "沒有任何結果")

# GUI layout
# Email input
email_label = tk.Label(root, text="輸入 Email(s):")
email_label.pack(pady=5)
email_textbox = tk.Text(root, height=5, width=40)
email_textbox.pack(pady=5)

# Password input
password_label = tk.Label(root, text="輸入新密碼:")
password_label.pack(pady=5)
password_entry = tk.Entry(root, show="*", width=40)
password_entry.pack(pady=5)

# Token input
token_label = tk.Label(root, text="輸入 Bearer Token:")
token_label.pack(pady=5)
token_entry = tk.Entry(root, show="*", width=40)
token_entry.pack(pady=5)

# Submit button
submit_button = tk.Button(root, text="修改密碼", command=change_password)
submit_button.pack(pady=20)

# Start GUI loop
root.mainloop()
