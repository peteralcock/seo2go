require 'metainspector'
require 'nokogiri'
require 'open-uri'
require 'csv'

# List of URLs to visit
urls = ['http://example.com/page1', 'http://example.com/page2'] # Add your URLs here
urls = File.read("links.txt").split("\n")

# User agent string to mimic a browser visit
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'

# Path to the CSV file to save the data
csv_file_path = 'website_data.csv'

CSV.open(csv_file_path, 'wb') do |csv|
  # CSV header
  csv << ['URL', 'Meta Title', 'Meta Description', 'Entry Title', 'Entry Content']
  
  urls.each do |url|
    puts ">> #{url} ..."

    begin
    newfilename = [url.split("/").last, ".txt"].join
    filename =  newfilename.gsub(" ", "")
    file = File.open(filename,"wb")

      inspector = MetaInspector.new(url)
      
      # Extract meta title and description
      meta_title = inspector.best_title                            
      meta_description = inspector.best_description
      doc = inspector.parsed
      entry_title =  meta_title
      # doc.at('.entry-title')&.text.strip || '' 
      entry_content = doc.at('.jupiterx-post-content.clearfix')&.text.strip || ''
      file << [meta_title,meta_description,entry_title,entry_content].join("\n\n")
      file.close
      puts filename
      puts entry_title
      puts ""
      
      # Save the extracted data to the CSV
      csv << [url, meta_title, meta_description, entry_title, entry_content]
      
      # Sleep to avoid being banned for bot crawler behaviors
      sleep 1
    rescue => e
      file.close
      puts "Failed to process #{url}: #{e.message}"
    end

    puts "[FINISHED] <<< #{url} >>>"
  end
end

puts "Data extraction complete. Check the #{csv_file_path} file."

