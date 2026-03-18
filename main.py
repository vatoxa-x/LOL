import flet as ft
import time

def main(page: ft.Page):
    page.title = "ВНИМАНИЕ"
    page.theme_mode = ft.ThemeMode.DARK
    page.window_full_screen = True
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # 1. Форсируем громкость Android на 100%
    try:
        from jnius import autoclass
        Context = autoclass('android.content.Context')
        AudioManager = autoclass('android.media.AudioManager')
        activity = autoclass('org.kivy.android.PythonActivity').mActivity
        audio_manager = activity.getSystemService(Context.AUDIO_SERVICE)
        
        STREAM_MUSIC = 3 # Индекс потока музыки в Android
        max_vol = audio_manager.getStreamMaxVolume(STREAM_MUSIC)
        # Устанавливаем макс громкость (флаг 0 - без ползунка на экране)
        audio_manager.setStreamVolume(STREAM_MUSIC, max_vol, 0)
    except Exception as e:
        print(f"Ошибка громкости: {e}")

    # 2. Настройка звука (файл gimn.mp3 должен быть в папке рядом с main.py)
    audio_player = ft.Audio(
        src="gimn.mp3", 
        autoplay=True, 
        volume=1.0
    )
    page.overlay.append(audio_player)

    # 3. Визуал
    page.add(
        ft.Icon(ft.Icons.WARNING_AMBER_ROUNDED, color="red", size=150),
        ft.Text("ВНИМАНИЕ!\nИГРАЕТ ГИМН", size=40, weight="bold", text_align="center"),
        ft.Container(height=30),
        ft.Text("ГРОМКОСТЬ: 100%", size=20, color="red")
    )
    
    page.update()

ft.app(target=main)
