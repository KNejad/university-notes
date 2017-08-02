#!/usr/bin/ruby -w

require "json"
require "yaml"

def containsJSON(directory) 
	return !(Dir[directory + "/**/*.json"].empty?)
end

def convert_files(directory) 

	directories =  Dir.entries(directory)

	directories.each do |entry|
		address = directory + "/" + entry
		if entry == "." or  entry == ".." then
			next
		elsif File.directory?(address) and containsJSON(address) then
			convert_files(address)
		elsif entry.end_with? ".json" then
			file_content = JSON.load(open(address))
	    File.delete(address)
      File.write("#{File.dirname(address)}/#{File.basename(address,'.*')}.yaml" ,file_content.to_yaml)
		end
	end
end



courses = ["cs2506", "cs2510", "cs2512", "cs2521"] 

courses.each do |course|
	convert_files(course)
end
