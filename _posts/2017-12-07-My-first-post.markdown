---
layout: post
title: "Why did I do this?! Lessons from creating this blog."
date:   2017-12-07 22:40:22 -0600
categories: jekyll update blog
---

## Hi, There!

Somewhere in the last 2 weeks, I felt that I needed a website... on github. In fact after looking at [Github Pages], I felt closer to achieving my long-term desire of having a website/blog where I can share things of interest to myself and engaging like-minded audience.

It wasn't until last friday that I actually got to thinking about it seriously! and it wasn't until yesterday that it actually came into being. This is a short story of the motivations behind making this blog and learning in the process of creating it. 

>This post should make life easier for anyone interested in making their [Github Pages] website. Or make you want to get started on making your own. Interested ?

## Motivation

Main motivations to create this were...
1. To share tips/ tricks I have learned over the course of my projects and work in my [areas of interest](/about)
1. To showcase specific projects, software, art I created or was inspired by
1. Share my experiences as a freelancer, contractor, employee so it may benefit anyone in a similar stage in their life.
1. Give my writing muscles some wear. Writing generally helps me make sense of what's happenning, organize my thoughts and calms me.
1. ... and to able to achieve all of that without having to spend a ton of time and money.

To be able to do that I needed a solution that is ...
1. Easy to setup and move between different platforms. I work on diverse systems from my iPad/ Phone to my laptop running windows and desktop running linux. Whatever was my blogging solution needed to be cross-platform.
2. Maximum focus on writing and minimum on formatting/ beautifying. Although the end-result (to be useful) should pass for good-looking.
3. High availability and throughput and able to scale with my needs. Fast and responsive so reader can focus on content. Search engine friendly - the whole point of writing this is to be found by those with the need for this information.
4. Since bulk of the content is expected to be technical it should be developer-friendly (basically this means syntax-highlighting for code, able to insert graphs/ charts/ media, etc.)

## Why Github-pages ?

[Github Pages] meets almost all of my requirements and more (I'm still learning what **all** it can do!). It is definitely developer friendly, fast, available, search-engine friendly and uses markdown which is the greatest tool for writers to present good-looking content without having to obsess with formatting it for hours (or days). Github-pages also provides options for making stunning sites with very little effort by leveraging years of accumulated "wisdom" - more on that later ([Check], [these], [out] if you don't believe me).

[Github Pages]: https://pages.github.com
[Check]: https://programminghistorian.org/
[these]: https://evanwill.github.io
[out]: https://software-carpentry.org

Github pages has [lots of options](https://github.com/madhuri2k/experience-experiment/blob/gh-pages/README.md#github-pages) and I will focus here on using jekyll to create website from markdown files. This is because... it's how [this site](https://github.com/madhuri2k/madhuri2k.github.io) is built.

## Setting up Jekyll

There are tons of great resources of jekyll and its battle-tested ecosystem of plugins. I especially found this [site] & [video] very useful. 

Although github is totally usable on web, hacking the site locally will be much faster since it can leverage my familiar tools (text editor, image editor etc) and keep it available offline (great way to write without distractions). So I needed to install jekyll locally. Instead of installing it on my computer, I decided to use [docker][https://www.docker.com/] to satisy my #1 goal (cross-platform portability). There is (of course) an official docker image for jekyll and the script below will fetch and deploy my site on it. A similar batch file does the job on windows.

{% highlight bash %}

export JEKYLL_VERSION=3.5

x-www-browser http://localhost:4000/ &

docker run --rm \
  --volume="$PWD:/srv/jekyll" \
  -e JEKYLL_UID=$(id -u) -e JEKYLL_GID=$(id -g) \
  -p 35729:35729 -p 4000:4000 \
  -it jekyll/jekyll:$JEKYLL_VERSION \
  jekyll serve
{% endhighlight %}

The very first time it will download the entire image (~150MB) from the docker registry but next time onwards everything is local. Having this running in the background makes it very quick to make an edit (, wait 0.12s for site to be auto-regenerated) and refresh the browser to see changes. Splendid!

Here's a screenshot of my workflow in action:
[![Edit Deploy in a whiff! Screenshot](https://i.imgur.com/rfQMd5l.png)](https://i.imgur.com/rfQMd5l.png)

Of course I had to see if this really works so this morning I booted up an old system running a recent update of [manjaro xfce](https://manjaro.org) and 
1. I [installed docker] and did post-install [steps](1) (adding user to docker group, enable  docker daemon and `sudo systemctl start docker`)
2. Clone my repo: `git clone htps://github.com/madhuri2k/madhuri2k.github.io.git`
3. Run: `cd madhuri2k.github.io && bin/run`

[aite]: https://evanwill.github.io/go-go-ghpages/
[video]: https://www.youtube.com/watch?v=SWVjQsvQocA
[installed docker]: https://docs.docker.com/engine/installation/
[1]: https://docs.docker.com/engine/installation/linux/linux-postinstall/

That's it! 

> You can try these steps right now and get a copy of this website running on your computer

I have found this really productive and easy to setup & maintain. When I am happy with the updates I commit and push the chages to remote. The site gets regenerated roughly within 1 minute. Of course instead of jekyll & markdown, you can also use a static site built entirely on HTML5 and CSS.

## Jekyll Themes

While using Jekyll, you have an option of using the built-in [theme-chooser] or using a gem-based theme like minima and plugins to generate the site. 

If you use the theme-chooser then all `.md` files are converted to HTML including `index.md` and `README.md`. You need to provide a hand-coded `index.md` file as the landing page to help visitors discover the rest of your site.

If you use minima (or other similar themes) then the index is auto-generated - this may be a good thing for blogs and such, since every time you add a post or an `.md` file, the index is regenerated to ensure the page is discoverable. However you need to provide a more detailed _config.yml configuration. See [here][jt2] for a sample configuration and [here][jt1] for more on themes.

If you have your blog setup with minima and then change to using theme-chooser as described [here][theme-chooser] then your github-pages landing page will be empty.

[theme-chooser]: https://help.github.com/articles/adding-a-jekyll-theme-to-your-github-pages-site-with-the-jekyll-theme-chooser/
[jt1]: https://evanwill.github.io/go-go-ghpages/3-jekyll.html
[jt2]: https://evanwill.github.io/go-go-ghpages/5-reference.html#Themes

## Conclusion

So that was an account of my journey of setting this up. In github pages I found the right mix of ease-of-use and flexibility. Github always puts a lot of thought and customer-focus on everything they do and Pages is no exception. The fact that it's free makes it all the more attractive to try-out and bring into the being the awesome web-site or blog that is inside of you.

This post would have met its goal if it makes you want to build your blog (or fork mine) or helps you along the way. Reach out to me with you questions and comments.

Good Luck!
