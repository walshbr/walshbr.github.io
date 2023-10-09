require 'html-proofer'
require 'front_matter_parser'

posts_dir       = "_drafts"    # directory for blog files
slab_dir        = "/Users/bmw9t/projects/scholarslab.org/collections/_posts"
slab_image_dir  = "/Users/bmw9t/projects/scholarslab.org/assets/post-media"
new_post_ext    = "md"  # default new post file extension when using the
deploy_dir      = "_deploy"   # deploy directory (for Github pages deployment)
public_dir      = "public"    # compiled site directory
source_dir      = "_site"
deploy_default  = "push"
deploy_branch  = "gh-pages"

task :test do
  sh "bundle exec jekyll build"
  # options = { :assume_extension => true,
  # :http_status_ignore => [0, 401]}
  HTMLProofer.check_directory("./_site").run
end

def get_stdin(message)
  print message
  STDIN.gets.chomp
end

desc "Begin a new post in #{posts_dir}"
task :new_post, :title do |t, args|
  if args.title
    title = args.title
  else
    title = get_stdin("Enter a title for your post: ")
  end
  clean_title = title.downcase.gsub(/\s/,'-')
  title_slug =clean_title.downcase.gsub(' ', '-').gsub(/[^\w-]/, '')
  filename = "#{posts_dir}/#{Time.now.strftime('%Y-%m-%d')}-#{clean_title}.#{new_post_ext}"
  if File.exist?(filename)
    abort("rake aborted!") if ask("#{filename} already exists. Do you want to overwrite?", ['y', 'n']) == 'n'
  end
  puts "Creating new post: #{filename}"
  open(filename, 'w') do |post|
    post.puts "---"
    post.puts "layout: post"
    post.puts "title: \"#{title.gsub(/&/,'&amp;')}\""
    post.puts "date: #{Time.now.strftime('%Y-%m-%d')}"
    post.puts "tags: [digital-humanities]"
    post.puts "crosspost:
  - title: the Scholars' Lab blog
    url: https://scholarslab.lib.virginia.edu/blog/#{title_slug}"
    post.puts "---"
  end
end

task :default do
  puts "Running CI tasks..."
  # Runs the jekyll build command for production
  # TravisCI will now have a site directory with our
  # statically generated files.
  sh("JEKYLL_ENV=production bundle exec jekyll build")
  options = { :assume_extension => true,
    # :http_status_ignore => [301, 302],
    :cache => { :timeframe => '2w' },
    :typhoeus => {
    :ssl_verifypeer => false,
    :ssl_verifyhost => 0 },
    :url_ignore => ['http://diss.herokuapp.com']
  }
  HTMLProofer.check_directory("./_site", options).run
  puts "Jekyll successfully built"
end

desc "Makes a crossposted file in the slab folder"
task :crosspost, [:file_name, :images] do |t, args|
  if args.file_name
    file_name = args.file_name
  else
    title = get_stdin("Enter the filename for your post to crosspost: ")
  end
  puts file_name
  old_file = "_posts/#{file_name}"
  new_file = "#{slab_dir}/#{file_name}"
  puts new_file

  parsed = FrontMatterParser::Parser.parse_file(old_file, loader: FrontMatterParser::Loader::Yaml.new(allowlist_classes: [Date]))

  title_slug = parsed.front_matter['title'].downcase.gsub(' ', '-').gsub(/[^\w-]/, '')
  File.open(new_file, 'w'){|f|
f.puts("---
author: brandon-walsh
date: #{parsed.front_matter['date']}
layout: post
slug: #{title_slug}
title: #{parsed.front_matter['title']}
categories:
- Digital Humanities
tags:
- Digital humanities
crosspost:
  - title: Brandon' blog
  - url: https://walshbr.com/blog/#{title_slug}
---
#{parsed.content}
")
}
    puts "Crossposted file created at #{new_file}"
end