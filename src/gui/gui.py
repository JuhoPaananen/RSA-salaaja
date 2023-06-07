import tkinter as tk
import time
from services.keygen import generate_keys
from services.rsa import encrypt, decrypt

class RsaApplication:
    def __init__(self):
        self.public_key = None
        self.private_key = None
        self.keygen_time = None

        self._initialize_window()
        self._create_widgets()

    def _initialize_window(self):
        self.window = tk.Tk()
        self.window.title("RSA-salausohjelma")
        self.window.geometry("1280x720")
        self.window.grid_columnconfigure(0, weight=1)
        self.window.grid_columnconfigure(1, weight=1)
        self.window.grid_rowconfigure(0, weight=2)
        self.window.grid_rowconfigure(4, weight=2)

    def _create_widgets(self):
        # Generate keys button
        self.generate_button = tk.Button(self.window, text='Luo avaimet', command=self._create_keys, font='bold', bg='navy', fg='white')
        self.generate_button.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky="we")

        # Key labels
        self.public_key_label = tk.Label(self.window, text='Julkinen avain-tuple (e N)', font='bold')
        self.public_key_label.grid(row=1, column=0)
        self.private_key_label = tk.Label(self.window, text='Yksityinen avain-tuple (d N)', font='bold')
        self.private_key_label.grid(row=1, column=1)

        # Key entries
        self.public_key_entry = tk.Text(self.window, height=17, width=60, wrap='word')
        self.public_key_entry.grid(row=2, column=0, padx=5, pady=5, sticky="we")
        self.private_key_entry = tk.Text(self.window, height=17, width=60, wrap='word')
        self.private_key_entry.grid(row=2, column=1, padx=5, pady=5, sticky="we")

        # Copy and paste buttons with frames
        self.public_frame = tk.Frame(self.window)
        self.public_frame.grid(row=3, column=0, padx=5, pady=5, sticky="we")
        self.copy_public_key_button = tk.Button(self.public_frame, text='Kopioi', command=lambda: self._copy(self.public_key_entry))
        self.copy_public_key_button.pack(side=tk.LEFT, expand=True, fill=tk.X)
        self.paste_public_key_button = tk.Button(self.public_frame, text='Liitä', command=lambda: self._paste(self.public_key_entry))
        self.paste_public_key_button.pack(side=tk.LEFT, expand=True, fill=tk.X)

        self.private_frame = tk.Frame(self.window)
        self.private_frame.grid(row=3, column=1, padx=5, pady=5, sticky="we")
        self.copy_private_key_button = tk.Button(self.private_frame, text='Kopioi', command=lambda: self._copy(self.private_key_entry))
        self.copy_private_key_button.pack(side=tk.LEFT, expand=True, fill=tk.X)
        self.paste_private_key_button = tk.Button(self.private_frame, text='Liitä', command=lambda: self._paste(self.private_key_entry))
        self.paste_private_key_button.pack(side=tk.LEFT, expand=True, fill=tk.X)

        # How long key generation took
        self.keygen_time_label = tk.Label(self.window, text='Avainten generointi kesti:', font='bold')
        self.keygen_time_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="nwe")

        # Message and encrypted message labels
        self.message_label = tk.Label(self.window, text='Viesti', font='bold')
        self.message_label.grid(row=5, column=0)
        self.encrypted_message_label = tk.Label(self.window, text='Salattu viesti', font='bold')
        self.encrypted_message_label.grid(row=5, column=1)

        # Message and encrypted message entries
        self.message_entry = tk.Text(self.window, height=10, width=60, wrap='word')
        self.message_entry.grid(row=6, column=0, padx=5, pady=5, sticky="nsew")
        self.encrypted_message_entry = tk.Text(self.window, height=10, width=60, wrap='word')
        self.encrypted_message_entry.grid(row=6, column=1, padx=5, pady=5, sticky="nsew")

        # copy, paste, encrypt and decrypt buttons with frames
        self.message_frame = tk.Frame(self.window)
        self.message_frame.grid(row=7, column=0, padx=5, pady=5, sticky="we")
        self.copy_msg_button = tk.Button(self.message_frame, text='Kopioi', command=lambda: self._copy(self.message_entry))
        self.copy_msg_button.pack(side=tk.LEFT, expand=True, fill=tk.X)
        self.paste_msg_button = tk.Button(self.message_frame, text='Liitä', command=lambda: self._paste(self.message_entry))
        self.paste_msg_button.pack(side=tk.LEFT, expand=True, fill=tk.X)
        self.encrypt_button = tk.Button(self.message_frame, text='Salaa', command=self._encrypt_message, font='bold', bg='navy', fg='white')
        self.encrypt_button.pack(side=tk.LEFT, expand=True, fill=tk.X)

        self.encrypt_frame = tk.Frame(self.window)
        self.encrypt_frame.grid(row=7, column=1, padx=5, pady=5, sticky="we")
        self.copy_encrypted_msg_button = tk.Button(self.encrypt_frame, text='Kopioi', command=lambda: self._copy(self.encrypted_message_entry))
        self.copy_encrypted_msg_button.pack(side=tk.LEFT, expand=True, fill=tk.X)
        self.paste_encrypted_msg_button = tk.Button(self.encrypt_frame, text='Liitä', command=lambda: self._paste(self.encrypted_message_entry))
        self.paste_encrypted_msg_button.pack(side=tk.LEFT, expand=True, fill=tk.X)
        self.decrypt_button = tk.Button(self.encrypt_frame, text='Pura', command=self._decrypt_message, font='bold', bg='navy', fg='white')
        self.decrypt_button.pack(side=tk.LEFT, expand=True, fill=tk.X)
        
    def start(self):    
        self.window.mainloop()

    def _create_keys(self):
        self.public_key_entry.delete('1.0', 'end')
        self.private_key_entry.delete('1.0', 'end')
        start_time = time.time()
        self.public_key, self.private_key = generate_keys()
        self.keygen_time = time.time() - start_time
        self.public_key_entry.insert('1.0', self.public_key)
        self.private_key_entry.insert('1.0', self.private_key)
        self.keygen_time_label['text'] = f'Avainten generointi kesti: {self.keygen_time:.3} sekuntia'

    def _encrypt_message(self):
        if self.public_key == None:
            self.public_key = self.public_key_entry.get('1.0', 'end').strip()
        message = self.message_entry.get('1.0', 'end').strip()
        encrypted_message = encrypt(message, self.public_key)
        self.encrypted_message_entry.delete('1.0', 'end')
        self.encrypted_message_entry.insert('1.0', encrypted_message)

    def _decrypt_message(self):
        if self.private_key == None:
            self.private_key = self.private_key_entry.get('1.0', 'end').strip()
        encrypted_message = self.encrypted_message_entry.get('1.0', 'end').strip()
        decrypted_message = decrypt(int(encrypted_message), self.private_key)
        self.message_entry.delete('1.0', 'end')
        self.message_entry.insert('1.0', decrypted_message)

    def _copy(self, entry):
        self.window.clipboard_clear()
        self.window.clipboard_append(entry.get('1.0', 'end').strip())

    def _paste(self, entry):
        entry.delete('1.0', 'end')
        entry.insert('1.0', self.window.clipboard_get())