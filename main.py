'''
Multithread autoclicker

Functions:

    autoclicker(times: int, delay: int) -> None - click by mouse multiple times

    spam(click_times: int, threads_number: int, delay: int) -> None - run autoclicker() in multiple threads
'''
from tkinter import Tk, HORIZONTAL, VERTICAL
from tkinter.ttk import Button, Entry, Label, PanedWindow
from threading import Thread
from time import sleep
import pyautogui as autogui


def autoclicker(times: int = 10, delay: int = 10) -> None:
    '''
    autoclicker(times: int, delay: int) -> None

    Click by mouse multiple times

    Parameters:
    times: int - how many times to click.           Default: 10.
    delay: int - delay before clicking in seconds.  Default: 10.
    '''
    if not isinstance(times, int):
        raise TypeError(f'The "times" argument should be an int, but you passed {type(times)}')
    if not isinstance(delay, int):
        raise TypeError(f'The "delay" argument should be an int, but you passed {type(delay)}')
    sleep(delay)
    for _ in range(times):
        autogui.click()


def spam(click_times: int = 10, threads_number: int = 1, delay = 10) -> None:
    '''
    spam(clicks_number: int, threads_number: int) -> None

    Run autoclicker() in multiple threads.
    
    Parameters:
    click_times: int - how many times to click in one thread     Default: 10
    thread_number: int - number of threads to start              Default: 1
    delay: int - delay before autoclicker() will start clicking  Default: 10
    '''
    if not isinstance(click_times, int):
        raise TypeError(
            f'The "click_times" argument should be an int, but you passed {type(click_times)}'
        )
    if not isinstance(threads_number, int):
        raise TypeError(
            f'The "threads_number" argument should be an int, but you passed {type(threads_number)}'
        )
    if not isinstance(delay, int):
        raise TypeError(f'The "delay" argument should be an int, but you passed {type(delay)}')

    for _ in range(threads_number):
        thread = Thread(target=autoclicker, args=[click_times, delay])
        thread.start()


def _validate_entry(value: str) -> bool:
    '''
    _validate_entry(value: str) -> bool

    Inner function for validate entry input.
    Return True if value is number or empty.
    Return False if the value is not a number.
    '''
    if value.isdigit() or value == '':
        return True
    return False


if __name__ == "__main__":
    root = Tk()
    root.title("TapTron5000")
    root.geometry('500x150')
    root.wm_resizable(width=False, height=False)

    message = Label(root, text='Program wait 10 seconds after you press button.')
    message.pack()

    # declaration

    clicks_line = PanedWindow(root, orient = HORIZONTAL)
    threads_line = PanedWindow(root, orient = HORIZONTAL)
    buttons_line = PanedWindow(root, orient = VERTICAL)

    # some characters have 0.5 of character width
    clicks_label = Label(root, text='How many times to click:', anchor='w', width=28)
    threads_label = Label(root, text='How many threads you want to run:', anchor='w', width=28)

    vcmd = (root.register(_validate_entry), '%P')
    clicks_entry = Entry(root, width=100, validate='all', validatecommand=vcmd)
    clicks_entry.insert(1, '10')
    threads_entry = Entry(root, width=100, validate='all', validatecommand=vcmd)
    threads_entry.insert(0, '2')

    run_button = Button(
        root,
        text='Run',
        width=100,
        command=lambda: spam(int(clicks_entry.get()))
    )
    multirun_button = Button(
        root,
        text='Multithread run',
        command=lambda: spam(
            int(clicks_entry.get()),
            int(threads_entry.get())
        )
    )

    # place

    clicks_line.pack()
    threads_line.pack()
    buttons_line.pack()

    clicks_line.add(clicks_label)
    clicks_line.add(clicks_entry)

    threads_line.add(threads_label)
    threads_line.add(threads_entry)

    buttons_line.add(run_button)
    buttons_line.add(multirun_button)

    root.mainloop()
