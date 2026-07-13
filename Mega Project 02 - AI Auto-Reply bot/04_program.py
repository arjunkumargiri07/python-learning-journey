import pyautogui
import pyperclip
import time

# Give yourself a moment before automation starts
time.sleep(2)

# Step 1: Click the icon
pyautogui.click(1003, 1178)

# Wait for the application to open/focus
time.sleep(2)

# Step 2: Drag to select the text
pyautogui.moveTo(586, 56, duration=0.5)
pyautogui.dragTo(1200, 1100, duration=1.5, button='left')

# Small delay
time.sleep(0.5)

# Step 3: Copy selected text
pyautogui.hotkey('ctrl', 'c')

# Wait for clipboard to update
time.sleep(0.5)

# Step 4: Get copied text into a variable
copied_text = pyperclip.paste()

print("Copied Text:")
print(copied_text)