from time import monotonic

from textual import on
from textual.app import App
from textual.widgets import Footer, Header, Button, Static
from textual.reactive import reactive
from textual.containers import ScrollableContainer


class TimeDisplay(Static):
    """Custom time display widget"""
    time_elapsed = reactive(0)

    def watch_time_elapsed(self):
        time=self.time_elapsed
        time, seconds=divmod(time,60)
        hours,minutes=divmod(time,60)
        time_string=f"{hours:02.0f}:{minutes:02.0f}:{seconds:05.2f}"
        self.update(str(time_string))
    def start(self):
        """Start keeping track of thetime elapsed."""
        self.start_time=monotonic()
    def stop(self):
        """Stop keeping track of the time elapsed"""
        self.time_elapsed=monotonic()-self.start_time
    def reset(self):
        """Reset time elapsed"""

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
        self.query_one(TimeDisplay).start()

    @on(Button.Pressed, "#stop")
    def stop_stopwatch(self):
        self.remove_class("started")
        # queries the child elements
        self.query_one(TimeDisplay).stop()

    @on(Button.Pressed,"#reset")
    def reset_stopwatch(self):
        self.query_one(TimeDisplay).reset()


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
            yield Stopwatch()
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