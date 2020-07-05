

# install google chrome
```
dnf install fedora-workstation-repositories
dnf config-manager --set-enabled google-chrome
dnf install google-chrome-stable
```

ex) execute below this command 
```
# check google chrome version you want to use
$ dnf info --showduplicates google-chrome-stable
$ sudo dnf install google-chrome-stable-83.0.4103.116-1
```
and you change chromedriver-binary
```
$ pipenv install chromedriver-binary=83.0.4103.116-1
```
chromedriver-binary is dependency, and you use adapt google-chrome-stable.

# I referrence this site
(https://www.it-swarm.dev/ja/google-chrome/webdriverexception%EF%BC%9A%E4%B8%8D%E6%98%8E%E3%81%AA%E3%82%A8%E3%83%A9%E3%83%BC%EF%BC%9Achrome%E3%83%96%E3%83%A9%E3%82%A6%E3%82%B6%E3%82%92%E8%B5%B7%E5%8B%95%E3%81%97%E3%82%88%E3%81%86%E3%81%A8%E3%81%97%E3%81%9F%E3%81%A8%E3%81%8D%E3%81%ABdevtoolsactiveport%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB%E3%81%8C%E5%AD%98%E5%9C%A8%E3%81%97%E3%81%BE%E3%81%9B%E3%82%93/838364328/)