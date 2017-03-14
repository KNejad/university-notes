#!/usr/bin/ruby -w



require "json"

def containsJSON(directory) 
	return !(Dir[directory + "/**/*.json"].empty?)
end

def directory_hash(directory) 

	directories =  Dir.entries(directory).sort
	tree = Hash.new

	directories.each do |entry|
		address = directory + "/" + entry
		if entry == "." or  entry == ".." then
			next
		elsif File.directory?(address) and containsJSON(address) then
			tree[entry.capitalize] = directory_hash(address)
		elsif entry.end_with? ".json" then
			jsonFile = JSON.load(open(address))
			title = jsonFile["_title"]
			tree[title] = Hash.new
			tree[title]["_href"] = address
		end
	end
	return tree
end



courses = ["cs2506", "cs2510", "cs2512", "cs2521"] 

courses.each do |course|
	file = course +  '/index.json'
	File.delete(file) if File.exist?(file)
	courseTree = Hash.new
	courseTree["_title"] = course.upcase + " Index"
	courseTree["_date"] =  Time.now
	courseTree.merge!(directory_hash(course))

	File.write(file ,JSON.pretty_generate(courseTree))
end
