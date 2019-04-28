# 该脚本用于删除指定文件夹下的所有重复文件/图片
require 'find'
require 'digest'

base_dir = '指定文件夹'
sha2_map = {}
total_delete = 0
Find.find(base_dir) do |filename|
  file = File.new(filename)
  next unless File.file?(file)

  # 将文件内容进行SHA2运算得出唯一值，作为判断文件重复的依据
  sha2 = Digest::SHA2.hexdigest(File.read(filename))
  if sha2_map.include? sha2
    sha2_map[sha2] += 1
    File.delete filename
    puts "delete #{total_delete += 1} :#{filename}"
  else
    sha2_map[sha2] = 1
  end
end

# 打印文件重复的数量
sha2_map.each do |sha2,num|
  puts "#{sha2}:#{num}" if num > 1
end
