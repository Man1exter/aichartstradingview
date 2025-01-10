import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from data_manager import DataManager
from ai_module import AIModule
from PIL import Image, ImageTk

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Krypto Panel")
        self.geometry("1200x800")
        self.configure(bg="#2e2e2e")
        self.data_manager = DataManager()
        self.ai_module = AIModule()
        
        try:
          self.bg_image = Image.open("background.png") 
          self.bg_image = self.bg_image.resize((self.winfo_screenwidth(), self.winfo_screenheight()), Image.LANCZOS)
          self.bg_photo = ImageTk.PhotoImage(self.bg_image)
          self.background_label = tk.Label(self, image=self.bg_photo)
          self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        except FileNotFoundError:
          print("Warning: background.png not found")

        self.create_widgets()
        self.update_charts()

    def create_widgets(self):
        # Stylowanie przycisków
        button_style = ttk.Style()
        button_style.configure("TButton", padding=10, font=('Arial', 12), foreground="black", background="white")
        button_style.map("TButton",
                          background=[('active', '#d9d9d9')],  # Kolor po najechaniu myszą
                          foreground=[('active', 'black')]  # Tekst po najechaniu myszą
                         )
       
        # Kontener dla przycisków i wykresu
        frame = tk.Frame(self, bg="#2e2e2e")
        frame.pack(pady=20, padx=20, fill='both', expand=True)

        # Przycisk 1: Wyświetl wykresy
        self.plot_button = ttk.Button(frame, text="Wyświetl Wykresy", command=self.update_charts, style="TButton")
        self.plot_button.pack(side=tk.LEFT, padx=10)

        # Przycisk 2: Analiza AI
        self.ai_button = ttk.Button(frame, text="Analiza AI", command=self.open_ai_window, style="TButton")
        self.ai_button.pack(side=tk.LEFT, padx=10)

        # Przycisk 3: Najnowsze newsy
        self.news_button = ttk.Button(frame, text="Najnowsze Newsy", command=self.open_news_window, style="TButton")
        self.news_button.pack(side=tk.LEFT, padx=10)
    
        # Kontener na wykresy
        self.chart_frame = tk.Frame(frame, bg="#2e2e2e")
        self.chart_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, pady=10)
        
    def update_charts(self):
        # Usunięcie starych wykresów
        for widget in self.chart_frame.winfo_children():
            widget.destroy()
            
        top_cryptos = self.data_manager.get_top_n_cryptos(n=10)
        
        if top_cryptos.empty:
            tk.Label(self.chart_frame, text="Nie można pobrać danych.").pack(pady=20)
            return

        for index, row in top_cryptos.iterrows():
            crypto_id = row['symbol'].lower()
            historical_data = self.data_manager.get_historical_data(crypto_id)
            
            if historical_data.empty:
                continue
            
            fig, ax = plt.subplots(figsize=(5,3))
            ax.plot(historical_data['price'], color='skyblue')
            ax.set_title(f"{row['symbol']} - {row['current_price']:.2f}$", color='white')
            ax.set_facecolor("#3e3e3e")
            ax.tick_params(colors='white')
            fig.patch.set_facecolor("#2e2e2e")
            
            canvas = FigureCanvasTkAgg(fig, master=self.chart_frame)
            canvas_widget = canvas.get_tk_widget()
            canvas_widget.pack(side=tk.LEFT, padx=10)
            canvas.draw()

    def open_ai_window(self):
        ai_window = tk.Toplevel(self)
        ai_window.title("Chat z AI")
        ai_window.configure(bg="#2e2e2e")
        ai_window.geometry("800x600")
      
        # Input field
        prompt_entry = tk.Text(ai_window, height=10, bg="#3e3e3e", fg="white", insertbackground="white")
        prompt_entry.pack(pady=10, padx=10, fill=tk.X)
        
        # Chat Box
        chat_box = tk.Text(ai_window, height=20, state='disabled', bg="#3e3e3e", fg="white", insertbackground="white")
        chat_box.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
        
        def send_message():
           prompt = prompt_entry.get("1.0", "end-1c")
           chat_box.config(state='normal')
           chat_box.insert(tk.END, f"User: {prompt}\n", ("user"))
           chat_box.config(state='disabled')
           prompt_entry.delete("1.0", "end")
           
           # Pobieranie danych i tworzenie prognozy
           top_cryptos = self.data_manager.get_top_n_cryptos(n=1)
           if not top_cryptos.empty:
                crypto_id = top_cryptos['symbol'][0].lower()
                prices = self.data_manager.get_historical_data(crypto_id)['price']
           else:
                prices = None

           response = self.ai_module.chat_with_ai(prompt) if not prompt == '' else self.ai_module.get_price_predictions(prices) if prices is not None else "Error while retrieving data"
           chat_box.config(state='normal')
           chat_box.insert(tk.END, f"AI: {response}\n", ("ai"))
           chat_box.config(state='disabled')
           
           chat_box.tag_config("user", foreground="yellow")
           chat_box.tag_config("ai", foreground="skyblue")
        
        # Send button
        send_button = ttk.Button(ai_window, text="Send", command=send_message, style="TButton")
        send_button.pack(pady=10)
        
    def open_news_window(self):
       news_window = tk.Toplevel(self)
       news_window.title("Najnowsze Newsy")
       news_window.configure(bg="#2e2e2e")
       news_window.geometry("800x600")

       news_text = tk.Text(news_window, bg="#3e3e3e", fg="white", insertbackground="white")
       news_text.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
       
       news_text.insert(tk.END, self.data_manager.get_latest_news())
       news_text.config(state='disabled')

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()