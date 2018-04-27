require 'html-proofer'

task :test do
  sh "bundle exec jekyll build"
  options = { :assume_extension => true,
  :http_status_ignore => [401]}
  HTMLProofer.check_directory("./_site", options).run
end
