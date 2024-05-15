RueLib Public Version

This is just a nice importable for my most used, non-specific functions.

CLASSES

class ThreadPool(builtins.object)

       ThreadPool(thread_num=10)

       Used for basic threading of functions.

       Use with poolvar = ThreadPool(number_of_threads), poolvar.add_task(function_name, args if any), pool.wait_complete()

FUNCTIONS

    beep(type=None)

        Plays a windows beep. Type can be the following (default is asterisk):

        'SystemAsterisk'

        'SystemExclamation'

        'SystemExit'

        'SystemHand'

        'SystemQuestion'

    fromb64(s)

        Converts base64 string into decoded text

    is_palindrome(string)

        Returns if a string is a palindrome or not.

        Sick of this showing up on job interviews, ahaha. :)

    logprint(fn='log.txt', msg='', ts=False, prepend=True)

        Great for manually logging text.

        ts controls if you want a timestamp added.

        prepend controls if you want to prepend to the file (or, False for a standard append)

    maybe(fun)

        A simple one line try/except.

        fun is the function you want to call (example: maybe(roll("1d6")) or maybe(print("test")))

    merge_dicts(*dicts)

        Merge two dictionaries.

    parse_csv_as_listdict(csv_path)

        Takes a csv file. Returns a list, each row being a dictionary containing the data for each row (key as the header, value as the cell data).

    playsound(fn, flags)

        Plays a wav file. Library allows flags to be passed, but I'm not sure what they are.

        If fn is "None" it will stop playing any sound that's currently playing.

    read_json_from_file(filepath)

    remove_duplicates(val=[])

        Removes duplicates from a list.

    roll(dice='1d6', plus=0, minus=0, seed=None)

        Dice roller. dice is a string containing the D&D verbiage for the dice ("numdice d sizeofdice").

        You can optionally add a value to the total, subtract, or force the rng to a specific seed.

    timestamp()

        Returns a simple, easy to read timestamp. Military time.

    tob64(s)

        Converts text string into base64

    write_json_to_file(data, filepath)