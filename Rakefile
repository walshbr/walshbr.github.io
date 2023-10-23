require 'html-proofer'
require 'front_matter_parser'

posts_dir       = "_drafts"    # directory for blog files
blog_image_dir = 'assets/post-media'
slab_dir        = "/Users/bmw9t/projects/scholarslab.org/collections/_posts"
slab_image_dir  = "/Users/bmw9t/projects/scholarslab.org/assets/post-media"
new_post_ext    = "md"  # default new post file extension

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

desc "Makes a crossposted file in the slab folder"
task :crosspost, [:file_name, :images] do |t, args|
  if args.file_name
    file_name = args.file_name
  end
  puts file_name
  old_file = "_posts/#{file_name}"
  new_file = "#{slab_dir}/#{file_name}"
  puts new_file

  parsed = FrontMatterParser::Parser.parse_file(old_file, loader: FrontMatterParser::Loader::Yaml.new(allowlist_classes: [Date]))

  title_slug = parsed.front_matter['title'].downcase.gsub(' ', '-').gsub(/[^\w-]/, '')
  if File.exists?(new_file)
    File.delete(new_file)
  end
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
    url: https://walshbr.com/blog/#{title_slug}
---
#{parsed.content}
")
}
    puts "Crossposted file created at #{new_file}"
  post_image_folder = blog_image_dir + '/' + title_slug
  crosspost_image_folder = slab_image_dir  + '/' + title_slug
if args.images
  if File.exists?(crosspost_image_folder)
    FileUtils.rm_rf(crosspost_image_folder)
    Dir.mkdir(crosspost_image_folder) 
  end
  FileUtils.cp_r(post_image_folder + '/.', crosspost_image_folder)
end
end