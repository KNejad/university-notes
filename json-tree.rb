require "json"
def directory_hash(path, name=nil)
	data = {:data => (name || path)}
	data[:children] = children = []
	Dir.foreach(path) do |entry|
		next if (entry == '..' || entry == '.')
		full_path = File.join(path, entry)
		if File.directory?(full_path) 
			children << directory_hash(full_path, entry)
		elsif entry.end_with? ".json"
			children << entry
		end
	end
	return data
end


File.write('cs2506/index.json',directory_hash("cs2506").to_json)
File.write('cs2510/index.json',directory_hash("cs2510").to_json)
File.write('cs2512/index.json',directory_hash("cs2512").to_json)
File.write('cs2521/index.json',directory_hash("cs2521").to_json)
