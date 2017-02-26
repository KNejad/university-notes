require "json"
def directory_hash(course)  
	directory =  Dir[course + "/**/*.json"].sort
	
	tree = Hash.new
	tree["_title"] = course.upcase + " Index"
	tree["_date"] =  Time.now
	directory.each do |file|
		jsonFile = JSON.load(open(file))
		title = jsonFile["_title"]
		tree[title] = Hash.new
		tree[title]["_href"] = file
	end
	return JSON.pretty_generate(tree)
end



courses = ["cs2506", "cs2510", "cs2512", "cs2521"] 

courses.each do |course|
	file = course +  '/index.json'
	File.delete(file) if File.exist?(file)
	File.write(file ,directory_hash(course))
end
