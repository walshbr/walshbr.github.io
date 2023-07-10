require 'html-proofer'

posts_dir       = "_drafts"    # directory for blog files
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
    url: https://scholarslab.lib.virginia.edu/blog/FULL-SLUG-HERE"
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
