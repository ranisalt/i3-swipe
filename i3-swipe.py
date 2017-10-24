#!/usr/bin/env python3
import pyi3
import logging
import shlex
import subprocess
import sys


def run():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    args = ['stdbuf', '-oL', '--', 'libinput', 'debug-events']
    args.extend(sys.argv[1:])
    p = subprocess.Popen(args, bufsize=1, stdout=subprocess.PIPE,
                         universal_newlines=True)

    x, y = 0, 0
    c = pyi3.Connection()

    try:
        line = p.stdout.readline()
        while line:
            tokens = shlex.split(line)

            if 'GESTURE_SWIPE_BEGIN' == tokens[1]:
                logging.info('Swipe gesture begin')
                x, y = 0, 0

            elif 'GESTURE_SWIPE_UPDATE' == tokens[1]:
                delta_axis, *_ = ' '.join(tokens[4:]).split('(')
                data = (float(s.strip()) for s in delta_axis.split('/'))
                x, y = (a + b for a, b in zip((x, y), data))

            elif 'GESTURE_SWIPE_END' == tokens[1]:
                logging.info('Swipe gesture end')
                if tokens[3] == '3' and abs(x) > abs(y) >= 0:
                    # x must be != 0
                    c.command(f'workspace {"prev" if x < 0 else "next"}')

            line = p.stdout.readline()

    finally:
        socket.close()
        p.terminate()


if __name__ == '__main__':
    run()
