from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

# Start with the same mode Sideband currently uses.
Window.softinput_mode = "below_target"


class KeyboardTestApp(App):
    def build(self):
        self.title = "Kivy Keyboard Test"

        root = BoxLayout(
            orientation="vertical",
            padding=dp(12),
            spacing=dp(8),
        )

        title = Label(
            text="Kivy / Android IME test",
            size_hint_y=None,
            height=dp(42),
            font_size="20sp",
        )
        root.add_widget(title)

        help_label = Label(
            text=(
                "1. Choose a soft-input mode.\n"
                "2. Tap the message field at the bottom.\n"
                "3. Check whether the field and Send button stay visible above the keyboard.\n"
                "4. Hide the keyboard with Back and try another mode."
            ),
            halign="left",
            valign="middle",
            size_hint_y=None,
            height=dp(120),
        )
        help_label.bind(size=lambda inst, value: setattr(inst, "text_size", value))
        root.add_widget(help_label)

        modes = BoxLayout(
            orientation="horizontal",
            spacing=dp(6),
            size_hint_y=None,
            height=dp(48),
        )

        for label, mode in [
            ("below_target", "below_target"),
            ("pan", "pan"),
            ("resize", "resize"),
            ("none", ""),
        ]:
            btn = Button(text=label)
            btn.bind(on_release=lambda _btn, m=mode: self.set_mode(m))
            modes.add_widget(btn)

        root.add_widget(modes)

        self.status = Label(
            text="",
            halign="left",
            valign="top",
        )
        self.status.bind(size=lambda inst, value: setattr(inst, "text_size", value))
        root.add_widget(self.status)

        # Bottom bar deliberately resembles a chat composer.
        composer = BoxLayout(
            orientation="horizontal",
            spacing=dp(6),
            size_hint_y=None,
            height=dp(56),
        )

        self.message = TextInput(
            hint_text="Type something here...",
            multiline=False,
        )
        composer.add_widget(self.message)

        send = Button(
            text="Send",
            size_hint_x=None,
            width=dp(84),
        )
        send.bind(on_release=self.on_send)
        composer.add_widget(send)

        root.add_widget(composer)

        Clock.schedule_interval(self.update_status, 0.20)
        return root

    def set_mode(self, mode):
        # Kivy accepts an empty string as the default/no special soft-input mode.
        Window.softinput_mode = mode
        self.update_status(0)

    def on_send(self, *_args):
        self.status.text = (
            "Send button pressed.\n\n"
            f"Current text: {self.message.text!r}\n\n"
            + self.runtime_info()
        )

    def runtime_info(self):
        mode = Window.softinput_mode or "none"
        keyboard_height = getattr(Window, "keyboard_height", "n/a")
        return (
            f"softinput_mode: {mode}\n"
            f"Window size: {Window.width} x {Window.height}\n"
            f"keyboard_height: {keyboard_height}\n"
            f"TextInput focus: {self.message.focus}"
        )

    def update_status(self, _dt):
        if not self.status.text.startswith("Send button pressed"):
            self.status.text = self.runtime_info()


if __name__ == "__main__":
    KeyboardTestApp().run()
