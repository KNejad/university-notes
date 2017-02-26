require "json"
def directory_hash(course)  
	directory =  Dir[course + "/**/*.json"].sort
	
	tree = Hash.new
	tree["_title"] = course.upcase + " Index"
	directory.each do |file|
		jsonFile = JSON.load(open(file))
		title = jsonFile["_title"]
		tree[title] = Hash.new
		tree[title]["_href"] = file
	end
	return tree.to_json
end



courses = ["cs2506", "cs2510", "cs2512", "cs2521"] 

courses.each do |course|
	file = course +  '/index.json'
	File.delete(file) if File.exist?(file)
	File.write(file ,directory_hash(course))
end
