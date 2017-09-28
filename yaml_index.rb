#!/usr/bin/ruby -w

require 'yaml'

def contains_yaml(directory) 
	return !(Dir[directory + '/**/*.yaml'].empty?)
end

def directory_hash(directory) 

	directories =  Dir.entries(directory).sort
	tree = Hash.new

	directories.each do |entry|
		address = directory + '/' + entry
		if entry == '.' or  entry == '..' then
			next
		elsif File.directory?(address) and contains_yaml(address) then
			tree[entry.capitalize] = directory_hash(address)
		elsif entry.end_with? '.yaml' then
      yaml_file = YAML.load_file(address)
			title = yaml_file['_title']
			tree[title] = Hash.new
			tree[title]['_href'] = address
		end
	end
	return tree
end



courses = ['cs2506', 'cs2510', 'cs2512', 'cs2521', 'cs3027', 'cs3028'] 

courses.each do |course|
	file = course +  '/index.yaml'

  if File.exist?(file)
    original = YAML.load_file(file)
  else
    original = {}
  end
	course_tree = {}
	course_tree.merge!(directory_hash(course))
  course_tree.delete("#{course.upcase} Index")
  original.delete('_title')
  original.delete('_date')

  if course_tree != original
    course_tree = {'_title' => course.upcase + ' Index', '_date' => Time.now}.merge(course_tree)
    File.write(file, course_tree.to_yaml)
  end
end
