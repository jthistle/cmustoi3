# cmustoi3

A widget for py3status which displays what cmus is playing.

Here's what it looks like:

![playing](./playing.png)

![paused](./paused.png)

![stopped](./stopped.png)

## Installation

You must be using py3status. In your i3status.conf, add:

```properties
order += "external_script"

# ...

external_script {
        script_path = "/path/to/cmustoi3/main.py"
        cache_timeout = 1
}
```

Feel free to change the `cache_timeout` if you're not too bothered about slightly stale info.
