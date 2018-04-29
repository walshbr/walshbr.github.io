# Usage

For future reference, I'm using the guide [here](http://joshfrankel.me/blog/deploying-a-jekyll-blog-to-github-pages-with-custom-plugins-and-travisci/) to build my site using custom plugins. Things get built through travis on the source branch and then the \_site directory gets sent to the master branch for deploying. The main thing to remember is that all the files live off the source branch, so that's where you commit changes. Doing so triggers a travis build that will build to master. 
