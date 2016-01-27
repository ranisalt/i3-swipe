# i3-swipe

A simple daemon for using swipe gestures with i3.

## Usage
Install using the provided [install.sh](install.sh) script, which will detect
your path and try to install the files.

To enable the service with systemd:
```bash
systemd --user enable i3-swipe.service
```
Then start with:
```bash
systemd --user start i3-swipe.service
```

Or manually run `i3-swipe.py` which will, by default, be on your path. You can
alternatively pass `DESTDIR` to `install.sh` (`env DESTDIR=/tmp install.sh`) and
provide a different install path for the Python script.

The default action is to move to the next open workspace with three-finger right
swipe and to the previous with three-finger left swipe. If you know Python, just
edit the `'GESTURE_SWIPE_END' == tokens[1]` branch to send whatever command you
want or fork and open an issue.

## License
This work is licensed under the [MIT License](LICENSE).
