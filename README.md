# Banking

This a simple [flask](http://flask.pocoo.org/) example of [Banking Kata](http://kata-log.rocks/banking-kata "Banking Kata")

## Project Structure

The structure of the project is [Divisional](http://exploreflask.com/en/latest/blueprints.html#divisional)

## Setup 

- [Pipenv](https://pipenv.readthedocs.io/en/latest/)
- Python 3.7
- Flask
- Jinja2
- mysqlclient

## Installing mysqlclient on macOS Mojave

If you get the below mentioned error while installing mysqlclient 
``` 
clang: error: linker command failed with exit code 1 (use -v to see invocation)
error: command 'clang' failed with exit status 1
```

Export the below mentioned flag for the compilers to find OpenSSL in `zsh`

```bash
> export LDFLAGS="-L/usr/local/opt/openssl/lib"
> export CPPFLAGS="-I/usr/local/opt/openssl/include"
```

To find the right flags run `brew info openSSL`

## Running the application

```bash
  > export APP_SETTINGS="config.DevelopmentConfig"
  > flask run  

```

