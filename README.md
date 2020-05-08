# Hello World

> This repository consists of few first tries to trying something new.

--------------------------------------------------------
## Snake Game

* This game was try to explore p5.js and working with canvases.
* The snake game is the classic Nokia game.
* You can play this game [here](http://hetzzsnake.surge.sh/)

-------------------------------------------------------
## GSOC_Scrape

* My first try into the world of automation led me to scrape the GSOC website Due to my keen interest in Open Source.
* Used Jupyter Notebook to get acknowledged with the importance of unit testing.
* [GSOC.csv](https://github.com/hetzz/hello-world/blob/master/GSOC_Scrape/GSOC.csv) file will have the details of all the organisation of GSOC 2019.

-----------------------------------------------------------
## Background Wallpaper

* A small python script to automate the process for changing your wallpapers dynamically on your Ubuntu system.
* Download the script and edit the script to set the path to your folder at all required places.

> Now it's only a question of telling your system to change automatically the background every 15 minutes by editing your user's crontab table:

```
$ crontab -e
```

#### Then add these lines:

#### Edit this file to introduce tasks to be run by cron.
```
#
# m h  dom mon dow   command
*/15 *  * * *  /path/to/script.py
```