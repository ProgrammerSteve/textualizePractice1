from textual import on
from textual.app import App
from textual.widgets import Footer, Header, Button, Static
from textual.containers import ScrollableContainer


class TimeDisplay(Static):
    """Custom time display widget"""
    pass

# When you inherit a widget, you create a widget
class Stopwatch(Static):
    """Custom stopwatch widget."""
    def compose(self):
        """What subwidgets go in the widget"""
        yield Button("Start", variant="success", id="start")
        yield Button("Stop",variant="error",id="stop")
        yield Button("Reset",id="reset")
        yield TimeDisplay("00:00:00.00")
    
    # @on is a decorator that takes Button.Pressed as an input to handle that event
    @on(Button.Pressed, "#start")
    def start_stopwatch(self):
        self.add_class("started")
        
    @on(Button.Pressed, "#stop")
    def stop_stopwatch(self):
        self.remove_class("started")
        

class StopwatchApp(App):
    BINDINGS = [
        # (key,action name, description),
        ("d","toggle_dark_mode","Toggle dark mode"),
    ]

    # CSS="""
    # Stopwatch {
    #     layout: horizontal;
    # }
    # """
    CSS_PATH="./stopwatch.tcss"

    def compose(self):
        """What widgets is this app composed of?"""
        yield Header(show_clock=True)
        yield Footer()
        with ScrollableContainer(id= "stopwatches"):
            yield Stopwatch(classes="started")
            yield Stopwatch()
            yield Stopwatch()
        # yield ScrollableContainer(
        #     Stopwatch(),
        #     Stopwatch(),
        #     Stopwatch(),
        #     id= "stopwatches"
        # )
        

    # This is an ACTION method
    # It's an action method beacause it starts with action_
    # It's associated wtih the action called toggle_dark_mode
    def action_toggle_dark_mode(self):
        self.dark=not self.dark

if __name__ == "__main__":
    StopwatchApp().run()