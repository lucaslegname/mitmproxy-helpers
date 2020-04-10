# mitmproxy-helpers

**mitmproxy-helpers** is a repository gathering useful tips and scripts to make the use of **mitmproxy** as simple as possible.

## Tips

### Use mitmproxy with Docker

Using **mitmproxy** with Docker can be useful if you want to keep your computer clean or if you need to use multiple version of **mitmproxy** in parallel.

To do so, you can use this base command :

```bash
docker run --rm -it -p 8080:8080 mitmproxy/mitmproxy:4.0.4
```

With this simple command, you will be able to use **mitmproxy** without going through the install process. If you want to persist the certificate folder - in order to avoid reinstalling the certificates on your test devices every time - you can share the container's certificate folder with a local one :

```bash
docker run --rm -it -v ~/your/local/folder:/home/mitmproxy/.mitmproxy -p 8080:8080 mitmproxy/mitmproxy:4.0.4
```

To simplify the use of this command, just add an alias in your `~/.bash_profile` :

```bash
alias mitmproxy='docker run --rm -it -v ~/your/local/folder:/home/mitmproxy/.mitmproxy -p 8080:8080 mitmproxy/mitmproxy:4.0.4'
```

Now you can start **mitmproxy** using :

```bash
mitmproxy
```

And if you need to use parameters, no worries you can use params as you would do if **mitmproxy** was directly installed on your computer :

```bash
mitmproxy --set view_filter=google.com
```

## Scripts

Writing **mitmproxy** scripts is quite simple if you are a bit familiar with Python and if you have examples. Here are a few ones :

| Script                                   | Description                                                                  |
| :--------------------------------------- | :--------------------------------------------------------------------------- |
| [Redirect](Redirect)                     | Redirect requests to another server                                          |
| [EditableCache](EditableCache)           | Create a local and editable cache you can play with                          |
| [ChangeHTTPCode](ChangeHTTPCode)         | Change responses HTTP code                                                   |
