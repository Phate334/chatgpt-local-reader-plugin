# ChatGPT Local Reader Plugin

This is the simplest method for ChatGPT to read local files, providing a straightforward and efficient way to extend ChatGPT's capabilities.

## Usage

Just copy `server.py` and `.well-known` to your directory.

```bash
$ python server.py
Serving HTTP on :: port 8000 (http://[::]:8000/) ...
```

and then install localhost plugin in ChatGPT.

![install plugin in ChatGPT](imgs/install.jpg)

## Example

- Here is an example of reading [openai/openai-cookbook](https://github.com/openai/openai-cookbook/) and summarize Markdown file.

![example](imgs/example.jpg)
